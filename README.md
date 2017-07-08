Welcome to Redis Ansible Role’s documentation!
==============================================

Role Name
---------

This role install a zabbix environment running on containers. It create
three containers:

-   Postgresql
-   Zabbix-server
-   Zabbix-frontend (apache)

This role is mainly used by CI to test the monitoring of the components.

### Requirements

N/A

### Dependencies

-   repos
-   docker

### Example Playbook

Including an example of how to use your role (for instance, with
variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - role: username.rolename, x: 42 }

Zabbix Server ansible role default variables
--------------------------------------------

#### Sections

-   Zabbix docker management
-   Postgres management
-   Zabbix managment

### Zabbix docker management

`zabbix_server_docker_image`

Zabbix Server docker image

    zabbix_server_docker_image: zabbix/zabbix-server-pgsql

`zabbis_server_version`

Zabbix Server docker image version (TAG)

    zabbis_server_version: ubuntu-latest

`zabbix_server_docker_labels`

Yaml dictionary which maps Docker labels. os\_environment: Name of the
environment, example: Production, by default “default”.
os\_contianer\_type: Type of the container, by default zabbix\_server.

    zabbix_server_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: zabbix_server

`zabbix_frontend_docker_image`

Zabbix Frontend docker image

    zabbix_frontend_docker_image: zabbix/zabbix-web-nginx-pgsql

`zabbis_frontend_version`

Redis docker image version (TAG)

    zabbis_frontend_version: ubuntu-latest

`zabbix_frontend_docker_labels`

Yaml dictionary which maps Docker labels. os\_environment: Name of the
environment, example: Production, by default “default”.
os\_contianer\_type: Type of the container, by default zabbix\_frontend.

    zabbix_frontend_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: zabbix_frontend

`postgres_docker_image`

postgres docker image

    postgres_docker_image: postgres

`postgres_version`

Postgres docker image version (TAG)

    postgres_version: latest

`postgres_docker_labels`

Yaml dictionary which maps Docker labels. os\_environment: Name of the
environment, example: Production, by default “default”.
os\_contianer\_type: Type of the container, by default postgres.

    postgres_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: postgres

### Postgres management

`postgres_zabbix_user`

Postgresql database user for zabbix

    postgres_zabbix_user: zabbix

`postgres_zabbix_password`

Postgresql password for zabbix user

    postgres_zabbix_password: my_password

### Zabbix managment

Potsgresql server host

    postgres_host: localhost

Zabbix server host, used by zabbix-frontend

    zabbix_server_host: localhost

..envvar: zabbix\_frontend\_timezone

Timezone used by Zabbix Frontend

    zabbix_frontend_timezone: Europe/Madrid

Changelog
---------

**zabbix-server-docker**

This project adheres to Semantic Versioning and human-readable
changelog.

### zabbix-server-docker master - unreleased

##### Added

-   Create postgresq contaianer
-   Create zabbix-server container
-   Create zabbix-frontend container

##### Changed

-   First change

### zabbix-server-docker v0.0.0 - DATE

##### Added

-   Initial version

Copyright
---------

zabbix-server-docker

Copyright (C) DATE User/Company &lt;<email@email.com>&gt;

LICENSE
