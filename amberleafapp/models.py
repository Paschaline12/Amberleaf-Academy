from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=250)
    nameofparent = models.CharField(max_length=250)
    admissionno = models.CharField(max_length=15,unique=True)
    photo = models.ImageField()
    gradelevel = models.CharField(max_length= 200)
    age = models.IntegerField()
    yob = models.DateField()
    gender = models.CharField(max_length=19,choices=[('Male','Male'), ('Female','Female'), ('other','other')])
    address = models.CharField(max_length=50)
    joindate = models.DateField()
    def __str__(self):
        return self.fullname
    
class Parent(models.Model):
    fullname = models.CharField(max_length=250)
    nameofchild = models.CharField(max_length=200)
    age = models.IntegerField()
    yob = models.DateField()
    gender = models.CharField(max_length=19,choices=[('Male','Male'), ('Female','Female'), ('other','other')])
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField()
    address = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    def __str__(self):
        return self.fullname
    
class Teacher(models.Model):
    fullname = models.CharField(max_length=200)
    age = models.IntegerField()
    yob = models.DateField()
    payrollNo = models.CharField(max_length=15,unique=True)
    hireDate = models.CharField(max_length=15)
    photo = models.ImageField()
    subjects = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=19,choices=[('Male','Male'), ('Female','Female'), ('other','other')])
    address = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=14,decimal_places=4)
    experience = models.CharField(max_length=400)
    def __str__(self):
        return self.fullname

class Interview(models.Model):
    name_of_student = models.CharField(max_length=255, default='Default Name')
    grade = models.CharField(max_length=50)
    age = models.IntegerField()
    name_of_parent = models.CharField(max_length=255, default='Default Name')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, default='Default Phone Number')
    date_of_interview = models.DateField()
    message = models.TextField()
    def __str__(self):
        return self.name_of_student
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Member(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.fullname

class Transport(models.Model):
    student_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=50)
    address = models.TextField()
    parent_phone = models.CharField(max_length=15)
    pickup_time = models.TimeField()

    def __str__(self):
        return f"{self.student_name} - {self.grade}"

class SwimmingBooking(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    grade = models.CharField(max_length=50, verbose_name="Grade")
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        verbose_name="Gender"
    )
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name="Booking Date")

    def __str__(self):
        return f"{self.name} ({self.grade} - {self.gender})"

class YogaBooking(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    grade = models.CharField(max_length=50, verbose_name="Grade")
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        verbose_name="Gender"
    )
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name="Booking Date")

    def __str__(self):
        return f"{self.name} ({self.grade} - {self.gender})"
    
class SkateBooking(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    grade = models.CharField(max_length=50, verbose_name="Grade")
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        verbose_name="Gender"
    )
    booking_date = models.DateTimeField(auto_now_add=True, verbose_name="Booking Date")

    def __str__(self):
        return f"{self.name} ({self.grade} - {self.gender})"
    
class NoneTeaching(models.Model):
    fullname = models.CharField(max_length=200)
    age = models.IntegerField()
    yob = models.DateField()
    payrollNo = models.CharField(max_length=15,unique=True)
    hireDate = models.CharField(max_length=15)
    photo = models.ImageField()
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=19,choices=[('Male','Male'), ('Female','Female'), ('other','other')])
    address = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=14,decimal_places=4)
    def __str__(self):
        return self.fullname

class ImageDirectorModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    narration = models.CharField(max_length=500, default='Default narration text', blank=True)

    def __str__(self):
        return self.title

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    essay = models.CharField(max_length=500)

    def __str__(self):
        return self.title
