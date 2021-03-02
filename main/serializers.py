from rest_framework import serializers
from main import models


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = ('visitor_id', 'name', 'age', 'sex', 'allergies', 'cash')

class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stuff
        fields = ('stuff_id', 'name', 'post', 'salary')

class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stuff
        fields = ('stuff', 'violation')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('event_id', 'name', 'ticket_price', 'count', 'menu_id', 'gain_id')

class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bar
        fields = ('gain_id', 'earnings')

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Club
        fields = ('shedule_id')

class GainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gain
        fields = ('gain_id', 'earnings')

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ('menu_id', 'food', 'drinks')

class RequesiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requesite
        fields = ('requesite_id', 'name', 'number')

class SheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shedule
        fields = ('event_id', 'time')

class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Violation
        fields = ('visitor_id', 'name')

class EventAllSerializer(serializers.Serializer):
    event = EventSerializer(many = False)
    requesite = RequesiteSerializer(many = True)
    stuff = StuffSerializer(many = True)

# class VisitorEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.VisitorEvent
#         fields = ('visitor_event_id', 'visitor', 'event')
#
# class RequesiteEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.EventRequesites
#         fields = ('requesite_event_id', 'requesite', 'event')
#
# class StuffEventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.EventStuffs
#         fields = ('stuff_event_id', 'stuff', 'event')

# class LodgerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Lodger
#         fields = ('name','age','sex','chosen_animal','main_feature')
#
# class SearchSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Lodger
#         fields = ('person_id','name','age','sex')
#
# class SuitabilitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Suitability
#         fields = ('mutual_interest','days_to_couple')
#
# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Schedule
#         fields = ('name','description','day_of_week','time_int')
#
# class EscapeAttemptSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.EscapeAttempt
#         fields = ('person_id', 'date', 'success')
#
# class CouplesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Couples
#         fields = ['man_id','woman_id','date_of_creation','feature']