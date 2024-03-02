import os
import shutil

def organize_files(directory):
    # Define file types and corresponding folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.xls', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Audios': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Executables': ['.exe', '.msi'],
        'Scripts': ['.py', '.sh', '.bat', '.ps1'],
        'Others': []  # Any other file types
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        if not os.path.exists(os.path.join(directory, folder)):
            os.makedirs(os.path.join(directory, folder))

    # Organize files
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = os.path.splitext(filename)[1]
            moved = False
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(
                        os.path.join(directory, filename),
                        os.path.join(directory, folder, filename)
                    )
                    moved = True
                    break
            if not moved:
                shutil.move(
                    os.path.join(directory, filename),
                    os.path.join(directory, 'Others', filename)
                )

if __name__ == "__main__":
    folder_path = input("Enter the directory path to organize files: ")
    if os.path.isdir(folder_path):
        organize_files(folder_path)
        print("Files organized successfully!")
    else:
        print("Invalid directory path.")
