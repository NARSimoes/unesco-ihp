# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
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

from django.conf.urls import url
from django.views.generic import TemplateView
from ihp.content.views import (terms_of_use_view,
                               about_us_content_view,
                               SignupView)

import geonode.urls

print geonode.urls.urlpatterns

urlpatterns = [
                url(r'^timeseries/$',
                    TemplateView.as_view(template_name='time_series.html'),
                    name='time_series'),
                url(r'^terms-of-use$',
                    terms_of_use_view,
                    name='terms-of-use'),
                url(r'^about-us$',
                    about_us_content_view,
                    name='about-us'),
                url(r'^account/signup/$',
                    SignupView.as_view(),
                    name="account_signup"),
              ] + geonode.urls.urlpatterns
