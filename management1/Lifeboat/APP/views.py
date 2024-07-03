from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *


# Create your views here.
class Singup(APIView):
    def post(self, request):
        data = request.data
        mobile = data["mobile"]

        x = users.objects.filter(mobile=mobile)
        if x:
            res = {
                "sucess": False,
                "error": '',
                "info": 'not registered'

            }
            return Response(res)
        else:
            obj1 = users()
            obj1.name = data["name"]
            obj1.mobile = data["mobile"]
            obj1.password = data["password"]
            obj1.save()
            res = {
                "sucess": True,
                "error": '',
                "info": ''
            }
            return Response(res)


class Login(APIView):
    def post(self, request):
        mobile = request.data["mobile"]
        password=request.data["password"]
        z = users.objects.filter(mobile=mobile,password=password ).first()
        if z:
            token = RefreshToken.for_user(z)
            print(token)
            access_token = str(token.access_token)
            res = {
                "sucess": True,
                "error": '',
                "info": {
                    "access_token": access_token

                }
            }
            return Response(res)
        else:
            res = {
                "sucess": False,
                "error": '',
                "info": 'invalid credentials'
            }
            return Response(res)


class Course_data(APIView):
    def get(self, request):
        records = courses.objects.all().values()
        return Response(records)

    def post(self, request):
        data = request.data
        obj2 = courses()
        obj2.name = data["name"]
        obj2.fee = data["fee"]
        obj2.duration = data["duration"]
        obj2.is_active = data["is_active"]
        obj2.course_id=data["course_id"]
        obj2.save()
        res = {
            "sucess": True,
            "Error": '',
            "info": ''
        }
        return Response(res)

    def put(self, request, pk):
        print(pk)
        data = request.data
        records = courses.objects.filter(id=pk)
        if len(records) > 0:
            course = records[0]
            course.name = data["name"]

            course.fee = data["fee"]
            course.duration = data["duration"]
            course.is_active = data["is_active"]
            course.course_id = data["course_id"]
            course.save()
            res={
                "sucess": True,
                "Error": '',
                "info": ''
            }
            return Response(res)
        else:
            res={
                "sucess": False,
                "Error": '',
                "info": 'invalid credentials'
            }
            return Response(res)
    def delete(self,request,pk):
        print(pk)
        records=courses.objects.filter(id=pk).delete()
        return Response(records)
class Leads_data(APIView):
    def get(self,request):
        records1=leads.objects.all().values()
        return Response(records1)
    def post(self,request):
        data=request.data
        obj3=leads()
        obj3.mobile=data["mobile"]
        obj3.user_name=data["name"]
        course_id = request.data["course_id"]
        x = courses.objects.filter(course_id=course_id)
        if x:
            obj3.course_id = data["course_id"]
        else:
            res = {
                "sucess": False,
                "Error": 'course not available',
                "info": ''
            }
            return Response(res)

        obj3.date_of_visit=data["date_of_visit"]
        obj3.source=data["source"]
        obj3.mode=data["mode"]
        obj3.status=data["status"]
        obj3.mail=data["mail"]
        obj3.save()
        res = {
            "sucess": True,
            "Error": '',
            "info": ''
        }
        return Response(res)
    def put(self,request,pk):
        print(pk)
        data=request.data
        records1=leads.objects.filter(id=pk)
        if len(records1)>0:
            lead=records1[0]
            lead.mobile = data["mobile"]
            lead.name = data["name"]
            lead.course_id = data["course_id"]
            lead.date_of_visit = data["date_of_visit"]
            lead.source = data["source"]
            lead.mode = data["mode"]
            lead.status = data["status"]
            lead.mail=data["mail"]
            lead.save()
            res = {
                "sucess": True,
                "Error": '',
                "info": ''
            }
            return Response(res)
        else:
            res = {
                "sucess": False,
                "Error": '',
                "info": 'invalid credentials'
            }
            return Response(res)

    def delete(self,request,pk):
        print(pk)
        records1 = leads.objects.filter(id=pk).delete()
        return Response(records1)
class Trainers_data(APIView):
    def get(self,request):

        records2=Trainers.objects.all().values()
        return Response(records2)
    def post(self,request):
        data=request.data
        obj4=Trainers()
        obj4.name=data["name"]
        course_id=request.data["course_id"]
        y=courses.objects.filter(course_id=course_id)
        if y:
         obj4.course_id=data["course_id"]
        else:
            res={
                "sucess": False,
                "Error": 'course not available',
                "info": ''
            }
            return Response(res)

        obj4.mobile=data["mobile"]
        obj4.trainer_id=data["trainer_id"]
        obj4.save()
        res = {
            "sucess": True,
            "Error": '',
            "info": ''
        }
        return Response(res)
    def put(self,request,pk):
        print(pk)
        data=request.data
        records2 = Trainers.objects.filter(id=pk)
        if len(records2) > 0:
            trainer = records2[0]
            trainer.mobile = data["mobile"]
            trainer.name = data["name"]
            trainer.course_name = data["course_name"]
            trainer.trainer_id = data["trainer_id"]
            trainer.save()
            res = {
                "sucess": True,
                "Error": '',
                "info": ''
            }
            return Response(res)
        else:
            res = {
                "sucess": False,
                "Error": '',
                "info": 'invalid credentials'
            }
            return Response(res)
    def delete(self,request,pk):
        print(pk)
        records2 = Trainers.objects.filter(id=pk).delete()
        return Response(records2)
class Batches_data(APIView):
    def get(self,request):
        records3 = Batches.objects.all().values()
        return Response(records3)

    def post(self, request):
        data = request.data
        obj5 = Batches()
        course_id = request.data["course_id"]
        z = courses.objects.filter(course_id=course_id)
        if z:
            obj5.course_id = data["course_id"]
        else:
            res = {
                "sucess": False,
                "Error": 'course not available',
                "info": ''
            }
            return Response(res)

        trainer_id = request.data["trainer_id"]

        p=Trainers.objects.filter(trainer_id=trainer_id)
        if p:
            obj5.trainer_id = data["trainer_id"]

        else:
            res = {
                "sucess": False,
                "Error": 'course not available',
                "info": ''
            }
            return Response(res)

        obj5.status = data["status"]
        obj5.start_date=data["start_date"]
        obj5.end_date=data["end_date"]
        obj5.Batch_id = data["Batch_id"]
        obj5.leads=data["leads"]


        obj5.save()
        res = {
            "sucess": True,
            "Error": '',
            "info": ''
        }
        return Response(res)
    def put(self,request,pk):
        print(pk)
        data=request.data
        records3 = Batches.objects.filter(id=pk)
        if len(records3) > 0:
            batch=records3[0]
            batch.course_id = data["course_id"]
            batch.trainer_id = data["trainer_id"]
            batch.status = data["status"]
            batch.start_date = data["start_date"]
            batch.end_date = data["end_date"]
            batch.Batch_id = data["Batch_id"]
            batch.save()

            res = {
                "sucess": True,
                "Error": '',
                "info": ''
            }
            return Response(res)
        else:
            res = {
                "sucess": False,
                "Error": '',
                "info": 'invalid credentials'
            }
            return Response(res)

    def delete(self, request, pk):
        print(pk)
        records3 = Batches.objects.filter(id=pk).delete()
        return Response(records3)
class Students_data(APIView):
    def get(self,request):
        records4 = students.objects.all().values()
        return Response(records4)
    def post(self,request):
        data=request.data
        obj6=students()
        obj6.email=data["email"]

        course_id = request.data["course_id"]

        q = courses.objects.filter(course_id=course_id)
        if q:
            obj6.course_id = data["course_id"]

        else:
            res = {
                "sucess": False,
                "Error": 'course not available',
                "info": ''
            }
            return Response(res)



        Batch_id = request.data["Batch_id"]

        r =Batches.objects.filter(Batch_id=Batch_id)
        if r:
            obj6.Batch_id = data["Batch_id"]

        else:
            res = {
                "sucess": False,
                "Error": 'course not available',
                "info": ''
            }
            return Response(res)
        obj6.fee=data["fee"]
        obj6.paid=data["paid"]
        obj6.pending=data["pending"]
        obj6.name=data["name"]
        obj6.mobile=data["mobile"]
        obj6.status = data["status"]

        obj6.save()
        res = {
            "sucess": True,
            "Error": '',
            "info": ''
        }
        return Response(res)
    def put(self,request,pk):
        print(pk)
        data=request.data
        records4 = students.objects.filter(id=pk)
        if len(records4) > 0:
            student=records4[0]
            student.email = data["email"]

            student.fee = data["fee"]
            student.paid = data["paid"]
            student.pending = data["pending"]
            student.status = data["status"]
            student.name = data["name"]
            student.mobile = data["mobile"]
            student.save()

            res = {
                "sucess": True,
                "Error": '',
                "info": ''
            }
            return Response(res)
        else:
            res = {
                "sucess": False,
                "Error": '',
                "info": 'invalid credentials'
            }
            return Response(res)

    def delete(self, request, pk):
        print(pk)
        records4 = Batches.objects.filter(id=pk).delete()
        return Response(records4)
class Payment_data(APIView):
    def get(self,request):
        records5 = payments.objects.all().values()
        return Response(records5)
    def post(self,request):
        data=request.data
        obj7=payments()
        obj7.date_of_payment = data["date_of_payment"]
        obj7.student_id = data["student_id"]
        Batch_id = request.data["Batch_id"]

        s = Batches.objects.filter(Batch_id=Batch_id)
        if s:
            obj7.Batch_id = data["Batch_id"]

        else:
            res = {
                "sucess": False,
                "Error": 'course not available',
                "info": ''
            }
            return Response(res)

        obj7.Amount=data["Amount"]

        obj7.save()
        res = {
            "sucess": True,
            "Error": '',
            "info": ''
        }
        return Response(res)
    def put(self,request,pk):
        print(pk)
        data=request.data
        records5 = payments.objects.filter(id=pk)
        if len(records5) > 0:
            payment=records5[0]
            payment.date_of_payment = data["date_of_payment"]
            payment.student_id = data["student_id"]
            payment.Batch_id = data["Batch_id"]
            payment.Amount = data["Amount"]

            res = {
                "sucess": True,
                "Error": '',
                "info": ''
            }
            return Response(res)
        else:
            res = {
                "sucess": False,
                "Error": '',
                "info": 'invalid credentials'
            }
            return Response(res)

    def delete(self, request, pk):
        print(pk)
        records5 = payments.objects.filter(id=pk).delete()
        return Response(records5)


