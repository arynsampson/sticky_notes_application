Overview

Sticky Notes is a Django web application that allows users to create, view, edit, and delete notes. Each note has a title, content, owner, and topic. Topics are pre-populated with default values (Work, School, Admin, Other) and are rendered as a dropdown in forms. Owners can be entered as text fields, and a new owner is automatically created if it does not exist.

This application is designed for educational purposes and demonstrates:
- Django Models with ForeignKey relationships
- Forms with custom fields
- CRUD operations for notes
- Prepopulated data via data migrations
- Basic unit tests for models and views

Features
- Create Notes: Users can create new notes with a title, content, owner, and topic.
- View Notes: List all notes with details including owner and topic.
- Edit Notes: Update existing notes; owner and topic can be changed.
- Delete Notes: Remove notes from the database.
- Topic Management: Topics are automatically pre-populated and displayed as a dropdown in forms.
- Owner Management: Users can type an owner’s name when creating or editing a note; the system creates a new owner if needed.
