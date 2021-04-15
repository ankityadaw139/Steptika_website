from django.db import models
from django.utils.text import slugify
import re
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip
from steptika.settings import MEDIA_ROOT
import os


class Practice_set(models.Model):
    id = models.AutoField
    category = models.IntegerField(default=0)
    sub_code = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Practice(models.Model):
    id = models.AutoField
    practice_set_name = models.CharField(max_length=100)

    question_1 = models.CharField(max_length=300, default="", blank=True)
    A1 = models.CharField(max_length=200, default="", blank=True)
    B1 = models.CharField(max_length=200, default="", blank=True)
    C1 = models.CharField(max_length=200, default="", blank=True)
    D1 = models.CharField(max_length=200, default="", blank=True)
    answer_1 = models.IntegerField(default=0, blank=True)

    question_2 = models.CharField(max_length=300, default="", blank=True)
    A2 = models.CharField(max_length=200, default="", blank=True)
    B2 = models.CharField(max_length=200, default="", blank=True)
    C2 = models.CharField(max_length=200, default="", blank=True)
    D2 = models.CharField(max_length=200, default="", blank=True)
    answer_2 = models.IntegerField(default=0, blank=True)

    question_3 = models.CharField(max_length=300, default="", blank=True)
    A3 = models.CharField(max_length=200, default="", blank=True)
    B3 = models.CharField(max_length=200, default="", blank=True)
    C3 = models.CharField(max_length=200, default="", blank=True)
    D3 = models.CharField(max_length=200, default="", blank=True)
    answer_3 = models.IntegerField(default=0, blank=True)

    question_4 = models.CharField(max_length=300, default="", blank=True)
    A4 = models.CharField(max_length=200, default="", blank=True)
    B4 = models.CharField(max_length=200, default="", blank=True)
    C4 = models.CharField(max_length=200, default="", blank=True)
    D4 = models.CharField(max_length=200, default="", blank=True)
    answer_4 = models.IntegerField(default=0, blank=True)

    question_5 = models.CharField(max_length=300, default="", blank=True)
    A5 = models.CharField(max_length=200, default="", blank=True)
    B5 = models.CharField(max_length=200, default="", blank=True)
    C5 = models.CharField(max_length=200, default="", blank=True)
    D5 = models.CharField(max_length=200, default="", blank=True)
    answer_5 = models.IntegerField(default=0, blank=True)

    question_6 = models.CharField(max_length=300, default="", blank=True)
    A6 = models.CharField(max_length=200, default="", blank=True)
    B6 = models.CharField(max_length=200, default="", blank=True)
    C6 = models.CharField(max_length=200, default="", blank=True)
    D6 = models.CharField(max_length=200, blank=True)
    answer_6 = models.IntegerField(default=0, blank=True)

    question_7 = models.CharField(max_length=300, default="", blank=True)
    A7 = models.CharField(max_length=200, default="", blank=True)
    B7 = models.CharField(max_length=200, default="", blank=True)
    C7 = models.CharField(max_length=200, default="", blank=True)
    D7 = models.CharField(max_length=200, default="", blank=True)
    answer_7 = models.IntegerField(default=0, blank=True)

    question_8 = models.CharField(max_length=300, default="", blank=True)
    A8 = models.CharField(max_length=200, default="", blank=True)
    B8 = models.CharField(max_length=200, default="", blank=True)
    C8 = models.CharField(max_length=200, default="", blank=True)
    D8 = models.CharField(max_length=200, default="", blank=True)
    answer_8 = models.IntegerField(default=0, blank=True)

    question_9 = models.CharField(max_length=300, default="", blank=True)
    A9 = models.CharField(max_length=200, default="", blank=True)
    B9 = models.CharField(max_length=200, default="", blank=True)
    C9 = models.CharField(max_length=200, default="", blank=True)
    D9 = models.CharField(max_length=200, default="", blank=True)
    answer_9 = models.IntegerField(default=0, blank=True)

    question_10 = models.CharField(max_length=300, default="", blank=True)
    A10 = models.CharField(max_length=200, default="", blank=True)
    B10 = models.CharField(max_length=200, default="", blank=True)
    C10 = models.CharField(max_length=200, default="", blank=True)
    D10 = models.CharField(max_length=200, default="", blank=True)
    answer_10 = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.practice_set_name


class Articles(models.Model):
    id = models.AutoField
    article_name = models.CharField(max_length=100)
    article = models.CharField(max_length=50000)

    def __str__(self):
        return self.article_name

    def get_paras(self):
        out = []
        paras = re.split(r"<\w>&nbsp;<\/\w>", self.article)

        for para in paras:
            obj = {}
            soup = BeautifulSoup(para, "html.parser")
            children = [child for child in soup.children]
            no_of_lines = len(children)
            obj["no_of_Lines"] = no_of_lines

            for i in range(no_of_lines):
                obj[f"{i}"] = str(children[i])

            out.append(obj)

        return out

    def get_no_of_parts(self):
        return len(self.get_paras())


class Videos(models.Model):
    id = models.AutoField
    description = models.CharField(max_length=2000, default="")
    videos_name = models.CharField(max_length=100)
    videos = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.videos_name

    def get_video_length(self):
        video = VideoFileClip(os.path.join(MEDIA_ROOT, str(self.videos)))
        return video.duration


class Modules(models.Model):
    id = models.AutoField
    module_name = models.CharField(max_length=100)
    all_videos = models.ManyToManyField(Videos, blank=True)
    all_articles = models.ManyToManyField(Articles, blank=True)
    all_practice = models.ManyToManyField(Practice, blank=True)

    def __str__(self):
        return self.module_name


class Category(models.Model):
    category = models.CharField(max_length=56)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super().save(*args, **kwargs)


class CreateCourse(models.Model):
    id = models.AutoField
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, default="")
    image = models.ImageField(upload_to="courseimages/")
    resources = models.FileField(upload_to="resourses/")
    all_modules = models.ManyToManyField(Modules)
    isFree = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name
