from django.db import migrations


def create_default_topics(apps, schema_editor):
    Topic = apps.get_model('notes', 'Topic')
    defaults = ["Work", "School", "Admin", "Other"]
    for name in defaults:
        Topic.objects.get_or_create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_topics),
    ]
