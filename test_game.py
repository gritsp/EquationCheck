from main import *
import pytest

def test_login():
     assert login("TESTER") == "TESTER"

@pytest.mark.parametrize("num1,num2,num3,symbol1,symbol2,lv,result", [
    (1,2,3,"+","+","1", 3),
    (1,2,3,"-","+","1", -1),
    (1,2,3,"*","+","1", 2),
    (1,2,3,"/","+","1", 0.5),

    (1,2,3,"+","+","2", 6),
    (1,2,3,"+","-","2", 0),
    (1,2,3,"+","*","2", 9), 
    (1,2,3,"+","/","2", 1), 

    (1,2,3,"-","+","2", 2),
    (1,2,3,"-","-","2", -4),
    (1,2,3,"-","*","2", -3), 
    (1,2,3,"-","/","2", -1/3), 

    (1,2,3,"*","+","2", 1*2+3),
    (1,2,3,"*","-","2", 1*2-3),
    (1,2,3,"*","*","2", 1*2*3),
    (1,2,3,"*","/","2", 1*2/3),

    (1,2,3,"/","+","2", 1/2+3),
    (1,2,3,"/","-","2", 1/2-3),
    (1,2,3,"/","*","2", 1/2*3),
    (1,2,3,"/","/","2", 1/2/3)
])
def test_EquationCreate(num1,num2,num3,symbol1,symbol2,lv,result):
    assert EquationCreate(num1,num2,num3,symbol1,symbol2,lv)==result

@pytest.mark.parametrize("num1,num2,num3,symbol1,symbol2,lv,Equation,result", [
    (1,2,3,"+","+","1",3, 3),
    (1,2,3,"-","+","2",2, 2)
])
def test_answer(num1,num2,num3,symbol1,symbol2,lv,Equation,result):
    assert answer(num1,num2,num3,symbol1,symbol2,lv,Equation) == result

@pytest.mark.parametrize("Equation,answer_show,answer_input,result", [
    (1,1,"T", True),
    (1,2,"F", True),
    (1,2,"T", False),
    (1,1,"F", False)
])
def test_answer_check(Equation,answer_show,answer_input,result):
    assert answer_check(Equation,answer_show,answer_input) == result