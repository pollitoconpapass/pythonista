from datasets import Dataset, Audio
import gradio as gr


# EXAMPLES LIST OF VALUES
es_list = [" hola ", " como estas? ", "bien"]
en_list = [" hello ", " how are you? ", " fine "]

dataset = Dataset.from_dict({"spa": es_list, "eng": en_list})
dataset.push_to_hub(repo_id="test-dataset", token=gr.OAuthToken)


# if you want to push audio files: 
audios_list = ["audio1.wav", "audio2.wav"] # -> but with real audios yk
audio_dataset = Dataset.from_dict({"audios": audios_list, "texts": en_list}).cast_column("audios", Audio())
