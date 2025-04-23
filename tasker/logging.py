from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View


class LogOutView(LoginRequiredMixin, View):

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        if request.method == 'POST':
            if request.user.is_authenticated:
                logout(request)
        success_url = reverse_lazy("tasker:index")
        return redirect(success_url)
