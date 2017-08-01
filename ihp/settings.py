# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2012 OpenPlans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.

import os

# Load more settings from a file called local_settings.py if it exists
try:
    from ihp.local_settings import *
#    from geonode.local_settings import *
except ImportError:
    from geonode.settings import *


#
# General Django development settings
#

SITENAME = 'ihp'

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "ihp.wsgi.application"

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Note that Django automatically includes the "templates" dir in all the
# INSTALLED_APPS, se there is no need to add maps/templates or admin/templates
TEMPLATES[0]['DIRS'].insert(0, os.path.join(LOCAL_ROOT, "templates"))
TEMPLATES[0]['OPTIONS']['debug'] = True

INSTALLED_APPS += ('pinax.notifications', 'ihp', 'ihp.content')

# Location of url mappings
ROOT_URLCONF = 'ihp.urls'

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

#RISKS = {'DEFAULT_LOCATION': 'AF',
#         'PDF_GENERATOR': {'NAME': 'weasyprint_api',
#                           #'NAME': 'wkhtml2pdf',
#                           'BIN': '/usr/bin/xvfb-run /usr/bin/wkhtmltopdf',
#                           'ARGS': []}}

FREETEXT_KEYWORDS_READONLY = True
ADMIN_MODERATE_UPLOADS = True
GROUP_PRIVATE_RESOURCES = True
MODIFY_TOPICCATEGORY = True
USER_MESSAGES_ALLOW_MULTIPLE_RECIPIENTS = True
