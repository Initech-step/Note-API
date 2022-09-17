from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NotesSerializer, CategorySerializer
from api.models import Notes, Category
from rest_framework import status

# Create your views here.

class Index(APIView):
    def get(self, request):
        return Response({'success':True, 'message':'The index api'})


class NotesAPI(APIView):
    #add notes
    def post(self, request):
        validate_data = NotesSerializer(data=request.data)
        if validate_data.is_valid():
            validate_data.save()
            return Response(validate_data.data, status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 
        
    #get all notes
    def get(self, request):
        all_objects = Notes.objects.all()
        serialized = NotesSerializer(all_objects, many=True)
        return Response(serialized.data)


class CategoryAPI(APIView):
    def post(self, request):
        validate_data = CategorySerializer(data=request.data)
        if validate_data.is_valid():
            validate_data.save()
            return Response(validate_data.data, status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 
        
    #get all categories
    def get(self, request):
        all_objects = Category.objects.all()
        serialized = CategorySerializer(all_objects, many=True)
        return Response(serialized.data)


#get note, get, put, delete

class NoteDetail(APIView):
    def get(self, request, id):
        #try to get note
        try:
            get_note = Notes.objects.get(pk=id)
            friendly_category = get_note.category.category
            serialized = NotesSerializer(get_note)
            #converting to dict so i can make category friendly
            convert = dict(serialized.data)
            convert['category'] = friendly_category
            return Response(convert)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        #check validity of notes
        try:
            get_note = Notes.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        validate_data = NotesSerializer(data=request.data)
        if validate_data.is_valid():
            #check that the submited category is valid
            try:
                getcat = Category.objects.get(pk=validate_data.data['category'])
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            getstat = validate_data.update(get_note, validate_data.data, getcat)

            if getstat == False:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            get_note = Notes.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        get_note.delete()
        return Response(status=status.HTTP_200_OK)



class CategoryNotes(APIView):
    def get(self, request, id):
        try:
            get_category = Category.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        get_notes = Notes.objects.all().filter(category__id=id)
        serialized = NotesSerializer(get_notes, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)




class PreEdit(APIView):
    def get(self, request, id):
        #try to get note
        try:
            get_cat = Notes.objects.get(pk=id)
            serialized = NotesSerializer(get_cat)
            convert = dict(serialized.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        get_cat = Category.objects.all()
        serial = CategorySerializer(get_cat, many=True)
        convert_categories = list(serial.data)

        return JsonResponse({'status':True, 'note':convert, 'categories':convert_categories})