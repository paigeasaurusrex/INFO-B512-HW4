from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'personalweb/index2.html')
	
	
def s1(request):

	return render(request, 'personalweb/index.html')