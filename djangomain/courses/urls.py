from django.urls import path
from .views import CourseCreateView

# These will all sit under the /courses/ URL.
urlpatterns = [
    path("courses/create/", CourseCreateView.as_view(), name="course-create"),
]
