Lookups
=================

Ref: https://docs.ansible.com/ansible/2.9/user_guide/playbooks_lookups.html

1. let assume we need credential sto access our servers.
2. We have too many server and credentials store not in inventory file but else where in different file format.

To solve this, we have ansible lookup plugin.

CSV File: credentials.csv 
    Hostname, Password
    target1, Passw0rd
    target2, Passw@rd

    {{ lookup('csvfile', 'target1 file=/tmp/credentials.csv delimeter=,') }}  ==> Passw0rd
    {{ lookup('csvfile', 'target2 file=/tmp/credentials.csv delimeter=,') }}  ==> Passw@rd

There are few other lookups plugin.
  1. INI
  2. DNS
  3. MongoDB




