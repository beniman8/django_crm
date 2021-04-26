from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm, LeadModelForm
from django.views import generic

class LandingPageView(generic.TemplateView):
    template_name='landing.html'

def landing_page(request):
    return render(request, 'landing.html')

class HomePageView(generic.ListView):
    template_name='leads/home.html'
    queryset=Lead.objects.all()
    context_object_name = "leads"

def home_page(request):
    leads = Lead.objects.all()
    context={
        'leads':leads,

    }

    return render(request, 'leads/home.html', context)

class LeadDetailView(generic.DetailView):
    template_name='leads/detail.html'
    queryset=Lead.objects.all()
    context_object_name = "lead"

def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead':lead,
    }
    return render(request, 'leads/detail.html', context)

class LeadCreateView(generic.CreateView):
    template_name='leads/create.html'
    form_class=LeadModelForm
    

    def get_success_url(self):
        return reverse("leads:home")

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

class LeadUpdateView(generic.UpdateView):
    template_name='leads/update.html'
    queryset=Lead.objects.all()
    form_class=LeadModelForm
    

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


class LeadDeleteView(generic.DeleteView):
    template_name='leads/delete.html'
    queryset=Lead.objects.all()
    

    def get_success_url(self):
        return reverse("leads:home")


def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('/')



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
