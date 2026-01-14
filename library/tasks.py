from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from .models import BookLoan


@shared_task
def check_overdue_loans():
    today = timezone.now().date()
    overdue_loans = BookLoan.objects.filter(
        return_date__lt=today, return_date__isnull=False
    )

    for loan in overdue_loans:
        send_mail(
            "Просроченная книга",
            f'Книга "{loan.book.title}" была выдана вам {loan.loaned_at}. Пожалуйста, верните её.',
            "from@example.com",
            [loan.user.email],
            fail_silently=False,
        )
