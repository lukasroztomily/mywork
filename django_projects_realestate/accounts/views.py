from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
# Create your views here.

def register (request):
    if request.method == 'POST':
       # messages.error(request, 'Err mes')
       # return redirect('register')
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']
       if  password == password2:
           if User.objects.filter(username =username ).exists():
               messages.error(request, 'Err mes')
               return redirect('register')
           else:
                if User.objects.filter(username =username ).exists():
                   messages.error(request, 'Err mes')
                   return redirect('register')
                else:
                    user = User.objects.create_user(username = username, password = password, email = email, 
                                                    first_name = first_name, last_name = last_name)     
                    user.save();
                    # auth.login(request, user)
                    messages.success(request, 'Yes')
                    return redirect('index') 
       else:
           messages.error(request, 'Err mes')
           return redirect('register')                  
    else:    
        return render(request, 'accounts/register.html')


def login_view (request):
    if request.method == "POST":
        
     
        user = authenticate(username = request.POST["username"], password = request.POST["password"])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                print(request.GET)
                return redirect(request.POST['next'])
            #messages.success(request, 'Your profile was updated.')
                 
            return redirect('index')
        else:
            #messages.add_message(request, messages.INFO, 'Over 9000!')
            #print(messages.INFO)
            #messages.error(request, 'Bad password.')
            return render(request, 'accounts/login.html')
            #return render(request, 'accounts/login.html', {'error':'Bad password'})
    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='/accounts/login')
def dashboard (request):
    
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    
    context  = {
        'contacts': user_contacts
    }
    
    return render(request, 'accounts/dashboard.html', context)


def logout_view (request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Yes')
        return redirect('index')

