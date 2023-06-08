import random

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class NumeroSecreto(models.Model):
    id = models.BigAutoField(primary_key=True)
    segredo = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.segredo:
            self.segredo = random.randint(0, 100)
        super(NumeroSecreto, self).save(*args, **kwargs)


class Chute(models.Model):
    id_segredo = models.ForeignKey(
        "NumeroSecreto",
        on_delete=models.CASCADE,
    )
    tentativa = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    data_hora = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
