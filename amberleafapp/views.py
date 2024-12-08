from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse
from amberleafapp.forms import InterviewForm,ImageDirectorModelForm,ImageUploadForm,ContactMessageForm, MemberForm, StudentForm, ParentForm,TeacherForm,TransportForm,SwimmingBookingForm,YogaBookingForm,SkateBookingForm,NoneTeachingForm

from amberleafapp.models import Interview,ImageDirectorModel,ImageModel,ContactMessage,Member,Student,Parent,Teacher,Transport,SwimmingBooking,YogaBooking,SkateBooking,NoneTeaching
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def terms(request):
        return render(request, 'terms.html')

def admission(request):
    return render(request, 'admission.html')

def cocuricular(request):
    return render(request, 'co-curicular.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect('/contact')
                        
        else:
            return HttpResponse("All fields are required.", status=400)
    
    return render(request, 'contact.html')
    
def academic(request):
    return render(request, 'curiculum.html')

def digitalschool(request):
    return render(request, 'digitalschool.html')

def facilities(request):
    return render(request, 'facilities.html')

def show(request):
    return render(request, 'show.html')

def galery(request):
    return render(request, 'galery.html')

def starter(request):
    return render(request, 'starter.html')
def teachers(request):
    return render(request, 'teachers.html')

def interview_view(request):
    if request.method == "POST":
     
        interview = Interview(
            name_of_student=request.POST.get('nameOfStudent', '').strip(),
            grade=request.POST.get('grade', '').strip(),
            age=request.POST.get('age', '').strip(),
            name_of_parent=request.POST.get('nameOfParent', '').strip(),
            email=request.POST.get('email', '').strip(),
            phone_number=request.POST.get('phoneNumber', '').strip(),
            date_of_interview=request.POST.get('dateOfInterview', '').strip(),
            message=request.POST.get('message', '').strip(),
        )
        
        interview.save()
        return redirect('/interview')  
    return render(request, 'interview.html')

def login(request):
    if request.method == "POST":
        if Member.objects.filter(username=request.POST['username'],password=request.POST['password'],).exists():
            authorized=Member.objects.get(username=request.POST['username'],password=request.POST['password'],)
            return render(request,'show.html',{'authorized':authorized})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        members=Member(
            fullname=request.POST['fullname'],
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
    
def showinterview(request):
    allinterviews=Interview.objects.all()
    return render(request, 'showinterview.html', {'interview':allinterviews})

def showmessage(request):
    allmessages=ContactMessage.objects.all()
    return render(request, 'showmessage.html', {'message':allmessages})

def showmember(request):
    allmembers=Member.objects.all()
    return render(request, 'showmember.html', {'member':allmembers})

def showstudent(request):
    allstudents=Student.objects.all()
    return render(request, 'showstudent.html', {'student':allstudents})

def addstudent(request):
    if request.method == "POST":
        students=Student(
            fullname = request.POST['fullname'],
            nameofparent = request.POST['nameofparent'],
            admissionno = request.POST['admissionno'],
            photo = request.FILES['photo'],
            gradelevel = request.POST['gradelevel'],
            age = request.POST['age'],
            yob = request.POST['yob'],
            gender = request.POST['gender'],
            address = request.POST['address'],
            joindate = request.POST['joindate']
        )
        students.save()
        return redirect('/show')
    else:
        return render(request, 'addstudents.html')
    
def showparent(request):
    allparents=Parent.objects.all()
    return render(request, 'showparent.html', {'parent':allparents})

def showteacher(request):
    allteachers=Teacher.objects.all()
    return render(request, 'showteacher.html', {'teacher':allteachers})

def addteacher(request):
    if request.method == "POST":
        teachers=Teacher(
            fullname = request.POST['fullname'],
            age = request.POST['age'],
            yob = request.POST['yob'],
            payrollNo = request.POST['payrollNo'],
            hireDate = request.POST['hireDate'],
            photo = request.POST['photo'],
            subjects = request.POST['subjects'],
            email = request.POST['email'],
            phoneNumber = request.POST['phoneNumber'],
            gender = request.POST['gender'],
            address = request.POST['address'],
            salary = request.POST['salary'],
            experience = request.POST['experience']
        )

        teachers.save()
        return redirect('/show')
    else:
        return render(request, 'addteacher.html')

def addparent(request):
    if request.method == "POST":
        parents=Parent(
            fullname = request.POST['fullname'],
            nameofchild= request.POST['nameofchild'],
            age = request.POST['age'],
            yob = request.POST['yob'],
            gender = request.POST['gender'],
            phonenumber = request.POST['phonenumber'],
            email = request.POST['email'],
            photo = request.P['photo'],
            address = request.POST['address'],
            occupation = request.POST['occupation']
            
        )
        parents.save()
        return redirect('/addparent')
    else:
        return render(request, 'addparent.html')
    
def directors(request):
    return render(request, 'directors.html')

def nonteachingstaff(request):
    return render(request, 'nonteachingstaff.html')

def transportbooking(request):
    if request.method == "POST":
        busbookings = Transport(
         student_name = request.POST['student_name'],
         grade = request.POST['grade'], 
         address = request.POST['address'],
         parent_phone = request.POST['parent_phone'],
          pickup_time = request.POST['pickup_time'] 
        )
        busbookings.save()
        return HttpResponse("Your child's bus booking is successful! <a href='/'>Return to Home</a>")
    else:
            return render(request, 'transportbooking.html')
    
def swimbooking(request):
    
    success_message = None
    error_message = None
    name = None
    grade = None
    gender = None

    if request.method == "POST":
        
        name = request.POST.get('name', '').strip()  
        grade = request.POST.get('grade', '').strip()
        gender = request.POST.get('gender', '').strip()

        
        if name and grade and gender:
            
            SwimmingBooking.objects.create(name=name, grade=grade, gender=gender)
            success_message = "Your child's swimming class has been successfully booked."
        else:
            error_message = "All fields are required. Please fill out the form correctly."

    return render(request, 'swimbooking.html', {
        'success_message': success_message,
        'error_message': error_message,
        'name': name,
        'grade': grade,
        'gender': gender,
    })

def yogabooking(request):
    
    success_message = None
    error_message = None
    name = None
    grade = None
    gender = None

    if request.method == "POST":
        
        name = request.POST.get('name', '').strip()  
        grade = request.POST.get('grade', '').strip()
        gender = request.POST.get('gender', '').strip()

        
        if name and grade and gender:
            
            YogaBooking.objects.create(name=name, grade=grade, gender=gender)
            success_message = "Your child's yoga class has been successfully booked."
        else:
            error_message = "All fields are required. Please fill out the form correctly."

    return render(request, 'yogabooking.html', {
        'success_message': success_message,
        'error_message': error_message,
        'name': name,
        'grade': grade,
        'gender': gender,
    })

def skatebooking(request):
    
    success_message = None
    error_message = None
    name = None
    grade = None
    gender = None

    if request.method == "POST":
        
        name = request.POST.get('name', '').strip()  
        grade = request.POST.get('grade', '').strip()
        gender = request.POST.get('gender', '').strip()

        
        if name and grade and gender:
            
            SkateBooking.objects.create(name=name, grade=grade, gender=gender)
            success_message = "Your child's skate class has been successfully booked."
        else:
            error_message = "All fields are required. Please fill out the form correctly."

    return render(request, 'skatebooking.html', {
        'success_message': success_message,
        'error_message': error_message,
        'name': name,
        'grade': grade,
        'gender': gender,
    })
def showswimbooking(request):
    allswimbooking=SwimmingBooking.objects.all()
    return render(request, 'showswimbooking.html', {'swimbooking':allswimbooking})

def showskatebooking(request):
    allskatebooking=SkateBooking.objects.all()
    return render(request, 'showskatebooking.html', {'skatebooking':allskatebooking})

def showyogabooking(request):
    allyogabooking=YogaBooking.objects.all()
    return render(request, 'showyogabooking.html', {'yogabooking':allyogabooking})

def showtransportbooking(request):
    alltransportbooking=Transport.objects.all()
    return render(request, 'showtransportbooking.html', {'transportbooking':alltransportbooking})

def shownonteachingstaff(request):
    allnonteachingstaff=NoneTeaching.objects.all()
    return render(request, 'shownonteachingstaff.html', {'noneteaching':allnonteachingstaff})

def addnonteachingstaff(request):
    if request.method == "POST":
        nonteachingstaffmembers=NoneTeaching(
            fullname = request.POST['fullname'],
            age = request.POST['age'],
            yob = request.POST['yob'],
            payrollNo = request.POST['payrollNo'],
            hireDate = request.POST['hireDate'],
            photo = request.POST['photo'],
            email = request.POST['email'],
            phoneNumber = request.POST['phoneNumber'],
            gender = request.POST['gender'],
            address = request.POST['address'],
            salary = request.POST['salary'],
        )

        nonteachingstaffmembers.save()
        return redirect('/show')
    else:
        return render(request, 'addnonteachingstaff.html')

def deleteinterview(request, id):
    xinterview = Interview.objects.get(id=id)
    xinterview.delete()
    return redirect('/showinterview')

def deleteparent(request, id):
    xparent = Parent.objects.get(id=id)
    xparent.delete()
    return redirect('/showparent')

def deletestudent(request, id):
    xstudent = Student.objects.get(id=id)
    xstudent.delete()
    return redirect('/showstudent')

def deletecontactmessage(request, id):
    xcontact = ContactMessage.objects.get(id=id)
    xcontact.delete()
    return redirect('/showmessage')

def deleteteacher(request, id):
    xteacher = Teacher.objects.get(id=id)
    xteacher.delete()
    return redirect('/showteacher')

def deleteswimbooking(request, id):
    xswimXbooking = SwimmingBooking.objects.get(id=id)
    xswimXbooking.delete()
    return redirect('/showswimbooking')

def deleteskatebooking(request, id):
    xskatebooking = SkateBooking.objects.get(id=id)
    xskatebooking.delete()
    return redirect('/showskatebooking')

def deleteyogabooking(request, id):
    xyogabooking = YogaBooking.objects.get(id=id)
    xyogabooking.delete()
    return redirect('/showyogabooking')

def deletenonteachingstaff(request, id):
    xnoneteacher = NoneTeaching.objects.get(id=id)
    xnoneteacher.delete()
    return redirect('/shownonteachingstaff')

def deletetransportbooking(request, id):
    xtransport = Transport.objects.get(id=id)
    xtransport.delete()
    return redirect('/showtransportbooking')


def addnewmember(request):
    if request.method == "POST":
        members=Member(
            fullname = request.POST['fullname'],
            username= request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
          
            
        )
        members.save()
        return redirect('/show')
    else:
        return render(request, 'addnewmember.html')

def deletemember(request, id):
    xmember = Member.objects.get(id=id)
    xmember.delete()
    return redirect('/showmember')

def editskatebooking(request, id):
    myeditedskatebooking=SkateBooking.objects.get(id=id)
    return render(request, 'editskatebooking.html',{'editskatebooking1':myeditedskatebooking})

def editmember(request, id):
    myeditedmember=Member.objects.get(id=id)
    return render(request, 'editmember.html',{'editmember1':myeditedmember})

def editinterview(request, id):
    myeditedinterview=Interview.objects.get(id=id)
    return render(request, 'editinterview.html',{'editinterview1':myeditedinterview})

def editnonteachingstaff(request, id):
    myeditednoneteachingstaff=NoneTeaching.objects.get(id=id)
    return render(request, 'editnontechingstaff.html',{'editnonteaching1':myeditednoneteachingstaff})

def editparent(request, id):
    myeditedparent=Parent.objects.get(id=id)
    return render(request, 'editparent.html',{'editparent1':myeditedparent})

def editstudent(request, id):
    myeditedstudent=Student.objects.get(id=id)
    return render(request, 'editstudent.html',{'editstudent1':myeditedstudent})

def editswimbooking(request, id):
    myeditedswimbooking=SwimmingBooking.objects.get(id=id)
    return render(request, 'editswimbooking.html',{'editswimbooking1':myeditedswimbooking})

def editteacher(request, id):
    myeditedteacher=Teacher.objects.get(id=id)
    return render(request, 'editteacher.html',{'editteacher1':myeditedteacher})

def edittransportbooking(request, id):
    myeditedtransportbooking=Transport.objects.get(id=id)
    return render(request, 'edittransportbooking.html',{'edittransportbooking1':myeditedtransportbooking})

def edityogabooking(request, id):
    myeditedyogabooking=YogaBooking.objects.get(id=id)
    return render(request, 'edityogabooking.html',{'edityogabooking1':myeditedyogabooking})

def editcontactmessage(request, id):
    myeditedcontactmessage=ContactMessage.objects.get(id=id)
    return render(request, 'editcontactmessage.html',{'contactbooking1':myeditedcontactmessage})

def updatemember(request, id):
    updatedmember=Member.objects.get(id=id)
    form=MemberForm(request.POST, instance=updatedmember)
    if form.is_valid():
        form.save()
        return redirect('/showmember')
    else:
        return render(request, 'editmember.html')

def updateinterview(request, id):
    updatedinterview=Interview.objects.get(id=id)
    form=InterviewForm(request.POST, instance=updatedinterview)
    if form.is_valid():
        form.save()
        return redirect('/showinterview')
    else:
        return render(request, 'editinterview.html')

def updatenonteaching(request, id):
    updatednonteaching=NoneTeaching.objects.get(id=id)
    form=NoneTeachingForm(request.POST, instance=updatednonteaching)
    if form.is_valid():
        form.save()
        return redirect('/shownonteachingstaff')
    else:
        return render(request, 'editnonteachingstaff.html')

def updateparent(request, id):
    updatedparent=Parent.objects.get(id=id)
    form=ParentForm(request.POST, instance=updatedparent)
    if form.is_valid():
        form.save()
        return redirect('/showparent')
    else:
        return render(request, 'editparent.html')

def updatestudent(request, id):
    updatedstudent=Student.objects.get(id=id)
    form=StudentForm(request.POST, instance=updatedstudent)
    if form.is_valid():
        form.save()
        return redirect('/showstudent')
    else:
        return render(request, 'editstudent.html')

def updateacher(request, id):
    updatedteacher=Teacher.objects.get(id=id)
    form=TeacherForm(request.POST, instance=updatedteacher)
    if form.is_valid():
        form.save()
        return redirect('/showteacher')
    else:
        return render(request, 'editteacher.html')

def updatecontactmessage(request, id):
    updatedcontactmessage=ContactMessage.objects.get(id=id)
    form=ContactMessageForm(request.POST, instance=updatedcontactmessage)
    if form.is_valid():
        form.save()
        return redirect('/showmessage')
    else:
        return render(request, 'editcontactmessage.html')

def updateskatebooking(request, id):
    updatedskatebooking=SkateBooking.objects.get(id=id)
    form=SkateBookingForm(request.POST, instance=updatedskatebooking)
    if form.is_valid():
        form.save()
        return redirect('/showskatebooking')
    else:
        return render(request, 'editskatebooking.html')

def updateyogabooking(request, id):
    updatedyogabooking = YogaBooking.objects.get(id=id)
    form=YogaBookingForm(request.POST, instance=updatedyogabooking)
    if form.is_valid():
        form.save()
        return redirect('/showyogabooking')
    else:
        return render(request,'edityogabooking.html')
    
def updateswimmingbooking(request, id):
    updatedswimming=SwimmingBooking.objects.get(id=id)
    form=SwimmingBookingForm(request.POST, instance=updatedswimming)
    if form.is_valid():
        form.save()
        return redirect('/showswimbooking')
    else:
        return render(request,'editswimbooking.html')

def updatetransport(request, id):
    updatedtransport=Transport.objects.get(id=id)
    form=TransportForm(request.POST, instance=updatedtransport)
    if form.is_valid():
        form.save()
        return redirect('/showtransportbooking')
    else:
        return render(request, 'edittransportbooking.html')
    
def imagedirectordelete(request, id):
    image = ImageDirectorModel.objects.get(id=id)
    image.delete()
    return redirect('/showdirectorimage')

    
def uploaddirectorimage(request):
    if request.method == "POST":
        form = ImageDirectorModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showdirectorimage')
    else:
        form = ImageDirectorModel()
    return render(request, 'uploaddirectorimage.html', {'form': form})

def showdirectorimage(request):
    images = ImageDirectorModel.objects.all()
    return render(request, 'showdirectorimage.html', {'images': images})

def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')