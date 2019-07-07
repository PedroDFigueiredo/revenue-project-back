from django.contrib import admin

# Register your models here.
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
	model = Transaction
	list_display = ('value', 'description', 'date')


admin.site.register(Transaction, TransactionAdmin)
