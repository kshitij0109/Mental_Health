from django.contrib import admin
from .models import Session, CounselingQueue, CounselingSession

admin.site.register(Session)
admin.site.register(CounselingSession)
admin.site.register(CounselingQueue)

