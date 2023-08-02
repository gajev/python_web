from django.core import validators
from django.db import models


def check_age_is_over_18(value):
    if value < 18:
        raise validators.ValidationError("")


def len_username_is_over_2(value):
    if len(value) < 2:
        raise validators.ValidationError("The username must be a minimum of 2 chars")


def car_year_validator(value):
    if not 1980 <= value <= 2049:
        raise validators.ValidationError("Year must be between 1980 and 2049")


def price_validator(value):
    if value < 1:
        raise validators.ValidationError("")


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MAX_LEN_PASSWORD = 30
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_USERNAME,
        validators=[
            len_username_is_over_2
        ],
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            check_age_is_over_18,
        ],
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASSWORD,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_FIRST_NAME,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_LAST_NAME,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MAX_LEN_CAR_TYPE = 10
    MAX_LEN_CAR_MODEL = 20
    MIN_LEN_CAR_MODEL = 2

    SPORTSCAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_CHOICES = (
        (SPORTSCAR, SPORTSCAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    car_type = models.CharField(
        null=False,
        blank=False,
        choices=CAR_CHOICES,
        max_length=MAX_LEN_CAR_TYPE,
        verbose_name="Type"
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_CAR_MODEL,
        validators=[
            validators.MinLengthValidator(MIN_LEN_CAR_MODEL)
        ],
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            car_year_validator
        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            price_validator
        ],
    )