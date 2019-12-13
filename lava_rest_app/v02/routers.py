# -*- coding: utf-8 -*-
# Copyright (C) 2019 Linaro Limited
#
# Author: Stevan Radaković <stevan.radakovic@linaro.org>
#
# This file is part of LAVA.
#
# LAVA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License version 3
# as published by the Free Software Foundation
#
# LAVA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with LAVA.  If not, see <http://www.gnu.org/licenses/>.

from rest_framework_extensions.routers import ExtendedDefaultRouter
from . import views


router = ExtendedDefaultRouter()
router.register(r"aliases", views.AliasViewSet)
router.register(r"devices", views.DeviceViewSet)
router.register(r"devicetypes", views.DeviceTypeViewSet)
router.register(r"jobs", views.TestJobViewSet).register(
    r"suites",
    views.TestSuiteViewSet,
    base_name="jobs-suite",
    parents_query_lookups=["job_id"],
).register(
    r"tests",
    views.TestCaseViewSet,
    base_name="suites-test",
    parents_query_lookups=["suite__job_id", "suite_id"],
)
router.register(r"tags", views.TagViewSet)
router.register(r"workers", views.WorkerViewSet)
