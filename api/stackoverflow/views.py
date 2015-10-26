from django.shortcuts import render
from rest_framework import viewsets

from .models import Question, Answer
from .serializers import QuestionSerializer, QuestionDetailSerializer, AnswerSerializer


# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        else:
            return QuestionDetailSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
