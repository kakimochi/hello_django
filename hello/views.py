from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# import re

from django.shortcuts import redirect
from .forms import LogMessageForm
from .models import LogMessage
from django.views.generic import ListView

# Create your views here.
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

# def home(request):
#     return render(request, 'hello/home.html')

def about(request):
    return render(request, 'hello/about.html')

def contact(request):
    return render(request, 'hello/contact.html')

def log_message(request):
    if request.method == "POST":
        form = LogMessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()

            return redirect('home')
    else:
        form = LogMessageForm()

        return render(
            request, 
            'hello/log_message.html', 
            {
                'form':form
            }
        )

# def hello_there(request, name):
#     return render(
#         request,
#         'hello/hello_there.html',
#         {
#             'name': name,
#             'date': datetime.now(),
#         }
#     )

# def home(request):
#     return HttpResponse("Hello, Django!")

# def hello_there(request, name):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d, %B, %Y at %X")

#     match_obj = re.match("[a-zA-Z]+", name)

#     if match_obj:
#         clean_name = match_obj.group(0)
#     else:
#         clean_name = "Friend"
    
#     content = "Hello there, " + clean_name + "! It's " + formatted_now

#     return HttpResponse(content)
