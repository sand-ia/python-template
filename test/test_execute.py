from src.application.service.service import Service


def test_execute_success():
    service: Service = Service()
    assert service.execute() == 9


def test_execute_fail():
    service: Service = Service()
    assert service.execute() != 8
