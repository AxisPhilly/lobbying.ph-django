from django.contrib import admin
from lobbyingph.models import *


class SourceInline(admin.TabularInline):
    model = Source


class Exp_Direct_CommInline(admin.TabularInline):
    model = Exp_Direct_Comm
    filter_horizontal = ['officials', ]


class Exp_OtherInline(admin.TabularInline):
    model = Exp_Other


class Exp_Indirect_CommInline(admin.TabularInline):
    model = Exp_Indirect_Comm


class ArticleInline(admin.TabularInline):
    model = Article


class FilingAdmin(admin.ModelAdmin):
    inlines = [
        SourceInline,
        Exp_Direct_CommInline,
        Exp_Indirect_CommInline,
        Exp_OtherInline
    ]


class IssueAdmin(admin.ModelAdmin):
    inlines = [
        ArticleInline
    ]

admin.site.register(Lobbyist)
admin.site.register(Firm)
admin.site.register(Principal)
admin.site.register(Filing, FilingAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Bill)
admin.site.register(Official)
admin.site.register(Agency)
admin.site.register(Category)
admin.site.register(Communication_Method)
admin.site.register(Receipent_Group)
admin.site.register(Source)
