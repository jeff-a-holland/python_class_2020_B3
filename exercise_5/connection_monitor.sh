#!/bin/bash

# Script to monitor network connections while client and server are running
echo ''
echo '------------------------------------------------------------------------------'
while [ : ]
  do netstat -an | egrep '9999|^Proto Recv-Q Send-Q  Local Address'
     echo '------------------------------------------------------------------------------'
     sleep 10
done
