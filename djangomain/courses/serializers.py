from .models import Course, Module, ModuleItem, Lesson, Enrolment
from rest_framework import serializers

# Note, we can grab all their fields as there is no sensitive data in the models.


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def validate_course_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Course name must be at least 3 characters long."
            )

        if Course.objects.filter(course_name=value).exists():
            raise serializers.ValidationError(
                "Course name must be unique. A duplicate exists"
            )

        return value


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class ModuleItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModuleItem
        fields = "__all__"


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class EnrolmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrolment
        fields = "__all__"
