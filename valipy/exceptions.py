
from typing import Any


class InputValidationException(Exception):
    def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = ""
    ) -> None:
        self.input = input
        self.message = message
        self.rule = rule
        self.natural_language_message = natural_language_message
        super().__init__(self.message)

    
    def to_dict(self) -> dict:
        return {
            "input": self.input,
            "message": self.message,
            "rule": self.rule,
            "natural_language_message":self.natural_language_message
        }
    def __str__(self) -> str:
        return self.message



class InputSchemaNotMatchingKeysException(InputValidationException):
    def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = ""
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)
    

# specific Exceptions


class InputIsEqualException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not equal to the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsInstanceException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not an instance of the specified class"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsTypeException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not of the specified type"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsNumberException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not a number"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsNumericException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not numeric"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsNoneException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is None"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsLowerException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not fully lower case"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsUpperException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not fully upper case"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)
class InputIsCapitalizedException(InputValidationException):
    def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not capitalized"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)
class InputIsEveryWordCapitalizedException(InputValidationException):
    def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not capitalized at every word"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)
class InputAtStartException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input does not start with the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputAtEndException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input does not end with the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsEmptyStringException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is empty"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsEmptyException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is empty"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)


class InputIsMinLengthException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the length of the input is less than the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsMaxLengthException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the length of the input is greater than the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)


class InputIsInBetweenLengthException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the length of the input is not in between the specified values"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)


class InputIsLessThanException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is less than the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)


class InputIsGreaterThanException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is greater than the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsInBetweenException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not in between the specified values"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsEvenException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not even"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsNegativeException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not negative"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)
class InputIsPositiveException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not positive"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsOddException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not odd"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputItIncludesException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input does not include the specified value"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputItIncludeNumbersException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input does not include numbers"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsIntException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not a whole number"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputIsFloatException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input is not a decimal number"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputItHasSpacesException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "the input does not have spaces"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)

class InputItPassedSomeException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = "", natural_language_message: str = "all the validation rules for the input did not pass"
    ) -> None:
        super().__init__(input, message, rule, natural_language_message)



# exception rules
exception_rules: dict = {
    "isEqual": InputIsEqualException,
    "isInstance": InputIsInstanceException,
    "isType": InputIsTypeException,
    "isNumber": InputIsNumberException,
    "isNumeric": InputIsNumericException,
    "isNone": InputIsNoneException,
    "isLower": InputIsLowerException,
    "isCapitalized": InputIsCapitalizedException,
    "isEveryWordCapitalized": InputIsEveryWordCapitalizedException,
    "isUpper": InputIsUpperException,
    "atStart": InputAtStartException,
    "atEnd": InputAtEndException,
    "isEmptyString": InputIsEmptyStringException,
    "isEmpty": InputIsEmptyException,
  
    "isMaxLength": InputIsMaxLengthException,
    "isInBetweenLength": InputIsInBetweenLengthException,
    
    "isLessThan": InputIsLessThanException,
    "isGreaterThan": InputIsGreaterThanException,
    "isNegative": InputIsNegativeException,
    "isPositive": InputIsPositiveException,
    "isInBetween": InputIsInBetweenException,

    "isEven": InputIsEvenException,
    "isOdd": InputIsOddException,
    "itIncludes": InputItIncludesException,
    "itIncludeNumbers": InputItIncludeNumbersException,
    "isInt": InputIsIntException,
    "isFloat": InputIsFloatException,
    "itHasSpaces": InputItHasSpacesException,
    "itPassedSome": InputItPassedSomeException,
}
