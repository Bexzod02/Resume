from django.urls import path
from .views import single_view

app_name = 'posts'

urlpatterns = [
    path('', single_view, name='single'),
]
