from django.shortcuts import render,redirect
from .forms import CategoryForm, BookForm, NewsForm, UserForm, CommentForm, LoginForm
from .models import Book, Category, News
from django.contrib.auth import authenticate,login





def home(request):
    r = News.objects.all()
    return render(request, 'home.html', {'form': r})
    

def create_book(request):
    form = BookForm()


    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})

def create_tur(request):
    form = CategoryForm()

    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})

def create_news(request):
    form = NewsForm()

    if request.POST:
        form = NewsForm(request.POST, files=request.FILES)
        if form.is_valid():
            News.objects.create(
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                bolim = form.cleaned_data['bolim'],
                rasm = form.cleaned_data['rasm'],
                author = request.user
            )
            return redirect('home')
    return render(request, 'create.html', {'form': form})

def create_user(request):
    form = UserForm()

    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save() 
            parol = form.cleaned_data['password']
            user.set_password(parol)
            user.save()
            return redirect('home')
    return render(request, 'create.html', {'form': form})
    

# def create_comment(request):
#     form = CommentForm()
    
#     if request.POST:
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             news =  form.save()
#             news.author =request.user
#             news.save()
#             return redirect('home')
#     return render(request, 'comment.html', {'form': form})



def detail(request, id):
    form = CommentForm()
    one = News.objects.get(id=id)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.author = request.user
            com.news = one
            com.save()
            return redirect('detail', one.id)
    context = {
        'one': one,
        'com': form
    }
    return render(request, 'detail.html', context)

def Login(request):
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            a = request.POST['username']
            b = request.POST['password']
            f = authenticate(request, username=a, password=b)
            print(f)
            if f is not None:
                login(request, f)
                return redirect('home')
    return render(request, "login.html", {'form': form})













# Create your views here.
