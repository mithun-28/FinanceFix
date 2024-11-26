# financefix/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile')  # Redirect to profile page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def profile(request):
    return render(request, 'index.html', {'user': request.user})

from django.contrib.auth import logout

def logout_view(request):
    auth_logout(request)
    return redirect('home') 



from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import ExpenseTracker
from .forms import ExpenseForm
import logging

logger = logging.getLogger(__name__)

@login_required
def expense_tracker(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['month']
            year = form.cleaned_data['year']
            income = form.cleaned_data['income']

            expenses = []
            for i in range(1, 4):  # We have 3 dynamic expenses in the form
                name = form.cleaned_data.get(f'expense_name_{i}')
                amount = form.cleaned_data.get(f'expense_amount_{i}')
                if name and amount:
                    expenses.append({'name': name, 'amount': amount})

            # Save the data in MongoDB
            expense_tracker = ExpenseTracker.objects.create(
                user=request.user,
                month=month,
                year=year,
                income=income,
                expenses=expenses
            )

            # Store the ObjectId in the session
            request.session['expense_id'] = str(expense_tracker.pk)  # Store ObjectId as string

            # Redirect to visualization without needing ObjectId in URL
            return redirect('expense_visualization')
    else:
        form = ExpenseForm()

    return render(request, 'expense_tracker.html', {'form': form})

from bson import ObjectId
from django.shortcuts import redirect, render
from .models import ExpenseTracker

def expense_visualization(request):
    expense_id = request.session.get('expense_id')

    if not expense_id:
        # Redirect if no expense_id found in session
        return redirect('expense_tracker')

    try:
        # Fetch the expense data using ObjectId
        expense_tracker = ExpenseTracker.objects.get(pk=ObjectId(expense_id))

        # Prepare data for visualization
        labels = [expense['name'] for expense in expense_tracker.expenses]
        data = [expense['amount'] for expense in expense_tracker.expenses]
        saved_amount = expense_tracker.saved_amount

        return render(request, 'expense_visualization.html', {
            'expense_tracker': expense_tracker,
            'labels': labels,
            'data': data,
            'saved_amount': saved_amount
        })
    except ExpenseTracker.DoesNotExist:
        # Handle case where the ExpenseTracker entry doesn't exist
        return redirect('expense_tracker')
    

def emi(request):
    return render(request, 'emi.html')


def fscore(request):
    return render(request, 'fscore.html')

def et(request):
    return render(request, 'et.html')