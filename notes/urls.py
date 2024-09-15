from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('projects/', projects, name='projects'),
    path('notes/', notes, name='notes'),
    path('notes/add', create_note, name='create_note'),
    path('notes/<int:note_id>', edit_note, name='edit_note')
]