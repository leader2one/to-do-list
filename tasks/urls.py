from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
path('', views.index, name='list'),
path('update_task/<str:pk>', views.update_task, name='update_task'),
path('delete_task/<str:pk>', views.delete_task, name='delete_task'),
path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.png'))),
]