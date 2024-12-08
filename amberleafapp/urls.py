from django.contrib import admin
from django.urls import path
from amberleafapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('cocuricular/', views.cocuricular, name='cocuricular'),
    path('academic/', views.academic, name='academic'),
    path('digitalschool/', views.digitalschool, name='digitalschool'),
    path('facilities/', views.facilities, name='facilities'),
    path('galery/', views.galery, name='galery'),
    path('starter/', views.starter, name='starter'),
    path('curiculum/', views.academic, name='curiculum'),
    path('interview/', views.interview_view, name='interview'),
    path('teachers/', views.teachers, name='teachers'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('showinterview/', views.showinterview, name='showinterview'),
    path('terms/', views.terms, name='terms'),
    path('showmessage/', views.showmessage, name='showmessage'),
    path('showstudent/', views.showstudent, name='showstudent'),
    path('showmember/', views.showmember, name='showmember'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('showparent/', views.showparent, name='showparent'),
    path('addparent/', views.addparent, name='addparent'),
    path('showteacher/', views.showteacher, name='showteacher'),
    path('addteacher/', views.addteacher, name='addteacher'),
    path('directors/', views.directors, name='directors'),
    path('transportbooking/', views.transportbooking, name='transportbooking'),
    path('nonteachingstaff/', views.nonteachingstaff, name='nonteachingstaff'),
    path('swimbooking/', views.swimbooking, name='swimbooking'),
    path('yogabooking/', views.yogabooking, name='yogabooking'),
    path('show/', views.show, name='show'),
    path('skatebooking/', views.skatebooking, name='skatebooking'),
    path('showswimbooking/', views.showswimbooking, name='showswimbooking'),
    path('showskatebooking/', views.showskatebooking, name='showskatebooking'),
    path('showyogabooking/', views.showyogabooking, name='showyogabooking'),
    path('showtransportbooking/', views.showtransportbooking, name='showtransportbooking'),
    path('shownonteachingstaff/', views.shownonteachingstaff, name='shownonteachingstaff'),
    path('addnonteachingstaff/', views.addnonteachingstaff, name='addnonteachingstaff'),
    path('deleteinterview/<int:id>', views.deleteinterview),
    path('deleteparent/<int:id>', views.deleteparent),
    path('deletestudent/<int:id>', views.deletestudent),
    path('deletecontactmessage/<int:id>', views.deletecontactmessage),
    path('deleteteacher/<int:id>', views.deleteteacher),
    path('deleteskatebooking/<int:id>', views.deleteskatebooking),
    path('deleteyogabooking/<int:id>', views.deleteyogabooking),
    path('deletenonteachingstaff/<int:id>', views.deletenonteachingstaff),
    path('deletetransportbooking/<int:id>', views.deletetransportbooking),
    path('editinterview/<int:id>', views.editinterview, name='editinterview'),
    path('addnewmember/', views.addnewmember, name='addnewmember'),
    path('deletemember/<int:id>', views.deletemember),
    path('editmember/<int:id>', views.editmember, name='editmember'),
    path('editnonteachingstaff/<int:id>', views.editnonteachingstaff, name='editnonteachingstaff'),
    path('editparent/<int:id>', views.editparent, name='editparent'),
    path('editskatebooking/<int:id>', views.editskatebooking, name='editskatebooking'),
    path('editstudent/<int:id>', views.editstudent, name='editstudent'),
    path('editswimbooking/<int:id>', views.editswimbooking, name='editswimbooking'),
    path('editteacher/<int:id>', views.editteacher, name='editteacher'),
    path('edittransportbooking/<int:id>', views.edittransportbooking, name='edittransportbooking'),
    path('edityogabooking/<int:id>', views.edityogabooking, name='edityogabooking'),
    path('editcontactmessage/<int:id>', views.editcontactmessage, name='editcontactmessage'),
    path('updatemember/<int:id>', views.updatemember, name='updatemember'),
    path('updateinterview/<int:id>', views.updateinterview, name='updateinterview'),
    path('updatenonteaching/<int:id>', views.updatenonteaching, name='updatenonteaching'),
    path('updateparent/<int:id>', views.updateparent, name='updateparent'),
    path('updatestudent/<int:id>', views.updatestudent, name='updatestudent'),
    path('updateacher/<int:id>', views.updateacher, name='updateacher'),
    path('updatecontactmessage/<int:id>', views.updatecontactmessage, name='updatecontactmessage'),
    path('updateswimmingbooking/<int:id>', views.updateswimmingbooking, name='updateswimmingbooking'),
    path('updatetransport/<int:id>', views.updatetransport, name='updatetransport'),
    path('updateskatebooking/<int:id>', views.updateskatebooking, name='updateskatebooking'),
    path('updateyogabooking/<int:id>', views.updateyogabooking, name='updateyogabooking'),
    path('uploaddirectorimage/', views.uploaddirectorimage, name='uploaddirectorimage'),
    path('showdirectorimage/', views.showdirectorimage, name='showdirectorimage'),
    path('imagedirectordelete/<int:id>', views.imagedirectordelete),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

    


    



    
    

    











    

    

