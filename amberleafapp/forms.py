from django import forms
from django.forms import ModelForm

from amberleafapp.models import Student,ImageModel,ImageDirectorModel,Parent,Teacher,Interview,ContactMessage,Member,Transport,SwimmingBooking,YogaBooking,SkateBooking,NoneTeaching

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = '__all__'

class SwimmingBookingForm(forms.ModelForm):
    class Meta:
        model = SwimmingBooking
        fields = '__all__'

class YogaBookingForm(forms.ModelForm):
    class Meta:
        model = YogaBooking
        fields = '__all__'

class SkateBookingForm(forms.ModelForm):
    class Meta:
        model = SkateBooking
        fields = '__all__'

class NoneTeachingForm(forms.ModelForm):
    class Meta:
        model = NoneTeaching
        fields = '__all__'

class ImageDirectorModelForm(forms.ModelForm):
    class Meta:
        model = ImageDirectorModel
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','essay']