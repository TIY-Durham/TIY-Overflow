from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    accepted_answer = models.ForeignKey('Answer', null=True, related_name='accepted_for_question')
    user = models.ForeignKey(User, related_name='questions')

    def answer_count(self):
        return self.answers.count()

    def __str__(self):
        return "{}".format(self.title)


class Answer(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('Question', related_name='answers')
    user = models.ForeignKey(User, related_name='answers')

    def was_accepted(self):
        if self.accepted_for_question.count() > 0:
            return True
        else:
            return False

    def __str__(self):
        return self.body


def make_fake_data(num_questions=500, answers_per_question=5, num_users=5, delete_all=True):
    from faker import Faker
    from random import randint, random, choice
    fake = Faker()

    if delete_all:
        User.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()

    users = [
      User.objects.create_user(username=fake.user_name())
      for _ in range(num_users)
    ]

    for _ in range(num_questions):
        q = Question(
          title=fake.bs().title(),
          body=fake.paragraph(nb_sentences=5),
          user=choice(users)
        )
        q.save()
        q.created_on = fake.date_time_this_year()
        q.modified_on = fake.date_time_between(start_date=q.created_on)
        q.save()

        for __ in range(randint(0, answers_per_question)):
            a = Answer(
              body=fake.paragraph(nb_sentences=2),
              question=q,
              user=choice(users)
            )
            a.save()
            a.created_on = fake.date_time_between(start_date=q.created_on)
            a.modified_on = fake.date_time_between(start_date=a.created_on)
            a.save()

        if random() < 0.5 and q.answers.count() > 0:
            q.accepted_answer = choice(q.answers.all())
            q.save()


def pick_new_dates():
    from faker import Faker
    from random import randint, random, choice
    fake = Faker()

    for q in Question.objects.all():
        q.created_on = fake.date_time_this_year()
        q.modified_on = fake.date_time_between(start_date=q.created_on)
        q.save()

        for a in q.answers.all():
            a.created_on = fake.date_time_between(start_date=q.created_on)
            a.modified_on = fake.date_time_between(start_date=a.created_on)
            a.save()
