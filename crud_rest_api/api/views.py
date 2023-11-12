from django.shortcuts import render
import io
from api.serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from api.models import StudentModel
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# process to read the data or retive the data
def student_retrive_data(request):
    if(request.method == "GET"):
        json_data=request.body
        stream = io.BytesIO(json_data)
        #JSONParser because we dealing with request
        python_data=JSONParser().parse(stream)
        #python data contains all the data coming from request
        #so we will get id from it
        id=python_data.get('id',None) #if id not found give none
        if id is not None:
            stu=StudentModel.objects.get(id=id)
            serialize_data=StudentSerializer(stu)
            # if serialize_data.is_valid():
            #     serialize_data.save()
            json_data=JSONRenderer().render(serialize_data.data)
            return HttpResponse(json_data,content_type="application/json")
       
        # will give all the data from the table
        stu1 = StudentModel.objects.all()
        serializer = StudentSerializer(stu1,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")


# added csrf token 
@csrf_exempt 
def student_insert_data(request):
    if(request.method == "POST"):
        json_data= request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        seralize_data=StudentSerializer(data=python_data)
        if (seralize_data.is_valid()):
            seralize_data.save()
            msg={"msg":"data inserted successfully"}
            jsondata= JSONRenderer().render(msg)
            return HttpResponse(jsondata, content_type="application/json")
        jsondata=JSONRenderer().render(seralize_data.errors)
        return HttpResponse(jsondata, content_type="application/json")

@csrf_exempt 
def student_update_data(request):
    if(request.method == "PUT"):
        json_data=request.body
        stream = io.BytesIO(json_data)
        #JSONParser because we dealing with request
        python_data=JSONParser().parse(stream)
        #python data contains all the data coming from request
        #so we will get id from it
        id=python_data.get('id') 
        stu=StudentModel.objects.get(id=id)
        serialize_data=StudentSerializer(stu, data=python_data)
        if (serialize_data.is_valid()):
            serialize_data.save()
            msg={"msg":"data updated successfully"}
            jsondata= JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        jsondata=JSONRenderer().render(serialize_data.errors)
        return HttpResponse(jsondata, content_type="application/json")
       
        
@csrf_exempt 
def student_delete_data(request):
    if(request.method == "DELETE"):
        json_data=request.body
        stream = io.BytesIO(json_data)
        #JSONParser because we dealing with request
        python_data=JSONParser().parse(stream)
        #python data contains all the data coming from request
        #so we will get id from it
        id=python_data.get('id') 
        stu=StudentModel.objects.get(id=id)
        stu.delete()
        msg={"msg":"data deleted successfully"}
        jsondata= JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type="application/json")
