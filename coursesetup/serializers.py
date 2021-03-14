from rest_framework import serializers
from .models import Practice,CreateCourse,Modules,Articles,Videos

class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model=CreateCourse
        fields='__all__'


class ModulesSerializers(serializers.ModelSerializer):

    class Meta:
        model=Modules
        fields='__all__'


class PracticeSerializers(serializers.ModelSerializer):

    class Meta:
        model=Practice
        fields='__all__'

class ArticleSerializers(serializers.ModelSerializer):

    class Meta:
        model=Articles
        fields='__all__'


class VideoSerializers(serializers.ModelSerializer):

    class Meta:
        model=Videos
        fields='__all__'
