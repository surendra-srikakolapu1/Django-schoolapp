from django.contrib import admin

from .models import *



class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','contact']

class FeeAdmin(admin.ModelAdmin):
    list_display=['id','student','total_fee','fees_paid','fees_due' , 'paid_date']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','firstname','lastname','gender','age' , 'subject','email','contact','address']

class Id_cardAdmin(admin.ModelAdmin):
    list_display=['id','studentname' , 'reg_no' , 'fathername' , 'dob' , 'classname' , 'bloodgroup' , 'resident_add' , 'permanent_add' , 'image']


# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Fee,FeeAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Id_card,Id_cardAdmin)
