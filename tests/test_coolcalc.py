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
