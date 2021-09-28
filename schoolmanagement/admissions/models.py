from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=1000 , verbose_name = "STUDENT FULL NAME" )
    fathername = models.CharField(max_length=1000 , verbose_name = "FATHER NAME")

    CLASSNAME_CHOICES =(
         ('Nursery' , 'Nursery'),
         ('L.K.G' , 'L.K.G'),
         ('U.K.G' , 'U.K.G'),
         ('1ˢᵗ' , '1ˢᵗ'),
         ('2ⁿᵈ' , '2ⁿᵈ'),
         ('3ʳᵈ' , '3ʳᵈ'),
         ('4ᵗʰ' , '4ᵗʰ'),
         ('5ᵗʰ' , '5ᵗʰ'),
         ('6ᵗʰ' , '6ᵗʰ'),
         ('7ᵗʰ' , '7ᵗʰ'),
         ('8ᵗʰ' , '8ᵗʰ'),
         ('9ᵗʰ' , '9ᵗʰ'),
         ('10ᵗʰ' , '10ᵗʰ'),
    )

    classname = models.CharField(max_length=30 , choices=CLASSNAME_CHOICES , verbose_name = "CLASS")

    contact = models.CharField(max_length=30 , verbose_name = "CONTACT")
    email = models.EmailField(null = True , verbose_name = "EMAIL")

    def __str__(self):
        return self.name


class Fee(models.Model):
    student = models.OneToOneField(Student , on_delete = models.CASCADE, unique=True , verbose_name = "STUDENT")
    total_fee = models.CharField(max_length=30 , null = True , verbose_name = "TOTAL FEE")
    fees_paid = models.CharField(max_length=30 , null = True , verbose_name = "PAID FEE")
    fees_due = models.CharField(max_length=30 , null = True , verbose_name = "DUE FEE")

    books_fee =  models.CharField(max_length=30 , null=True , verbose_name = "BOOKS FEE")

    BOOKS_CHOICES = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
    )
    books_paid = models.CharField(max_length=10, choices=BOOKS_CHOICES , null = True , verbose_name = "BOOKS PAID")

    paid_date = models.DateField(null = True , verbose_name = "PAID DATE")

    def __str__(self):
        return self.student.name





class Teacher(models.Model):
    firstname = models.CharField(max_length=30 , verbose_name = "FIRST NAME")
    lastname = models.CharField(max_length=30 , verbose_name = "LAST NAME")


    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES , verbose_name = "GENDER")

    age = models.PositiveIntegerField(verbose_name = "AGE")

    SUBJECT_CHOICES = (
        ('Mathematics', 'Mathematics'),
        ('Telugu', 'Telugu'),
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Science', 'Science'),
        ('Social', 'Social'),
    )
    subject = models.CharField(max_length=15 , choices=SUBJECT_CHOICES , verbose_name = "SUBJECT")

    email = models.EmailField(max_length=40 , verbose_name = "EMAIL")
    contact = models.CharField(max_length=30 , verbose_name = "CONTACT")
    address = models.CharField(max_length=400 , verbose_name = "ADDRESS")

    def __str__(self):
        return self.firstname





class Id_card(models.Model):
    studentname = models.CharField(max_length=1000 ,  verbose_name = "Student Full Name")
    reg_no = models.PositiveIntegerField( verbose_name = "Registration Number")
    fathername = models.CharField(max_length=1000 ,  verbose_name = "Father Name")
    dob = models.DateField( verbose_name = "Date Of Birth")

    CLASSNAME_CHOICES =(
         ('Nursery' , 'Nursery'),
         ('L.K.G' , 'L.K.G'),
         ('U.K.G' , 'U.K.G'),
         ('1ˢᵗ' , '1ˢᵗ'),
         ('2ⁿᵈ' , '2ⁿᵈ'),
         ('3ʳᵈ' , '3ʳᵈ'),
         ('4ᵗʰ' , '4ᵗʰ'),
         ('5ᵗʰ' , '5ᵗʰ'),
         ('6ᵗʰ' , '6ᵗʰ'),
         ('7ᵗʰ' , '7ᵗʰ'),
         ('8ᵗʰ' , '8ᵗʰ'),
         ('9ᵗʰ' , '9ᵗʰ'),
         ('10ᵗʰ' , '10ᵗʰ'),
    )

    classname = models.CharField(max_length=30 , choices=CLASSNAME_CHOICES ,  verbose_name = "Class")

    BLOODGROUP_CHOICES =(
         ('A+' , 'A+'),
         ('A-' , 'A-'),
         ('B+' , 'B+'),
         ('B-' , 'B-'),
         ('O+' , 'O+'),
         ('O-' , 'O-'),
         ('AB+' , 'AB+'),
         ('AB-' , 'AB-'),

    )

    bloodgroup = models.CharField(max_length=30 , choices=BLOODGROUP_CHOICES ,  verbose_name = "Blood Group")

    resident_add = models.CharField(max_length=2000 ,  verbose_name = "Residential Address")

    permanent_add = models.CharField(max_length=2000 ,  verbose_name = "Permanent Address")

    image = models.ImageField(upload_to ='media/' , null = True ,  verbose_name = "Student Photo Id")

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



    def __str__(self):
        return self.studentname
