from django.conf.urls import url, include
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.UserFormView.as_view(), name="register"),
    url(r'^login/$', views.UserLoginView.as_view(), name="login"),
    url(r'^logout/$', views.UserLogoutView, name="logout"),
]
