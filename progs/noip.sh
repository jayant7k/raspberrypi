#! /bin/sh
### BEGIN INIT INFO
# Provides:          noip
# Required-Start:    $all
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Manage my noip client
### END INIT INFO
# . /etc/rc.d/init.d/functions	# uncomment/modify for your killproc
case "$1" in
    start)
	echo "Starting noip2."
	/usr/local/bin/noip2
    ;;
    stop)
	echo -n "Shutting down noip2."
	killproc -TERM /usr/local/bin/noip2
    ;;
    *)
	echo "Usage: $0 {start|stop}"
	exit 1
esac
exit 0
