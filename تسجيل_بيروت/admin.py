from django.contrib import admin
from .models import *

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
# Register your models here.
admin.site.register(تسجيل_بيروت,بيروتAdmin)
admin.site.register(تسجيل_طرابلس,طرابلسAdmin)
admin.site.register(تسجيل_عكار,عكارAdmin)
admin.site.register(تسجيل_صيدا,عرمونAdmin)
admin.site.register(تسجيل_عرمون,صيداAdmin)