from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from listings.models import Listing
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from asgiref.sync import sync_to_async


# Create your views here.


@sync_to_async
def contact (request):
    if request.method == 'POST':
        listing_id  =  request.POST['listing_id']
        name  =  request.POST['name']
        email  =  request.POST['email']
        phone  =  request.POST['phone']
        message  =  request.POST['message']
        user_id  =  request.POST['user_id']
        
        
        

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contact = Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
           
            if has_contact:
                messages.error(request, 'no')
                return redirect('/listings/' + listing_id )
        list  = get_object_or_404(Listing, pk = listing_id)
        print(list.realtor.email, 111)
        messages.success(request, 'YES')
        contact = Contact(listing = list.title, listing_id =  listing_id, name = name, email = email,
        phone = phone,  message = message, user_id = user_id)
        
        contact.save()

        send_mail(
                    list.title,
                    'Here is the message. From '+ name,
                    'lroztomily@gmail.com',
                    [list.realtor.email],
                    fail_silently=False
            )
        
        #subject = list.title
        #to = [list.realtor.email]
        #from_email = 'lroztomily@gmail.com'

        #message = get_template('email.html')
        #message = message.render()

        #msg = EmailMessage(subject, message, to=to, from_email=from_email)
        #msg.content_subtype = 'html'
        #msg.send()

        return redirect('/listings/' + listing_id )