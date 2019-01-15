#!/usr/bin/python3
""" This script makes a tgz archive from the contents of web_static
folder of the cloned repo using do_pack
It will make a directory named versions if not exists
Then it will create, zip, files, verbose the files to be zipped.
We then return this zipperino bad boi unless it fails. then NONE
"""
from fabric.api import *
from time import strftime
env.hosts = ['35.196.154.244', '35.227.97.207']


def do_pack():
    """ function that does all the the stated above """
    temp = strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static/".
              format(temp))
    except:
        return None
    return ("versions/web_static_{}.tgz".format(temp))


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

def deploy():
    """ Packs and deploys. This is with no args or kwargs. """
    f = do_pack()
    return do_deploy(f) if f else False
