from django.contrib import admin
from amberleafapp.models import Student,ImageModel,Parent,ImageDirectorModel,Teacher,Interview,ContactMessage,Member,SwimmingBooking,Transport,YogaBooking,SkateBooking,NoneTeaching

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Interview)
admin.site.register(ContactMessage)
admin.site.register(Member)
admin.site.register(SwimmingBooking)
admin.site.register(Transport)
admin.site.register(YogaBooking)
admin.site.register(SkateBooking)
admin.site.register(NoneTeaching)
admin.site.register(ImageDirectorModel)
admin.site.register(ImageModel)