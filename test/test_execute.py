from src.application.service.service import Service


def test_execute_():
    service: Service = Service()
    assert service.execute() == 9


def test_execute():
    service: Service = Service()
    assert service.execute() != 8
