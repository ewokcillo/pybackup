#!/usr/bin/env python
import os
import time
from ConfigParser import SafeConfigParser
import tarfile

#This script is based on:
#http://codepoets.co.uk/2010/python-script-to-backup-mysql-databases-on-debian/
#http://stackoverflow.com/questions/5849999/how-to-make-tar-backup-using-python


config = SafeConfigParser()
config.read("pybackup.cnf")
username = config.get('mysql', 'user')
password = config.get('mysql', 'password')
hostname = config.get('mysql', 'host')

web_dir = config.get('webs', 'web_dir')
backup_dir = config.get('webs', 'backup_dir')
webs_dirs = [ name for name in os.listdir(web_dir) if os.path.isdir(os.path.join(web_dir, name)) ]

filestamp = time.strftime('%Y-%m-%d')

for web in webs_dirs:
    full_dir = os.path.join(home, directory)
    tar = tarfile.open(os.path.join(backup_dir, directory+'.tar.gz'), 'w:gz')
    tar.add(full_dir)
    tar.close()

database_list_command="mysql -u %s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
for database in os.popen(database_list_command).readlines():
    database = database.strip()
    if database == 'information_schema':
        continue
    if database == 'performance_schema':
        continue
    filename = backup_dir + "%s-%s.sql" % (database, filestamp)
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c &gt; %s.gz" % (username, password, hostname, database, filename))</pre>
