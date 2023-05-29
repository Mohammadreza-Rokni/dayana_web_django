from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import TemplateView
from.models import Article, Portfolio,Contact
from .form import ContactForm

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
    
class AboutUs(TemplateView):
    template_name = 'abuot.html'

class Services(TemplateView):
    template_name = 'services.html'




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            Contact.objects.create(name=name, email=email, text=text)
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})





def portfolio (request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio':portfolio
    }
    return render(request,'portfolio.html',context)
    


def blogs (request):
    blogs = Article.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

def article_detail(request,id):
    article = Article.objects.get(id=id)
    context={
        "article": article
    }
    return render(request, 'article_detail.html', context)