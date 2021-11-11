import os

from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.conf import settings

from .models import Scheme
from .forms import SchemeForm
from .services import make_csv

@login_required
def generate_csv(request, *args, **kwargs):
    """
    calls a celery task and redirects to the same page
    """
    if request.POST:
        scheme_id = int(request.POST.get("scheme"))
        scheme = Scheme.objects.get(pk=scheme_id)
        make_csv(scheme_id=scheme_id)
        return redirect('dataset-list')
    else:
        raise Http404()


@method_decorator(login_required, name='dispatch')
class SchemeListView(ListView):
    model = Scheme


@method_decorator(login_required, name='dispatch')
class DatasetListView(ListView):
    template_name = 'generator/dataset_list.html'
    model = Scheme


@method_decorator(login_required, name='dispatch')
class SchemeCreateView(CreateView):
	model = Scheme
	form_class = SchemeForm
	template_name = 'generator/scheme_create.html'
	success_url = '/scheme_list/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class SchemeUpdateView(UpdateView):
	model = Scheme
	form_class = SchemeForm
	template_name = 'generator/scheme_create.html'
	success_url = '/scheme_list/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class SchemeDeleteView(DeleteView):
	model = Scheme
	template_name = 'generator/scheme_confirm_delete.html'
	success_url = '/scheme_list/'

