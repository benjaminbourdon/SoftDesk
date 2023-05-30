from django.conf import settings
from django.db import models


class Projects(models.Model):
    class Plateforms(models.TextChoices):
        BACKEND = "BE", "Back-End"
        FRONTEND = "FE", "Front-End"
        IOS = "IO", "iOS"
        ANDROID = "AN", "Android"

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    type = models.CharField(max_length=2, choices=Plateforms.choices)
    # author = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL,
    #     on_delete=models.PROTECT,
    # )


class Contributors(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributions",
    )
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    # permission = models.TextChoices()
    # role = models.CharField()


class Issues(models.Model):
    class Tag(models.TextChoices):
        BUG = "BUG", "Bug"
        IMPROVEMENT = "IMPROVE", "Amélioration"
        TASK = "TASK", "Tâche"

    class Priority(models.TextChoices):
        LOW = "LOW", "Faible"
        MODERATE = "MODERATE", "Moyenne"
        HIGH = "HIGH", "Élevée"

    class Status(models.TextChoices):
        TO_DO = "TODO", "À faire"
        IN_PROGRESS = "PROGRESS", "En cours"
        COMPLETED = "COMPLETED", "Terminé"

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    tag = models.CharField(max_length=10, choices=Tag.choices)
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MODERATE,
    )
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.TO_DO,
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_projects",
    )
    assignee = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_projects",
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    description = models.CharField(max_length=2048)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_comments",
    )
    issue = models.ForeignKey(
        to=Issues,
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(auto_now_add=True)
