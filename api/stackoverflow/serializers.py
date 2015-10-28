from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='question')
    answerer = serializers.StringRelatedField(read_only=True, source='user')

    class Meta:
        model = Answer
        fields = ('id', 'body', 'created_on', 'modified_on', 'was_accepted', 'question_id', 'answerer')

    def create(self, validated_data):
        validated_data['question_id'] = self.context['question_pk']
        answer = Answer.objects.create(**validated_data)
        return answer


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    accepted_answer = serializers.StringRelatedField(many=False, read_only=False)
    asker = serializers.StringRelatedField(read_only=True, source='user')

    # very_special_title = serializers.CharField(source='title')

    class Meta:
        model = Question
        fields = ('id', 'url', 'title', 'body', 'created_on', 'modified_on', 'accepted_answer', 'answer_count', 'asker')


class QuestionDetailSerializer(QuestionSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta(QuestionSerializer.Meta):
        fields = tuple(list(QuestionSerializer.Meta.fields) + ['answers'])


class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'questions', 'answers', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
