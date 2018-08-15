#!/usr/bin/env python
"""Create temp_urls for files in a Cloud Files Container"""


# -*- coding: utf-8 -*-
from __future__ import print_function
import os
#import time
#import requests
import pyrax
#import pyrax.exceptions as exc

########################################################
# This script uses a config file for credential storage:
# [rackspace_cloud]
# username = username
# api_key = LOLnopeLOL
########################################################

#cf_ord = pyrax.connect_to_cloudfiles("ORD")
#cf.list_containers()
#cf.get_container("DoubleTake")
#cont.get_objects()
pyrax.set_setting("identity_type", "rackspace")
CREDS_FILE = os.path.expanduser("~/.rax_creds")
pyrax.set_credential_file(CREDS_FILE)
CF = pyrax.cloudfiles
CONT_NAME = 'DoubleTake'
ONAME = 'doubletake_8.1.1.808.0-Linux.zip'
CF.set_temp_url_key()
CONT = CF.get_container("DoubleTake")
OBJ = CONT.get_object('doubletake_8.1.1.808.0-Linux.zip')
TEMP_URL = OBJ.get_temp_url(seconds=6000)
print(TEMP_URL)
