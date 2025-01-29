from django.db import models
from django.utils import timezone

# The models in this file are the core of the learning management system. They define the structure of the courses, modules, and lessons that make up the learning experience.
# Each course can have multiple modules, each module can have multiple items, and each item can be a lesson, quiz, assignment, video, etc.
# Users will progress through the items and track their access and completion of the items.


# The course is the main model and collection of items that makes up a learning experience.
class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    course_overview = models.TextField()
    course_duration = models.IntegerField()
    course_image = models.TextField()  # This would be a thumbnail image for the course.
    course_slug = models.SlugField(max_length=100)
    course_date = models.DateTimeField(auto_now_add=True)
    course_blueprint = models.BooleanField(
        default=False
    )  # a blueprint course is a course that is used as a template for other courses
    created_date = models.DateTimeField()
    lastest_update_date = models.DateTimeField()
    # last edited user

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return f"/courses/{self.course_slug}/"


# The module is a chunk of learning, containing a number of lessons or units of learning or assessments.
class Module(models.Model):
    module_name = models.CharField(max_length=100)
    module_overview = models.TextField()
    module_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_name


# The module item is a single unit of learning or assessment within a module.
class ModuleItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_overview = models.TextField()
    item_type = models.CharField(
        max_length=50
    )  # This could be 'lesson', 'quiz', 'assignment', 'video', etc.
    item_id = (
        models.IntegerField()
    )  # This is used to look up the item based on the type.
    item_module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100)
    lesson_overview = models.TextField()
    lesson_content = models.TextField()  # This will be a pages worth of HTML content.
    lesson_module_item = models.ForeignKey(ModuleItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name


# This manages users in the course.
class Enrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    user_role = models.CharField(
        max_length=50, default="student"
    )  # student, teacher, admin, mentor
    date_enroled = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} enrolled in {self.course} on {self.date_enroled}"
