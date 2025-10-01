from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ollama import generate
import json

def index(request):
    return render(request, 'chat/chat.html')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # Générer la réponse avec Ollama
            text = generate(
                model='gemma3',
                prompt=user_message,
                stream=False
            )
            
            ai_message = text['response']
            
            return JsonResponse({
                'success': True,
                'message': ai_message
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})