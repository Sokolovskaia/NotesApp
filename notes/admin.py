from django.contrib import admin

# Register your models here.
from notes.models import Author, Tag, Note

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Note)