from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404
from django.urls import reverse_lazy
from django.db.models import Q
from apps.core.models import Costumer
from django.contrib import messages
from apps.core.forms import CostumerForm
from django.shortcuts import render
from apps.core.mixins import UserGroupMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from apps.core.mixins import NoPermissionMixin, UserGroupMixin, UpdateMixin, DeleteMixin


class CostumerList(UserGroupMixin, NoPermissionMixin, LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Costumer
    permission_required = 'core.view_costumer'
    template_name = 'index/costumer.html'
    context_object_name = 'costumers'
    paginate_by = 5
    queryset = None
    def get_queryset(self):
        query = self.request.GET.get('query')

        if query:
            queryset = self.model.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query) | Q(id_number__icontains = query))
            return queryset
        
        else:
            return self.model.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Clientes'
        return context
       
class CostumerCreate(UserGroupMixin, NoPermissionMixin, LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Costumer
    permission_required = 'core.add_costumer'
    form_class = CostumerForm
    template_name = "index/new_costumer.html"
    success_url = reverse_lazy('core:costumer')
        
    def form_valid(self, form):
        id = form.cleaned_data['id_number']
        existing_costumer = Costumer.objects.filter(id_number = id).exists()
        
        if existing_costumer:
            messages.error(self.request, 'Ya existe un cliente con este número de identificación.')
            return self.form_invalid(form)
        
        else:
            return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo cliente'
        return context

class CostumerUpdate(UserGroupMixin, NoPermissionMixin, LoginRequiredMixin, PermissionRequiredMixin, UpdateMixin, UpdateView):
    model = Costumer
    permission_required = 'core.change_costumer'
    form_class = CostumerForm
    template_name = "index/new_costumer.html"
    success_url = reverse_lazy('core:costumer')
    
    def form_valid(self, form):
        id = form.cleaned_data['id_number']
        existing_costumer = self.model.objects.filter(id_number=id).exclude(pk=self.object.pk).exists()
        
        if existing_costumer:
            messages.error(self.request, 'Ya existe un cliente con este número de identificación.')
            return self.form_invalid(form)
        
        else:
            return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar cliente'
        return context

class CostumerDelete(UserGroupMixin, NoPermissionMixin, LoginRequiredMixin, PermissionRequiredMixin, DeleteMixin, DeleteView):
    model = Costumer
    template_name = 'index/delete_costumer.html'
    permission_required = 'core.delete_costumer'
    context_object_name = 'costumer'
    success_url = reverse_lazy('core:costumer')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar cliente'
        return context
    