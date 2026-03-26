#!/usr/bin/env bash
START_TIME=$(date +%s)

if [ -f "/tmp/ice_breaker.lock" ]; then
	echo "ERROR: SESSION ALREADY ACTIVE."
	exit 1
fi

trap 'rm -f /tmp/ice_breaker.lock; echo " SESSION TERMINATED. UPTIME LOGGED."; exit' SIGINT SIGTERM

echo $BASHPID >/tmp/ice_breaker.lock

echo "ACCESS GRANTED: WELCOME, ${USER^^}."

while true; do
	sleep 60
	echo "SYSTEM UPTIME: $((($(date +%s) - START_TIME) / 60)) MINUTES."
done
