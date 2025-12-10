from django.shortcuts import render, get_object_or_404
from .models import chaiVariety, store
from .forms import chaiVarietyForm
from django.views import View


# Create your views here.
class all_chai(View):
    def get(self,request):
            chai_show=chaiVariety.objects.all()
            return render(request, 'chaiapp/all_chai.html',{'chais':chai_show})

class chai_detail(View):
    def get(self,request,chai_id):
        chai=get_object_or_404(chaiVariety,pk=chai_id)
        return render(request,'chaiapp/chai_detail.html',{'chai':chai})


class chai_store_view(View):
    def get(self,request):
        stores=store.objects.all()
        form=chaiVarietyForm()
        return render(
            request, 'chaiapp/chai_stores.html',
            {'form':form,'stores':stores}
        )
    def post(self,request):
        form=chaiVarietyForm(request.POST)
        stores=store.objects.all()

        if form.is_valid():
            chai_variety=form.cleaned_data['chai_variety']
            stores=store.objects.filter(chai_varieties=chai_variety)

        return render(
            request,'chaiapp/chai_stores.html',{'form':form,"stores":stores}
        )    
    