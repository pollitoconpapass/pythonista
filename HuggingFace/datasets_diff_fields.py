import gradio as gr
from datasets import DatasetDict, Dataset


train_dataset = Dataset.from_dict({"a": [1, 2, 3], "b": [4, 5, 6]})
eval_dataset = Dataset.from_dict({"a": [3, 2, 1], "b": [6, 5, 4]})

dataset = DatasetDict({"train": train_dataset, "eval": eval_dataset})
dataset.push_to_hub(repo_id="test-2fields-dataset", token=gr.OAuthToken)
