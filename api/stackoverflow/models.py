from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    accepted_answer = models.ForeignKey('Answer', null=True, related_name='accepted_for_question')

    def answer_count(self):
        return self.answers.count()

    def __str__(self):
        return "{}".format(self.title)


class Answer(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('Question', related_name='answers')

    def was_accepted(self):
        if self.accepted_for_question.count() > 0:
            return True
        else:
            return False

    def __str__(self):
        return self.body
