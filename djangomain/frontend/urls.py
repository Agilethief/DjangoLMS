from django.urls import path
from . import views

# These will all sit under the /frontend/ URL.
urlpatterns = [
    path("", views.home, name="frontend-home"),  # This is the home page.
    # path("", views.courses, name="frontend-courses"),  # List all courses
    # path("", views.people, name="frontend-people"),  # List all users and their role
]
