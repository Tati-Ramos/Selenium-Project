import pytest

class TesteSimulação:
    @pytest.mark.simulation
    def test_simulation_1(self):
        assert 1 == 1
    @pytest.mark.simulation
    @pytest.mark.skip #vai pular o teste
    def test_simulation_2(self):
        assert 2 == 2
