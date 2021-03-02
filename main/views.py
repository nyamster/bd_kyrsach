from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from main.models import *
import json
from collections import namedtuple

EventAll = namedtuple('EventAll', ('event', 'requesite', 'stuff'))

class VisitorView(viewsets.ModelViewSet):
    serializer_class = VisitorSerializer
    queryset = Visitor.objects.all()

class GainView(viewsets.ModelViewSet):
    serializer_class = GainSerializer
    queryset = Gain.objects.all()
    @action(methods=['get'], detail=False, url_path='get_gain', url_name='get_gain')
    def get_gain(self, request):
        _id = request.GET.get('id')
        _queryset = Gain.objects.all().filter(gain_id=_id)
        serializer = self.get_serializer(_queryset, many=True)
        return Response(serializer.data)

class MenuView(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

class BarView(viewsets.ModelViewSet):
    serializer_class = BarSerializer
    queryset = Bar.objects.all()

class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @action(methods=['get'], detail=False, url_path='create_ev', url_name='create_ev')
    def create_event(self, request):
        _name = request.GET.get('name')
        _ticket = request.GET.get('ticket')
        _count = request.GET.get('count')
        _menu = request.GET.get('menu')
        g = Gain.objects.create(earnings=0)
        e, create = Event.objects.get_or_create(event_id=g.gain_id, name=_name, ticket_price=_ticket, count=_count, menu_id=_menu, gain_id=g.gain_id)
        serializer = self.get_serializer(e, many=False)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='delete_ev', url_name='delete_ev')
    def delete_event(self, request):
        _event_id = request.GET.get('eventid')
        e = Event.objects.get(event_id = _event_id)
        g = Gain.objects.get(gain_id = _event_id)
        e.delete()
        g.delete()
        return Response()

    @action(methods=['get'], detail=False, url_path='getEvents', url_name='getEvents')
    def get_event(self, request):
        # _event_id = request.GET.get('eventid')
        # e = Event.objects.get(event_id=_event_id)
        # serializer = self.get_serializer(e)
        queryset = Event.objects.all()
        data = []
        for e in queryset:
            serializer = self.get_serializer(e)

            _queryset1 = Event.objects.get(event_id=e.event_id).requesites.all()
            serializer1 = RequesiteSerializer(_queryset1, many=True)

            _queryset2 = Event.objects.get(event_id=e.event_id).stuffs.all()

            events = EventAll(event = e, requesite = _queryset1, stuff = _queryset2)
            data1 = EventAllSerializer(events)
            data.append(data1.data)
        return Response(data)

    @action(methods=['post'], detail=False, url_path='createAll', url_name='createAll')
    def add_elements(self, request):
        if request.method == 'POST':
            json1 = request.body
            data = json.loads(json1)
            # data = {"name":"zhopa","ticket":50,"count":5,"menu":1,"stuffIds":[1,2],"requisiteIds":[1,2]}
            g = Gain.objects.create(earnings=0)
            e, create = Event.objects.get_or_create(event_id=g.gain_id, name=data['name'], ticket_price=data['ticket'], count=data['count'],
                                                        menu_id=data['menu'], gain_id=g.gain_id)
            stuffids = data['stuffIds']
            reqids = data['requisiteIds']
            for i in stuffids:
                s = Stuff.objects.get(stuff_id=i)
                se, create = EventStuffs.objects.get_or_create(stuff=s, event=e)
            for i in reqids:
                r = Requesite.objects.get(requesite_id=i)
                ee, create = EventRequesites.objects.get_or_create(requesite=r, event=e)
        return Response()



class RequesiteView(viewsets.ModelViewSet):
    serializer_class = RequesiteSerializer
    queryset = Requesite.objects.all()
    @action(methods=['get'], detail=False, url_path='create_req', url_name='create_req')
    def create_req(self, request):
        _name = request.GET.get('name')
        _number = request.GET.get('number')
        r, created = Requesite.objects.get_or_create(name=_name, number=_number)
        serializer_class = self.get_serializer(r, many=False)
        return Response(serializer_class.data)

    @action(methods=['get'], detail=False, url_path='add_req', url_name='add_req')
    def add_req(self, request):
        _event_id = request.GET.get('eventid')
        _req_id = request.GET.get('reqid')
        e = Event.objects.get(event_id=_event_id)
        r = Stuff.objects.get(stuff_id=_req_id)
        se, create = EventRequesites.objects.get_or_create(requesite=r, event=e)
        return Response()
    @action(methods=['post'], detail=False, url_path='addReq', url_name='addReq')
    def addReq(self, request):
        json1 = request.body
        data = json.loads(json1)
        # data = {"eventid":1,"requisiteIds":[1,2]}
        e = Event.objects.get(event_id=data['eventid'])
        reqids = data['requisiteIds']
        for i in reqids:
            r = Requesite.objects.get(requesite_id=i)
            ee, create = EventRequesites.objects.get_or_create(requesite=r, event=e)
        return Response()

    @action(methods=['get'], detail=False, url_path='delete_req', url_name='delete_req')
    def delete_req(self, request):
        _req_id = request.GET.get('reqid')
        r = Requesite.objects.get(requesite_id=_req_id)
        r.delete()
        return Response()

    @action(methods=['get'], detail=False, url_path='get_req', url_name='get_req')
    def get_req(self, request):
        _event_id = request.GET.get('eventid')
        _queryset = Event.objects.get(event_id=_event_id).requesites.all()
        serializer = self.get_serializer(_queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='unboundReq', url_name='unboundReq')
    def unbound_req(self, request):
        _event_id = request.GET.get('eventid')
        _req_id = request.GET.get('reqid')
        re = EventRequesites.objects.get(event=_event_id, requesite=_req_id)
        re.delete()
        return Response()

class StuffView(viewsets.ModelViewSet):
    serializer_class = StuffSerializer
    queryset = Stuff.objects.all()
    @action(methods=['get'], detail=False, url_path='create_stuff', url_name='create_stuff')
    def create_stuff(self, request):
        _name = request.GET.get('name')
        _post = request.GET.get('post')
        _salary = request.GET.get('salary')
        s, create = Stuff.objects.get_or_create(name=_name, post=_post, salary=_salary)
        serializer_class = self.get_serializer(s)
        return Response(serializer_class.data)

    @action(methods=['get'], detail=False, url_path='delete_stuff', url_name='delete_stuff')
    def delete_stuff(self, request):
        _stuff_id = request.GET.get('stuffid')
        s = Stuff.objects.get(stuff_id=_stuff_id)
        s.delete()
        return Response()

    @action(methods=['get'], detail=False, url_path='add_stuff', url_name='add_stuff')
    def add_stuff(self, request):
        _event_id = request.GET.get('eventid')
        _stuff_id = request.GET.get('stuffid')
        e = Event.objects.get(event_id=_event_id)
        s = Stuff.objects.get(stuff_id=_stuff_id)
        se, create = EventStuffs.objects.get_or_create(stuff=s, event=e)
        return Response()
    @action(methods=['post'], detail=False, url_path='addStuff', url_name='addStuff')
    def addStuff(self, request):
        json1 = request.body
        data = json.loads(json1)
        # data = {"eventid":5,"stuffIds":[1,2]"}
        e = Event.objects.get(event_id=data['eventid'])
        stuffids = data['stuffIds']
        for i in stuffids:
            s = Stuff.objects.get(stuff_id=i)
            se, create = EventStuffs.objects.get_or_create(stuff=s, event=e)
        return Response()
    @action(methods=['get'], detail=False, url_path='get_stuff', url_name='get_stuff')
    def get_stuff(self, request):
        _event_id = request.GET.get('eventid')
        _queryset = Event.objects.get(event_id=_event_id).stuffs.all()
        serializer = self.get_serializer(_queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, url_path='unboundStuff', url_name='unboundStuff')
    def unbound_stuff(self, request):
        _event_id = request.GET.get('eventid')
        _stuff_id = request.GET.get('stuffid')
        se = EventStuffs.objects.get(event=_event_id, stuff=_stuff_id)
        se.delete()
        return Response()

# class SortedSuitabilityView(viewsets.ModelViewSet):
#     serializer_class = SuitabilitySerializer
#     queryset = Suitability.objects.all().order_by('days_to_couple')

# class TransformView(viewsets.ModelViewSet):
#     serializer_class = LodgerSerializer
#     queryset = Lodger.objects.all().filter(days_left=0)

# class LodgerView(viewsets.ModelViewSet):
#     serializer_class = LodgerSerializer
#     queryset = Lodger.objects.all()
#
#     @action(methods=['get'], detail=False, url_path='update_day', url_name='update_day')
#     def update_day(self, request):
#         self.queryset = self.queryset.exclude(days_left=-1)
#         self.queryset.update(days_left=F('days_left') - 1)
#         return Response()
#
# class SearchView(viewsets.ModelViewSet):
#     serializer_class = SearchSerializer
#     queryset = Lodger.objects.all()
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name']
#
# class SuitabilityView(viewsets.ModelViewSet):
#     serializer_class = SuitabilitySerializer
#     queryset = Suitability.objects.all()
#
#     @action(methods=['get'], detail=False, url_path='get', url_name='get')
#     def get_object(self, request):
#         _man_id = request.GET.get('man_id')
#         _woman_id = request.GET.get('woman_id')
#         _queryset = Suitability.objects.all().filter(man_id=_man_id, woman_id=_woman_id)
#         serializer = self.get_serializer(_queryset, many=True)
#         if _queryset.count() == 0:
#             return Response(status=404)
#         return Response(serializer.data)

# class ScheduleView(viewsets.ModelViewSet):
#     serializer_class = ScheduleSerializer
#     queryset = Schedule.objects.all()
#
# class EscapeAttemptView(viewsets.ModelViewSet):
#     serializer_class = EscapeAttemptSerializer
#     queryset = EscapeAttempt.objects.all()
#     #schedule = Schedule.objects.all()
#
# class CouplesView(viewsets.ModelViewSet):
#     serializer_class = CouplesSerializer
#     queryset = Couples.objects.all()
#
#
#     @action(methods=['get'], detail=False, url_path='set', url_name='set')
#     def set_couple(self, request):
#         _man_id = request.GET.get('man_id')
#         _woman_id = request.GET.get('woman_id')
#         try:
#             _check = self.queryset.get(man_id=_man_id)
#             _check = self.queryset.get(woman_id=_woman_id)
#         except BaseException:
#             self.queryset.create(man_id=_man_id,woman_id=_woman_id)
#             return Response()
#         return Response(status=400)



