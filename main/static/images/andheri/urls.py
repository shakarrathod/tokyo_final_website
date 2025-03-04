from django.urls import path

from . import views
from .views import index, murugeshpalya

from .views import index

urlpatterns = [
    path('andheri/', index, name='andheri_home'),
    path('murugeshpalya/', murugeshpalya, name='murugeshpalya'),


    path("payment_form/", views.payment_form, name="payment_form"),
    path("payment_success/", views.payment_success, name="payment_success"),

    path("download_pdf/<str:payment_id>/", views.download_pdf, name="download_pdf"),
]




   
