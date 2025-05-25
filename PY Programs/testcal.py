from calculato import square
def main():
    testSqu()
def testSqu():
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(0)==0