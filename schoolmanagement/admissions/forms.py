from django import forms
from .models import *



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name' , 'fathername' , 'classname' , 'contact' , 'email']

class FeeModelForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['student' , 'total_fee' , 'fees_paid' , 'fees_due' , 'books_fee' , 'books_paid' ,'paid_date']

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname' , 'lastname' , 'gender' , 'age' , 'subject' , 'email' , 'contact' , 'address']


class Id_cardModelForm(forms.ModelForm):
    class Meta:
        model = Id_card
        fields = ['id' , 'studentname' , 'reg_no' , 'fathername' , 'dob' , 'classname' , 'bloodgroup' , 'resident_add' , 'permanent_add' , 'image']
