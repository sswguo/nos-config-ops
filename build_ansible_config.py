#!/usr/bin/python

import os
import subprocess

# subprocess.call('ansible-vault encrypt_string --vault-password-file /Users/wguo/.nos/ansible_vault_password "12345"', shell=True)

# ~/GitRepo/nos-ansible-playbooks/playbooks/newcastle/vaults/indy-master/

# Encrypt the credentials via ansible vault

## ansible-vault encrypt --vault-password-file ~/.nos/ansible_vault_password <files>

# - brew secrets
# - keycloak secrets

list_dir = [ "etc/brew/", "etc/keycloak/"  ]

## for several special files, need to encoded by base64 first 

## base64 data.txt > data.b64

# - kafka secrets
# - proxy secrets

list_dir_2 = ["etc/kafka/", "etc/proxy/"]


def vault():
  print "##### Ansible Vault ######"
  for d in list_dir:
    print d
    # TODO    

def b64_and_vault():
  print "##### Base64 and Ansible Vault ######"
  for d in list_dir_2:
    print d
    # TODO

def main():
  vault()
  b64_and_vault()
  

if __name__ == "__main__":
  main()
