from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse

from musiclink.models import LinkQueue, MusicLink, MusicRating, User, UserQueue
from musiclink.signals import admin_action_send_music_email_to_user


def force_send_music_email(modeladmin, request, user_queryset):
    action_result = ''
    for user in user_queryset:
        result = admin_action_send_music_email_to_user.send(sender=User, user=user)
        action_result += '<p>{0.0} - {0.1}</p>'.format(result)
    return HttpResponse(action_result)
force_send_music_email.short_description = "寄出音樂信件至此使用者的所有email"


class MyUserAdmin(UserAdmin):
    actions = [force_send_music_email]
admin.site.register(User, MyUserAdmin)

class UserQueueAdmin(admin.ModelAdmin):
    pass

class LinkQueueAdmin(admin.ModelAdmin):
    pass

class MusicLinkAdmin(admin.ModelAdmin):
    pass

class MusicRatingAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserQueue, UserQueueAdmin)
admin.site.register(LinkQueue, LinkQueueAdmin)
admin.site.register(MusicLink, MusicLinkAdmin)
admin.site.register(MusicRating, MusicRatingAdmin)
