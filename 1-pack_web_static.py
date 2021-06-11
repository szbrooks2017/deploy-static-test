#!/usr/bin/env bash
""" compressing fabric"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """pack up our web_static"""
    now = datetime.now()
    tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    tarArchivePath = "versions/" + tarArchiveName

    local("sudo mkdir -p versions")
    local("tar -czvf " + tarArchivePath + " web_static")
