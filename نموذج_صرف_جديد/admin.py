from django.contrib import admin
from .models import *

class بيروتAdmin(admin.ModelAdmin):
    list_display =["لامر"]

class طرابلسAdmin(admin.ModelAdmin):
    list_display =["لامر"]

class عكارAdmin(admin.ModelAdmin):
    list_display =["لامر"]

class عرمونAdmin(admin.ModelAdmin):
    list_display =["لامر"]

class صيداAdmin(admin.ModelAdmin):
    list_display =["لامر"]


admin.site.register(بيروت,بيروتAdmin)
admin.site.register(طرابلس,طرابلسAdmin)
admin.site.register(عكار,عكارAdmin)
admin.site.register(عرمون,عرمونAdmin)
admin.site.register(صيدا,صيداAdmin)