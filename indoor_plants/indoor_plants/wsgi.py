"""
WSGI config for indoor_plants project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
project_home = '/home/Emms/indoor_plants_api'  # Update this to your project path
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'indoor_plants.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()