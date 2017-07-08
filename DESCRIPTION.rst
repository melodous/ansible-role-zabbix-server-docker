Role Name
=========

This role install a zabbix environment running on containers. It create three containers:

- Postgresql
- Zabbix-server
- Zabbix-frontend (apache)

This role is mainly used by CI to test the monitoring of the components.

Requirements
------------

N/A

Dependencies
------------

- repos
- docker

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

.. code::

  - hosts: servers
    roles:
      - role: username.rolename, x: 42 }
