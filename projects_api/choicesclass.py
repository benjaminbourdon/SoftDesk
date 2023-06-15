from django.db import models


class Permission(models.IntegerChoices):
    CONTRIBUTOR = 1, "Contributeur ou Contributrice"
    AUTHOR = 9, "Auteur ou Autrice"
