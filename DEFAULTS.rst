
Zabbix Server ansible role default variables
============================================

.. contents:: Sections
   :local:

Zabbix docker management
------------------------

.. envvar:: zabbix_server_docker_image

Zabbix Server docker image
::

  zabbix_server_docker_image: zabbix/zabbix-server-pgsql



.. envvar:: zabbis_server_version

Zabbix Server docker image version (TAG)
::

  zabbis_server_version: ubuntu-latest


.. envvar:: zabbix_server_docker_labels

Yaml dictionary which maps Docker labels.
os_environment: Name of the environment, example: Production, by default "default".
os_contianer_type: Type of the container, by default zabbix_server.
::

  zabbix_server_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: zabbix_server




.. envvar:: zabbix_frontend_docker_image

Zabbix Frontend docker image
::

  zabbix_frontend_docker_image: zabbix/zabbix-web-nginx-pgsql



.. envvar:: zabbis_frontend_version

Redis docker image version (TAG)
::

  zabbis_frontend_version: ubuntu-latest


.. envvar:: zabbix_frontend_docker_labels

Yaml dictionary which maps Docker labels.
os_environment: Name of the environment, example: Production, by default "default".
os_contianer_type: Type of the container, by default zabbix_frontend.
::

  zabbix_frontend_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: zabbix_frontend





.. envvar:: postgres_docker_image

postgres docker image
::

  postgres_docker_image: postgres



.. envvar:: postgres_version

Postgres docker image version (TAG)
::

  postgres_version: latest


.. envvar:: postgres_docker_labels

Yaml dictionary which maps Docker labels.
os_environment: Name of the environment, example: Production, by default "default".
os_contianer_type: Type of the container, by default postgres.
::

  postgres_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: postgres




Postgres management
-------------------

.. envvar:: postgres_zabbix_user

Postgresql database user for zabbix
::

  postgres_zabbix_user: zabbix



.. envvar:: postgres_zabbix_password

Postgresql password for zabbix user
::

  postgres_zabbix_password: my_password



Zabbix managment
----------------

.. envvar: postgres_host

Potsgresql server host
::

  postgres_host: localhost



.. envvar: zabbix_server_host

Zabbix server host, used by zabbix-frontend
::

  zabbix_server_host: localhost



..envvar: zabbix_frontend_timezone

Timezone used by Zabbix Frontend
::

  zabbix_frontend_timezone: Europe/Madrid
