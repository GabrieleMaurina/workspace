import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load(librosa.util.example_audio_file())

D = librosa.stft(y)

'''print(sr)

print(y)

print(D)'''

plt.plot(D)
plt.show()