from django.contrib import admin
from api.models import StudentModel
# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=["id","name","roll","city"]