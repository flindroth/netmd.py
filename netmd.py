#!/usr/bin/python2

from libnetmd.download import download
from optparse import OptionParser
parser = OptionParser()
parser.add_option('-b', '--bus')
parser.add_option('-d', '--device')
parser.add_option('-f', '--filename')
parser.add_option('-F', '--format')
parser.add_option('-t', '--title')
(options, args) = parser.parse_args()
assert len(args) < 4
filename=options.filename
informat=options.format

WF_PCM = 0
WF_105KBPS = 0x90
WF_LP2 = 0x94
WF_LP4 = 0xA8


wireformat = WF_PCM

if informat == '' or informat == 'PCM' or informat == 'SP':
	wireformat = WF_PCM

if informat == 'LP2':
    wireformat = WF_LP2

if options.title != None:
    title=options.title
else:
    title=''

download(filename,title,wireformat)
	




