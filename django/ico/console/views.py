from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from accounts.models import Account, UserProfile
from blog.models import Blog
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import EmailMessage
from accounts.forms import UserForm, UserProfileForm, AddUserForm
from blog.forms import  AddBlogForm, EditBlogForm


# Create your views here.
def list_blocked_user(request):
     accounts = Account.objects.filter(is_blocked = True)
     context = {
        'accounts': accounts
      }
     return render(request, 'console/list_blocked_user.html', context)


def unblocked_user(request, user_id):
    accounts = get_object_or_404(Account, id=user_id)
    accounts.is_blocked = False
    accounts.save()
    return redirect('list_blocked_user')


def blocked_user(request, user_id):
    accounts = get_object_or_404(Account, id=user_id)
    accounts.is_blocked = True
    accounts.save()
    return redirect('user_admin')

def waiting_approve_user(request):
     accounts = Account.objects.filter(is_email_verify=True, is_active=False, is_admin=False, is_staff=False, is_superadmin = False)
     context = {
        'accounts': accounts
      }
     return render(request, 'console/waiting_approve_user.html', context)

def approve_user(request, user_id):
    accounts = get_object_or_404(Account, id=user_id)
    accounts.is_active = True
    accounts.save()
    return redirect('waiting_approve_user')


def remove_user(request, user_id):
    accounts = get_object_or_404(Account, id=user_id)
    accounts.delete()
    return redirect('user_admin')


def unpublished_blog(request, blog_id):
    blogs = get_object_or_404(Blog, id=blog_id)
    blogs.is_published = False
    blogs.save()
    return redirect('blog_admin')


def published_blog(request, blog_id):
    blogs = get_object_or_404(Blog, id=blog_id)
    blogs.is_published = True
    blogs.save()
    return redirect('blog_list_published')



def login_admin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password, is_staff = False)

        if user is not None:
            
            if user.is_staff:
                auth.login(request, user)   
                messages.success(request, 'Jsi zalogovany')
                url = request.META.get('HTTP_REFERER')
                try:
                    query = requests.utils.urlparse(url).query
                    # next=/cart/checkout/
                    params = dict(x.split('=') for x in query.split('&'))
                    if 'next' in params:
                        nextPage = params['next']
                        return redirect(nextPage)                
                except:
                    return redirect('home_admin')
            else:        
                    messages.error(request, 'Nejsi admin')
        else:
            print(password)
            messages.error(request, 'Nejsi zalogovany')
            return redirect('login_admin')
    
    return render(request, 'console/login.html')

def home_admin(request):
    return render(request, 'console/home.html')

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = BaseUserManager().make_random_password()
            print(password)
            username = email.split('@')
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.phone_number = phone_number
            user.save()

            profile = UserProfile()
            profile.user_id = user.id
            profile.profile_picture = 'userprofile/default.png'
            profile.save()

            mail_subject = 'Activuj ucet'
            message =  'Tvoje heslo je ' + password         
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Vyslo to!')
            return redirect('add_user')
    else:
        form = AddUserForm()

    context = {'form': form}
    return render(request, 'console/add_user.html', context)
    

def user_admin(request):
    accounts = Account.objects.all().filter(is_active = True, is_blocked = False)
    context = {
        'accounts': accounts
    }
    return render(request, 'console/user_admin.html', context)

def blog_list_published(request):
    blogs = Blog.objects.filter(is_published=False)
    context = {
        'blogs': blogs
    }
    return render(request, 'console/blog_list_published.html', context)

def blog_admin(request):
    blogs = Blog.objects.filter(is_published=True)
    context = {
        'blogs': blogs
    }
    return render(request, 'console/blog_admin.html', context)

@login_required(login_url='login_admin')
def logout_admin(request):
    auth.logout(request)
    messages.success(request, 'Jsi odhlasen')
    return redirect('login')


def edit_user(request, user_id):
    accounts = get_object_or_404(Account, id=user_id)
    userprofile = get_object_or_404(UserProfile, user = accounts)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = accounts)
        profile_form = UserProfileForm(request.POST, request.FILES, instance = userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Yes')
            return redirect('edit_user', user_id)
    else:
            user_form = UserForm(instance = accounts)
            profile_form = UserProfileForm(instance = userprofile)
    context = {
        'user_id': user_id,
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile
    }

    return render(request, 'console/edit_user.html', context)


def edit_blog(request, blog_id):
    blogs = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog_form = EditBlogForm(request.POST, instance = blogs)
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Yes')
            return redirect('edit_blog', blog_id)
    else:
            blog_form = EditBlogForm(instance = blogs)
    context = {
        'blog_id': blog_id,
        'blog_form': blog_form
    }

    return render(request, 'console/edit_blog.html', context)


def remove_blog(request,blog_id):
    blogs = get_object_or_404(Blog, id=blog_id)
    blogs.delete()
    return redirect('blog_admin')


def add_blog(request):
    if request.method == 'POST':
        form = AddBlogForm(request.POST)
        if form.is_valid():
            title_sk = form.cleaned_data['title_sk']
            text_sk = form.cleaned_data['text_sk']
            headline_sk = form.cleaned_data['headline_sk']
            title_en = form.cleaned_data['title_en']
            text_en = form.cleaned_data['text_en']
            headline_en = form.cleaned_data['headline_en']
            title_de = form.cleaned_data['title_de']
            text_de = form.cleaned_data['text_de']
            headline_de = form.cleaned_data['headline_de']
            is_published = form.cleaned_data['is_published']
            blog = Blog(
                        title_sk = title_sk, 
                        text_sk = text_sk, 
                        title_en = title_en, 
                        text_en = text_en,                         
                        title_de = title_de, 
                        text_de = text_de,                         
                        name = request.user.username, 
                        headline_sk = headline_sk,
                        headline_en = headline_en,
                        headline_de = headline_de,
                        is_published= is_published
                        )

            blog.save()


            messages.success(request, 'Vyslo to!')
            return redirect('add_blog')
    else:
        form = AddBlogForm()

    context = {'form': form}
    return render(request, 'console/add_blog.html', context)