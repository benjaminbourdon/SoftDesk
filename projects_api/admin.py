from django.contrib import admin

from projects_api.models import Project, Issue, Contributor, Comment


class IssuesTubularInline(admin.TabularInline):
    model = Issue
    classes = ["collapse"]
    extra = 1


class CommentsTubularInline(admin.TabularInline):
    model = Comment
    classes = ["collapse"]
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type", "author")
    list_filter = ["type"]
    ordering = ["-id"]

    inlines = [IssuesTubularInline]


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ("project", "user", "permission")
    list_filter = ("project", "user")
    ordering = ["-id"]


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "project", "tag", "priority", "created_time")
    list_filter = ("project", "author")
    ordering = ["-created_time"]
    readonly_fields = ["created_time"]

    inlines = [CommentsTubularInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "issue", "created_time")
    list_filter = ("issue", "issue__project")
    ordering = ["-created_time"]
    readonly_fields = ["created_time"]
