from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from apps.core.mixins import UserGroupMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from apps.core.mixins import NoPermissionMixin, UserGroupMixin, DeleteMixin
from apps.optical.models import UserGlasses


class OpticalList(LoginRequiredMixin, ListView):
    model = UserGlasses
    template_name = 'optical_list.html'
    context_object_name = 'glasses'
    paginate_by = 5
    queryset = None
    def get_queryset(self):
        query = self.request.GET.get('query')
        
        queryset = self.model.objects.filter(user=self.request.user)

        if query:
            
            queryset = queryset.filter(Q(glass__Lente__icontains = query) | Q(date__icontains = query))
            return queryset
        
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de lentes'
        return context
    
class OpticalDelete(LoginRequiredMixin, DeleteMixin, DeleteView):
    model = UserGlasses
    #template_name = 'index/delete_costumer.html'
    #context_object_name = 'glassr'
    #success_url = reverse_lazy('core:costumer')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar lente'
        return context