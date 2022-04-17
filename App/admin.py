from django.contrib import admin
from App.models import Order, Flavor
from django.utils.html import format_html

admin.site.register(Flavor)

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['situation']
    list_display = ['id', 'name', 'flavour', 'created_at', 'status', '_']

    def _(self, obj):
        if obj.situation == 'Done':
            return True
        else:
            return False
    _.boolean = True

    def status(self, obj):
        if obj.situation == 'Done':
            color = '#281745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True

admin.site.register(Order, OrderAdmin)

