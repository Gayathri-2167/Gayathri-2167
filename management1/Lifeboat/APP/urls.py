from django.urls import path

from .views import Singup, Login, Course_data, Leads_data, Trainers_data, Batches_data, Students_data, Payment_data

urlpatterns = [
path('singup',Singup.as_view() ),
path('login',Login.as_view() ),
path('course/<int:pk>/',Course_data.as_view() ),
path('course',Course_data.as_view() ),
path('leads',Leads_data.as_view() ),
path('leads/<int:pk>/',Leads_data.as_view() ),
path('trainer',Trainers_data.as_view() ),
path('trainer/<int:pk>/',Trainers_data.as_view() ),
path('batch',Batches_data.as_view() ),
path('batch/<int:pk>/',Batches_data.as_view() ),
path('student',Students_data.as_view() ),
path('student/<int:pk>/',Students_data.as_view() ),
path('payment',Payment_data.as_view() ),
path('payment/<int:pk>/',Payment_data.as_view() )



]