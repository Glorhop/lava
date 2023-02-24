# coding: utf-8
#
# Copyright (C) 2018-2019 Linaro Limited
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

from voluptuous import Any, Match, Optional, Required

from lava_common.schemas import test
from lava_common.schemas.test.testdef import testdef


def schema():
    common = {
        Required("path"): str,
        Required("name"): Match(r"^[-_a-zA-Z0-9.]+$"),
        Optional("skip_install"): [
            Any("keys", "sources", "deps", "steps", "git-repos", "all")
        ],
        # Optional("parameters"):
        Optional("lava-signal"): Any("kmsg", "stdout"),
    }

    base = {
        Required("definitions"): [
            Any(
                {
                    Required("repository"): str,
                    Required("from"): "git",
                    Optional("branch"): str,
                    Optional("history"): bool,
                    Optional("revision"): str,
                    Optional("parameters"): dict,
                    Optional("params"): dict,
                    **common,
                },
                {
                    Required("repository"): str,
                    Required("from"): "url",
                    Optional("compression"): str,
                    Optional("parameters"): dict,
                    Optional("params"): dict,
                    **common,
                },
                {
                    Required("repository"): {**testdef()},
                    Required("from"): "inline",
                    **common,
                },
            )
        ]
    }
    return {**test.schema(), **base}
