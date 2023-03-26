from django.contrib import admin

# Register your models here.
from .models import (User, Subject, Quiz, Question, 
    Answer, Student, TakenQuiz, AuditEntry)


@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    readonly_fields = ['log_time',]
    list_display = ['action', 'username', 'log_time','show_ip_url',]
    list_filter = ['action',]

    def show_ip_url(self, obj):
        ip = obj.ip
        if ip in [None,'127.0.0.1']: return ip
        from django.utils.html import format_html
        url = f'https://ipinfo.io/{obj.ip}/json' #  https://stackoverflow.com/a/55432323/2351696
        
        return format_html("<a href='{url}'>{ip}</a>", url=url, ip=ip)

# admin.site.register(AuditEntry)

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)