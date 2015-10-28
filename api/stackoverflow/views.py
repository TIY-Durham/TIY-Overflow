from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import detail_route, api_view
from rest_framework.response import Response


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

@api_view(['GET'])
def whoami(request):
    user = request.user
    if user.is_authenticated():
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response('', status=status.HTTP_404_NOT_FOUND)



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
