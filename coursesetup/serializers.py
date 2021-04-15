from rest_framework import serializers
from .models import Practice, CreateCourse, Modules, Articles, Videos, Category


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = CreateCourse
        fields = "__all__"


class ModulesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = "__all__"


class PracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = "__all__"


class StringListField(serializers.ListField):
    child = serializers.CharField()


# UNNESSCARY FOR GET
# class ArticleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Articles
#         fields = ("id", "article_name", "no_of_parts", "article")


class VideoSerializers(serializers.ModelSerializer):
    video_length = serializers.CharField(source='get_video_length', read_only=True)

    class Meta:
        model = Videos
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
