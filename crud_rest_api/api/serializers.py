from rest_framework import serializers
from .models import StudentModel
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100,default="")
    roll=serializers.IntegerField(default=0)
    city=serializers.CharField(max_length=100,default="")

# for update and insert you need to create a method in serializer.property
# not in the case of delete
    def create(self,validated_data):   #create means insert
        return StudentModel.objects.create(**validated_data)

    def update (self,instance,validate_data):
        instance.name= validate_data.get("name",instance.name)
        instance.roll= validate_data.get("roll",instance.roll)
        instance.city= validate_data.get("city",instance.city)
        instance.save()
        return instance
