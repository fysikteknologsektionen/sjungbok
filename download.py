#!/usr/bin/env python
import os,sys,urllib2
f = open(os.path.basename ("master2.tar.gz"), 'w')
f.write(urllib.urlopen(sys.argv[1]).read())
f.close()