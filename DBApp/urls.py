from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.views import *

router = routers.DefaultRouter()
router.register(r'visitor', VisitorView)
router.register(r'requesite', RequesiteView)
router.register(r'stuff', StuffView)
router.register(r'event', EventView)
router.register(r'gain', GainView)
router.register(r'bar', BarView)
router.register(r'menu', MenuView)
# router.register(r'lodger', LodgerView)
# router.register(r'transform',TransformView)
# router.register(r'search', SearchView)
# router.register(r'suitability',SuitabilityView)
# router.register(r'sortsuitability',SortedSuitabilityView)
# router.register(r'schedule',ScheduleView)
# router.register(r'security',EscapeAttemptView)
# router.register(r'couples', CouplesView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
