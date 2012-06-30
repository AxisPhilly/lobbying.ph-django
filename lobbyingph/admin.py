from django.contrib import admin
from lobbyingph.models import *

class Exp_Direct_CommInline(admin.TabularInline):
    model = Exp_Direct_Comm
    filter_horizontal = ['officials',]

class Exp_OtherInline(admin.TabularInline):
    model = Exp_Other

class Exp_Indirect_CommInline(admin.TabularInline):
    model = Exp_Indirect_Comm

class FilingAdmin(admin.ModelAdmin):
    inlines = [
        Exp_Direct_CommInline,
        Exp_Indirect_CommInline, 
        Exp_OtherInline
    ]

admin.site.register(Lobbyist)
admin.site.register(Firm)
admin.site.register(Principal)
admin.site.register(Filing, FilingAdmin)
admin.site.register(Issue)
admin.site.register(Bill)
admin.site.register(Official)
admin.site.register(Agency)
admin.site.register(Category)
admin.site.register(Communication_Method)
admin.site.register(Receipent_Group)