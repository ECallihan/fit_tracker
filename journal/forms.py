from django.db.models import fields
from django.forms import widgets
from .models import Technique, Entry, Exercise_Set
from django import forms
from django.forms import modelformset_factory


class DateInput(forms.DateInput):
    input_type = 'date'


class TechniqueForm(forms.ModelForm):
    class Meta:
        model = Technique
        fields = ('user_id', 'technique_name', 'for_strength',
                  'for_cardio', 'for_flexibility', 'has_time',
                  'has_resistance', 'has_reps')


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('user_id', 'entry_date', 'entry_notes')
        widgets = {
            'entry_date': DateInput(),
            'entry_notes': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter notes here...'
            })

        }


Exercise_SetFormset = modelformset_factory(
    Exercise_Set,
    fields=('set_number', 'set_count', 'rep_count', 'weight', 'duration'),
    extra=1,

)
