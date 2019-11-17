from rest_framework import path, include
from groups import views

router = DefaultRouter()
router.register(r'groups', views.GroupView, 'groups')
router.register(r'members', views.MemberView, 'members')

urlpatterns = [
    path('api/', include(router.urls))
]
