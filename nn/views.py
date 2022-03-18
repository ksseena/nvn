
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import myuploadfile
# Create your views here.
def home(request):
    s="hello"
    # name = request.GET['name']
    if request.GET:
        name = request.GET['name']
        print(name)
    data ={
        "s":s,  
    }
    return render(request,'index.html',data)


def simple_upload(request):
    if request.method == 'POST':
        myfile=request.FILES.getlist('uploadfoles')
        for f in myfile:
            myuploadfile(myfiles=f).save()
        print(myfile)

    """ l=[]
        for i in request.FILES.getlist('myfile'):
            fname=i.name
            l.append(fname)
        print(l)
       
        fs=FileSystemStorage()
        
        filename=fs.save(l1.name,)
       # upload_file_url = fs.url(filename)"""
    return HttpResponse("ok")





def logout(request):
    return render(request,"logout.html")


from .Add import add as r
def f1(request):
    a=10
    b=2
    re = r(a,b)
    data={
        're':re
    }
    print(re)
    return render(request,"index.html",data)


def home1(request):
    return render(request,"home.html")




















        















"""
import glob

import pandas as pd

# get data file names

local_path = r'/my_files'

filenames = glob.glob(local_path + "/*.csv")

dfs = [pd.read_csv(filename)) for filename in filenames]


# if needed concatenate all data into one DataFrame

big_frame = pd.concat(dfs, ignore_index=True)




                
                
                """
