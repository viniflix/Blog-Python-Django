from django.shortcuts import render
from django.utils import timezone
from .models import Post, Contact
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def form_contact(request):
    return render(request, 'blog/form_contact.html')

@require_POST
def submited_form(request):
    nome = request.POST['nome']
    email = request.POST['email']
    assunto = request.POST['assunto']
    mensagem = request.POST['mensagem']

    new_contact = Contact.objects.create(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
    new_contact.save()

    return HttpResponseRedirect('/')