from rest_framework import serializers
from .models import Notes, Category


class NotesSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data, getCategory):
        try:
            instance.note = validated_data.get('note', instance.note)
            instance.category = getCategory
            instance.save()
            return instance
        except:
            return False


    class Meta:
        model = Notes
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
