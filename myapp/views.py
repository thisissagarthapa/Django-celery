from django.shortcuts import render
from myCelery.celery import add
from myapp.task import sub
from celery.result import AsyncResult
# Create your views here.

# Enque task usng delay
def index(request):
    print('results:')
    result=add.delay(10,20)
    # result2=sub.delay(10,20)
    # print("result2:",result2)
    return render(request,"index.html",{'result':result})
    
""" def index(request):
    print('results:')
    result=add.apply_async(args=[10,20])
    result2=sub.apply_async(args=[50,20])
    print("result:",result)
    print("result2:",result2)
    return render(request,"index.html",{'result':result}) """

def check_result(request,task_id):
    # Retrive the task result with task_id
    result=AsyncResult(task_id)
    print("result:",result)
    print('Ready:',result.ready()),
    print('Successful:',result.successful())
    print('Failed:',result.failed())
    return render(request,'result.html',{'result':result})




def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")