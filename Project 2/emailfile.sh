#!/bin/bash
cd /usr/local/bin/testdir
mostrecentfile=$(ls -t /usr/local/bin/testdir | head -1)
echo "here is the most recent file [${mostrecentfile}]" | mailx -s "New file detected" -a "$mostrecentfile" youremail@gmail.com
