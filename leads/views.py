from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Lead,Agent,Category
from .forms import LeadForm, LeadModelForm,CustomUserCreationForm,AssignAgentForm
from django.views import generic
from agents.mixins import OrganizerAndLoginRequiredMixin


#CRUD+L - Create, Retrieve, Update and Delete + List


class SignupView(generic.CreateView):
    template_name='registration/signup.html'
    form_class=CustomUserCreationForm

    
    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name='landing.html'

def landing_page(request):
    return render(request, 'landing.html')

class HomePageView(LoginRequiredMixin,generic.ListView):
    template_name='leads/home.html'
    
    context_object_name = "leads"


    def get_queryset(self):
        user = self.request.user

        # initial queryset of the leads for the entire organisation
        if user.is_organizer:
            queryset=Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            queryset=Lead.objects.filter(organisation=user.agent.organisation, agent__isnull=False)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        
        return queryset

    def get_context_data(self,**kwargs):
        
        context = super(HomePageView,self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset=Lead.objects.filter(organisation=user.userprofile, agent__isnull=True)

            context.update({
                "unassigned_leads":queryset
            })

        return context


def home_page(request):
    leads = Lead.objects.all()
    context={
        'leads':leads,

    }

    return render(request, 'leads/home.html', context)

class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name='leads/detail.html'
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user

        # initial queryset of the leads for the entire organisation
        if user.is_organizor:
            queryset=Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset=Lead.objects.filter(organisation=user.agent.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        
        return queryset


def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead':lead,
    }
    return render(request, 'leads/detail.html', context)

class LeadCreateView(OrganizerAndLoginRequiredMixin,generic.CreateView):
    template_name='leads/create.html'
    form_class=LeadModelForm

    
    def get_success_url(self):
        return reverse("leads:home")

    def form_valid(self,form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to check it out",
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )

        return super(LeadCreateView,self).form_valid(form)
    


def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect("/")

    context = {
        'form':form
        
    }
    return render(request, 'leads/create.html', context)

class LeadUpdateView(OrganizerAndLoginRequiredMixin,generic.UpdateView):
    template_name='leads/update.html'
    form_class=LeadModelForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of the leads for the entire organisation
        return Lead.objects.filter(organisation=user.userprofile)
        

    

    def get_success_url(self):
        return reverse("leads:home")

def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()           
            return redirect("/")

    context = {
    'form':form

    }

    return render(request, 'leads/update.html', context)


class LeadDeleteView(OrganizerAndLoginRequiredMixin,generic.DeleteView):
    template_name='leads/delete.html'
    
    def get_queryset(self):
        user = self.request.user
        # initial queryset of the leads for the entire organisation
        return Lead.objects.filter(organisation=user.userprofile)
        
    

    def get_success_url(self):
        return reverse("leads:home")


def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/')



class AssignAgentView(OrganizerAndLoginRequiredMixin,generic.FormView):
    template_name='leads/assign_agent.html'
    form_class=AssignAgentForm

    def get_form_kwargs(self,**kwargs):
        kwargs = super(AssignAgentView,self).get_form_kwargs(**kwargs)
        kwargs.update({"request":self.request})

        return kwargs


    def get_success_url(self):
        return reverse("leads:home")

    def form_valid(self,form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView,self).form_valid(form)


class CategoryListView(LoginRequiredMixin,generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"


    def get_context_data(self,**kwargs):
        context = super(CategoryListView,self).get_context_data(**kwargs)

        user = self.request.user

        # initial queryset of the leads for the entire organisation
        if user.is_organizer:
            queryset=Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset=Lead.objects.filter(organisation=user.agent.organisation)
        
        context.update({
            "unassigned_lead_count":queryset.filter(category__isnull=True).count()
        })

        return context


    def get_queryset(self):
        user = self.request.user

        # initial queryset of the leads for the entire organisation
        if user.is_organizer:
            queryset=Category.objects.filter(organisation=user.userprofile)
        else:
            queryset=Category.objects.filter(organisation=user.agent.organisation)
        
        return queryset

    


# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent)
#             return redirect("/")

#     context = {
#         'form':form
        
#     }
#     return render(request, 'leads/create.html', context)

# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             age=form.cleaned_data['age']
#             agent = Agent.objects.first()
            
#             lead.first_name=first_name,
#             lead.last_name=last_name,
#             lead.age=age,
#             lead.agent=agent
#             lead.save()
#             return redirect("/")

#     context = {
#     'form':form

#     }

#     return render(request, 'leads/update.html', context)
