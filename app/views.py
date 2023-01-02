from django.shortcuts import render


def Ravi(request):
    d={'a':10 , 'b':20}
    return render(request,'Ravi.html',d)
