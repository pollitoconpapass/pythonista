from huggingface_hub import create_repo, upload_folder

repo_name = "whisper-quz" # -> model name
namespace = "usernamexyz" # -> username
repo_id = f"{namespace}/{repo_name}"

create_repo(repo_id, exist_ok=True)
upload_folder(
    repo_id=repo_id,
    folder_path="./path/to/folder/with/data",
)

print("Model pushed to hub!")