from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm



class AgentsListView(LoginRequiredMixin,generic.ListView):
    template_name="agents/list.html"
    

    def get_queryset(self):
        return Agent.objects.all()

class AgentsCreateView(LoginRequiredMixin,generic.CreateView):
    template_name="agents/create.html"
    form_class=AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")


    def form_valid(self,form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentsCreateView,self).form_valid(form)


