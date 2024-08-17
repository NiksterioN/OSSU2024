#!/bin/bash

# Calls ./some_script.sh until a failure condition, and prints how many calls are done
# Requires the proper permissions for the ./some_script.sh

log_file="test.log"
call_num=1;

./some_script.sh>$log_file 

while [[ $? -ne 1 ]]; do
	call_num=$(($call_num + 1))
	./some_script.sh>>$log_file 
done

echo "Total Number of Script Calls to failure: $call_num">>$log_file


