from django.contrib import admin
from lobbyingph.models import Lobbyist, Firm, Principal
from lobbyingph.models import Filing, Exp_Direct_Comm, Exp_Indirect_Comm
from lobbyingph.models import Issue, Bill, Official, Agency, Category

class Exp_Direct_CommInline(admin.TabularInline):
    model = Exp_Direct_Comm

class Exp_Indirect_CommInline(admin.TabularInline):
    model = Exp_Indirect_Comm

class FilingAdmin(admin.ModelAdmin):
    inlines = [
        Exp_Direct_CommInline,
        Exp_Indirect_CommInline  
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