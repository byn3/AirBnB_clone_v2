#!/usr/bin/python3
""" This script makes a tgz archive from the contents of web_static
folder of the cloned repo using do_pack
It will make a directory named versions if not exists
Then it will create, zip, files, verbose the files to be zipped.
We then return this zipperino bad boi unless it fails. then NONE
"""

# if __name__ == "__main__":
from fabric.api import *
from time import strftime
# import tarfile

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
