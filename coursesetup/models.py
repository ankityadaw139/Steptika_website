from django.db import models

# Create your models here.



# Create your models here.


# Create your models here.
class Practice_set(models.Model):
    id = models.AutoField
    category = models.IntegerField(default=0)
    sub_code=models.CharField(max_length=50,default="")
    name=models.CharField(max_length=50,default="")


    def __str__(self):
        return self.name




class Practice(models.Model):
    id = models.AutoField
    practice_set_name = models.CharField(max_length=100)

    question_1 = models.CharField(max_length=300, default="",blank=True)
    A1 = models.CharField(max_length=200, default="" ,blank=True)
    B1 = models.CharField(max_length=200, default="",blank=True)
    C1 = models.CharField(max_length=200, default="",blank=True)
    D1 = models.CharField(max_length=200, default="",blank=True)
    answer_1 = models.IntegerField(default=0,blank=True)

    question_2 = models.CharField(max_length=300, default="",blank=True)
    A2 = models.CharField(max_length=200, default="",blank=True)
    B2 = models.CharField(max_length=200, default="",blank=True)
    C2 = models.CharField(max_length=200, default="",blank=True)
    D2 = models.CharField(max_length=200, default="",blank=True)
    answer_2 = models.IntegerField(default=0,blank=True)

    question_3 = models.CharField(max_length=300, default="",blank=True)
    A3 = models.CharField(max_length=200, default="",blank=True)
    B3 = models.CharField(max_length=200, default="",blank=True)
    C3 = models.CharField(max_length=200, default="",blank=True)
    D3 = models.CharField(max_length=200, default="",blank=True)
    answer_3 = models.IntegerField(default=0,blank=True)

    question_4 = models.CharField(max_length=300, default="",blank=True)
    A4 = models.CharField(max_length=200, default="",blank=True)
    B4 = models.CharField(max_length=200, default="",blank=True)
    C4 = models.CharField(max_length=200, default="",blank=True)
    D4 = models.CharField(max_length=200, default="",blank=True)
    answer_4 = models.IntegerField(default=0,blank=True)

    question_5 = models.CharField(max_length=300, default="",blank=True)
    A5 = models.CharField(max_length=200, default="",blank=True)
    B5 = models.CharField(max_length=200, default="",blank=True)
    C5 = models.CharField(max_length=200, default="",blank=True)
    D5 = models.CharField(max_length=200, default="",blank=True)
    answer_5 = models.IntegerField(default=0,blank=True)

    question_6 = models.CharField(max_length=300, default="",blank=True)
    A6 = models.CharField(max_length=200, default="",blank=True)
    B6 = models.CharField(max_length=200, default="",blank=True)
    C6 = models.CharField(max_length=200, default="",blank=True)
    D6 = models.CharField(max_length=200,blank=True)
    answer_6 = models.IntegerField(default=0,blank=True)

    question_7 = models.CharField(max_length=300, default="",blank=True)
    A7 = models.CharField(max_length=200, default="",blank=True)
    B7 = models.CharField(max_length=200, default="",blank=True)
    C7 = models.CharField(max_length=200, default="",blank=True)
    D7 = models.CharField(max_length=200, default="",blank=True)
    answer_7 = models.IntegerField(default=0,blank=True)

    question_8 = models.CharField(max_length=300, default="",blank=True)
    A8 = models.CharField(max_length=200, default="",blank=True)
    B8 = models.CharField(max_length=200, default="",blank=True)
    C8 = models.CharField(max_length=200, default="",blank=True)
    D8 = models.CharField(max_length=200, default="",blank=True)
    answer_8 = models.IntegerField(default=0,blank=True)

    question_9 = models.CharField(max_length=300, default="",blank=True)
    A9 = models.CharField(max_length=200, default="",blank=True)
    B9 = models.CharField(max_length=200, default="",blank=True)
    C9 = models.CharField(max_length=200, default="",blank=True)
    D9 = models.CharField(max_length=200, default="",blank=True)
    answer_9 = models.IntegerField(default=0,blank=True)

    question_10 = models.CharField(max_length=300, default="",blank=True)
    A10 = models.CharField(max_length=200, default="",blank=True)
    B10 = models.CharField(max_length=200, default="",blank=True)
    C10 = models.CharField(max_length=200, default="",blank=True)
    D10 = models.CharField(max_length=200, default="",blank=True)
    answer_10 = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.practice_set_name

class Articles(models.Model):
    id = models.AutoField
    article_name=models.CharField(max_length=100)
    article=models.CharField(max_length=50000)

    def __str__(self):
        return self.article_name


class Videos(models.Model):
    id = models.AutoField
    videos_name=models.CharField(max_length=100)
    videos=models.URLField()

    def __str__(self):
        return self.videos_name



class Modules(models.Model):
    id = models.AutoField
    module_name = models.CharField(max_length=100)
    all_videos=models.ManyToManyField(Videos,blank=True)
    all_articles=models.ManyToManyField(Articles,blank=True)
    all_practice = models.ManyToManyField(Practice,blank=True)


    def __str__(self):
        return self.module_name




class CreateCourse(models.Model):
    id = models.AutoField
    course_name = models.CharField(max_length=100)
    all_modules=models.ManyToManyField(Modules)


    def __str__(self):
        return self.course_name

