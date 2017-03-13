from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_list$', views.get_list, name='get_list'),
    url(r'^upload$', views.AjaxPhotoUploadView.as_view(), name='upload'),
]
