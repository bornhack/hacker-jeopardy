from django.db import models


class Answer(models.Model):
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    answer = models.CharField(max_length=255)

    question = models.CharField(max_length=255)

    VIDEO = 'video'
    IMAGE = 'image'
    AUDIO = 'audio'
    CHANCE = 'chance'
    TEXT = 'text'
    ANSWER_TYPES = [
        (VIDEO, 'Video'),
        (IMAGE, 'Image'),
        (AUDIO, 'Audio'),
        (TEXT, 'Text'),
    ]

    answer_type = models.CharField(
        max_length=10,
        choices=ANSWER_TYPES,
        default=TEXT
    )

    attachment = models.FileField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.answer


class AnswerCategoryRelation(models.Model):
    answer = models.ForeignKey('jeopardy.Answer')
    category = models.ForeignKey('jeopardy.Category')
    value = models.PositiveIntegerField()


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=255)

    answers = models.ManyToManyField(
        'jeopardy.Answer',
        related_name='category',
        through='jeopardy.AnswerCategoryRelation',
    )

    def __str__(self):
        return self.title


class CategoryRoundRelation(models.Model):
    category = models.ForeignKey('jeopardy.Category')
    round = models.ForeignKey('jeopardy.Round')
    number = models.PositiveIntegerField()


class Round(models.Model):
    class Meta:
        verbose_name = 'Round'
        verbose_name_plural = 'Rounds'

    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(
        'jeopardy.Category',
        related_name='round'
    )

    NORMAL = 'normal'
    CHANCE = 'chance'
    TYPES = [
        (NORMAL, 'Normal'),
        (CHANCE, 'Chance')
    ]

    round_type = models.CharField(max_length=10, choices=TYPES, default=NORMAL)

    def __str__(self):
        return self.name


class RoundGameRelation(models.Model):
    round = models.ForeignKey('jeopardy.Round')
    game = models.ForeignKey('jeopardy.Game')
    number = models.PositiveSmallIntegerField()


class Game(models.Model):
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    title = models.CharField(max_length=255)

    rounds = models.ManyToManyField(
        'jeopardy.Round',
        related_name='game'
    )

    contestants = models.ManyToManyField(
        'jeopardy.Contestant',
        related_name='game'
    )

    def __str__(self):
        return self.title


class Contestant(models.Model):
    class Meta:
        verbose_name = 'Contestant'
        verbose_name_plural = 'Contestants'

    name = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return self.name
