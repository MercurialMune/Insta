from django.conf.urls import url
from insta import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^reg/',views.user,name = 'register'),

]
