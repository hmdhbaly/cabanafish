import logging
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Quotation

logger = logging.getLogger(__name__)

REQUIRED_FIELDS = ['name', 'email', 'company', 'country', 'product']


@csrf_exempt
def health_check(request):
    from django.db import connection
    try:
        connection.ensure_connection()
        db_status = 'ok'
    except Exception as e:
        db_status = str(e)
    return JsonResponse({'status': 'ok', 'db': db_status})



@csrf_exempt
@require_POST
def submit_quote(request):
    data = request.POST

    # Validate required fields
    missing = [f for f in REQUIRED_FIELDS if not data.get(f, '').strip()]
    if missing:
        return JsonResponse({'ok': False, 'missing': missing}, status=400)

    # Persist to database
    quotation = Quotation.objects.create(
        name     = data['name'].strip(),
        email    = data['email'].strip(),
        company  = data['company'].strip(),
        country  = data['country'].strip(),
        product  = data['product'].strip(),
        format   = data.get('format', '').strip(),
        quantity = data.get('quantity', '').strip(),
        port     = data.get('port', '').strip(),
        message  = data.get('message', '').strip(),
    )

    # Send admin notification email
    _send_admin_email(quotation)

    # Send confirmation to the client
    _send_client_email(quotation)

    return JsonResponse({'ok': True, 'id': quotation.pk})


# ── Email helpers ──────────────────────────────────────────────────────────────

def _send_admin_email(q: Quotation):
    subject = f"[CABANA FISH] New quotation #{q.pk} — {q.company} · {q.country}"
    body = f"""\
New quotation request received on cabanafish.com

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPANY INFORMATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Name     : {q.name}
Email    : {q.email}
Company  : {q.company}
Country  : {q.country}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRODUCT REQUIREMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Product  : {q.product}
Format   : {q.format  or '—'}
Quantity : {q.quantity or '—'}
Port     : {q.port     or '—'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ADDITIONAL DETAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{q.message or '(none)'}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reference : #{q.pk}
Received  : {q.created_at.strftime('%Y-%m-%d %H:%M UTC')}
""".strip()

    _try_send(subject, body, [settings.ADMIN_EMAIL])


def _send_client_email(q: Quotation):
    subject = f"Your quotation request has been received — CABANA FISH"
    body = f"""\
Dear {q.name},

Thank you for contacting CABANA FISH.

We have received your quotation request for {q.product} and our export team
will review it and get back to you within one business day.

Your request reference is #{q.pk}. Please quote this number in any follow-up.

If you have urgent questions, please write to {settings.ADMIN_EMAIL}.

Best regards,
CABANA FISH Export Team
Nouadhibou, Mauritania
""".strip()

    _try_send(subject, body, [q.email])


def _try_send(subject: str, body: str, recipients: list):
    try:
        send_mail(
            subject      = subject,
            message      = body,
            from_email   = settings.DEFAULT_FROM_EMAIL,
            recipient_list = recipients,
            fail_silently  = False,
        )
    except Exception as exc:
        logger.error("Email to %s failed: %s", recipients, exc)
