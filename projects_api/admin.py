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


admin.site.register(Issue)
admin.site.register(Comment)
