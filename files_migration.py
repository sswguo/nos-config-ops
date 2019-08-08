#!/usr/bin/python

import os
import shutil

SOURCE_GIT = '/Users/wguo/GitRepo/pnc-indy-etc'
TARGET_GIT = '/Users/wguo/GitRepo/nos-ansible-playbooks'

FROM_PATH = SOURCE_GIT + '/indy/upshift/newcastle-devel/indy-stable-next/'
TO_PATH = TARGET_GIT + '/roles/indy/files/indy-devel-stable-next/'

CREDENTIAL_PATH = TARGET_GIT + '/playbooks/newcastle/vaults/indy-stable-next/'

BREW_CONFIG_DIR     = 'etc/brew'
PROXY_CONFIG_DIR    = 'etc/proxy'
KEYCLOAK_CONFIG_DIR = 'etc/keycloak'

if os.path.exists(TO_PATH):
  print "Clear existing content in {}.".format(TO_PATH)
  shutil.rmtree(TO_PATH)

print "Copying from {} to {}".format(FROM_PATH, TO_PATH)
shutil.copytree(FROM_PATH, TO_PATH)

print "Moving credentials from {} to {}".format(TO_PATH, CREDENTIAL_PATH)
if os.path.exists(CREDENTIAL_PATH + BREW_CONFIG_DIR):
  print 'etc/brew files exists.'
else: 
  shutil.move(TO_PATH + BREW_CONFIG_DIR, CREDENTIAL_PATH + BREW_CONFIG_DIR)

if os.path.exists(CREDENTIAL_PATH + PROXY_CONFIG_DIR):
  print 'etc/proxy files exists.' 
else:
  shutil.move(TO_PATH + PROXY_CONFIG_DIR, CREDENTIAL_PATH + PROXY_CONFIG_DIR)

if os.path.exists(CREDENTIAL_PATH + KEYCLOAK_CONFIG_DIR):
  print 'etc/keycloak files exists.'
else:
  shutil.move(TO_PATH + KEYCLOAK_CONFIG_DIR, CREDENTIAL_PATH + KEYCLOAK_CONFIG_DIR)
