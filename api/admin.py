from django.contrib import admin
from api.models import Contributor, Project, Issue, Comment


class ContributorAdmin(admin.ModelAdmin):
    list_display = ("user", "project")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "author")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "tag", "priority", "status", "project", "author", "assign")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "issue")


admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
