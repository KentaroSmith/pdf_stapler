# PDF Stapler
## Overview
PDF Stapler is a simple app to combine multiple PDF documents in to one file. Simply enter the filepath of a folder containing all of your PDF's and the title you want to give the resulting document and it will do the rest.

## Instructions:
- pip install -r requirements.txt
- pyinstaller stapler.py -F -w -i=pdf.ico --onefile
    - stapler.exe will be placed inside the "dist" folder after pyinstaller finishes running