from django.urls import path
from Ecommerceapp import views


urlpatterns = [
    path(" ", views.index, name="index"),
    path("Contact ", views.Contact, name="Contact"),
    path("About ", views.About, name="About"),
]
