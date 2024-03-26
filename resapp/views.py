from django.shortcuts import render, redirect

from .models import ModelCv,CreateContact,Portfolio,Education,Experience,Skills

# Create your views here.

def index(request):
    cvform=ModelCv.objects.all()
    cvform1=CreateContact.objects.all()
    cvform2=Portfolio.objects.all()
    cvform3=Education.objects.all()
    cvform4=Experience.objects.all()
    cvform5=Skills.objects.all()


    return render(request,'base.html',{'form': cvform, 'form1': cvform1, 'form2': cvform2,
                                       'form3':cvform3,'form4':cvform4, 'form5':cvform5})


