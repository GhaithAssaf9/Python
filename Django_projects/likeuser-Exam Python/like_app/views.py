from like_app.models import users, UserManager
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from like_app.models import *
import bcrypt


def index(request):
    context = {
        'user': users.objects.all()
    }
    return render(request, 'login.html', context)

def login(request):
    if 'login' in request.POST:
        x = users.objects.filter(email = request.POST['emaill'])
        
        if x:
            logged_user = x[0] 
  
            
            request.session['userid'] = logged_user.id
            request.session['fname'] = logged_user.first_name
            request.session['lname'] = logged_user.last_name
            return redirect('/wall')
        return HttpResponse('you have a big problem')

def success(request):
    though.objects.all().order_by('-created_at')
    context = {
        'all_posts': though.objects.all().order_by('-created_at'),
        "user":users.objects.get(id=request.session['userid'])
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
        password=request.POST["password"]
        errors = users.objects.register(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
            
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

def add_post(request):
    errors3 = users.objects.post(request.POST)
    if len(errors3) > 0:
        for key, value in errors3.items():
            messages.error(request, value)
        return redirect('/wall')
    user_id = request.session['userid']
    new_post = though.objects.create(post = request.POST['post'], user = users.objects.get(id = user_id))
    though.objects.all().order_by('created_at')
    context = {
        'all_posts': though.objects.all().order_by('-created_at'),
        'user':users.objects.get(id=user_id)
    }
    
    return render(request, 'success.html', context)

def delete_post(request, pp_id):
    c = though.objects.get(id = pp_id)
    c.delete()
    return redirect("/wall")

def delete_comment(request, cc_id):
    c = comments.objects.get(id = cc_id)
    c.delete()
    return redirect("/wall")

def like(request, id):
    user = users.objects.get(id = request.session['userid'])
    post = though.objects.get(id = id)
    user.post_like.add(post)
    return redirect('/details/'+str(id))


def dislike(request, id):
    user = users.objects.get(id = request.session['userid'])
    post = though.objects.get(id = id)
    user.post_like.remove(post)
    return redirect('/details/'+str(id))

def details(request,id):
    if 'userid' in request.session:
        context = {
            'posts': though.objects.all(),
            'users': users.objects.all(),
            'user': users.objects.get(id = request.session['userid']),
            'post': though.objects.get(id = id),
        }
        return render(request, 'after.html', context)
    # return redirect('/')
