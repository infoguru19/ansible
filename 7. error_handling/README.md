Error Handling
=====================

The Default Behavior of Ansible Error Handliing.
 1. For Single host: If any task failed then it stop further execution.
 2. For Multiple hosts: If any task failed in one server then it stop further execution on this server. But continue on other servers as many as can complete.
   To avoid this, we use " any_errors_fatal: true "

   ![image](https://github.com/user-attachments/assets/b46f14e5-a586-48b7-b752-2bdc780186fa)

To ignore error for non-critical task: " ignore_errors: yes "

![image](https://github.com/user-attachments/assets/75dcbd7f-d06b-4104-8dcc-68a3f3004991)

Failed the task based on condition: 
  failed_when : " 'Error' in command_output.stdout "

  ![image](https://github.com/user-attachments/assets/b5a1cc56-187b-40a4-80c0-ba1e47010df2)

