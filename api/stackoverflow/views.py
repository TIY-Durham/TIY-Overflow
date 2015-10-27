from django.shortcuts import render, get_object_or_404
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

    def get_queryset(self):
        question_pk = self.kwargs['question_pk']
        get_object_or_404(Question, pk=question_pk)
        return self.queryset.filter(question_id=question_pk)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        context['question_pk'] = self.kwargs['question_pk']
        return context
        # return {'question_pk': self.kwargs['question_pk']}
