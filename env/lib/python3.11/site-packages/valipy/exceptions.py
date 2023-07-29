
from typing import Any


class InputValidationException(Exception):
    def __init__(
        self, input: Any, message: str = "Input is not valid", rule: str = ""
    ) -> None:
        self.input = input
        self.message = message
        self.rule = rule
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message} for {self.input} failed at rule {self.rule}"

# specific Exceptions


class InputIsEqualException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsInstanceException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsTypeException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsNumberException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsNumericException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsNoneException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsLowerException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsUpperException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputAtStartException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputAtEndException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsEmptyStringException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsEmptyArrayException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsEmptyDictException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsMinLengthException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsMinEqualLengthException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsMaxLengthException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsMaxEqualLengthException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsNegativeException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)
class InputIsPositiveException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsBetweenException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsBetweenOrEqualException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsLessThanException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsLessThanOrEqualException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsGreaterThanException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsGreaterThanOrEqualException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsEvenException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsOddException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputItIncludesException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputItIncludeNumbersException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsIntException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputIsFloatException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputItHasSpacesException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

class InputItPassedSomeException(InputValidationException):
     def __init__(
        self, input: Any, message: str = "Input", rule: str = ""
    ) -> None:
        super().__init__(input, message, rule)

# exception rules
exception_rules: dict = {
    "isEqual": InputIsEqualException,
    "isInstance": InputIsInstanceException,
    "isType": InputIsTypeException,
    "isNumber": InputIsNumberException,
    "isNumeric": InputIsNumericException,
    "isNone": InputIsNoneException,
    "isLower": InputIsLowerException,
    "isUpper": InputIsUpperException,
    "atStart": InputAtStartException,
    "atEnd": InputAtEndException,
    "isEmptyString": InputIsEmptyStringException,
    "isEmptyArray": InputIsEmptyArrayException,
    "isEmptyDict": InputIsEmptyDictException,
    "isMinLength": InputIsMinLengthException,
    "isMinEqualLength": InputIsMinEqualLengthException,
    "isMaxLength": InputIsMaxLengthException,
    "isMaxEqualLength": InputIsMaxEqualLengthException,
    "isNegative": InputIsNegativeException,
    "isPositive": InputIsPositiveException,
    "isBetween": InputIsBetweenException,
    "isBetweenOrEqual": InputIsBetweenOrEqualException,
    "isLessThan": InputIsLessThanException,
    "isLessThanOrEqual": InputIsLessThanOrEqualException,
    "isGreaterThan": InputIsGreaterThanException,
    "isGreaterThanOrEqual": InputIsGreaterThanOrEqualException,
    "isEven": InputIsEvenException,
    "isOdd": InputIsOddException,
    "itIncludes": InputItIncludesException,
    "itIncludeNumbers": InputItIncludeNumbersException,
    "isInt": InputIsIntException,
    "isFloat": InputIsFloatException,
    "itHasSpaces": InputItHasSpacesException,
    "itPassedSome": InputItPassedSomeException,
}
