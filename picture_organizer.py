#!/usr/local/bin/python

import shutil
import os
import sys
import IPython as ipy
from datetime import datetime

#TODO
#Deal with photo booth library
#Add Configuration File or command-line arguments to edit final directory
#Preserve .JPG and .MOV

# Traverse the file directory tree and copy all the files into one folder, renaming them something conventional.

ignore = ['.DS_Store', 'Master.apmaster', 'Version-0.apversion', 'Version-1.apversion']

basedir = '/Users/shane/Pictures/'

finaldir = '/Users/shane/Documents/myphotos/'

if not os.path.exists(finaldir):
	print "Can't find directory %s" % finaldir + ". Creating it for you."
	os.makedirs(finaldir)

i = 0

for root,dirs,files in os.walk(basedir):
	for fname in files:
		if fname in ignore:
			continue
		i = i + 1
		mod_time = datetime.fromtimestamp(
	        os.stat(root+'/'+fname)[8]
	    ).strftime('%Y-%m-%d %H:%M:%S')
		shutil.copy2(root+'/'+fname, finaldir+mod_time)

print i, "pictures processed."