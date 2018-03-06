# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .	models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(HostelAdmin)
admin.site.register(HostelBlock)
admin.site.register(Complaint)
admin.site.register(RoomAllotment)
admin.site.register(NoticeBoard)