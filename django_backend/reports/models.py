from django.db import models


class ReportLog(models.Model):

    REPORT_CHOICES = [
        ("sales_csv", "Sales CSV"),
        ("orders_csv", "Orders CSV"),
        ("products_csv", "Products CSV"),
        ("sales_pdf", "Sales PDF"),
    ]

    report_type = models.CharField(
        max_length=30,
        choices=REPORT_CHOICES
    )

    generated_by = models.CharField(
        max_length=150
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.report_type} - {self.generated_at}"
