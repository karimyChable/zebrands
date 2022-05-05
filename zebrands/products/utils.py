from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template


def send_product_email(new_product):
    #TODO: Pending Filter by admins
    admins = User.objects.all()
    # emails = [admin.email for admin in admins]
    emails = ['karimy@sunwise.mx']

    template_html = get_template('product.html')
    context = {
        'action': 'agregado' if new_product else 'editado'
    }
    html_message = template_html.render(context)
    send_mail(
        'Modificación en Catálogo de Productos',
        'Modificación en Catálogo de Productos',
        settings.EMAIL_HOST_USER,
        emails,
        html_message=html_message
    )
