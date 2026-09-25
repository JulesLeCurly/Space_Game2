from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# Fonction pour lire le texte avec la voix de Google
def text_to_speech(text):
    # Crée un objet gTTS (Google Text-to-Speech)
    tts = gTTS(text=text, lang='fr')  # 'fr' pour la langue française, vous pouvez changer la langue si nécessaire

    # Sauvegarde le fichier audio généré par gTTS dans le fichier temporaire
    tts.save("text_to_speech.mp3")

    chemin_complet = os.path.abspath("FichierTemporaire\\text_to_speech.mp3")
    print(chemin_complet)
    # Chargez le fichier audio
    audio = AudioSegment.from_file("text_to_speech.mp3")

    # Jouez le fichier audio
    play(audio)