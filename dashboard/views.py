from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# first entry view for when the user logs in
@login_required
def DashboardView(request):
    return render(request, 'dashboard/index.html' )