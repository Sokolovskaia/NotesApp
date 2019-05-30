from django.db import models

# Create your models here.
from django.db.models import ManyToManyField


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'author id: {}, name: {}'. format(self.id, self.name)

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'tag id: {}, name: {}'. format(self.id, self.name)


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField(default='No Content')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = ManyToManyField(Tag)

    def __str__(self):
        return 'note id: {}, author: {}'. format(self.id, self.author.name)