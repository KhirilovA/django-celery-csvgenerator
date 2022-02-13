import os

from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings

from .models import Scheme, SchemeColumn
from .forms import SchemeForm, SchemeColumnForm
from .services import make_csv

@login_required
def generate_csv(request, *args, **kwargs):
    """
    calls a celery task and redirects to the same page
    """
    if request.POST:
        scheme_id = int(request.POST.get("scheme"))
        scheme = Scheme.objects.get(id=scheme_id)
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


@method_decorator(login_required, name='dispatch')
class SchemeColumnCreateView(CreateView):
	model = SchemeColumn
	form_class = SchemeColumnForm
	template_name = 'generator/scheme_column_create.html'

	def form_valid(self, form):
		try:
			scheme_id = int(self.request.GET.get('scheme_id'))
			form.instance.scheme = Scheme.objects.get(id=scheme_id)
			return super().form_valid(form)
		except Exception:
			messages.error(self.request, f"Orders should be unique :(")
			return super().form_invalid(form)

	def get_success_url(self):
		return ''.join(('/scheme/', self.request.GET.get('scheme_id'), '/'))


@method_decorator(login_required, name='dispatch')
class SchemeColumnListView(ListView):
	template_name = 'generator/scheme_column_list.html'

	def get_queryset(self) :
		queryset = SchemeColumn.objects.filter(scheme=self.kwargs['scheme__id']).order_by('order')
		return queryset


@method_decorator(login_required, name='dispatch')
class SchemeColumnUpdateView(UpdateView):
	model = SchemeColumn
	form_class = SchemeColumnForm
	template_name = 'generator/scheme_column_create.html'

	def form_valid(self, form):
		scheme_id = int(self.request.GET.get('scheme_id'))
		form.instance.scheme = Scheme.objects.get(id=scheme_id)
		return super().form_valid(form)

	def get_success_url(self):
		return ''.join(('/scheme/', self.request.GET.get('scheme_id'), '/'))


@method_decorator(login_required, name='dispatch')
class SchemeColumnDeleteView(DeleteView):
	model = SchemeColumn
	template_name = 'generator/scheme_column_confirm_delete.html'

	def get_success_url(self):
		return ''.join(('/scheme/column/list/', str(self.kwargs['pk'])))
