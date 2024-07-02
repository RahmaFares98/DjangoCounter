# Counter_assig/views.py
from django.shortcuts import render, redirect


def index(request):
    # Counter_assig/views.py
    if 'visit_count' not in request.session:
        request.session['visit_count'] = 0  # Initialize visit_count if not present
    if request.session.get('flag', True):
        request.session['visit_count'] += 1  # Increment visit_count on every visit
    request.session['flag'] = True  # Reset the flag after checking
    if 'counter' not in request.session:
        request.session['counter'] = 0  # Initialize counter if not present
    
    context = {
        'visit_count': request.session['visit_count'],
        'counter': request.session['counter'],
    }
    return render(request, 'index_counter.html', context)


def increment_by_2_view(request):
    request.session['counter'] = request.session.get('counter', 0) + 2
    request.session['flag'] = False  
    return redirect('/')

def increment_view(request):
    if request.method == 'POST':
        increment_value = int(request.POST.get('increment_value', 1))
        request.session['counter'] = request.session.get('counter', 0) + increment_value
        request.session['flag'] = False  
    return redirect('/')

def destroy_session_view(request):
    request.session.flush()
    return redirect('/')

def reset_counter_view(request):
    request.session['counter'] = 0
    request.session['flag'] = False  
    return redirect('/')
