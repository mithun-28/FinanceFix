
from django.contrib import admin
from django.urls import path
from financefix import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('expense-tracker/', views.expense_tracker, name='expense_tracker'),
    path('expense-visualization/', views.expense_visualization, name='expense_visualization'),
    path('emi/', views.emi, name='emi_calculator'),
    path('fscore/', views.fscore, name='fscore'),
    path('et/', views.et, name='et'),
]

