from django.shortcuts import render, redirect
from .models import Project, Note

from .forms import NoteForm


def index(request):
    note_obj = Note.objects.get(pk=1)
    note = NoteForm(instance=note_obj)
    context = {'note': note}
    return render(request, template_name='notes/home.html', context=context)


def projects(request):
    if not request.user.is_anonymous:
        projects = Project.objects.filter(owner=request.user)
        context = {'projects': projects}
        return render(request, template_name='notes/projects.html', context=context)
    else:
        return render(request, template_name='notes/projects.html')


def notes(request):
    if not request.user.is_anonymous:
        notes_obj = Note.objects.filter(owner=request.user).order_by('-date_created')
        notes = [NoteForm(instance=note) for note in notes_obj]
        context = {'notes': notes}
        return render(request, template_name='notes/notes.html', context=context)
    else:
        return render(request, template_name='notes/not_authorized.html')


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_note = Note.objects.create(owner=request.user,
                                           title=cd['title'],
                                           description=cd['description'])
            new_note.save()
            notes_obj = Note.objects.filter(owner=request.user)
            notes = [NoteForm(instance=note) for note in notes_obj]
            empty_form = NoteForm()
            context = {'notes': notes, 'empty': empty_form}
            return redirect('notes')
    else:
        form=NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})



def edit_note(request, note_id):
    try:
        note = Note.objects.get(owner=request.user, id=note_id)
        if request.method == 'POST':
            form = NoteForm(request.POST, instance=note)
            if form.is_valid():
                cd = form.cleaned_data
                note.title=cd['title']
                note.description=cd['description']
                note.save()
                notes = Note.objects.filter(owner=request.user)
                context = {'notes': notes}
                return render(request, 'notes/notes.html', context=context)
        else:
            form=NoteForm(instance=note)
        return render(request, 'notes/edit_note.html', {'form': form})
    except Exception as e:
        print(e.args)
        return redirect('notes')



def delete_note(request, note_id):
    try:
        note = Note.objects.get(owner=request.user, id=note_id)
        note.delete()
    except Exception as e:
        print(e)
    return redirect('notes')

