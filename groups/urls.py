from rest_framework import routers
from django.urls import path, include
from groups import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupView, 'groups')
router.register(r'people', views.PersonView, 'people')
router.register(r'memberships', views.MembershipView, 'memberships')

urlpatterns = [
    path('', include(router.urls)),
]
