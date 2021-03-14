from django.contrib import admin

# Register your models here.




from .models import Practice,Modules,Practice_set,Articles,CreateCourse,Videos

admin.site.register(Practice)
admin.site.register(Practice_set)
admin.site.register(Modules)
admin.site.register(CreateCourse)
admin.site.register(Videos)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    class Media:
        js=('tinymce1.js',)


