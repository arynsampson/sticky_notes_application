from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .models import Owner
from .models import Topic
from .forms import NoteForm

# Create your views here.


def notes_list(request):
    '''
    View to display a list of all sticky notes.

    :param request: HTTP request object.
    :return: Rendered template with a list of sticky notes.
    '''
    notes = Note.objects.all()

    context = {
        "notes": notes,
    }

    return render(request, "notes/notes_list.html", context)


def note_detail(request, pk):
    '''
    View to display details of a specific sticky note.

    :param request: HTTP request object.
    :param pk: Primary key of the sticky note.
    :return: Rendered template with details of the specified sticky note.
    '''
    note = get_object_or_404(Note, pk=pk)

    context = {
        "note": note,
        "show_home_button": True,
    }

    return render(request, "notes/note_detail.html", context)


def note_create(request):
    '''
    View to display creating a new sticky note.

    :param request: HTTP request object.
    :return: Rendered template for creating a new sticky note.
    '''
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            owner, created = Owner.objects.get_or_create(name=owner_name)
            topic = Topic.objects.get(pk=1)
            note = form.save(commit=False)
            note.topic = topic
            note.owner = owner
            note.save()
            return redirect("notes_list")
    else:
        form = NoteForm()

    context = {
        "form": form,
        "show_home_button": True,
    }
    return render(request, "notes/note_form.html", context)


def note_update(request, pk):
    '''
    View to display updating a sticky note.

    :param request: HTTP request object.
    :param pk: Primary key of the sticky note.
    :return: Rendered template for updating a sticky note.
    '''
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            owner, created = Owner.objects.get_or_create(name=owner_name)
            note = form.save(commit=False)
            note.owner = owner
            note.save()
            return redirect("notes_list")
    else:
        form = NoteForm(instance=note,
                        initial={
                            "owner_name": note.owner.name
                        })

    context = {
        "form": form,
        "show_home_button": True,
    }
    return render(request, "notes/note_form.html", context)


def note_delete(request, pk):
    '''
    Docstring for note_delete

    :param request: HTTP request object.
    :param pk: Primary key of the sticky note that is to be deleted.
    :return: Redirect to list of sticky notes after deletion.
    '''
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("notes_list")
