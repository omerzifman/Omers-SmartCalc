from logics import solve

def test_simple1():
    assert solve("3$$2")
def test_simple2():
    assert solve("3$")
def test_simple3():
    assert solve("#2")
def test_simple4():
    assert solve("0-")
def test_simple5():
    assert solve("3/0")

def test_gibrish():
    assert solve("gfiodhg5e8htbsufionb")

def test_empty():
    assert solve("")

def test_white():
    assert solve("   ")

def test_1():
    assert solve("1+2") == str("3.0")
def test_2():
    assert solve("1-2") == str("-1.0")
def test_3():
    assert solve("1*2") == str("2.0")
def test_4():
    assert solve("1/2") == str("0.5")
def test_5():
    assert solve("2^0") == str("1.0")
def test_6():
    assert solve("4%3") == str("1.0")
def test_7():
    assert solve("2^0") == str("1.0")
def test_8():
    assert solve("2^0") == str("1.0")
def test_9():
    assert solve("4%2") == str("0.0")
def test_10():
    assert solve("2$3.3") == str("3.3")
def test_11():
    assert solve("2&3.3") == str("2.0")
def test_12():
    assert solve("2@0") == str("1.0")
def test_13():
    assert solve("~5.8") == str("-5.8")
def test_14():
    assert solve("5!") == str("120")
def test_15():
    assert solve("21#") == str("3")

def test_comp_1():
    assert solve("(3-5)*2+2^3/5+5--4!-1") == str("25.6")
def test_comp_2():
    assert solve(".5$3&1*2-(6%5*2)/2---3") == str("-2.0")
def test_comp_3():
    assert solve(".5^2--3/(3&0.5-1)  + 2.") == str("-3.75")
def test_comp_4():
    assert solve("  - 4 + 4 % 2 - - - - (5*7)") == str("31.0")
def test_comp_5():
    assert solve("21# @ (2---2) -- 2+-1/.2") == str("-1.5")
def test_comp_6():
    assert solve("(-5) + (--5) ^ 4 -1---2----3") == str("620.0")
def test_comp_7():
    assert solve("(2 +~-----------3)/.44") == str("11.363636363636363")
def test_comp_8():
    assert solve("12340#! / (25*4)^3") == str("3.6288")
def test_comp_9():
    assert solve("1!@2#+3$4^5 -- 1*~21#") == str("1022.5")
def test_comp_10():
    assert solve("3+~-3 - 3+~-3 --5&6*5") == str("25.0")
def test_comp_11():
    assert solve("10%4^2#-4 - ( 5$4)^3") == str("-125.0")
def test_comp_12():
    assert solve("10/9/8^2&1+3!+12345/54321") == str("6.366149064511577")
def test_comp_13():
    assert solve("123456789#^0.5 - 3* ( --- 3)") == str("15.70820393249937")
def test_comp_14():
    assert solve("2%1+1+2-3*4/5^6&7+8$9") == str("11.999232")
def test_comp_15():
    assert solve("8!@189*0.00 0 5 + .3") == str("10.42725")
def test_comp_16():
    assert solve("--~- -- --    --(-5)") == str("-5.0")
def test_comp_17():
    assert solve("1$2$3$4&-3*(123# -2)") == str("-12.0")
def test_comp_18():
    assert solve("12@3+0.001^.01 * 3%2") == str("8.43325430079699")
def test_comp_19():
    assert solve("(31$2^2+.2-3.) - (33.33/3)") == str("947.09")
def test_comp_20():
    assert solve("1---054-44^312#+555&1") == str("-7256313908.0")

# pytest test.py
