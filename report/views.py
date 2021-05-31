import json
from django.shortcuts import render
from report.models import Report

import requests
# Create your views here.

def index(request):

    return render(request,"report/index.html")

def newdata(request):

    data=Report.objects.order_by('-year')
    list_dic={
        "list_data":data
    }
    return render(request,"report/newdata.html",context=list_dic)

def overallsales(request):
    p= Report.objects.raw('select avg([sale]) as sale, petroleum_product, country from report_Report where sale!=0 group by [country],[petroleum_product]')
    sale_dict={"list_sale":p}
    return render(request,"report/overallsales.html",context=sale_dict)

def avgsale(request):
    p=Report.objects.raw('select petroleum_product, avg([sale]) as sale, (year/2)*2 || "-" || (year/2)+1 as year from report_Report where sale!=0 group by year/2, petroleum_product')
    avgsal_dict={"list_avgsale":p}
    return render(request,"report/avgsaleininterval.html",context=avgsal_dict)

def leastsale(request):
    p=Report.objects.raw('select petroleum_product, year, min([sale]) as sale from report_Report where sale!=0 group by year, petroleum_product')
    least_dict={"list_leastsale":p}
    return  render(request,"report/leastsale.html",context=least_dict)
