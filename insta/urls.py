from django.conf.urls import url
from insta import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^userspace/', views.userspace, name='userspace'),
    url(r'^post/', views.upload_form, name='post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

