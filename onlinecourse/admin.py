from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
class Question(admin.ModelAdmin):
    course = admin.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    text = admin.CharField(max_length=500)
    grade_point = admin.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.course.name} - Question {self.id}: {self.text}' # pylint: disable=no-member

    
# class Choice(models.Model):
class Choice(admin.ModelAdmin):
    question = admin.ForeignKey(Question, on_delete=models.CASCADE)
    text = admin.CharField(max_length=500)
    is_correct = admin.BooleanField(default=False)

    def __str__(self):
        return self.text
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
