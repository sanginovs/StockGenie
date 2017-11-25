'''
This file is called by "from app import app" inside the app.py file.

It includes all the imports to be used in the app (from allImports import *).
It also includes all the application files that are used as "pages" in the app
(e.g., "from app import start" imports all the code in start.py that is behind the start.html webpage)
'''

from allImports import *
from app import allImports

# Include an import for every python file that is serving a webpage
#import your new python files here. It is not a part of the module until it is imported
print("Starting application") #I don't see this print - Cody Myers

from app import start
from app import routes
