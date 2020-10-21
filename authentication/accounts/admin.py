from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'fullname', 'employee_id', 'student_id', 'date_joined', 'last_login', 'is_admin', 'is_staff'
    ]
    search_fields = ('email', 'employee_id', 'student_id')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
