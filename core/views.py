from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm
from .utils import send_contact_email


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm
        context = {"form": form}
        return render(request, "core/index.html", context)

    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            form = ContactForm(request.POST)
            if form.is_valid():
                context = {"name": name, "email": email, "message": message}
                send_contact_email("core/emails/send_contact_email.html", context)
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "failed"})
        else:
            return JsonResponse({"status": "failed"})
