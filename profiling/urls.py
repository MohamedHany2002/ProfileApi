
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter 


router= DefaultRouter()
router.register('hello-api',views.hellViewset,basename='hello-ap')
router.register('profile',views.profileViewSet,basename='profile')
router.register('login',views.LoginViewSet,basename='login')
router.register('list',views.itemViewSet,basename='items')
urlpatterns = [
    # path('',views.get_profile.as_view(),name='profile' ),
    path('',include(router.urls) ),
    path('feed/',include(router.urls) ),
]
