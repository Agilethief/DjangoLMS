# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Course
from django.urls import reverse

# Create your tests here.


class CourseCreateAPITestCase(APITestCase):
    def setUp(self):

        Course.objects.create(
            course_name="Test Course",
            course_overview="xyz.",
            course_duration=5,
            course_image="https://www.example.com/image.jpg",
            course_slug="test-course",
            course_date="2021-01-01",
            course_blueprint=False,
            created_date="2021-01-01",
            lastest_update_date="2021-01-01",
        )

    # Sanity check to ensure setup is functional.
    def test_get_course_name(self):
        course = Course.objects.get(course_name="Test Course")
        self.assertEqual(course.course_name, "Test Course")

    def test_create_course(self):
        url = reverse("course-create")
        data = {
            "course_name": "Test Course Unique",
            "course_overview": "This is a test course.",
            "course_duration": 10,
            "course_image": "https://www.example.com/image.jpg",
            "course_slug": "test-course",
            "course_date": "2021-01-01",
            "course_blueprint": False,
            "created_date": "2021-01-01",
            "lastest_update_date": "2021-01-01",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["course_name"], "Test Course Unique")

    def test_create_course_invalid_data(self):
        url = reverse("course-create")
        data = {
            "course_name": "",
            "course_overview": "This is a test course.",
            "course_duration": 10,
            "course_image": "https://www.example.com/image.jpg",
            "course_slug": "test-course",
            "course_date": "2021-01-01",
            "course_blueprint": False,
            "created_date": "2021-01-01",
            "lastest_update_date": "2021-01-01",
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Called afer the original creation test.
    def test_duplicate_course_creation(self):
        url = reverse("course-create")
        data = {
            "course_name": "Test Course",
            "course_overview": "This is a test course.",
            "course_duration": 10,
            "course_image": "https://www.example.com/image.jpg",
            "course_slug": "test-course",
            "course_date": "2021-01-01",
            "course_blueprint": False,
            "created_date": "2021-01-01",
            "lastest_update_date": "2021-01-01",
        }

        response = self.client.post(url, data, format="json")

        # Check for HTTP 400 response
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn("course_name", response.data)
        self.assertEqual(
            response.data["course_name"][0],
            "course with this course name already exists.",
        )
