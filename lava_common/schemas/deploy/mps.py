# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Linaro Limited
#
# Author: Rémi Duraffort <remi.duraffort@linaro.org>
#
# This file is part of LAVA.
#
# LAVA is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# LAVA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along
# with this program; if not, see <http://www.gnu.org/licenses>.

from voluptuous import All, Length, Optional, Required

from lava_common.schemas import deploy


def schema():
    base = {
        Required("to"): "mps",
        Required("images"): All(
            {
                Optional("recovery_image"): deploy.url(),
                Optional("test_binary"): {**deploy.url(), Optional("rename"): str},
            },
            Length(min=1),
        ),
    }
    return {**deploy.schema(), **base}
