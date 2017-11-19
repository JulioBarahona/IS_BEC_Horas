from django.conf.urls import url
from . import views
app_name = 'student'
urlpatterns =[
	url(r'^$',views.index,name='index'),
	url(r'^create/',views.create,name='save'),
	url(r'^modify/', views.modify, name='modify'),
]