import os
import shutil

folder = "."

files = os.listdir(folder)

folders = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Music": [".mp3"],
    "Videos": [".mp4"]
}

for folder_name in folders:

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

for file in files:

    if file ["main.py", "README.md", "LICENSE", ".gitignore"]:
        continue

    for folder_name in folders:

        for extension in folders[folder_name]:

            if file.endswith(extension):

                shutil.move(file, os.path.join(folder_name, file))

                print(file, "moved to", folder_name)

                break

print("\nDone organizing files.")
