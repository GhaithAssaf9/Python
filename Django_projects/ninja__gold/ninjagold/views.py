from django.shortcuts import redirect, render, HttpResponse
import random
from time import gmtime, strftime
# random.randint(1, 100)

def first(request):
    request.session['time'] = strftime("%Y-%m-%d %H:%M %p", gmtime())
    if 'gold' in request.session:
        return render(request, 'index.html')
    else:
        request.session['gold'] = 0
        request.session['list'] = []
        return render(request, 'index.html')

def goldcc(request):
    if request.method == 'POST':
            if request.POST['hidden'] == 'hidden1':
                request.session['gold'] += random.randint(10, 20)
                x = f'earned { request.session["gold"] } golds from the farm! { request.session["time"] }'
                request.session['list'].append(x)
                request.session.save()
                return redirect('/')
            if request.POST['hidden'] == 'hidden2':
                request.session['gold'] += random.randint(5, 10)
                x = f'earned { request.session["gold"] } golds from the cave! { request.session["time"] }'
                request.session['list'].append(x)
                request.session.save()
                return redirect('/')
            if request.POST['hidden'] == 'hidden3':
                request.session['gold'] += random.randint(2, 5)
                x = f'earned { request.session["gold"] } golds from the house! { request.session["time"] }'
                request.session['list'].append(x)
                request.session.save()
                return redirect('/')
            if request.POST['hidden'] == 'hidden4':
                request.session['gold'] += random.randint(-50, 50)
                x = f'earned { request.session["gold"] } golds from the casino! { request.session["time"] }'
                request.session['list'].append(x)
                request.session.save()
                return redirect('/')
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')