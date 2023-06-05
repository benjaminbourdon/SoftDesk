from django.contrib import admin

from projects_api.models import Project, Issue, Contributor, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type")
    list_filter = ["type"]
    ordering = ["-id"]


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ("project", "user")
    list_filter = ("project", "user")
    ordering = ["-id"]


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "project", "tag", "priority")
    list_filter = ("project", "author")
    ordering = ["-created_time"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "issue")
    list_filter = ("issue", "issue__project")
    ordering = ["-created_time"]
