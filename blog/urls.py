from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('form_contact/', views.form_contact, name='form_contact'),
    path('form_submit/', views.submited_form),
]