from django.shortcuts import render
from .models import chaiVariety, store
from django.shortcuts import  get_object_or_404
from .forms import chaiVarietyForm

# Create your views here.
def all_chai(request):
    chai_show=chaiVariety.objects.all()
    return render(request, 'chaiapp/all_chai.html',{'chais':chai_show})

def chai_detail(request, chai_id):
    chai=get_object_or_404(chaiVariety,pk=chai_id)
    return render(request,'chaiapp/chai_detail.html',{'chai':chai})


def chai_store_view(request):
    stores=None
    if request.method=='POST':
        form=chaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety=form.cleaned_data['chai_variety']
            stores=store.objects.filter(chai_varieties=chai_variety)
    else:
        form=chaiVarietyForm()   
    return render(request,'chaiapp/chai_stores.html',{'stores':stores,'form':form})
