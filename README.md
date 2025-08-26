project:
  name: File Organizer (Python)
  description: >
    A Python automation tool that organizes files in a selected folder by file type.
    It sorts files into categorized subfolders, handles duplicates gracefully, and
    logs all actions taken. Includes a junk file generator and line-by-line explanation file.
  tagline: Organize files by type with logging and duplicate handling.
  license: MIT

features:
  - Organizes files by extension into dedicated folders.
  - Creates a log file (file_organizer_log.txt) of all file movements.
  - Handles files without extensions by placing them in a NO_EXTENSION folder.
  - Automatically renames duplicates to avoid overwriting (e.g., file(1).txt).
  - GUI folder picker (via tkinter) for easy selection.
  - Includes a junk folder generator to test the program.
  - Comes with a line-by-line explanation text file for learning/demo purposes.

requirements:
  python: ">=3.8"
  libraries:
    - os (standard library)
    - shutil (standard library)
    - tkinter (standard library)
    - random (standard library)
    - string (standard library)

project_structure:
  - file_organizer.py: Main script that organizes files
  - junk_file_generator.py: Script to create a test folder with 100 random files
  - line_explanations.txt: Line-by-line explanation of the organizer script
  - README.md: Project documentation

usage:
  file_organizer:
    command: python file_organizer.py
    description: >
      Opens a folder selection window. The selected folder is organized by extension,
      and a log file is generated.
  junk_file_generator:
    command: python junk_file_generator.py
    description: >
      Creates a TestFolder on the Desktop with 100 random files for testing.

example:
  before:
    - notes.txt
    - picture.png
    - data.pdf
    - script.py
    - randomfile
  after:
    TXT:
      - notes.txt
    PNG:
      - picture.png
    PDF:
      - data.pdf
    PY:
      - script.py
    NO_EXTENSION:
      - randomfile
    - file_organizer_log.txt
