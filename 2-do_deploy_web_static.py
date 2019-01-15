#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy:
"""

from fabric.api import *
env.hosts = ['35.196.154.244', '35.227.97.207']


def do_deploy(archive_path):
    """ Script that does a lot of magic =) like penn and teller """
    if (archive_path is False or archive_path is None):
        return False
    try:
        # this will be the web_static_NUMBERSSSS.tgz
        last = archive_path.split("/")[-1]
        # and this will be the stuff without the dot extension
        foldName = "/data/web_static/releases/" + last.split(".")[0]
        
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(foldName))
        run("sudo tar -xzf /tmp/{} -C {}".format(last, foldName))
        run("sudo rm /tmp/{}".format(last))
        run("sudo mv {}/web_static/* {}/".format(foldName, foldName))
        run("sudo rm -rf {}/web_static".format(foldName))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(foldName))
    except:
        return False
    return True
