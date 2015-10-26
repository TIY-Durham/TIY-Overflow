from rest_framework import serializers

from .models import Question, Answer


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='question')

    class Meta:
        model = Answer
        fields = ('id', 'body', 'created_on', 'modified_on', 'question_id', 'was_accepted')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    accepted_answer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Question
        fields = ('id', 'url', 'title', 'body', 'created_on', 'modified_on', 'accepted_answer', 'answer_count')


class QuestionDetailSerializer(QuestionSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta(QuestionSerializer.Meta):
        fields = tuple(list(QuestionSerializer.Meta.fields) + ['answers'])
