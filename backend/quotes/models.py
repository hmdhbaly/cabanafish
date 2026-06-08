from django.db import models


class QuotationStatus(models.TextChoices):
    PENDING   = 'pending',   'Pending'
    REVIEWED  = 'reviewed',  'Reviewed'
    COMPLETED = 'completed', 'Completed'
    DECLINED  = 'declined',  'Declined'


class Quotation(models.Model):
    # ── Company information ───────────────────────────────────────────────
    name    = models.CharField(max_length=200)
    email   = models.EmailField()
    company = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    # ── Product requirements ──────────────────────────────────────────────
    product  = models.CharField(max_length=100)
    format   = models.CharField(max_length=100, blank=True)
    quantity = models.CharField(max_length=100, blank=True)
    port     = models.CharField(max_length=100, blank=True)
    message  = models.TextField(blank=True)

    # ── Management ────────────────────────────────────────────────────────
    status     = models.CharField(max_length=20, choices=QuotationStatus.choices, default=QuotationStatus.PENDING)
    notes      = models.TextField(blank=True, help_text='Internal notes — not visible to the client.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'Quotation'
        verbose_name_plural = 'Quotations'

    def __str__(self):
        return f"#{self.pk} · {self.company} ({self.country}) — {self.product}"
