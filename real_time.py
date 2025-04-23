import sounddevice as sd
import scipy.io.wavfile as wav
#import numpy as np
import os
import time
from transformers import pipeline
from datetime import datetime
from pathlib import Path

# Configuration
DURATION = 5  # secondes par segment
SAMPLE_RATE = 16000
OUTPUT_WAV = "temp_audio.wav"
TRANSCRIPT_FILE = "transcription.txt"
PARENT_PATH = Path(__file__).parent
MODEL_PATH = PARENT_PATH / "whisper_small" 


# Chargement du modèle
asr = pipeline("automatic-speech-recognition", model=MODEL_PATH)

# Nettoyage du fichier de sortie
if os.path.exists(TRANSCRIPT_FILE):
    os.remove(TRANSCRIPT_FILE)

print("Démarrage de la transcription vocale en temps réel. Appuyez sur Ctrl+C pour arrêter.")

try:
    while True:
        # Enregistrement
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Enregistrement en cours...")
        audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="int16")
        sd.wait()
        wav.write(OUTPUT_WAV, SAMPLE_RATE, audio)

        # Transcription
        result = asr(OUTPUT_WAV, return_timestamps=True)

        # Cas 1 : dictionnaire avec chunks (timestamps disponibles)
        if isinstance(result, dict) and 'chunks' in result:
            text_segment = " ".join([seg['text'] for seg in result['chunks']])

        # Cas 2 : dictionnaire simple (pas de timestamps)
        elif isinstance(result, dict) and 'text' in result:
            text_segment = result['text']

        # Cas 3 : résultat brut (chaîne de caractères)
        elif isinstance(result, str):
            text_segment = result

        else:
            text_segment = "[ERREUR : format de sortie inattendu]"

        # Affichage et sauvegarde
        print(text_segment)
        with open(TRANSCRIPT_FILE, "a", encoding="utf-8") as f:
            f.write(text_segment + "\n")

except KeyboardInterrupt:
    print("\nArrêt demandé par l'utilisateur.")
