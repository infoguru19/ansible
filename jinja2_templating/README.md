Jinja2 Templating
=========================
Ref: https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html
     https://jinja.palletsprojects.com/en/stable/templates/

Templating: It is the process of generating dynamic content of expression.
Example: I am from India. Here India is a variable and we can replace with country.
         
         I am from {{ country }}  {{ .... }} ==> It is jinja2
         I am from {{ country | upper }} ==> To convert in upper case
         I am from {{ country | lower }} ==> To convert in lower case
      These upper, lower are called filters.
Default value.
  I am from {{ country | default("India") }} ==> To convert in lower case

Filters: LIST and SET

  {{ [1,2,3] | min }} ==> 1
  {{ [1,2,3] | max }}  ==> 3

  {{ [1,2,3,2] | unique }}  ==> 1,2,3,4

  {{ [1,2,3,4] | union( [4,5]) }}  ==> 1,2,3,4,5
  {{ [1,2,3,4] | intersect( [4,5]) }} ==> 4

  {{ 100 | random }}  ==> Random Number
  
  {{ ["I", "am", "from", "India"] | join(" ") }} ==> I am from India

fiter: FILE
{{ "/etc/hosts" | basename }} ==> hosts
  


