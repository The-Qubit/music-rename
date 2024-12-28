import os
from openai import OpenAI

def rename_music_files(directory, openai_api_key):
    client = OpenAI(
        api_key=openai_api_key,
    )

    if not os.path.exists(directory):
        print(f"Error: The directory {directory} does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)

    for file_name in files:
        print(file_name)
        full_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(full_path):
            continue

        try:
            response = response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "I want you the rename my music. Exclude things like feat or and stuff only output the main artist and song title. You should only output the new name. For example '10. Rupert Holmes - Escape (The Piña Colada Song).m4a' should be 'Escape - Rupert Holmes.m4a'"},
                    {"role": "user", "content": f"Rename this file: {file_name}"}
                ]
            )
            print(response)

            new_name = response.choices[0].message.content.strip()

            new_full_path = os.path.join(directory, new_name)
            os.rename(full_path, new_full_path)

            print(f"Renamed: {file_name} -> {new_name}")

        except Exception as e:
            print(f"Error processing file {file_name}: {e}")

rename_music_files('path/to/files', os.environ["ChatGPT"])
