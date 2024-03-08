from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    return render(request, 'register.html') 
   
# def dashboard(request):
#     return render(request, 'dashboard.html')

def login(request):
    if request.method == "POST":
        name = request.POST.get("your_name")
        password = request.POST.get("your_pass")
        print(name)
        print(password)
        
        # Authenticate user
        user = authenticate(request, username=name, password=password)
        print(user,"*********************************")

        if user is not None:
            print("1234")
            # User is authenticated, log them in
            auth_login(request, user)
            print("5678")
            return redirect('dashboard')
        else:
            # Authentication failed, render login page with error message
            return render(request, 'login.html', {'error_message': 'Invalid email or password.'})

    return render(request, 'login.html')
        

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        print(name,"######################################")
        print(password)

        try:
            user = User.objects.create_user(username = email.split('@')[0],
                                       email = email,
                                       first_name = name)
            # Set password using set_password() method
            user.set_password(password)
            user.save()
            return redirect('login')
            
        except:          
            return render(request, 'register.html', {'error_message': 'Registration failed. Please try again.'})
            
    return render(request, 'register.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('dashboard')
   
