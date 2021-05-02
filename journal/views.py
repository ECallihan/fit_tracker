from django.http import response
from django.shortcuts import redirect, render
from .models import Entry, Exercise_Set, Technique
from django.contrib import messages
from .forms import EntryForm, Exercise_SetFormset, TechniqueForm

# Create your views here.


def home(request):
    entries = Entry.objects.all().filter(user_id=request.user.id)
    entry_ids = list(entries.values_list('entry_id', flat=True))
    techniques = Technique.objects.all().filter(user_id=request.user.id)
    exercise_sets = Exercise_Set.objects.all().filter(
        exercise_set_id__in=entry_ids)
    return render(request, 'home.html', {'entries': entries,
                                         'techniques': techniques,
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
    if request.method == 'POST':
        pass

    form = EntryForm()
    return render(request, 'journal/new_entry.html', {'form': form})


def add_details(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['user_id'] = request.user.id
        form = EntryForm(post)
        if form.is_valid():
            my_model = form.save()
            response = {}
            response['id'] = my_model.entry_id
            response['model'] = my_model
            response['form'] = add_details

            return render(request, 'journal/add_details.html', response)


def create_entry_with_exercises(request):
    template_name = 'journal/entry.html'
    if request.method == 'GET':
        entryform = EntryForm(request.GET or None)
        exercise_set_formset = Exercise_SetFormset(
            queryset=Exercise_Set.objects.none())
        techniques = Technique.objects.all().filter(user_id=request.user.id)
    elif request.method == 'POST':

        edited_post = request.POST.copy()
        edited_post['user_id'] = request.user.id

        entryform = EntryForm(edited_post)
        exercise_set_formset = Exercise_SetFormset(request.POST)
        if entryform.is_valid() and exercise_set_formset.is_valid():
            # save the entryform first so it can be referenced by the
            # Exercise formset
            entry = entryform.save()
            for i in range(len(exercise_set_formset)):
                exercise_set = exercise_set_formset[i].save(commit=False)
                exercise_set.entry_id = entry
                tech_id = request.POST.get(f'techniques{i}')
                print("The result of technique string is: " +
                      request.POST.get(f'techniques{i}'))
                tech = Technique.objects.get(tech_id=tech_id)
                exercise_set.technique_id = tech
                exercise_set.save()
            # for form in exercise_set_formset:
            #     # so the entry can be attatched to the set instance
            #     exercise_set = form.save(commit=False)
            #     exercise_set.entry_id = entry
            #     exercise_set.technique_id = request.POST.get('techniques')

            #     # exercise_set.technique_id
            #     exercise_set.save()
            return redirect(home)
    return render(request, template_name, {
        'entryform': entryform,
        'exercise_set_formset': exercise_set_formset,
        'techniques': techniques,
    })
