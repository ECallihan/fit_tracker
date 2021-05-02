from django.urls import path
from .views import home,  new_exercise, new_entry, add_details, create_entry_with_exercises

urlpatterns = [
    path('', home, name='home'),
    # path('add_exercise/', add_exercise, name='add_exercise'),
    path('new_exercise/', new_exercise, name='new_exercise'),
    path('new_entry/', new_entry, name='new_entry'),
    path('add_details/', add_details, name='add_details'),
    path('entry/', create_entry_with_exercises, name='entry'),

]
