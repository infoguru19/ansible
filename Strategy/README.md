Strategy
====================
Strategy define how a playbook will execute in Ansible.

Type of Strategy
1. Liner (default): Execute tasks one after another in each server. Ex: "strategy: liner"
2. Free: In this each server run of their tasks independently.
3. Batch: It is types of linear strategy but it execute tasks in batch like 5 nodes then another 5 nodes. Ex: "strategy: serial: 5"

How many server ansible communicate at a time ?
  by default 5 servers.
  
Define in, ansible.cfg
  fork = 5

