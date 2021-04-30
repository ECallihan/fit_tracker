from django.urls import path
from .views import home, add_exercise, new_exercise

urlpatterns = [
    path('', home, name='home'),
    path('add_exercise/', add_exercise, name='add_exercise'),
    path('new_exercise/', new_exercise, name='new_exercise')
]
