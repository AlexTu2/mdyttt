# mdyttt quickstart

mdyttt or markdown youtube tooltip is a script that inserts youtube statistics as a Material for Mkdocs tooltip


Add 'content.tooltips' to features in your mkdocs.yml like so
```
theme:
  name: material
  logo:  assets/logo.png
  features:
    - content.tooltips
```

Usage:
youtube.py -f markdown.md

# mdyttt

mdyttt or markdown youtube tooltip is a script that inserts youtube statistics as a Material for Mkdocs improved tooltips

## Installation 

You will need python 3 installed

Perform the following steps (**in order**):
### 1. Clone the project
  `git clone https://github.com/AlexTu2/mdyttt.git`

### 2. Go to the project directory
  `cd mdyttt`

### 3. Create A Virtual Environment
  `pip install virtualenv`

  `python3 -m venv venv`

### 4. Activate the Virtual Environment 

#### On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat
  `venv\Scripts\activate.bat`

#### On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1
  `venv\Scripts\Activate.ps1`

#### On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate
  `source venv/bin/activate`

### 5. Install the Requirements in `requirements.txt`
  `pip install -r requirements.txt`



## Usage/Examples
  `python youtube.py -f markdown.md`


## Notes

You also need to setup the Google API
https://developers.google.com/youtube/v3/quickstart/python
***
