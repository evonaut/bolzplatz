from django.contrib import admin

from .models import Group, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'score')
    list_filter = ('group',)
    search_fields = ('user__username',)
    ordering = ('user',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    def profile_count(self, obj):
        return obj.profile_set.count()
    profile_count.short_description = 'Users'
    list_display = ('slug', 'profile_count')
    ordering = ('slug',)
