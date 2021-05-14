from django.shortcuts import render

# Create your views here.





def index(request):
    'This view displays the index page the where all the blog post is located'

    return render(request,'index.html')


def blogDetail(request,pk=None):
    'this view renders the blog-detail markup'
    context = {'pk':pk}


    return render(request,'single.html',context)




