#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,)
#                        unicode_literals)

import itertools
import sys

# Small Py2/3 compatibility layer
if sys.version_info.major == 2:
    map = itertools.imap
    range = xrange

else:  # >= 3
    pass


if __name__ == '__main__':
    test_cases = open(sys.argv[1], 'r')

    out = {(False, False): 'FB', (False, True): 'F', (True, False): 'B'}

    for line in test_cases:
        x, y, n = map(int, line.split())
        r = map(lambda i: out.get((bool(i % x), bool(i % y)), i), range(1, n + 1))
        print(' '.join(map(str, r)))

    test_cases.close()
