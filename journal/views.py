from django.shortcuts import render
from .models import Entry, Exercise, Exercise_Set, Technique
from django.contrib import messages
from .forms import TechniqueForm

# Create your views here.


def home(request):
    entries = Entry.objects.all().filter(user_id=request.user.id)
    entry_ids = list(entries.values_list('entry_id', flat=True))
    techniques = Technique.objects.all().filter(user_id=request.user.id)
    exercises = Exercise.objects.all().filter(exercise_id__in=entry_ids)
    exercise_ids = list(exercises.values_list('exercise_id', flat=True))
    exercise_sets = Exercise_Set.objects.all().filter(
        exercise_set_id__in=exercise_ids)
    return render(request, 'home.html', {'entries': entries,
                                         'techniques': techniques,
                                         'exercises': exercises,
                                         'exercise_sets': exercise_sets})


def new_exercise(request):
    message = ''
    if request.method == 'POST':
        post = request.POST.copy()
        post['user_id'] = request.user.id
        form = TechniqueForm(post)
        if form.is_valid():
            form.save()

            message = f'successfully added {post["technique_name"]} to available exercises.'
            my_moves_query = Technique.objects.all().filter(user_id_id=request.user.id)
            my_moves = list(my_moves_query.values_list(
                'technique_name', flat=True))
            return render(request, 'journal/new_exercise.html', {'form': form,
                                                                 'message': message,
                                                                 'my_moves': my_moves})

    form = TechniqueForm()
    my_moves_query = Technique.objects.all().filter(user_id_id=request.user.id)
    my_moves = list(my_moves_query.values_list(
        'technique_name', flat=True))
    return render(request, 'journal/new_exercise.html', {'form': form,
                                                         'message': message,
                                                         'my_moves': my_moves})


def new_entry(request):

    return render(request, 'journal/new_entry.html', {})
