from django.contrib import admin
from .models import Portfolio
#from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter  # 모듈 불러오기


# Register your models here.
# admin.py
class PortfolioAdmin(admin.ModelAdmin):
    admin.site.register(Portfolio)


