from django.shortcuts import render, redirect   

def index(request):
    return render(request, "index.html")

def create(request):
    request.session['character'] = request.POST['character_name']
    request.session['region'] = request.POST['region']
    request.session['special'] = request.POST['special']
    request.session['gender'] = request.POST['gender']

    return redirect('/character_dash')

def dashboard(request):
    context = {
        'character': request.session['character'],
        'region': request.session['region'],
        'special': request.session['special'],
        'gender': request.session['gender']
    }
    return render(request, 'character.html', context)