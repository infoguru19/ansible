Error Handling
=====================

The Default Behavior of Ansible Error Handliing.
 1. For Single host: If any task failed then it stop further execution.
 2. For Multiple hosts: If any task failed in one server then it stop further execution on this server. But continue on other servers as many as can complete.
   To avoid this, we use " any_errors_fatal: true " 

To ignore error for non-critical task: " ignore_errors: yes "
Failed the task based on condition: 
  failed_when : " 'Error' in command_output.stdout "
