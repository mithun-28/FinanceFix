


# financefix/models.py
from djongo import models
from django.contrib.auth.models import User

class Expense(models.Model):
    name = models.CharField(max_length=100)  # Name of the expense (e.g., "Rent", "Groceries")
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Expense amount

    class Meta:
        abstract = True  # Embeds inside another document
from bson import ObjectId
class ExpenseTracker(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=50)  # Name of the month
    year = models.IntegerField()  # Year
    income = models.DecimalField(max_digits=10, decimal_places=2)  # Monthly income
    expenses = models.ArrayField(model_container=Expense)  # List of expenses
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Calculated saved amount

    def save(self, *args, **kwargs):
        total_expenses = sum(expense['amount'] for expense in self.expenses)
        self.saved_amount = self.income - total_expenses  # Calculate savings
        super().save(*args, **kwargs)

    class Meta:
        managed = False  # This disables migrations for this model
