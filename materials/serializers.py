from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer:
    lesson_in_course = SerializerMethodField()

    def get_lesson_in_course(self, lesson):
        return Lesson.objects.filter(course=lesson.course)

    class Meta:
        model = Course
        fields = ("name", "description",)


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
