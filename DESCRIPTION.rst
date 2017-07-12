Zabbix Server Docker
====================

This role install a zabbix environment running on containers. It create three containers:

- Postgresql
- Zabbix-server
- Zabbix-frontend (apache)

This role is mainly used by CI to test the monitoring of the components.

Requirements
------------

Docker engine configure and running.

Dependencies
------------

- repos
- docker

Example Playbook
----------------

.. code::

  - hosts: servers
    roles:
      - role: zabbix-server-docker
