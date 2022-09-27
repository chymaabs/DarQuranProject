from django.contrib import admin

class بيروتAdmin(admin.ModelAdmin):
    list_display = [ "الاسم_الثلاثي"]

class طرابلسAdmin(admin.ModelAdmin):
    list_display = [ "الاسم_الثلاثي"]

class عكارAdmin(admin.ModelAdmin):
    list_display = [ "الاسم_الثلاثي"]

class عرمونAdmin(admin.ModelAdmin):
    list_display = [ "الاسم_الثلاثي"]

class صيداAdmin(admin.ModelAdmin):
    list_display = [ "الاسم_الثلاثي"]

from .models import *

admin.site.register(بيروت,بيروتAdmin)
admin.site.register(طرابلس,طرابلسAdmin)
admin.site.register(عكار,عكارAdmin)
admin.site.register(عرمون,عرمونAdmin)
admin.site.register(صيدا,صيداAdmin)