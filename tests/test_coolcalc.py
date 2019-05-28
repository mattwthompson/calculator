from calculator import CoolCalc


def test_add():
    coolcalc = CoolCalc()
    a = 1
    b = 1
    mysum = coolcalc.add_a_b(a, b)
    assert mysum == 2

def test_multiply():
    coolcalc = CoolCalc()
    a = 1
    b = 1
    myproduct = coolcalc.multiply_a_b(a, b)
    assert myproduct == 1

def test_power():
    coolcalc = CoolCalc()
    a = 2
    b = 3
    mypower = coolcalc.power_a_b(a, b)
    assert mypower == 8

def test_div():
    coolcalc = CoolCalc()
    a = 8
    b = 2
    mydiv = coolcalc.divide_a_b(a, b)
    assert mydiv == 4
