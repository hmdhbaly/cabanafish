import random
import string
from django.db import models


def _generate_reference():
    while True:
        ref = (
            random.choice(string.ascii_uppercase)
            + random.choice(string.ascii_uppercase)
            + ''.join(random.choices(string.digits, k=4))
        )
        if not Quotation.objects.filter(reference=ref).exists():
            return ref


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
    reference  = models.CharField(max_length=6, unique=True, blank=True)
    status     = models.CharField(max_length=20, choices=QuotationStatus.choices, default=QuotationStatus.PENDING)
    notes      = models.TextField(blank=True, help_text='Internal notes — not visible to the client.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name        = 'Quotation'
        verbose_name_plural = 'Quotations'

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = _generate_reference()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference} · {self.company} ({self.country}) — {self.product}"
