from django.shortcuts import render
from gtts import gTTS
import os
from . models import Visitors
import datetime
import socket

# def home(request):
#     return render(request, 'index.html')


def home(request):
    if  request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        language = request.POST.get('lang')
        accent = request.POST.get('accent')
        date = datetime.datetime.now()
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        if accent == "cn":
            tts = gTTS(text=text, lang=language, slow=False)
        else:
            tts = gTTS(text=text, lang=language, tld=accent, slow=False)

        audio_dir = os.path.join('static', 'audio')
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)

        file_name = f'maekandex-{title}.mp3'
        file_path = os.path.join(audio_dir, file_name)
        tts.save(file_path)

        Visitors.objects.create(title=title, text=text, ipaddress=ip_address, date=date, language=language,
                                accent=accent)

        return render(request, 'audio.html', {'audio_file': f'audio/{file_name}'})

    else:
        return render(request, 'index.html')

