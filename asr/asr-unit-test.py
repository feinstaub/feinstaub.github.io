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
import subprocess

TESTDATA_DIR = "generated-testdata"


def createTestdataFile(name, contents):

    if not os.path.exists(TESTDATA_DIR):
        os.makedirs(TESTDATA_DIR)

    filename = os.path.join(TESTDATA_DIR, name)
    with open(filename, "w") as text_file:
        text_file.write(contents)

    return filename


def readTestdataFile(name):
    if not os.path.exists(os.path.join(TESTDATA_DIR, name)):
        return None

    with open(os.path.join(TESTDATA_DIR, name), "r") as text_file:
        return text_file.readline()


class SelfTest(unittest.TestCase):

    def test1(self):
        createTestdataFile("selftest", "hallo")
        self.assertEquals(readTestdataFile("selftest"), "hallo")


class EncryptDecryptTest(unittest.TestCase):

    def test1(self):
        filenamePlain = createTestdataFile("encdec-clear", "hallo world")
        filenameEnc = os.path.join(TESTDATA_DIR, "encdec-enc")
        filenameDecrypted = os.path.join(TESTDATA_DIR, "encdec-decrypted")

        asr.encrypt(filenamePlain, "muh", filenameEnc)

        #
        # assert input and output are not the same
        #
        outputContents = readTestdataFile("encdec-enc")
        self.assertNotEqual(outputContents, "hallo world")

        #
        # assert wrong password throws
        #
        try:
            asr.decrypt(filenameEnc, "wrong", filenameDecrypted)
            self.fail()
        #except Exception as e:
        except subprocess.CalledProcessError as e:
            print(type(e))
            print(e)
            self.assertTrue(True)

        #
        # assert correct pw gets original content
        #
        asr.decrypt(filenameEnc, "muh", filenameDecrypted)
        outputContents = readTestdataFile("encdec-decrypted")
        self.assertEqual(outputContents, "hallo world")


class ExchangePointsTest(unittest.TestCase):

    # @unittest.skip("not a test") # http://pybites.blogspot.de/2009/03/unittest-now-with-test-skipping-finally.html
    # http://stackoverflow.com/questions/6961099/non-test-methods-in-a-python-testcase
    def helperUploadDownloadAbstract(self, name, exPoint):

        testPakFilename = "ExchangePointTest-" + name
        pakFilename = createTestdataFile(testPakFilename, "Hallo Welt")
        exPoint.uploadFile(pakFilename, "ut-sender-1", "ut-receiver-1")
        #
        # no automatic assert
        #

        self.assertEqual(len(exPoint.listDir("ut-sender-1", "receiver-non-ex")), 0)

        self.assertEqual(len(exPoint.listDir("ut-sender-1", "ut-receiver-1")), 1)

        downloadDir = os.path.join(TESTDATA_DIR, "download", name)
        if not os.path.exists(downloadDir):
            os.makedirs(downloadDir)

        exPoint.downloadFile("ut-sender-1", "ut-receiver-1", testPakFilename, downloadDir)

        downloadedContents = readTestdataFile(os.path.join("download", name, testPakFilename))
        self.assertEqual(downloadedContents, "Hallo Welt")

    def testUploadDownloadFilesystem(self):
        exPoint = asr.FilesystemExchangePoint()
        expointPath = os.path.join(TESTDATA_DIR, "expoint-fs")
        if not os.path.exists(expointPath):
            os.mkdir(expointPath)

        exPoint.readConfig({ "Path": expointPath })

        self.helperUploadDownloadAbstract("filesystem", exPoint)

    def off_testUploadDownloadFtp(self):
        exPoint = asr.FtpExchangePoint()
        cfg = asr.readConfigFile(os.path.expanduser("~/asr/configfiles/send-via-biohost-ftp"))
        exPoint.readConfig(cfg["ExchangePointSend"]["ftp_config"])

        self.helperUploadDownloadAbstract("ftp", exPoint)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
