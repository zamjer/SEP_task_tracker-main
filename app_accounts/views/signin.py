from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from app_accounts.forms import SignInForm


class SignInView(View):
    """ User registration view """

    template_name = "app_accounts/signin.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("app_events:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)
