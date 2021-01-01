from django.urls import path
from .views import CreateTest

urlpatterns = [
    path('', CreateTest.as_view())
]
