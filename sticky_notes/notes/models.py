from django.db import models

# Create your models here.


class Note(models.Model):
    '''
    Model representing a sticky note.

    Fields:
    - title: CharField for the note title with a maximum length of 35
    characters.
    - content: TextField for the note content.
    - owner: CharField for the note owner.
    - topic: DropDown showing the prepopulated topic options.
    - created_at: DateTime field for the date and time the note was created.

    Methods:
    - __str__: Returns a string representation of the note, showing the title.

    :param models.Model: Django's base model class.
    '''
    title = models.CharField(max_length=35)
    content = models.TextField()
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE)
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Owner(models.Model):
    '''
    Model representing an owner of a note.

    Fields:
    - name: CharField for the note title with a maximum length of 50
    characters.

    Methods:
    - __str__: Returns a string representation of the owner.

    :param models.Model: Django's base model class.
    '''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Topic(models.Model):
    '''
    Model representing the topics.

    Fields:
    - topic: DropDown for the topic options with a maximum length of 20
    characters.

    Methods:
    - __str__: Returns a string representation of the topics.

    :param models.Model: Django's base model class.
    '''
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
