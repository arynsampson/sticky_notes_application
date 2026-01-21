from django.test import TestCase
from django.urls import reverse
from .models import Note
from .models import Owner
from .models import Topic


# Create your tests here.
class OwnerModelTest(TestCase):
    '''
    Test suite for the Owner model.

    These tests verify that Owner instances are created correctly,
    have the expected string representation, and store the correct
    name value in the database.
    '''

    def setUp(self):
        '''
        Create an Owner instance for use in tests.

        Ensures that an Owner with the name "John" can be created
        (or retrieved if it already exists) and that its string
        representation returns the owner's name.
        '''
        owner, created = Owner.objects.get_or_create(name="John")
        self.assertEqual(owner.name, "John")
        self.assertEqual(str(owner), "John")

    def test_owner_name(self):
        '''
        Test that the Owner name is stored and retrieved correctly.

        Fetches the Owner instance from the database and verifies
        that the name field matches the expected value.
        '''
        owner = Owner.objects.get(name="John")
        self.assertEqual(owner.name, "John")


class NoteModelTest(TestCase):
    '''
    Test suite for the Note model.

    These tests verify that Note instances are created correctly,
    store the expected field values, can be updated, and can be
    deleted from the database.
    '''
    def setUp(self):
        '''
        Create test data for Note model tests.

        Sets up an Owner, a Topic, and a Note instance that will be
        reused across all model-related tests.
        '''
        self.owner, created = Owner.objects.get_or_create(name="Jane")
        self.topic, created = Topic.objects.get_or_create(name="Admin")

        self.note = Note.objects.create(title="My first note!",
                                        content="This is text content",
                                        owner=self.owner,
                                        topic=self.topic)

    def test_note_has_title(self):
        '''
        Test that a Note has the correct title.

        Ensures the title field is stored and retrieved correctly.
        '''
        self.assertEqual(self.note.title, "My first note!")

    def test_note_has_owner(self):
        '''
        Test that a Note is associated with the correct Owner.

        Ensures the owner relationship is set correctly.
        '''
        self.assertEqual(self.note.owner.name, "Jane")

    def test_note_has_content(self):
        '''
        Test that a Note has the correct content.

        Ensures the content field is stored and retrieved correctly.
        '''
        self.assertEqual(self.note.content, "This is text content")

    def test_note_has_topic(self):
        '''
        Test that a Note is associated with the correct Topic.

        Ensures the topic relationship is set correctly.
        '''
        self.assertEqual(self.note.topic.name, "Admin")

    def test_update_note_title(self):
        '''
        Test updating a Note's title.

        Ensures that changes to the title field are saved
        and persisted in the database.
        '''
        self.note.title = "My first note!"
        self.note.save()
        updated_note_object = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note_object.title,
                         "My first note!")

    def test_update_note_content(self):
        '''
        Test updating a Note's content.

        Ensures that changes to the content field are saved
        and persisted in the database.
        '''
        self.note.content = "BLAH new content value from the test!"
        self.note.save()
        updated_note_object = Note.objects.get(id=self.note.id)
        self.assertEqual(updated_note_object.content,
                         "BLAH new content value from the test!")

    def test_delete_note(self):
        '''
        Test deleting a Note.

        Ensures that a Note instance can be deleted
        and is removed from the database.
        '''
        self.note.delete()
        self.assertEqual(Note.objects.count(), 0)


class NoteViewTest(TestCase):
    '''
    Test suite for Note-related views.

    These tests verify that the list, detail, and edit views for
    Note objects load successfully and display the correct content.
    '''
    def setUp(self):
        '''
        Create test data for Note view tests.

        Sets up an Owner, a Topic, and a Note instance that will be
        used across all view tests to ensure consistent test data.
        '''
        self.owner, created = Owner.objects.get_or_create(name="Bruh")
        self.topic, created = Topic.objects.get_or_create(name="School")

        self.note = Note.objects.create(title="My Note to view on page",
                                        content="This is for testing "
                                        "the UI page.",
                                        owner=self.owner,
                                        topic=self.topic)

    def test_note_list_view(self):
        '''
        Test that the note list view loads correctly.

        Ensures the list view returns an HTTP 200 response and
        displays the title of the created note.
        '''
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Note to view on page")

    def test_note_detail_view(self):
        '''
        Test that the note detail view displays the correct note.

        Ensures the detail view returns an HTTP 200 response and
        shows both the note title and content.
        '''
        response = self.client.get(reverse("note_detail",
                                           args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Note to view on page")
        self.assertContains(response, "This is for testing the UI page.")

    def test_note_edit_view(self):
        '''
        Test that the note edit view loads correctly.

        Ensures the edit (update) view returns an HTTP 200 response
        and pre-populates the form with the note's existing data.
        '''
        response = self.client.get(reverse("note_update",
                                           args=[str(self.note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Note to view on page")
        self.assertContains(response, "This is for testing the UI page.")
