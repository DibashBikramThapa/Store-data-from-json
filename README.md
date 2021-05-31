**start project and accessing admin panel**

## Start the project

To start the project:

1. Here before start the project use python populate.py
2. Then start the project using python manage.py runserver
3. Follow the link
4. Click the links to view the problems solved. 


---

## Run the project

Next, to access the admin:

1. Simply add "/admin" to the hosted url by python manage.py runserver
2. Admin credentials are:
    i. username: myintern
    ii. pw: myintern
3. View the records where sales is made primary key and country is self returned on calling the report class with attributes: year, petroleum_product, sale and country.

#ABout the queries used to display the conditions:

1.  data=Report.objects.order_by('-year') for all stored data.

2.  Report.objects.raw('select avg([sale]) as sale, petroleum_product, country from report_Report where sale!=0 group by [country],[petroleum_product]')
    FOR OverallAverageSale Grouped by Country

3.  Report.objects.raw('select petroleum_product, avg([sale]) as sale, (year/2)*2 || "-" || (year/2)+1 as year from report_Report where sale!=0 group by year/2, petroleum_product')
    Fpr AverageSale for Each Petroleum Product in interval however in front end i couldnot show the 2007-2008 like this way.

4.  Report.objects.raw('select petroleum_product, year, min([sale]) as sale from report_Report where sale!=0 group by year, petroleum_product')
    For Least sale for Each Petroleum Product




