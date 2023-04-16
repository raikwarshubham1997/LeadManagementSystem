from django.shortcuts import render
from SuperAdmin.models import *
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, "emp/dashboard.html")


def get_all_lead(request):
    # cobjs = LeadCreate.objects.all().order_by("id").reverse()
    ServiceData = LeadCreate.objects.all()
    paginator = Paginator(ServiceData, 6)
    page_number = request.GET.get('page')
    all_lead = paginator.get_page(page_number)
    totalpage = all_lead.paginator.num_pages
    # for i in all_lead:
    #     print(i)
    data = {
        'all_lead':all_lead,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range(totalpage)]
    }
    return render(request, "emp/list_of_leads.html",data)

