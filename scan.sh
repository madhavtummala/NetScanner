IP=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')
IP=$(echo $IP | cut -d"." -f1-3)
fping -a -q -t50 -r1 -g $IP".1/24"
