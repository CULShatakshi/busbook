from django.urls import path
from . import views
app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('app/', views.appView, name='app'),
    path('end/',views.addView,name='end'), 
     
] 