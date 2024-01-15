from django.shortcuts import render

from django.http import JsonResponse 
from transformers import AutoTokenizer, AutoModelWithLMHead
import torch

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium')
model = AutoModelWithLMHead.from_pretrained('aanandan/RickGPT-medium-Aditya')


# Create your views here.

def index(request):
    if request.method == 'POST': 
        message = request.POST.get('message')
        response = get_Chat_response(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')


def get_Chat_response(text):
    # Let's chat for 5 lines
    for step in range(5):
        new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        response_text = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response_text  # Make sure there's a return statement inside the loop
    
