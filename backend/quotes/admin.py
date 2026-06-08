from django.contrib import admin
from django.utils.html import format_html
from .models import Quotation, QuotationStatus


STATUS_COLORS = {
    QuotationStatus.PENDING:   ('#f59e0b', '#fff'),
    QuotationStatus.REVIEWED:  ('#3b82f6', '#fff'),
    QuotationStatus.COMPLETED: ('#10b981', '#fff'),
    QuotationStatus.DECLINED:  ('#ef4444', '#fff'),
}


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display  = ('ref', 'company', 'name', 'email', 'country', 'product', 'colored_status', 'status', 'created_at')
    list_filter   = ('status', 'product', 'country')
    search_fields = ('name', 'email', 'company', 'country', 'product', 'message')
    list_editable = ('status',)   # change status directly from the list
    readonly_fields = ('created_at', 'updated_at')
    ordering      = ('-created_at',)
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Company Information', {
            'fields': ('name', 'email', 'company', 'country'),
        }),
        ('Product Requirements', {
            'fields': ('product', 'format', 'quantity', 'port', 'message'),
        }),
        ('Management', {
            'fields': ('status', 'notes', 'created_at', 'updated_at'),
        }),
    )

    def ref(self, obj):
        return f'#{obj.pk}'
    ref.short_description = 'Ref'
    ref.admin_order_field = 'pk'

    def colored_status(self, obj):
        bg, fg = STATUS_COLORS.get(obj.status, ('#6b7280', '#fff'))
        return format_html(
            '<span style="background:{};color:{};padding:3px 10px;border-radius:3px;font-size:11px;font-weight:700;">{}</span>',
            bg, fg, obj.get_status_display(),
        )
    colored_status.short_description = 'Status'
    colored_status.admin_order_field = 'status'
