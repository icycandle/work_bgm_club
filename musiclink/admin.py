from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from musiclink.models import User, UserQueue, LinkQueue, MusicLink, MusicRating

admin.site.register(User, UserAdmin)

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
