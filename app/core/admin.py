from django.contrib import admin # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from core import models
from game.models import Game
from tag.models import Tag
from gameconsole.models import GameConsole
from publisher.models import Publisher
from consolemaker.models import ConsoleMaker

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ('Permissions'),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser"
                )
            }
        )
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }),
    )

admin.site.register(models.User, UserAdmin)
admin.site.register(Game)
admin.site.register(Tag)
admin.site.register(GameConsole)
admin.site.register(Publisher)
admin.site.register(ConsoleMaker)