from django.shortcuts import render,HttpResponse
import pandas as pd

def welcome(request):
    return render(request,'welcome.html')

def home(request):
    return render(request,'home.html')

def form(request):
    if request.method=='POST':
        data = request.POST.dict()
        phase=data.get('phase')
        if phase=="first":
            a=pd.read_csv('mcet/static/mcet/eamcetfirst.csv')
        else:
            a=pd.read_csv('mcet/static/mcet/Emacet.csv')
        rank=data.get('rank')
        rank=int(rank)+2000
        gender=data.get('gender')
        caste=data.get('category')
        district=request.POST.getlist('district')
        if district:
            a=a.loc[a.DISTRICT.isin(district)]
        branch=request.POST.getlist('branch')
        if branch:
            a=a.loc[a.BRANCH.isin(branch)]
        coed=data.get('coed')
        if coed:
            b=coed==a['COED']
            a=a[b]
        category=caste+' '+gender
        selected_columns = ['INST CODE','INSTITUTE NAME','PLACE','COED','TYPE','DISTRICT','YEAR OF ESTB','BRANCH','BRANCH NAME',category,'TUITION FEE','AFFILIATED']
        a=a[selected_columns]
        b=a[category]<=rank
        a=a[b].sort_values(category, ascending=True)
        headers = a.columns.tolist()
        a=a.to_html(index=False)
        context = {'data': a,'head': headers}
        return render(request,'data_display.html',context)
