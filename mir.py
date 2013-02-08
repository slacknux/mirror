#!/usr/bin/env python

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# guelfoweb@gmail.com wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Gianni 'guelfoweb' Amato
# Improved by slacknux
# ----------------------------------------------------------------------------

import sys, os

def help(code):
	if code:
		print "File not found:", ifile
		sys.exit()
	print "mir v1.0 - Reverses the bytes of a file"
	print "Author: Gianni 'guelfoweb' Amato"
	print "\nUSAGE:"
	print "\tmir [FROM FILE] [TO FILE]"
	sys.exit()

# Arguments
if len(sys.argv) != 3:
	help(0)

ifile  = sys.argv[1]
ofile = sys.argv[2]

# File not exist
if not os.path.isfile(ifile):
	help(1)
	
fs = os.stat(ifile).st_size 
sz = 8192

print "Reversing", fs, "bytes..."

i = open(ifile, 'rb')
o = open(ofile, 'w+b')

while fs:
	fs -= sz
	if fs < 0:
		sz += fs
		fs = 0
	i.seek(fs)
	o.write(i.read(sz)[::-1])

o.close()
i.close()
print "\033[1A\033[0KDone!"
