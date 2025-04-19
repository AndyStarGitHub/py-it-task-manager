from django.contrib.auth import logout
from django.shortcuts import redirect


def user_logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
    return redirect('/accounts/logged_out.html')
