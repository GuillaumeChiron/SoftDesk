from django.db import models
from django.conf import settings
import uuid


class Contributor(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributions",
    )
    project = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributors",
    )
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "project"], name="unique_contributor_per_project"
            )
        ]

    def __str__(self):
        return f"{self.author} -> {self.project}"


class Project(models.Model):

    BACKEND = "Back-end"
    FRONTEND = "Front-end"
    IOS = "IOS"
    ANDROID = "Android"

    TYPE_CHOICES = [
        (BACKEND, "Back-end"),
        (FRONTEND, "Front-end"),
        (IOS, "IOS"),
        (ANDROID, "Android"),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_projects",
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Issue(models.Model):

    BUG = "Bug"
    FEATURE = "Feature"
    TASK = "Task"

    TAG_CHOICES = [(BUG, "Bug"), (FEATURE, "Feature"), (TASK, "Task")]

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

    PRIORITY_CHOICES = [(LOW, "Low"), (MEDIUM, "Medium"), (HIGH, "High")]

    TO_DO = "To do"
    IN_PORGRESS = "In progress"
    FINISHED = "Finished"

    STATUS_CHOICES = [
        (TO_DO, "To do"),
        (IN_PORGRESS, "In_prgoress"),
        (FINISHED, "Finished"),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField()
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TO_DO)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="issues"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_issues",
    )
    assign = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="assign_issues",
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_comments",
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} à commenté(e) {self.issue}"
