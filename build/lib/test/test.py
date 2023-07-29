from valipy.myFunctions import Valipy, InputValidationException
from valipy.exceptions import InputIsNegativeException, InputIsPositiveException

def test_valipy():
    assert Valipy(22).isInt().isEven().isPositive().validate() == False

x = Valipy('test text 22').isType(str).isMinLength(5).itHasSpaces().itIncludesNumbers().validate()
print(x)


