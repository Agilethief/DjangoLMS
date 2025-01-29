from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from .models import Course, Module, ModuleItem, Lesson, Enrolment
from .serializers import (
    CourseSerializer,
    ModuleSerializer,
    ModuleItemSerializer,
    LessonSerializer,
    EnrolmentSerializer,
)


# Create your views here.
class CourseCreateView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]  # TODO: Apply proper permissions!!


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()  # could sort here as well.
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]  # TODO: Apply proper permissions!!


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.AllowAny]  # TODO: Apply proper permissions!!


class ModuleItemViewSet(viewsets.ModelViewSet):
    queryset = ModuleItem.objects.all()
    serializer_class = ModuleItemSerializer
    permission_classes = [permissions.AllowAny]  # TODO: Apply proper permissions!!


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.AllowAny]  # TODO: Apply proper permissions!!


class EnrolmentViewSet(viewsets.ModelViewSet):
    queryset = Enrolment.objects.all()
    serializer_class = EnrolmentSerializer
    permission_classes = [permissions.AllowAny]  # TODO: Apply proper permissions!!
