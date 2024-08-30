from django.shortcuts import render, redirect
from blog.models import Post
from projects.models import Proyecto
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    proyectos = Proyecto.objects.all()
    posts = Post.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'proyectos': proyectos})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email_template.html',{
            'name': name,
            'email': email,
            'message': message,
        })

        email= EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['danielriveravelasquez@gmail.com']
        )

        email.fail_silently = False
        email.send()

        messages.success(request, 'Se ha enviado tu correo.')
        return redirect('home')


def linksview(request):
    return render(request, 'main/linktree.html')
