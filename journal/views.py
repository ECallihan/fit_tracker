from django.shortcuts import render
from .models import Entry, Exercise, Exercise_Set, Technique
from django.contrib import messages

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
    return render(request, 'journal/new_exercise.html', {})


def add_exercise(request):
    if request.method == 'POST':
        p = request.POST
        if ((p.get('name') and ((p.get('stength') == "1") or
                                (p.get('cardio') == "1") or
                                (p.get('flexibility') == "1"))) and
            (p.get('reps') == "1" or
             (p.get('duration') == "1") or
             (p.get('resistance') == "1"))):
            post = Technique()
            post.technique_name = p.get('name')
            post.for_strength = True if p.get('strength') == "1" else False
            post.for_flexibility = True if p.get(
                'flexibility') == "1" else False
            post.for_cardio = True if p.get('cardio') == "1" else False
            post.has_reps = True if p.get('reps') == "1" else False
            post.has_resistance = True if p.get('resistance') == "1" else False
            post.has_time = True if p.get('duration') == "1" else False
            post.save()
            messages.success(request, "Exercise Added.")
            return render(request, 'journal/new_exercise.html', {})
        else:
            messages.error(
                request, "Exercises must have a name, at least 1 type and at least 1 metric.")
            return render(request, 'journal/new_exercise.html', {})
    else:
        return render(request, 'journal/new_exercise.html', {})
