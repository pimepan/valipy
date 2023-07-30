from valipy import Valipy, InputValidationException, InputIsNumericException, InputIsEqualException, InputIsInBetweenLengthException
personModel = {
    "name": Valipy().isType(str).isInBetweenLength(3, 20),
    "age": Valipy().isType(int).isInBetween(18, 100),
    

}

testData = {
    "name": "",
	"age": 20,
}
# validate
try:
	x = Valipy().schema(personModel).validateSchema(testData, strict=True, useExcept=True)

except InputIsNumericException as e:
	print(e)

except InputIsInBetweenLengthException as e:
	print(e)


email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = Valipy().isValidPattern(email_pattern).validate('jjvonchong@outloo')

print('email', email) # True