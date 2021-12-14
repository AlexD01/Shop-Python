
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:name>/', views.section, name='section'),
    path('storage/<str:name>/', views.storage, name='storage'),
    path('detail/<int:id>/', views.detail, name='detail'),

] 
urlpatterns+=[
        url(r'^media/(?P<path>.*)$',serve,{
            'document_root':settings.MEDIA_ROOT}),
    ]
