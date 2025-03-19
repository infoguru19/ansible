Custom Plugin
================
Ref: https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html
Ref: https://github.com/ansible/ansible/tree/devel/lib/ansible/plugins
We need custom plugin when we need to perform some specific task and existing plugin not fit to this like average of numbers.

Average Plugins
==================

![image](https://github.com/user-attachments/assets/55c35f1d-34d1-47d5-bbeb-f8c62c6e5802)

Callback Plugin
=================
Callback plugin is another type of plugin. The output we will see after execution of playbook that's because of callback plugin.

Default Ouput is called Skippy.
We can change callback plugin to Json istead of text format.
  export ANSIBLE_STDOUT_CALLBACK=json; ansible-playbook playbook.yml

![image](https://github.com/user-attachments/assets/7c7f297b-2f37-4cd3-ae23-651ab76b0022)




