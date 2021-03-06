from django.urls import path

from workforce import views

app_name = 'workforce'

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departmentList, name='departmentList'),
    path('departmentDetail/<int:department_id>/', views.detail, name='departmentDetail'),
	path('employees/', views.employeeList, name='employeeList'), #to load the page with employee list
    path('employees/<int:employee_id>/', views.employeeDetail, name='employeeDetail'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('training/', views.trainingList, name='training'),
    path('addtraining/', views.newTraining, name='addTraining'),
    path('editTraining/<int:program_id>', views.editProgramForm, name='editTraining'),
    path('addAttendee/<int:program_id>', views.newAttendee, name='addAttendee'),
    path('deleteAttendee/<int:trainingProgram_id>', views.deleteAttendee, name='deleteAttendee'),
    path('deleteTraining/<int:program_id>', views.deleteProgram, name='deleteTraining'),
    path('editProgram/<int:program_id>', views.editProgram, name='editProgram'),
    path('programs/<int:program_id>/', views.programsDetail, name='programsDetail'),
    path('pastprograms/', views.pastTrainingList, name='pastTraining'),
    path('departmentForm/', views.departmentForm, name='departmentForm'),
    path('addDepartment/', views.addDepartment, name='addDepartment'),
    path('computer/', views.computerList, name='computers'),
]

# example from DjangoMusic Exercise
# urlpatterns = [
#     # ex: /artists/
#     path('', views.index, name='index'),
#     # ex: /artists/5/
#     path('<int:artist_id>/', views.detail, name='detail'),
#     path('postartist/', views.addArtistForm, name='addArtistForm'),
#     path('postartist/submittal/', views.postartist, name='postartist')
# ]





