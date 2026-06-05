from django.contrib import admin
from api.models import Contributor, Project, Issue, Comment


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "author")


class IssueAdmin(admin.ModelAdmin):
    list_display = ("title", "tag", "priority", "status", "project", "author", "assign")


admin.site.register(Contributor)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment)
