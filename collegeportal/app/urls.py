from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userlog',views.userlog,name='userlog'),
    path('logout',views.logout,name='logout'),
    path('courseadd',views.courseadd,name='courseadd'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('showcourses',views.showcourses,name='showcourses'),
    path('editcourse/<int:pc>',views.editcourse,name='editcourse'),
    path('updatecourse/<int:uc>',views.updatecourse,name='updatecourse'),
    path('deletecourse/<int:cd>',views.deletecourse,name='deletecourse'),
    path('studentadd',views.studentadd,name='studentadd'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('managestudent',views.managestudent,name='managestudent'),
    path('editstdudent/<int:es>',views.editstdudent,name='editstdudent'),
    path('updatestudent/<int:us>',views.updatestudent,name='updatestudent'),
    path('deletestudent/<int:sd>',views.deletestudent,name='deletestudent'),
    path('manageteacher',views.manageteacher,name='manageteacher'),
    path('deleteteacher/<int:td>',views.deleteteacher,name='deleteteacher'),
    path('teacherhome',views.teacherhome,name='teacherhome'),
    path('teacherprofile/<int:tp>/', views.teacherprofile, name='teacherprofile'),
    path('editteacher/<int:et>',views.editteacher,name='editteacher'),
    path('updateteacher/<int:ut>/', views.updateteacher, name='updateteacher'),
]