from django.shortcuts import render

#retrieve_view
#getting the template home.html
def home(request):
    return render(request, "home.html", {})
