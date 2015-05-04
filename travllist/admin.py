# coding=utf-8
from django.contrib import admin
from models import User, Travel


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'create_time', 'last_modify_time')
    ording = ('-id',)
    list_per_page = 30
    list_filter = ('create_time', 'last_modify_time',)
    search_fields = ['username']


class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'travel_code', 'travel_date', 'adult_price', 'child_price', 'get_time', 'remark')
    ording = ('-id',)
    list_per_page = 30
    search_fields = ['travl_code']


admin.site.register(Travel, TravelAdmin)
admin.site.register(User, UserAdmin)
