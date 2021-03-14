from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CreateCourse,Modules,Articles,Practice,Videos

from .serializers import CourseSerializers,ModulesSerializers,ArticleSerializers,PracticeSerializers,VideoSerializers



class Courses1(APIView):

    def get(self,request):
        summary1=CreateCourse.objects.all()
        serializer=CourseSerializers(summary1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Modules1(APIView):

    def get(self,request):
        summary1=Modules.objects.all()
        serializer=ModulesSerializers(summary1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class Articles1(APIView):

    def get(self,request):
        summary1=Articles.objects.all()
        serializer=ArticleSerializers(summary1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class Practices1(APIView):

    def get(self,request):
        summary1=Practice.objects.all()
        serializer=PracticeSerializers(summary1,many=True)
        return Response(serializer.data)

    def post(self):
        pass


class Videos1(APIView):

    def get(self,request):
        summary1=Videos.objects.all()
        serializer=VideoSerializers(summary1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
