Ansible establish connection through ssh to target server to perform task.
This means ssh connection alive though out the execution of the tasks.
If we have a long running tasks which exceed the ssh timeout or may be connection broken b/w master.

" To solve this we have Asynchronous action " 

Asynchronous Action
==========================
1. Run a process and check on it later
2. Run multiple process at once and check them later
3. Run processes and forget

All of these can achived using Asynchronous Actions

async: 360   # This means, we tell ansible this is an Asynchronous tasks and kick it off and check on later after 6 mins.

By default asible check status of script every 10 seconds.
 poll: 60   # To change check after 5 mins 
 poll: 0    # For parallel Execution two or more tasks

Note: All Modules do not support async.

