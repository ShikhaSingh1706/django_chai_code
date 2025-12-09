from django.shortcuts import render
from .models import chaiVariety
from django.shortcuts import  get_object_or_404

# Create your views here.
def all_chai(request):
    chai_show=chaiVariety.objects.all()
    return render(request, 'chaiapp/all_chai.html',{'chais':chai_show})

def chai_detail(request, chai_id):
    chai=get_object_or_404(chaiVariety,pk=chai_id)
    return render(request,'chaiapp/chai_detail.html',{'chai':chai})
