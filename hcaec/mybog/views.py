from django.shortcuts import redirect, render
from .forms import ClientForm,ApplyForm
from . models import Post,University
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    post = Post.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        if request.method == 'POST':
           form = ClientForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('mybog:index')
    
    else:
        form = ClientForm()
    return render(request, 'mybog/index.html',{'form':form, 'post':post})

def about(request):
    return render(request, 'mybog/about.html')

def blog(request):
    post = Post.objects.all().order_by('-id')
    return render(request, 'mybog/blog.html',{'post':post})

def service(request):
    return render(request, 'mybog/service.html')

def contact(request):
    if request.method == 'POST':
        if request.method == 'POST':
           form = ClientForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('mybog:contact')
    
    else:
        form = ClientForm()
    return render(request, 'mybog/contact.html',{'form':form})

def university(request):
    p = Paginator(University.objects.all().order_by('-id'),6)
    page = request.GET.get('page')
    university = p.get_page(page)
    return render(request, 'mybog/university.html',{'university':university})

def apply(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)

        if form.is_valid():
           form.save()
           return redirect('mybog:apply')
    
    else:
        form = ApplyForm()
    return render(request, 'mybog/apply.html',{'form':form})

def blogdetail(request,post_id,):
    post = Post.objects.get(pk=post_id)
    posts = Post.objects.all().order_by('-id')[:5]
    context ={'post':post, 'posts':posts}
    return render(request, 'mybog/blogdetail.html',context)


    

