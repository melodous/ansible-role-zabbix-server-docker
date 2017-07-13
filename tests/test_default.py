def test_zabbix_frontend_running_and_enabled(Command, Service):
    # Check that zabbix-frontend service is running and enabled
    zabbix_frontend_service = Service("zabbix-frontend")
    assert zabbix_frontend_service.is_running
    assert zabbix_frontend_service.is_enabled


def test_zabbix_server_running_and_enabled(Command, Service):
    # Check that zabbix-server service is running and enabled
    zabbix_server_service = Service("zabbix-server")
    assert zabbix_server_service.is_running
    assert zabbix_server_service.is_enabled


def test_postgres_server_running_and_enabled(Command, Service):
    # Check that postgres service is running and enabled
    postgres_service = Service("postgres")
    assert postgres_service.is_running
    assert postgres_service.is_enabled
