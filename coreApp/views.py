from django.shortcuts import render
from gtts import gTTS
import os

def home(request):
    return render(request, 'index.html')


def text_to_speech(request):
    text = request.GET.get('text')  
    title = request.GET.get('title')  
    language = request.GET.get('lang')
    accent = request.GET.get('accent')

    if accent == "cn":
        tts = gTTS(text=text, lang=language, slow=False)
    else:
        tts = gTTS(text=text, lang=language, tld=accent, slow=False)
   
    audio_dir = os.path.join('static', 'audio')
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    
    file_name = f'maek-{title}.mp3'
    file_path = os.path.join(audio_dir, file_name)
    tts.save(file_path)

    return render(request, 'audio.html', {'audio_file': f'audio/{file_name}'})
