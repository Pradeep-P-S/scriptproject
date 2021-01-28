from django.shortcuts import render
def cylinder(request):
    context= {}
    return render(request,'mathapp/cylinder.html',context)

def triangle(request):
    context= {}
    return render(request,'mathapp/triangle.html',context)
# Create your views here.
