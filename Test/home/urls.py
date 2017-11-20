from django.conf.urls import url
from home import views
from home.views import PublishView, HomeView, EstudianteView

urlpatterns = [
url(r'^$', HomeView.as_view(), name='home'),
url(r'^publish$', PublishView.as_view(), name='publish'),
url(r'^actividad$', EstudianteView.as_view(), name='actividad'),
]
