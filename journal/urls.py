from django.urls import path
from .views import home,  new_exercise, new_entry

urlpatterns = [
    path('', home, name='home'),
    # path('add_exercise/', add_exercise, name='add_exercise'),
    path('new_exercise/', new_exercise, name='new_exercise'),
    path('new_entry/', new_entry, name='new_entry'),
]
