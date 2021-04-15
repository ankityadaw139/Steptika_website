from django.urls import path
from . import views


urlpatterns = [
    path("api/1", views.Courses1.as_view()),
    path("api/2", views.Modules1.as_view()),
    path("api/3", views.Practices1.as_view()),
    path("api/4", views.Articles1.as_view()),
    path("api/5", views.Videos1.as_view()),
    path("api/6", views.Category1.as_view()),
]
