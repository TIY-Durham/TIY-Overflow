from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from django.http import HttpResponse

from .models import Question, Answer
from .serializers import QuestionSerializer, QuestionDetailSerializer, AnswerSerializer, UserSerializer
from .permissions import IsAskerOrReadOnly, IsReadOnly

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAskerOrReadOnly)

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        else:
            return QuestionDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'





class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        question_pk = self.kwargs['question_pk']
        get_object_or_404(Question, pk=question_pk)
        return self.queryset.filter(question_id=question_pk)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        context['question_pk'] = self.kwargs['question_pk']
        return context
        # return {'question_pk': self.kwargs['question_pk']}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



def set_timezone_eastern(request):
    request.session['django_timezone'] = 'US/Eastern'
    return HttpResponse('Timeznoe set to eatern')
