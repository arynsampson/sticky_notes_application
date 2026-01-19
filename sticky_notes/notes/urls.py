from django.urls import path
from .views import (
    notes_list,
    note_detail,
    note_create,
    note_update,
    note_delete,
)

urlpatterns = [
    # URL for displaying all sticky notes
    path("", notes_list, name="notes_list"),

    # URL for displaying details of a specific sticky note
    path("note/<int:pk>/", note_detail, name="note_detail"),

    # URL for creating a new sticky note
    path("note/create/", note_create, name="note_create"),

    # URL for updating a sticky note
    path("note/<int:pk>/edit/", note_update, name="note_update"),

    # URL for deleting a sticky note
    path("note/<int:pk>/delete/", note_delete, name="note_delete"),
]
