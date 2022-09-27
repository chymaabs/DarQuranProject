from django.contrib import admin
from .models import *

class بيروتAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الحافظ"]

class طرابلسAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الحافظ"]

class عكارAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الحافظ"]

class عرمونAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الحافظ"]

class صيداAdmin(admin.ModelAdmin):
    list_display = [ "اسم_الحافظ"]
admin.site.register(بيروت,بيروتAdmin)
admin.site.register(طرابلس,طرابلسAdmin)
admin.site.register(عكار,عكارAdmin)
admin.site.register(عرمون,عرمونAdmin)
admin.site.register(صيدا,صيداAdmin)
