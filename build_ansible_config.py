#!/usr/bin/python

import os
import subprocess
import sys
import shutil
import pipes

# pro_dir = "/Users/wguo/GitRepo/pnc-indy-etc/indy/upshift/newcastle-devel/indy-master/"

try:
  pro_dir = sys.argv[1]
except IndexError as e:
  print "Please specify the target etc dir."
  sys.exit(e)

# Default true
Dryrun = 1

try:
  Dryrun = sys.argv[2]
except IndexError:
  print "Use default setting: Dryrun is enabled."

print "Dryrun: " + Dryrun

# ~/GitRepo/nos-ansible-playbooks/playbooks/newcastle/vaults/indy-master/

vault_password_file = "~/.nos/ansible_vault_password"

work_dir = "/tmp/wd/"

# Encrypt the credentials via ansible vault

## ansible-vault encrypt --vault-password-file ~/.nos/ansible_vault_password <files>

# - brew secrets
# - keycloak secrets

# - NOTE: remove brew secrets, since we have the root ca installed in the base image
# "etc/brew/"
list_dir = [ "etc/keycloak/"  ]

## for several special files, need to encoded by base64 first 

## base64 data.txt > data.b64

# - kafka secrets
# - proxy secrets

# comment out etc/kafka TODO
list_dir_2 = ["etc/proxy/"]

def run(cmd):
  print cmd
  if Dryrun == "0":
    print ">>"
    subprocess.call(cmd, shell=True)
    print "<<"

# Encrypt the credentials via ansible vault 
# 
# ansible-vault encrypt --vault-password-file ~/.nos/ansible_vault_password <files>
#
def vault():
  print "##### Ansible Vault ######"
  for d in list_dir:
    print d
    print "-------------"
    for file in os.listdir(work_dir + d):
      print file
      cmd = 'ansible-vault encrypt --vault-password-file {} {}'.format(vault_password_file, pipes.quote(work_dir + d + file))
      run(cmd)
      print ""
  print ""    


# for several special files like keystore/truststores, need to encoded by base64 first
#
# base64 data.txt > data.b64
#
def b64_and_vault():
  print "##### Base64 and Ansible Vault ######"
  for d in list_dir_2:
    print d
    print "-------------"
    for file in os.listdir(work_dir + d):
      print file
      cmd = 'base64 {} > {}'.format(pipes.quote(work_dir + d + file), pipes.quote(work_dir + d + file+'.b64'))
      run(cmd) 
      cmd = 'ansible-vault encrypt --vault-password-file {} {}'.format(vault_password_file, pipes.quote(work_dir + d + file+'.b64'))
      run(cmd)
      print ""
  print ""

def prepare():
  shutil.rmtree(work_dir)
  shutil.copytree(pro_dir, work_dir)
  for file in os.listdir(work_dir):
    print file

  print ""

def main():
  prepare()
  vault()
  b64_and_vault()
  

if __name__ == "__main__":
  main()
