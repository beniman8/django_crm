import random
from django.shortcuts import render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail



class AgentListView(OrganizerAndLoginRequiredMixin,generic.ListView):
    template_name="agents/list.html"
    

    def get_queryset(self):
        organisation = self.request.user.userprofile

        return Agent.objects.filter(organisation=organisation)

class AgentCreateView(OrganizerAndLoginRequiredMixin,generic.CreateView):
    template_name="agents/create.html"
    form_class=AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")


    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizor = False
        user.set_password(f"{random.randint(0,1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
            )
        # agent.organisation = self.request.user.userprofile
        # agent.save()

        send_mail(
        
            subject="You are invited to be an agent",
            message="Go to the site to check it out",
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        

        )
        return super(AgentCreateView,self).form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin,generic.DetailView):

    template_name="agents/detail.html"
    context_object_name="agent"
    

    def get_queryset(self):
        organisation = self.request.user.userprofile

        return Agent.objects.filter(organisation=organisation)

class AgentUpdateView(OrganizerAndLoginRequiredMixin,generic.UpdateView):
    template_name='agents/update.html'
    
    form_class=AgentModelForm
    def get_queryset(self):
        return Agent.objects.all()
    

    def get_success_url(self):
        return reverse("agents:agent-list")

class AgentDeleteView(OrganizerAndLoginRequiredMixin,generic.DeleteView):
    template_name='agents/delete.html'
    def get_queryset(self):
        organisation = self.request.user.userprofile

        return Agent.objects.filter(organisation=organisation)
    

    def get_success_url(self):
        return reverse("agents:agent-list")

    
