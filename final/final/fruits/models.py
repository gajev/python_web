from django.db import models
from django.core import validators


def check_first_letter_is_alpha(some_string):
    if not some_string[0].isalpha():
        raise validators.ValidationError("Your name must start with a letter!")


def check_string_is_alpha_only(some_string):
    for ch in some_string:
        if not ch.isalpha():
            raise validators.ValidationError("Fruit name should contain only letters!")
# Create your models here.


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 25
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 35
    MIN_LEN_LAST_NAME = 1
    MAX_LEN_EMAIL = 40
    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 8

    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_FIRST_NAME,
        verbose_name="First Name",
        validators=[
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            check_first_letter_is_alpha,
        ],
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_LAST_NAME,
        verbose_name="Last Name",
        validators=[
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            check_first_letter_is_alpha,
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=MAX_LEN_EMAIL,
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASSWORD,
        validators=[
            validators.MinLengthValidator(MIN_LEN_PASSWORD),
        ],
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name="Image URL"
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18
    )


class Fruit(models.Model):
    MAX_LEN_NAME = 30
    MIN_LEN_NAME = 2

    name = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_NAME,
        validators=[
            validators.MinLengthValidator(MIN_LEN_NAME),
            check_string_is_alpha_only,
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

