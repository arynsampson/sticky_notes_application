from django.test import TestCase
from django.urls import reverse
from .models import Note
from .models import Owner
from .models import Topic


# Create your tests here.
class OwnerModelTest(TestCase):
    def setUp(self):
        owner, created = Owner.objects.get_or_create(name="John")
        self.assertEqual(owner.name, "John")
        self.assertEqual(str(owner), "John")

    def test_owner_name(self):
        owner = Owner.objects.get(id=1)
        self.assertEqual(owner.name, "John")


class NoteModelTest(TestCase):
    def setUp(self):
        self.owner, created = Owner.objects.get_or_create(name="Jane")
        self.topic, created = Topic.objects.get_or_create(name="Admin")

        self.note = Note.objects.create(title="My first note!",
                                        content="This is text content",
                                        owner=self.owner,
                                        topic=self.topic)

    def test_note_has_title(self):
        self.assertEqual(self.note.title, "My first note!")

    def test_note_has_owner(self):
        self.assertEqual(self.note.owner.name, "Jane")

    def test_note_has_content(self):
        self.assertEqual(self.note.content, "This is text content")

    def test_note_has_topic(self):
        self.assertEqual(self.note.topic.name, "Admin")

    def test_update_note_title(self):
        self.note.title = "My first note!"
        self.note.save()
        updated_note_object = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note_object.title,
                         "My first note!")

    def test_update_note_content(self):
        self.note.content = "BLAH new content value from the test!"
        self.note.save()
        updated_note_object = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note_object.content,
                         "BLAH new content value from the test!")

    def test_delete_note(self):
        self.note.delete()
        self.assertEqual(Note.objects.count(), 0)


class NoteViewTest(TestCase):
    def setUp(self):
        self.owner, created = Owner.objects.get_or_create(name="Bruh")
        self.topic, created = Topic.objects.get_or_create(name="School")

        self.note = Note.objects.create(title="My Note to view on page",
                                        content="This is for testing "
                                        "the UI page.",
                                        owner=self.owner,
                                        topic=self.topic)

    def test_note_list_view(self):
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Note to view on page")

    def test_note_detail_view(self):
        response = self.client.get(reverse("note_detail",
                                           args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Note to view on page")
        self.assertContains(response, "This is for testing the UI page.")

    def test_note_edit_view(self):
        response = self.client.get(reverse("note_update",
                                           args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Note to view on page")
        self.assertContains(response, "This is for testing the UI page.")
