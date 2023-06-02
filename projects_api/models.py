from django.conf import settings
from django.db import models


class Project(models.Model):
    class Plateforms(models.TextChoices):
        BACKEND = "BE", "Back-End"
        FRONTEND = "FE", "Front-End"
        IOS = "IO", "iOS"
        ANDROID = "AN", "Android"

    title = models.CharField(max_length=128, verbose_name="titre")
    description = models.CharField(
        max_length=2048,
        blank=True,
        verbose_name="description",
    )
    type = models.CharField(
        max_length=2,
        choices=Plateforms.choices,
        verbose_name="Type (plateforme)",
    )
    # author = models.ForeignKey(
    #     to=settings.AUTH_USER_MODEL,
    #     on_delete=models.PROTECT,
    #     verbose_name = "Auteurice"
    # )

    def __str__(self):
        return f"#{self.id} - {self.title}"

    def contributors_name(self):
        # return [contribution.user.username for contribution in self.contributors.all()]
        return self.contributors.values_list("user__username", flat=True)

    class Meta:
        verbose_name = "Projet"


class Contributor(models.Model):
    class Permission(models.IntegerChoices):
        CONTRIBUTOR = 1, "Contributeur ou Contributrice"
        AUTHOR = 9, "Auteur ou Autrice"

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributions",
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name="contributors",
    )
    permission = models.IntegerField(
        choices=Permission.choices,
        default=Permission.CONTRIBUTOR,
    )
    role = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.user} participe à {self.project.title}"

    class Meta:
        unique_together = (
            "user",
            "project",
        )


class Issue(models.Model):
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
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
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

    @property
    def contributors(self):
        return self.project.contributors.all()


class Comment(models.Model):
    description = models.CharField(max_length=2048)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_comments",
    )
    issue = models.ForeignKey(
        to=Issue,
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(auto_now_add=True)

    @property
    def contributors(self):
        return self.issue.project.contributors.all()
