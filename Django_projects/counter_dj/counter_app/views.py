from django.shortcuts import redirect, render ,HttpResponse
def index(request):
    if 'count' in request.session:
        request.session["count"]+=1
    else:
        request.session["count"] = 1

    return render(request,"counter.html")


def destroy(request):
    request.session.clear()
    return redirect('/')

    


