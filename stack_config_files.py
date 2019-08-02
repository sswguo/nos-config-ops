#!/usr/bin/python

import sys
import os

# argv[1]:  ~/GitRepo/nos-ansible-playbooks/roles/indy/files/indy-devel-master/

# Config structure
#
# |-- main.conf
# |-- conf.d
# |   |-- README.txt
# |   |-- brew.conf
# |   |-- content-browse.conf
# |   |-- depgraph.conf
# |   |-- environment.conf
# |   |-- httprox.conf

conf_dir = sys.argv[1] + "/etc/"
sub_conf_dir = "conf.d/"

with_comment = 1

def output_line(line):
  if not with_comment and not line.startswith("#"):
    print line.strip()
  elif with_comment:
    print line.strip()

def handle_line(line, skip_empty_line=0):
  line = line.strip()
  if skip_empty_line:
    if line:
      output_line(line)
  else:
    output_line(line)

def read_main_conf():
  fo = open(conf_dir + "main.conf", "r")
  lines = fo.readlines()
  for line in lines:
    handle_line(line);
  print ""


def read_sub_conf():
  for f in os.listdir(conf_dir + sub_conf_dir):
    if f.endswith(".conf"):
    
      print "# ../indy/etc/conf.d/" + f
      print "------------"
      print ""
    
      fo = open(conf_dir + sub_conf_dir + f, "r")
      lines = fo.readlines()
      for line in lines:
        handle_line(line, 1)
      print ""
    
      fo.close()

def main():
  read_main_conf()
  read_sub_conf()

if __name__ == "__main__":
  main()

