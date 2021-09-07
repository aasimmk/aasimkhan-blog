from django.urls import path

from core.views import ContactFormView


app_name = 'core'

urlpatterns = (
    path('contact/', ContactFormView.as_view(), name='contact_form_view'),
)
