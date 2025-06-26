from django.shortcuts import render, get_object_or_404, redirect , HttpResponse
from .models import Candidate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'pollzone/index.html')

def home(request):
    candidates = Candidate.objects.all()[:3] 
    return render(request, 'pollzone/home.html', {'candidates': candidates})

def vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    candidate.votes += 1
    candidate.save()
    return redirect('result')

def result(request):
    candidates = Candidate.objects.all().order_by('-votes')
    total_votes = sum(c.votes for c in candidates)

    for candidate in candidates:
        if total_votes > 0:
            candidate.percentage = round((candidate.votes / total_votes) * 100, 2)
        else:
            candidate.percentage = 0
    return render(request, 'pollzone/result.html', {'candidates': candidates})

def base_view(request):
    return HttpResponse("Base view content")

def criteria(request):
    return render(request, 'pollzone/criteria.html')

def proof(request):
    return render(request, 'pollzone/proof.html')


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # ✅ Redirect to home page
        else:
            return render(request, 'pollzone/login.html', {
                'error': 'Invalid username or password',
                'body_class': 'bg-login'
            })

    return render(request, 'pollzone/login.html', {'body_class': 'bg-login'})


# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # ✅ Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'pollzone/register.html', {
                'error': 'Username already taken.',
                'body_class': 'bg-register'
            })

        # ✅ Optional: check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'pollzone/register.html', {
                'error': 'Email already used.',
                'body_class': 'bg-register'
            })

        # ✅ Create new user
        User.objects.create_user(username=username, password=password, email=email)
        return redirect('login')  # After registration

    return render(request, 'pollzone/register.html', {'body_class': 'bg-register'})



def check_eligibility(request):
    result =''
    if request.method == 'POST':
        age = int(request.POST.get('age', 0))
        if age >= 18:
            result = "You are eligible to vote!"
        else:
            result = "You are not eligible to vote."

    return render(request, 'pollzone/eligibility.html', {'result': result})

