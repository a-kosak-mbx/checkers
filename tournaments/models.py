from django.db import models
from django.utils.translation import gettext_lazy as _


class Turn(models.Model):
    player = models.IntegerField()
    timestamp = models.DateTimeField()


class Step(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    start_position = models.CharField(max_length=2, null=False)
    end_position = models.CharField(max_length=2, null=False)
    models.ManyToManyField(Turn)


class Result(models.Model):
    class Outcome(models.IntegerChoices):
        EMPTY = 0, _('Empty')
        EAT = 1, _('Eat')
        QUEEN = 2, _('Queen')

    outcome = models.IntegerField(choices=Outcome.choices, null=False)
    captured_position = models.CharField(max_length=2, null=True)


'''
Author
---------------------------
| id | name |
---------------------------

Book
------------------------------------------------
| id | title |
------------------------------------------------


AuthorBookRelationships
---------------------
| author_id | book_id |
---------------------
|     1     |    1    |
|     2     |    1    |
|     1     |    2    |
-----------------------
(1) карпук (2) жевняк     (1) высшая математика
(1) карпук                (2) теория вероятности



Game (Player1, Player2, StartTime, EndTime, Winner, Turns)

Turn (Player, Timestamp, Steps, Results)
'''
