from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    '''
    Form for creating and updating Note objects.

    Fields:
    - title: CharField for the sticky note title.
    - content: TextField for the sticky note content.
    - owner_name: CharField to input the name of the sticky note owner.

    Meta class:
    - Defines the model to use (Note) and the fields to include in the
    form.

    :param forms.ModelForm: Django's ModelForm class.
    '''

    owner_name = forms.CharField(max_length=50, label="Owner")

    class Meta:
        model = Note
        fields = ["title", "content", "owner_name", "topic"]
