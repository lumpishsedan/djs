@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

this project is about filters, the idea is to use forms to filter results from 
database. 

the video tutorial link is - https://www.youtube.com/watch?v=nle3u6Ww6Xk

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

before we proceed to work with the video and use forms for queries, 

we will try to see using basic concepts if we are able to query the database
and list out results where keyone value = 2 without using the video tutorial

the help required will be taken from the data driven website skillshare django tutorial
video named - 14-Dynamic Data in a Template

Another help source will be the youtube video - https://youtu.be/WimXjp0ryOo
this video uses filters in shell to for queries.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Completed - query listview

what does that mean ?
this means that its not necessary to use forms to perform select 
query on the database you can do it with views.py.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

So now its a good idea to reevaluate our position vis-a-vis why we started working on 
queries in the first place.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

The next part of the project is this
we are able to render a selected list from the database.
our aim is to modify the template select.html so that it will be 
rendered dynamically using a logic.
the logic is this. 
lets say there are two values of keyone available in database.
then the select.html should be rendered containing two hyperlinks 
keyone value = 1 link and keyone value = 2 link
when you click 1st link you should be routed to home.html and list be rendered with keyone value = 1
when you click 2nd link you should be routed to home.html and list be rendered with keyone value = 2

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

this part of the project has been completed with help of stackoverflow
https://stackoverflow.com/questions/59017021/how-to-render-links-in-a-template-for-database-filtering-in-django

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

