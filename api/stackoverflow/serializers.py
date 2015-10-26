from rest_framework import serializers

from .models import Question, Answer


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'created_on', 'modified_on', 'accepted_answer', 'answers', 'answer_count')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='question')
    class Meta:
        model = Answer
        fields = ('id', 'body', 'created_on', 'modified_on', 'question_id', 'was_accepted')
