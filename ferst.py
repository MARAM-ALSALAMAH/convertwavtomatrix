!pip install librosa
import librosa
import numpy as np
import sounddevice as sd

# قراءة الملف الصوتي
audio_file = 'CristianoRonaldo.wav'  # يجب استبدال path_to_audio_file بمسار الملف الفعلي
audio, sr = librosa.load(audio_file, sr=None)  # sr=None يحافظ على معدل العينات الأصلي

# إنشاء مصفوفة الصوت
audio_matrix = librosa.feature.melspectrogram(y=audio, sr=sr)
