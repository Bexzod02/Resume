from django.urls import path
from .views import person_vew, single_view
app_name = 'person'

urlpatterns = [
    path('', person_vew, name='person'),
    path('single/<slug:slug>/', single_view,  name='single'),
]