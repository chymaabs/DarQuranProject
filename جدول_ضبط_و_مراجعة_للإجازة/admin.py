from django.contrib import admin
from .models import *


class بيروتAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الطالب"]


class طرابلسAdmin(admin.ModelAdmin):
    list_display = ["اسم_الطالب"]


class عكارAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الطالب"]


class عرمونAdmin(admin.ModelAdmin):
    list_display =[ "اسم_الطالب"]


class صيداAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الطالب"]


admin.site.register(بيروت, بيروتAdmin)
admin.site.register(طرابلس, طرابلسAdmin)
admin.site.register(عكار, عكارAdmin)
admin.site.register(عرمون, عرمونAdmin)
admin.site.register(صيدا, صيداAdmin)
