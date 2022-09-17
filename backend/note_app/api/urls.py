from . import views
from django.urls import path

"""
when django finds 
the matching pattern it will call the function with the 
http request object as the first parameter
"""

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # post and get all notes
    path('note/', views.NotesAPI.as_view(), name='notes'),

    #get note, put, delete
    path('note/<int:id>/', views.NoteDetail.as_view(), name='notedetail'),

    #posting and getting all categories
    path('category/', views.CategoryAPI.as_view(), name='category'),

    path('predit/<int:id>/', views.PreEdit.as_view(), name='predit'),

    #get all notes by category
    path('category/<int:id>/notes/', views.CategoryNotes.as_view(), name='categorynotes'),

    
]
