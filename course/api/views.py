from rest_framework import generics
from ..models import Subject, Course, Content
from .serializers import SubjectSerizalizer, CourseSerializer, ContentSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerizalizer