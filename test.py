# app.py
# This is a test commit
#This is another test commit added 
def add(a, b):
    print(`{a} and {b }`)
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    print("Hello Tests are executed")
