from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='Name can only contain letters and spaces.',
            ),
        ],
    )

    def __str__(self):
        return self.name
