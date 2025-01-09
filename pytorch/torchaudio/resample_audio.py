import torchaudio

audio_data = "path/to/audio.wav"
audio_data, original_sampling_rate = torchaudio.load(audio_data)
resampled_audio_data = torchaudio.transforms.Resample(original_sampling_rate, 16000)(audio_data)