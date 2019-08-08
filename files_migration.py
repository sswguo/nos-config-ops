#!/usr/bin/python

import os
import shutil

SOURCE_GIT = '/Users/wguo/GitRepo/pnc-indy-etc'
TARGET_GIT = '/Users/wguo/GitRepo/nos-ansible-playbooks'

FROM_PATH = SOURCE_GIT + '/indy/upshift/newcastle-devel/indy-stable-next/'
TO_PATH = TARGET_GIT + '/roles/indy/files/indy-devel-stable-next/'

CREDENTIAL_PATH = TARGET_GIT + '/playbooks/newcastle/vaults/indy-stable-next/'

if os.path.exists(TO_PATH):
  print "Clear existing content in {}.".format(TO_PATH)
  shutil.rmtree(TO_PATH)

print "Copying from {} to {}".format(FROM_PATH, TO_PATH)
shutil.copytree(FROM_PATH, TO_PATH)

print "Moving credentials from {} to {}".format(TO_PATH, CREDENTIAL_PATH)
if os.path.exists(CREDENTIAL_PATH + 'etc/brew'):
  print 'etc/brew files exists.'
else: 
  shutil.move(TO_PATH + 'etc/brew', CREDENTIAL_PATH + 'etc/brew')

if os.path.exists(CREDENTIAL_PATH + 'etc/proxy'):
  print 'etc/proxy files exists.' 
else:
  shutil.move(TO_PATH + 'etc/proxy', CREDENTIAL_PATH + 'etc/proxy')

if os.path.exists(CREDENTIAL_PATH + 'etc/keycloak'):
  print 'etc/keycloak files exists.'
else:
  shutil.move(TO_PATH + 'etc/keycloak', CREDENTIAL_PATH + 'etc/keycloak')
