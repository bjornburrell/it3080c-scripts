inotifywait -m /tmp/test -e create -e moved_to |
    while read path action file; do
        newestFile = ls -Art | tail -n 1
    	python /Users/bjornburrell/it3080c-scripts/Project 2/emailfile.py newestFile 
    done