from django.shortcuts import render, HttpResponse, redirect
import random
def game(request):
    request.session['number'] = random.randint(1, 100)
    return render(request, 'game.html')

def result(request):
    if request.session['number'] == int(request.POST['num_v']):
        request.session['x'] = "You're right! %s was the number" % (request.session['number'])
        return render(request, 'yes.html')
    if request.session['number'] < int(request.POST['num_v']):
        request.session['x'] = 'Too High!'
        return render(request, 'game.html')
    if request.session['number'] > int(request.POST['num_v']):
        request.session['x'] = 'Too low!'
        return render(request, 'game.html')

def playagain(request):
    request.session.clear()
    return redirect('/')