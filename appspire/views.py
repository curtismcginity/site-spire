from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
        return render(request,'contact.html')

def research(request):
        return render(request,'research.html')

def consulting(request):
        return render(request,'consulting.html')

def initiatives(request):
        return render(request,'initiatives.html')

def testgallery(request):
        return render(request,'gallery1col.html')

def post(request):
        return render(request,'post.html')