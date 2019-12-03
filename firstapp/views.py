from django.shortcuts import render
# from django.http.response import HttpResponse
# Create your views here. method views is old style letest style is class base view
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Notice,Profile


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):
    return render(request, "index.html", {"homename": "firstpage"})


def about(request):
    return render(request, "about.html", {"aboutname": "aboutpage"})


def contact(request):
    return render(request, "contact.html", {"contactname": "contactpage"})


class NoticeListView(ListView):
    model = Notice

    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""

        if self.request.user.is_superuser:
            return Notice.objects.order_by("-id")
        else:
            return Notice.objects.filter(Q(branch=self.request.user.profile.branch) | Q(branch__isnull=True)).filter(subject__icontains=si).order_by("-id")


@method_decorator(login_required, name="dispatch")
class NoticeDetailView(DetailView):

    model = Notice


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["branch"]