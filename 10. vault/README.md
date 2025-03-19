Vault
====================
Ref: https://docs.ansible.com/ansible/2.8/user_guide/vault.html
1. Ansible vault is use to store data in encrypted format.
2. There are multiple way to use ansible vault.
    Example: To store encrypt password.

To encrypt file
  ansible-vault encrypt inventory.yml

 ansible-playbook -i inventory.yml playbook.yml
  Give an Error: ...Decryption failed

 ansible-playbook -i inventory.yml playbook.yml -ask-vault-pass
 Vault Password: ==> Same password use while encrypting the file.

To Pass Vault Password through file
 ansible-playbook -i inventory.yml playbook.yml -vault-password-file ./tmp/vault_pwd.py

To view the content of file
 ansible-vault view inventory.yml

To Create the vault of file
 ansible-vault create inventory.yml




