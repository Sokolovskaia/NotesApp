from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from notes.models import Author, Note


def authors(request: HttpRequest):
    return render(
        request,
        template_name='authors.html',
        context={
            'authors': Author.objects.all()[:5]
        }
    )


def author(request: HttpRequest, author_id: int):
    return render(
        request,
        template_name='author.html',
        context={
            'author': Author.objects.get(id=author_id),
            'notes': Note.objects.filter(author_id=author_id)[:5]
        }
    )


def notes(request: HttpRequest, author_id: int):
    return HttpResponse(Note.objects.filter(author_id=author_id))


def note(request: HttpRequest, author_id: int, note_id: int):
    return render(
        request,
        template_name='note.html',
        context={
            'note': Note.objects.get(author_id=author_id, id=note_id)
        }
    )
