from django.core.exceptions import ValidationError
from django.db import models


class OrderWithRespectToConstraintMixin(models.Model):

    child_limit = None

    class Meta:
        abstract = True

    def clean(self):
        super().clean()

        key = self._meta.order_with_respect_to.attname

        kwargs = {
            key: getattr(self, key)
        }

        if self.__class__.objects.filter(**kwargs).count() >= self.child_limit:
            raise ValidationError('Limit of {} reached'.format(self.child_limit))


class Answer(OrderWithRespectToConstraintMixin, models.Model):
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        order_with_respect_to = 'category'

    answer = models.CharField(max_length=255)
    category = models.ForeignKey('jeopardy.Category')

    child_limit = 5

    VIDEO = 'video'
    IMAGE = 'image'
    AUDIO = 'audio'
    CHANCE = 'chance'
    TEXT = 'text'
    ANSWER_TYPES = [
        (VIDEO, 'Video'),
        (IMAGE, 'Image'),
        (AUDIO, 'Audio'),
        (CHANCE, 'Chance'),
        (TEXT, 'Text'),
    ]

    answer_type = models.CharField(
        max_length=10,
        choices=ANSWER_TYPES,
        default=TEXT
    )

    def __str__(self):
        return self.answer


class Category(OrderWithRespectToConstraintMixin, models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        order_with_respect_to = 'round'

    child_limit = 6

    title = models.CharField(max_length=255)
    round = models.ForeignKey('jeopardy.Round')

    def __str__(self):
        return self.title


class Round(OrderWithRespectToConstraintMixin, models.Model):
    class Meta:
        verbose_name = 'Round'
        verbose_name_plural = 'Rounds'
        order_with_respect_to = 'game'

    child_limit = 3

    game = models.ForeignKey('jeopardy.Game')


class Game(models.Model):
    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    title = models.CharField(max_length=255)

    player1 = models.ForeignKey('jeopardy.player', related_name='player1')
    player2 = models.ForeignKey('jeopardy.player', related_name='player2')
    player3 = models.ForeignKey('jeopardy.player', related_name='player3')

    def __str__(self):
        return self.title


class Player(models.Model):
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    name = models.CharField(max_length=255)
    points = models.IntegerField()

    def __str__(self):
        return self.name
