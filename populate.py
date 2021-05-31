import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','petroleumReport.settings')
import requests
import django
django.setup()
import json
from report.models import Report

r= requests.get('https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json').json()



def populate(N=len(r)):


        for i in range(len(r)):

            f_year=r[i]['year']

            f_petroleum_products=r[i]['petroleum_product']

            f_sales=r[i]['sale']

            f_country=r[i]['country']

            report = Report.objects.get_or_create(year=f_year,
                                              petroleum_product=f_petroleum_products,
                                              sale=f_sales,
                                              country=f_country)


if __name__ == '__main__':
    print("populating")
    populate(256)
    print("done ")
