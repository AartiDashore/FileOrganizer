# FileOrganizer


This Python script organizes files in a directory based on their file type. It categorizes files into separate folders such as Images, Documents, Videos, Audios, Archives, Executables, Scripts, and Others.

## Features

- Automatically sorts files into appropriate folders based on their file type.
- Customizable file type categories and corresponding folders.
- Simple and easy-to-use command-line interface.

## Usage

1. Clone the repository or download the `File_Organizer.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `File_Organizer.py`.
4. Run the script by executing the command:
   ```
   python File_Organizer.py
   ```
5. Follow the prompt to enter the directory path you want to organize.

## Customization

You can customize the file type categories and corresponding folders by modifying the `file_types` dictionary in the script. Simply add or remove file extensions and their corresponding folder names as needed.

```python
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
```

## Requirements
- Python 3.x

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
