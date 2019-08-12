## Scripts

The scripts are used to move our configuration files from pnc-indy-etc into ansible repo,  and meanwhile encode the credentails as required.  

---
### `files_migration.py`
Move the config files from gerrit repo into ansible repo

---
### `build_ansible_config.py`
The script uses the ansible vault to encode the credentials, so the ansible password file is required in place.
It generates the files in a temproray dir /tmp/wd , so need to copy the generated files to the right place.

args[1]: the dir of config that need to be handled  
```
  e.g.: ~/GitRepo/nos-ansible-playbooks/playbooks/newcastle/vaults/indy-master/  
```
args[2]: dryrun, default is True

---
### `stack_config_files.py`
Inline all of conf.d/*.conf in the main.conf


args[1]: the dir of config that need to be handled  
```
  e.g.: ~/GitRepo/pnc-indy-etc/indy/upshift/newcastle-devel/indy-master/
```

