from django.contrib import admin
from .models import (
    AboutPageContent,
    Activity, ActivityMedia,
    Announcement,
    TeamMember,
    Sponsor,
    Visit,
    VisitMedia
)

admin.site.register(AboutPageContent)
admin.site.register(Announcement)
admin.site.register(Activity)
admin.site.register(ActivityMedia)
admin.site.register(TeamMember)
admin.site.register(Sponsor)
admin.site.register(Visit)
admin.site.register(VisitMedia)