from django.shortcuts import render
from .chatbot_logic import chatbot

def chatbot_view(request):
    if request.method == 'POST':
        user = request.POST['user_message']
        bot = chatbot.get_response(user_message)
    else:
        response = "Hello, how can I assist you?"

    return render(request, 'chat.html', {'response': bot})

# Create your views here.
