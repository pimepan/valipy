from valipy import Valipy, InputValidationException, InputIsNumericException, InputIsEqualException, InputIsInBetweenLengthException
personModel = {
    "name": Valipy().isType(str).isInBetweenLength(3, 20),
    "age": Valipy().isType(int).isInBetween(18, 100),
    

}

testData = {
    "name": "t",
	"age": 20,
}
# validate
try:
	x = Valipy().isSchema(personModel).validateSchema(testData, strict=True, useExcept=True)

except InputIsNumericException as e:
	print(e)

except InputIsInBetweenLengthException as e:
	print(e)
	print(e.to_dict())