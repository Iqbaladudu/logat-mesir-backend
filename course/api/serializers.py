from rest_framework import serializers
from ..models import Subject, Course, Module, Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"

class ModuleSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Module
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = "__all__"

class SubjectSerizalizer(serializers.ModelSerializer):
    courses = CourseSerializer(read_only=True, many=True)

    class Meta:
        model = Subject
        fields = "__all__"