from login_app.models import users, UserManager
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from login_app.models import *
import bcrypt


def index(request):
    context = {
        'user': users.objects.all()
    }
    return render(request, 'login.html', context)

def login(request):
    if 'login' in request.POST:
        x = users.objects.filter(email = request.POST['emaill'])
        # request.session['id'] = x[0].id
        if x:
            logged_user = x[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
            # if bcrypt.checkpw(request.POST['passwordd'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            
            request.session['userid'] = logged_user.id
            request.session['fname'] = logged_user.first_name
            request.session['lname'] = logged_user.last_name
            return redirect('/wall')
        return HttpResponse('you have a big problem')

def success(request):
    messages.objects.all().order_by('-created_at')
    context = {
        'all_posts': messages.objects.all().order_by('-created_at'),
        # 'new_comment': request.session['new_comment'],
        # 'p_comments': request.session['p_comments'],
    }
    
    return render(request, 'success.html', context)

    # for x in users.objects.all():
    #     if ((x.email == request.POST['emaill']) and (x.password == request.POST['passwordd'])):
    #         request.session['fname'] = x.first_name
    #         request.session['lname'] = x.last_name
    #         return render(request, 'success.html')
    #     else:
    #         request.session['false'] = 'the email or the password that you provided does not match'
    #         return redirect('/')

def sign_up(request):
    if 'register' in request.POST:
        # errors = users.objects.register(request.POST)
        # if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            # for key, value in errors.items():
            #     messages.error(request, value)
            # return redirect('/')
        # else:
        # # redirect the user back to the form to fix the errors
        #     password = request.POST['password']
        #     pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            
        users.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = request.POST['password'])
        context = {
            'user': users.objects.all()
            }
        request.session['fname'] = request.POST['first_name']
        request.session['lname'] = request.POST['last_name']

        return render(request, 'register.html', context)

def logout(request):
    del request.session['fname']
    del request.session['lname']
    return redirect('/')
###########################################################################################################################
def add_post(request):
    user_id = request.session['userid']
    new_post = messages.objects.create(post = request.POST['post'], user = users.objects.get(id = user_id))
    # request.session['all_posts'] = messages.objects.all()
    # request.session['date'] = new_post.created_at
    messages.objects.all().order_by('created_at')
    context = {
        'all_posts': messages.objects.all().order_by('-created_at'),
        'date': new_post.created_at
    }
    
    return render(request, 'success.html', context)

def add_comment(request, m_id):
    user_id = request.session['userid']
    m_id = m_id
    if 'comment' in request.POST:
        new_comment = comments.objects.create(comment = request.POST['comment'], user = users.objects.get(id = user_id), message = messages.objects.get(id = m_id))
        m_comments = comments.objects.filter(message = messages.objects.get(id = m_id))
        context = {
            'all_posts': messages.objects.all(),
        }
    return render(request, 'success.html', context)

# def view_comments(request, p_id):
#     p_comments = comments.objects.filter(message = messages.objects.get(id = p_id))
#     request.session['p_comments'] = p_comments
#     return redirect('/wall')

def delete_post(request, pp_id):
    c = messages.objects.get(id = pp_id)
    c.delete()
    return redirect("/wall")

def delete_comment(request, cc_id):
    c = comments.objects.get(id = cc_id)
    c.delete()
    return redirect("/wall")