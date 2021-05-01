from django.db.models import fields
from .models import Technique, Entry, Exercise, Exercise_Set
from django import forms


class TechniqueForm(forms.ModelForm):
    class Meta:
        model = Technique
        fields = ('user_id', 'technique_name', 'for_strength',
                  'for_cardio', 'for_flexibility', 'has_time',
                  'has_resistance', 'has_reps')
