from django.conf.urls import url, include
from rest_framework import routers
from views import UserViewSet, GroupViewSet

#from django.contrib.auth.views import user-detail

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^my_test', user-detail.as_view()),
]
