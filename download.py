import os
import pycurl
import certifi
import sys


def progress(total, existing, upload_t, upload_d):
    existing = existing + os.path.getsize(filename)
    try:
        frac = float(existing)/float(total)
    except:
        frac = 0
    sys.stdout.write("\r%s %3i%%" % ("File downloaded - ", frac*100))

url = input('Enter URL to download folder/file: ')
filename = url.split("/")[-1].strip()


def test(debug_type, debug_msg):
    print("debug(%d): %s" % (debug_type, debug_msg))

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(c.CAINFO, certifi.where())
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.setopt(pycurl.MAXREDIRS, 5)

# Setup writing
if os.path.exists(filename):
    f = open(filename, "ab")
    c.setopt(pycurl.RESUME_FROM, os.path.getsize(filename))
else:
    f = open(filename, "wb")

c.setopt(pycurl.WRITEDATA, f)

#c.setopt(pycurl.VERBOSE, 1) 
c.setopt(pycurl.DEBUGFUNCTION, test)
c.setopt(pycurl.NOPROGRESS, 0)
c.setopt(pycurl.PROGRESSFUNCTION, progress)
try:
    c.perform()
except:
    pass
