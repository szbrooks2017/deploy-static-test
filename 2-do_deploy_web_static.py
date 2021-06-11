#!/usr/bin/env bash
""" compressing fabric"""
from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ['35.231.1.112', '54.167.91.234']

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    try:
        archiveName = archive_path[9:]
        archiveNameWithoutExtention = archiveName[:-4]
        put(archive_path, '/tmp/' + archiveName)
        run("tar -xzvf /tmp/" + archiveName + " -C " + "/data/web_static/releases/" + archiveNameWithoutExtention + " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("ln -sf /data/web_static/releases/" + archiveNameWithoutExtention + " /data/web_static/current")
        return True
    except:
        return False

def do_pack():
    try:
        now = datetime.now()
        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        tarArchivePath = "versions/" + tarArchiveName
        local("sudo mkdir -p versions")
        local("tar -czvf " + tarArchivePath + " web_static")
        return tarArchivePath
    except:
        return None
