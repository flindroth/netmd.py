#!/usr/bin/python2
import sys
import os
from libnetmd.download import download
from optparse import OptionParser
from songutils.id3reader import Reader
from songutils.transcoder import transcode

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
    title=None

if title == None:
    id3r = Reader(filename)
    id3performer = id3r.getValue('performer')
    id3title = id3r.getValue('title')
    if id3title != None and id3performer != None:
        title = "%s - %s" % (id3performer, id3title)
    elif id3title != None and id3performer == None:
        title = id3title
    else:
        title = os.path.basename(filename)

tr_filename = transcode(filename)

if tr_filename == None:
    print "ERROR: Could not transcode source file. ffmpeg is required."
    sys.exit(1)

download(tr_filename,title,wireformat)
	




