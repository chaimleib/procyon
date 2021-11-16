#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2017 The Procyon Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess
from .context import PNTOK, pntest


def pntok(source):
    tokenized, _ = pntest.check_output([PNTOK], stdin=source, stdout=subprocess.PIPE)
    return tokenized


def test_lex(run):
    run(pntok)


def pytest_generate_tests(metafunc):
    metafunc.parametrize("run", pntest.LEX_CASES, ids=pntest.DIRECTORIES)


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main())
