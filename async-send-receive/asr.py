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

#####################################################################
##
## asr - async send receive
## ------------------------
##
## Asr is a tool built around the idea to exchange data between
## two computers using a third, potentially completely untrusted, party
## (like internet hosting services, corporate network shares etc.)
## in an asynchronous way.
##
## Asr currently does not target the ultra-mobile-cloud-user audience
## but more the being-offline kind of use cases. Places in the Internet
## are classified as untrusted sites and private data should lie
## around needlessly or even unprotected.
## So asr tries to provide an electronic way of sending someone a
## package via postal service; including privacy of correspondence,
## posts and telecommunications.
##
## If you send someone a postal package there is usually no trace of the
## package's content between sender and receiver. The only metadata
## which is tracked is who sent it and who received it. Asr also
## tries to minimize public metadata.
##
## As with regular email, the process of sending and receiving is
## asynchronous. The receiver does not have to be online when a package
## is sent.
##
#####################################################################

"""
    Requirements
    ------------
    - tar
    - openssl
    - python-guidata (has some more python deps)
    - gnome-web-photo (optional)
    - wget (optional)
"""

"""
    TODOs
    -----
    * add --keep-intermediate-files to debug things, otherwise delete old stuff
    * "Package": { "PasswordFromFile": "~/common-secrets/alice-bob" },
    * $ asr send <files>
       => asks for receiver via GUI (see configfiles)
    * common config of senderId (extra file)
    * common config of exchange points and then reference only (extra file)
    * asr receive <list of sender ids> or --all
    * use some git bundle mechanism to keep two git repos in private sync
    * Cache FTP connection to avoid IP blocking
"""

#
# This file is was edited using kdevelop's Python plugin.
# Praise for kdevelop's plugin:
#   "I just started editing another python script file and remembered that there was the kdevelop-python-plugin.
#   I always thought it comes with kdevelop until I realized it is a separate package.
#   Now that it is installed I can tell you I love it.
#   It makes python editing as fun as it is supposed to be! Great stuff!"
#

#
# general:
# http://stackoverflow.com/questions/125951/command-line-program-to-create-website-screenshots-on-linux
#

# gnome-web-photo:
#
# http://xmodulo.com/how-to-take-full-length-screenshot-of-web-page-in-linux.html
# gnome-web-photo -t 20 -m photo http://xmodulo.com/how-to-take-full-length-screenshot-of-web-page-in-linux.html out.png
#
# gnome-web-photo -t 20 -m photo http://192.168.2.200/visu.html?mode=1&flag=16&offset=-1 out2.png
# Timed out while loading 'http://192.168.2.200/visu.html?mode=1&flag=16&offset=-1'. Nothing to output...

# http://cutycapt.sourceforge.net/
# ...

#
# Integration tests:
# -----------------
#
# cd ~/dev/src/feinstaub.github.io/async-send-receive
#
## show help:
# ./asr -h
#
## send SourceList as configured in given demo-config
# ./asr send --configfile asr-demo-config
#
## send given source dir
# ./asr send --sourcedir ~/tmp/apidocs --configfile asr-demo-config
#
## send given some fake source
# ./asr send --unittest use-fake-source --configfile asr-demo-config
#
## unpack (unencrypt, extract to target dir) given package
# ./asr unpack-only --packagefile demo1-2015-03-27T09_58_16.823101.pak --configfile asr-demo-config
#
## process sources and show output directory
# ./async-send-receive/asr process-sources-only --configfile asr-demo-config
#

import argparse
import json
from datetime import datetime
import os
#from subprocess import call
import subprocess
import tempfile
import sys
import shutil
# import guidata

args = None
cfg = None

PAK_EXT = ".pak"
DONE_EXT = ".done"
ARCHIVED_EXT = ".tar"
DOWNLOADED_SUBDIR = "_intermediate/1_downloaded" # will ideally eventually contain 0 byte .done files
DECRYPTED_SUBDIR = "_intermediate/2_decrypted"   # created file will be cleaned after unpack (TODO)
UNPACKED_SUBDIR = "unpacked"
SUBJECTLINE_FILENAME = "ASR_SUBJECTLINE"

g_senderId = None
g_receiverId = None
g_subjectLine = None
g_outboxDir = None
g_inboxDir = None

def dateTimeNowIso():
    """Returns e.g. "2015-03-28T11_36_51-099832"
    """
    now = datetime.today()
    nowStr = now.isoformat().replace(":", "_").replace(".", "-")
    return nowStr

def archiveToFile(sourceDir, targetFilenameBase):
    """compresses the sourceDir to one file
    returns the resulting filename.
    Directory where targetFilenameBase should be created must exist!

    todo/later: make compression optional
    """
    print("archiveToFile: sourceDir:{0}, targetFilenameBase:{1}".format(sourceDir, targetFilenameBase))

    # tar -zcvf test.tar.gz 2015-03-25T22_18_46.529128/
    # http://www.cyberciti.biz/faq/how-do-i-compress-a-whole-linux-or-unix-directory/
    # http://stackoverflow.com/questions/939982/how-do-i-tar-a-directory-of-files-and-folders-without-including-the-directory-it
    targetFilename = targetFilenameBase + ARCHIVED_EXT

    #print(os.path.basename(sourceDir))
    #print(os.path.dirname(sourceDir))

    print("[STATUS]: Archiving... Please wait...")

    sys.stdout.flush() # flush all python prints so far
    #                            sourceDir="/tmp/hallo/test" =>   /tmp/hallo                  test
    #retCode = call(["tar", "-zcvf", targetFilename, "-C", os.path.dirname(sourceDir), os.path.basename(sourceDir)])
    # do not use -z (=> no compression)
    retCode = subprocess.check_call(["tar", "-cvf", targetFilename, "-C", sourceDir, "."])
    return targetFilename

def extractArchive(inputFilename, targetDir):
    print("extractArchive: inputFilename:{0}, targetDir:{1}".format(inputFilename, targetDir))
    print("[STATUS]: Extracting archive... Please wait...")

    sys.stdout.flush() # flush all python prints so far
    # do not use -z (=> no compression)
    subprocess.check_call(["tar", "-xvf", inputFilename, "-C", targetDir])

def encrypt(sourceFilename, pw, targetFilename):
    """encrypts the file
    """
    print("encrypt: sourceFilename:{0}, pw:(secret), targetFilename:{1}".format(sourceFilename, targetFilename))

    print("[STATUS]: Encrypting... Please wait...")

    # openssl aes-128-cbc -salt -in t1 -out t1.enc -k abcPW
    # http://serverfault.com/questions/489140/what-is-a-good-solution-to-encrypt-some-files-in-unix
    # NOTE: https://www.openssl.org/docs/apps/enc.html
    # - The -salt option should ALWAYS be used if the key is being derived from a password unless you want compatibility with previous versions of OpenSSL and SSLeay.
    #- see there also for cyphers
    sys.stdout.flush() # flush all python prints so far
    subprocess.check_call(["openssl", "aes-128-cbc", "-salt", "-in", sourceFilename, "-out", targetFilename, "-k", pw])

    # not used: gpg
    #http://askubuntu.com/questions/17641/create-encrypted-password-protected-zip-file
    #http://www.cyberciti.biz/tips/linux-how-to-encrypt-and-decrypt-files-with-a-password.html

def decrypt(inputFilename, pw, outputFilename):
    """# openssl aes-128-cbc -d -salt -in t1.enc -out t1.dec -k abcPW
    Creates the intermediate directories of outputFilename if not exist
    """
    print("decrypt: inputFilename:{0}, pw:(secret), outputFilename:{1}".format(inputFilename, outputFilename))
    print("[STATUS]: Decrypting... Please wait...")

    p1 = os.path.dirname(outputFilename)
    if not os.path.exists(p1):
        print("decrypt target dir does not exist. CREATE: {0}".format(p1))
        os.makedirs(p1)

    sys.stdout.flush() # flush all python prints so far

    subprocess.check_call(["openssl", "aes-128-cbc", "-d", "-salt", "-in", inputFilename, "-out", outputFilename, "-k", pw])

def unpackPackageToInbox(inputFilename):
    """NOTE that inputFilename can contain an absolute path.
    Respects and processes ASR_SUBJECTLINE.
    """
    print("unpackPackageToInbox")
    inputBasename = os.path.basename(inputFilename) # final component of pathname
    (packageName, ext) = os.path.splitext(inputBasename)
    if ext != PAK_EXT:
        print("WARN: unpackPackageToInbox: inputFilename should end with PAK_EXT")

    print("packageName: {0}".format(packageName))

    uncryptedFilename = os.path.join(g_inboxDir, DECRYPTED_SUBDIR, g_senderId, packageName + ARCHIVED_EXT)

    decrypt(inputFilename, cfg["Package"]["Password"], uncryptedFilename)

    print("decrypted: {0}".format(uncryptedFilename))

    unpackBaseDir = os.path.join(g_inboxDir, UNPACKED_SUBDIR)
    print("unpackBaseDir: {0}".format(unpackBaseDir))

    unpackDir = os.path.join(unpackBaseDir, g_senderId, packageName)
    print("unpackDir: {0}".format(unpackDir))

    if not os.path.exists(unpackDir):
        print("unpackDir does not exist. CREATE: {0}".format(unpackDir))
        os.makedirs(unpackDir)
    else:
        raise Exception("unpackDir (or its proxyfile) already exists. Either delete it or delete the downloaded pak file or specifiy another package file from command line.")

    extractArchive(uncryptedFilename, unpackDir)
    print("unpacked to: {0}".format(os.path.abspath(unpackDir)))

    #
    # process subject line
    #
    subjectLineFileName = os.path.join(unpackDir, SUBJECTLINE_FILENAME)
    if os.path.exists(subjectLineFileName):
        subjectLineFile = open(subjectLineFileName, 'r')
        subjectLine = subjectLineFile.readline()
        subjectLineFile.close()

        os.remove(subjectLineFileName)

        subjectedDirName = "{0} - {1}".format(unpackDir, subjectLine)
        shutil.move(unpackDir, subjectedDirName)

        proxyFileForOriginalDir = open(unpackDir, 'w')
        proxyFileForOriginalDir.write("WAS MOVED TO: {0}".format(subjectedDirName))
        proxyFileForOriginalDir.close()

def processSources():
    """either processes the SourceList defined in the config file
    or takes the --sourcedir argument from command line.

    In the first case the generated temp directory path is returned.
    In the second case the --sourcedir argument is returned as is.
    """
    if (args.sourcedir is not None):
        print("processSources: take --sourcedir which is: {0}. Absolute: {1}".format(args.sourcedir, os.path.abspath(args.sourcedir)))
        if not os.path.exists(args.sourcedir):
            raise Exception("args.sourcedir must exist")
        return args.sourcedir
    else:
        print("processSources: use SourceList from config file")

        #
        # generate sourcesTargetDir
        #
        sourcesTargetDir = tempfile.mkdtemp()

        #
        # process SourceList or Unit test
        #
        if args.unittest == "use-fake-source":
            print("UNIT TEST because --unittest use-fake-source")
            with open(os.path.join(sourcesTargetDir, "unit-test-file.txt"), "w") as text_file:
                text_file.write("This is a test file")
        else:
            sourceList = cfg["SourceList"]

            for item in sourceList:
                #print(item)
                filename = os.path.join(sourcesTargetDir, item["Filename"]);
                desc = item["Description"];
                uri = item["Uri"];
                tool = item["Tool"];
                print("Name: {0}, Uri: {1}".format(filename, uri))

                if tool == "gnome-web-photo":
                    timeout = item["Timeout"];

                    # gnome-web-photo -t 20 -m photo http://kde.org. out2.png
                    # http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
                    sys.stdout.flush() # flush all python prints so far
                    subprocess.check_call(["gnome-web-photo", "-t", str(timeout), "-m", "photo", uri, filename])
                elif tool == "wget-file":
                    sys.stdout.flush() # flush all python prints so far
                    subprocess.check_call(["wget", uri, "-O", filename])
                elif tool == "wget-web":
                    sys.stdout.flush() # flush all python prints so far
                    subprocess.check_call(["wget", uri])
                else:
                    print("UNKNOWN TOOL: {0}".format(tool))

        return sourcesTargetDir

"""
ExchangePoint type
------------------
methods
    * readConfig(self, configObj)
    * uploadFile(self, pakFilename, senderId, receiverId)
    * listDir(self, senderId, receiverId)
    * downloadFile(self, senderId, receiverId, filename, downloadDir)
"""

class FilesystemExchangePoint:

    exchangeBaseDir = None

    def __init__(self):
        print("cfgExchangePointType == filesystem")

    def readConfig(self, configObj):
        configPath = configObj["Path"]

        self.exchangeBaseDir = os.path.expanduser(configObj["Path"])
        absTargetBaseDir = os.path.abspath(self.exchangeBaseDir)
        print("targetDir: configured='{0}', absolute='{1}'".format(self.exchangeBaseDir, absTargetBaseDir))
        if not os.path.exists(self.exchangeBaseDir):
            raise Exception("ERROR: exchangeBaseDir must exist: {0}".format(absTargetBaseDir))

    def uploadFile(self, pakFilename, senderId, receiverId):
        targetDir = os.path.join(self.exchangeBaseDir, senderId, receiverId)
        if not os.path.exists(targetDir):
            print("targetDir does not exist. CREATE: {0}".format(targetDir))
            os.makedirs(targetDir)

        shutil.copy(pakFilename, targetDir)

    def listDir(self, senderId, receiverId):
        sourceDir = os.path.join(self.exchangeBaseDir, senderId, receiverId)

        if not os.path.exists(sourceDir):
            print("sourceDir does not exist. Nothing to do")
            return []

        sourceFileList = os.listdir(sourceDir)
        return sourceFileList

    def downloadFile(self, senderId, receiverId, filename, downloadDir):
        sourceDir = os.path.join(self.exchangeBaseDir, senderId, receiverId)
        shutil.copy(os.path.join(sourceDir, filename), downloadDir)


class FtpExchangePoint:

    host = None
    user = None
    pw = None

    def __init__(self):
        print("cfgExchangePointType == ftp")

    def readConfig(self, configObj):
        self.host = configObj["host"]
        self.user = configObj["user"]
        self.pw = configObj["pw"]

    def uploadFile(self, pakFilename, senderId, receiverId):
        import ftplib
        print("Connect to FTP: host={0}, user={1}, ...".format(self.host, self.user))
        sys.stdout.flush() # flush all python prints so far
        ftp = ftplib.FTP(self.host, self.user, self.pw)

        if not senderId in ftp.nlst():
            print("senderId does not exist. CREATE: {0}".format(senderId))
            ftp.mkd(senderId)

        print("cwd {0}".format(senderId))
        ftp.cwd(senderId)

        if not receiverId in ftp.nlst():
            print("receiverId does not exist. CREATE: {0}".format(receiverId))
            ftp.mkd(receiverId)

        print("cwd {0}".format(receiverId))
        ftp.cwd(receiverId)

        pakBasename = os.path.basename(pakFilename)
        print("STOR binary: pakBasename: {0}. Please wait...".format(pakBasename))

        sys.stdout.flush() # flush all python prints so far

        pakFileObject = open(pakFilename, 'r')
        ftp.storbinary("STOR {0}".format(pakBasename), pakFileObject)
        pakFileObject.close()

        print("ftp.quit()")
        ftp.quit()

    def listDir(self, senderId, receiverId):
        import ftplib
        ftp = ftplib.FTP(self.host, self.user, self.pw)

        if not senderId in ftp.nlst():
            print("senderId ({0}) does not exist. Nothing to do.".format(senderId))
            return []

        print("cwd {0}".format(senderId))
        ftp.cwd(senderId)

        if not receiverId in ftp.nlst():
            print("receiverId ({0}) does not exist. Nothing to do.".format(receiverId))
            return []

        print("cwd {0}".format(receiverId))
        ftp.cwd(receiverId)

        sourceFileList = ftp.nlst()

        print("ftp.quit()")
        ftp.quit()

        return sourceFileList

    def downloadFile(self, senderId, receiverId, filename, downloadDir):
        import ftplib
        ftp = ftplib.FTP(self.host, self.user, self.pw)

        ftp.cwd(senderId)
        ftp.cwd(receiverId)

        ftp.retrbinary("RETR {0}".format(filename), open(os.path.join(downloadDir, filename), 'wb').write)

        print("ftp.quit()")
        ftp.quit()


def sendPackage(pakFilename, senderId, receiverId):

    print("sendPackage: pakFilename:{0}, senderId:{1}, receiverId:{2}".format(pakFilename, senderId, receiverId))
    print("[STATUS]: Sending package... Please wait...")

    sys.stdout.flush() # flush all python prints so far

    cfgExchangePointType = cfg["ExchangePointSend"]["Type"]

    exPoint = None

    if cfgExchangePointType == "filesystem":
        exPoint = FilesystemExchangePoint()
        exPoint.readConfig(cfg["ExchangePointSend"]["filesystem_config"])

    elif cfgExchangePointType == "ftp":
        exPoint = FtpExchangePoint()
        exPoint.readConfig(cfg["ExchangePointSend"]["ftp_config"])
    else:
        raise Exception("ERROR: cfgExchangePointType unknown: {0}".format(cfgExchangePointType))

    sys.stdout.flush() # flush all python prints so far
    exPoint.uploadFile(pakFilename, senderId, receiverId)


def downloadPackages():
    """Copies all packages from the given g_senderId/g_receiverId subfolder
    from the configured exchange point and stores them to the download dir.

    TODO: implement mechanism of deleting the remote files
    """
    cfgExchangePointType = cfg["ExchangePointReceive"]["Type"]

    exPoint = None

    if cfgExchangePointType == "filesystem":
        exPoint = FilesystemExchangePoint()
        exPoint.readConfig(cfg["ExchangePointReceive"]["filesystem_config"])
    elif cfgExchangePointType == "ftp":
        exPoint = FtpExchangePoint()
        exPoint.readConfig(cfg["ExchangePointSend"]["ftp_config"])
    else:
        raise Exception("ERROR: cfgExchangePointType unknown: {0}".format(cfgExchangePointType))

    sourceFileList = exPoint.listDir(g_senderId, g_receiverId)
    print("SOURCE file list: " + str(sourceFileList))

    downloadBaseDir = os.path.join(g_inboxDir, DOWNLOADED_SUBDIR)
    downloadDir = os.path.join(downloadBaseDir, g_senderId)

    if not os.path.exists(downloadDir):
        print("downloadBaseDir does not exist. CREATE: {0}".format(downloadDir))
        os.makedirs(downloadDir)

    inboxFileList = os.listdir(downloadDir)
    print("INBOX file list: " + str(sourceFileList))

    for filename in sourceFileList:
        packageName = os.path.splitext(filename)[0]
        if packageName + PAK_EXT in inboxFileList:
            print("{0} already downloaded. Skip. (normally a downloaded package will unpacked and marked as done)".format(filename))
        elif packageName + DONE_EXT in inboxFileList:
            print("{0} already unpacked. Skip. (todo: delete from remote)".format(filename))
        else:
            print("{0} not downloaded yet. Download.".format(filename))
            print("[STATUS]: Downloading... Please wait...")
            exPoint.downloadFile(g_senderId, g_receiverId, filename, downloadDir)


def unpackDownloadedPackages():
    """Processes all not processed packages (".pak" is not processed, ".done" is processed)
    and unpacks them to the unpack dir.
    The contents of a pak files marked as "done" will be cleared since we still have the unencrypted
    files present.
    """
    downloadBaseDir = os.path.join(g_inboxDir, DOWNLOADED_SUBDIR)
    downloadDir = os.path.join(downloadBaseDir, g_senderId)

    if not os.path.exists(downloadDir):
        print("downloadDir '{0}' does not exist. Nothing to do.".format(downloadDir))
        return

    downloadedFilesList = os.listdir(downloadDir)
    for filename in downloadedFilesList:
        (packageName, ext) = os.path.splitext(filename)
        if ext == PAK_EXT:
            packageFilename = os.path.join(downloadDir, filename)

            unpackPackageToInbox(packageFilename)

            #
            # now mark as done to prevent double processing
            #
            open(packageFilename, 'w').close() # erase contents !!!

            # /path/to/packageName.pak --> /path/to/packageName.done
            doneName = os.path.join(os.path.dirname(packageFilename), packageName + DONE_EXT)
            shutil.move(packageFilename, doneName)

        elif ext == DONE_EXT:
            # ignore because already done
            pass
        else:
            print("WARN: unknown filename extension in download dir: {0}".format(ext))

def actionSend():
    #
    # Process sources
    #
    sourceDir = processSources()
    print("sourceDir: {0}".format(os.path.abspath(sourceDir)))

    #
    # put subject file to sourceDir
    #
    subjectLineFileName = os.path.join(sourceDir, SUBJECTLINE_FILENAME)
    if os.path.exists(subjectLineFileName):
        raise Exception("SUBJECTLINE_FILENAME must not exist in source dir")
    subjectLineFile = open(subjectLineFileName, 'w')
    subjectLineFile.write(g_subjectLine)
    subjectLineFile.close()

    #
    # make package
    #
    outboxPackagesBaseDir = g_outboxDir

    outboxDir = os.path.join(outboxPackagesBaseDir, g_receiverId)

    if not os.path.exists(outboxDir):
        print("outboxDir does not exist. CREATE: {0}".format(outboxDir))
        os.makedirs(outboxDir)

    # todo: make hash out of senderId? (https://docs.python.org/2/library/hashlib.html)

    packageBaseFilename = os.path.join(outboxDir, dateTimeNowIso())
    print("packageBaseFilename: {0}".format(os.path.abspath(packageBaseFilename)))

    pakFilename = archiveToFile(sourceDir, packageBaseFilename)
    print("archived: {0}".format(os.path.abspath(pakFilename)))


    print("remove SUBJECTLINE_FILENAME")
    os.remove(subjectLineFileName)


    packageFilename = packageBaseFilename + PAK_EXT
    encrypt(pakFilename, cfg["Package"]["Password"], packageFilename)
    print("package filename: {0}".format(packageFilename))

    #
    # send
    #
    sendPackage(packageFilename, g_senderId, g_receiverId)

def actionReceive():
    downloadPackages()
    unpackDownloadedPackages()

def readConfigFile(configFilename):
    with open(configFilename, 'r') as cfgfile:
        cfg = json.load(cfgfile)
        return cfg

def main():
    #
    # globals
    #
    # use option -h to show help
    #
    # see https://docs.python.org/3/library/argparse.html
    #
    parser = argparse.ArgumentParser(description='asr (async-send-receive) by Gregor Mi (2015)')
    parser.add_argument('action', help="'send': retrieve source, make package and send | 'receive': retrieve package and unpack | 'process-sources-only': only processes the sources defined in SourceList | 'unpack-only': unpacks a given package file (see --packagefile)")
    parser.add_argument('--configfile', help="The config file shared with sender and receiver")
    parser.add_argument('--sourcedir', help="for --action send: use this directory instead of the configured ones in the configfile (SourceList)")
    parser.add_argument('--packagefile', help="filename to a package file; needed for --action unpack")
    parser.add_argument('--unittest', help="'use-fake-source': don't process source defined in config file but create a fake file")
    global args # TODO: refactor this
    args = parser.parse_args()
    print("ARGS: action: {0}".format(args.action))
    print("ARGS: configfile: {0}".format(args.configfile))
    print("ARGS: sourcedir: {0}".format(args.sourcedir))
    print("ARGS: packagefile: {0}".format(args.packagefile))
    print("ARGS: unittest: {0}".format(args.unittest))

    global cfg # TODO: refactor this
    cfg = readConfigFile(args.configfile)

    #print("debug config:--------")
    #print(cfg)
    #print("--------")

    global g_senderId
    g_senderId = cfg["SenderId"] # TODO: let this be overridable by command line arguments

    global g_receiverId
    g_receiverId = cfg["ReceiverId"] # TODO: let this be overridable by command line arguments

    # subjectLine must be a valid filename
    global g_subjectLine
    g_subjectLine = cfg["SubjectLine"] # TODO: let this be overridable by command line arguments

    global g_outboxDir
    g_outboxDir = os.path.expanduser("~/asr/outbox") # todo: let this be overridable by some config file

    global g_inboxDir
    g_inboxDir = os.path.expanduser("~/asr/inbox") # todo: let this be overridable by some config file

    if args.action == "send":
        actionSend()

    elif args.action == "receive":
        actionReceive()

    elif args.action == "unpack-only":
        print("unpack-only")
        print("--packagefile: {0}".format(args.packagefile))
        # g_senderId must be defined (todo: set unknownSender by default)
        unpackPackageToInbox(args.packagefile)

    elif args.action == "process-sources-only":
        print("process-sources-only")
        processResultDir = processSources()
        print("--------------------")
        print("processResultDir: {0}".format(processResultDir))
        print("--------------------")

    else:
        print("UNKNOWN OR EMPTY --action value")
        exit(1)


def tests():
    # https://pythonhosted.org/guidata/examples.html#basic-example
    # from guidata import tests
    # tests.run()

    #import webbrowser
    # url = " mailto:abc@gmx.de"
    # webbrowser.open(url,new=1)
    print("nothing")


#
# run main
#
if __name__ == '__main__':
    main()
    # tests()
