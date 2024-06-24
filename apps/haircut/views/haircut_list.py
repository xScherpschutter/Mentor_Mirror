from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from apps.core.mixins import UserGroupMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from apps.core.mixins import NoPermissionMixin, UserGroupMixin, DeleteMixin
from apps.haircut.models import UserHaircuts

class HaircutList(LoginRequiredMixin, ListView):
    model = UserHaircuts
    template_name = 'haircut_list.html'
    context_object_name = 'haircuts'
    paginate_by = 5
    queryset = None
    def get_queryset(self):
        query = self.request.GET.get('query')
        
        queryset = self.model.objects.filter(user=self.request.user)

        if query:
            
            queryset = queryset.filter(Q(haircut__Corte__icontains = query) | Q(date__icontains = query))
            return queryset
        
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de peinados'
        return context