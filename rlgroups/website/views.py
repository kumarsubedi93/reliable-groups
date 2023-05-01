from django.shortcuts import render
from .models import Team, Feedback
from django.contrib import messages
from django.http.response import JsonResponse

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message  = request.POST.get('message')
        feedback = Feedback(name=name, email=email, subject=subject, message=message)
        feedback.save()
        return JsonResponse({"message": "Your message has been successfully sent. We will contact as soon as possible"}, status=200)
    teams = Team.objects.order_by('-id').all()
    return render(request, template_name='index.html', context={
        'teams': teams
    })


def error_404(request, exception):
    return render(request, template_name='404.html', status=404)