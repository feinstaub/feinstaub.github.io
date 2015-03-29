#!/usr/bin/python

# Copyright (C) 2015 by Gregor Mi <codestruct@posteo.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

# http://stackoverflow.com/questions/3371255/writing-unit-tests-in-python-how-do-i-start
# 1) http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html
# 2) http://www.onlamp.com/pub/a/python/2005/02/03/tdd_pyunit2.html
#

import unittest
import os
import asr

TESTDATA_DIR = "generated-testdata"

def createTestdataFile(name, contents):

    if not os.path.exists(TESTDATA_DIR):
        os.makedirs(TESTDATA_DIR)

    with open(os.path.join(TESTDATA_DIR, name), "w") as text_file:
        text_file.write(contents)

def readTestdataFile(name):
    with open(os.path.join(TESTDATA_DIR, name), "r") as text_file:
        return text_file.readline()

class SelfTest(unittest.TestCase):

    def test1(self):
        createTestdataFile("selftest", "hallo")
        self.assertEquals(readTestdataFile("selftest"), "hallo")

class EncryptDecryptTest(unittest.TestCase):

    def test1(self):
        #asr.decrypt("a", "b", "c")
        print("test1")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
