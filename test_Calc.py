from Calc import Calc
import yaml
import pytest


def getData(name, type):
    with open('./data.yml') as f:
        allDatas = yaml.safe_load(f)
    datas = allDatas[name][type]['datas']
    ids = allDatas[name][type]['ids']
    print(datas)
    print(ids)
    return (datas, ids)


class TestCalc:
    add_int_data = getData('add', 'int')
    add_float_data = getData('add', 'float')
    div_int_data = getData('div', 'int')
    div_float_data = getData('div', 'float')
    div_zero_data = getData('div', 'zero')

    def setup(self):
        print('开始计算')
        self.calc = Calc()

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize("a,b,result", add_int_data[0], ids=add_int_data[1])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, a, b, result):
        assert result == round(self.calc.add(a, b), 10)

    @pytest.mark.parametrize("a,b,result", div_int_data[0], ids=div_int_data[1])
    def test_div(self, a, b, result):
        assert result == self.calc.div(a, b)

    @pytest.mark.parametrize("a,b,result", div_zero_data[0], ids=div_zero_data[1])
    def test_div_zero(self, a, b, result):
        with pytest.raises(ZeroDivisionError):
            assert result == self.calc.div(a, b)

    @pytest.mark.parametrize("a,b,result", div_float_data[0], ids=div_float_data[1])
    def test_div_float(self, a, b, result):
        assert result == round(self.calc.div(a, b), 10)
