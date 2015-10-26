from rest_framework import serializers

from .models import Question, Answer


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='question')

    class Meta:
        model = Answer
        fields = ('id', 'body', 'created_on', 'modified_on', 'question_id', 'was_accepted')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    accepted_answer = AnswerSerializer(many=False)

    class Meta:
        model = Question
        fields = ('id', 'url', 'title', 'body', 'created_on', 'modified_on', 'accepted_answer', 'answers', 'answer_count')
