# financefix/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)


# financefix/forms.py
from django import forms
from .models import ExpenseTracker, Expense

class ExpenseForm(forms.Form):
    month = forms.CharField(max_length=50, label="Month")
    year = forms.IntegerField(label="Year")
    income = forms.DecimalField(max_digits=10, decimal_places=2, label="Monthly Income")

    # Dynamically generate multiple expense fields
    expense_name_1 = forms.CharField(max_length=100, label="Expense 1 Name")
    expense_amount_1 = forms.DecimalField(max_digits=10, decimal_places=2, label="Expense 1 Amount")

    expense_name_2 = forms.CharField(max_length=100, label="Expense 2 Name", required=False)
    expense_amount_2 = forms.DecimalField(max_digits=10, decimal_places=2, label="Expense 2 Amount", required=False)

    expense_name_3 = forms.CharField(max_length=100, label="Expense 3 Name", required=False)
    expense_amount_3 = forms.DecimalField(max_digits=10, decimal_places=2, label="Expense 3 Amount", required=False)

    # Add more fields as necessary




