kwargs = {
    "dataset_tags": dataset_name,
    "dataset": "The name of the dataset, e.g. IMDB",
    "dataset_config_name": "Config: ..., Split: ..., etc",
    "language": "en",
    "model_name": "distilbert-base-uncased",
    "finetuned_from": "distilbert-base-uncased",
    "tasks": "text-to-speech"
}

trainer.push_to_hub(**kwargs) # -> trainer is the process of fine-tuning

# DIFFERENCES BETWEEN MODEL_NAME / FINETUNED_FROM AND DATASET_CONFIG_NAME / DATASET

# dataset and model_name are for the README of the model
# dataset_config_name and dataset are for the tags of the model
