# ContentVoice

**ContentVoice** is an open-source text-to-speech (TTS) web application built with Django. It supports multiple languages and accents, allowing users to convert text into speech with downloadable audio output. This project aims to provide a simple yet powerful tool for generating spoken audio from written text.

## Features
- Multi-language support (English, French, Chinese, Portuguese, Spanish, and more)
- Selectable accents for different languages
- User-friendly interface for text input and conversion
- Downloadable audio files in MP3 format
- Easily customizable and extendable for additional features


## Getting Started
### Prerequisites
- Python 3.x
- Django
- gTTS (Google Text-to-Speech)

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/stephen-excel/contenvoice.git
   cd talkvoice

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run Migrations**
   ```bash
   python manage.py migrate

5. **Run the Application**
   ```bash
   python manage.py runserver

6. **Open your web browser and navigate to http://127.0.0.1:8000/ to use the application.**
   
