from typing import Any, Self, Union, Type
from .exceptions import InputValidationException, exception_rules


  


class Valipy:
    def __init__(self, input: Any) -> None:
        self.input: Any = input
        self.pipeline: list = []

    # validation strategies
    def validate(self) -> bool:
        for item in self.pipeline:
            if item["passed"] == False:
                return False
        return True

    def tryValidate(self) -> Union[str, InputValidationException]:

        for item in self.pipeline:
            if item["passed"] == False:
                if item["rule"] in exception_rules:
                    raise exception_rules[item["rule"]](input = self.input, rule=item["rule"])
                else:
                    InputValidationException(input = self.input, rule=item["rule"])
        return self.input

    def __pushToPipeline(self, rule: str, result: bool) -> None:
        self.pipeline.append({"rule": rule, "passed": result})

    # validation rules
    def isEqual(self, val: Any) -> Self:
        if self.input != val:
            self.__pushToPipeline("equal", False)
            return self
        self.__pushToPipeline("equal", True)

        return self

    def isNumber(self) -> Self:
        if type(self.input) != int and type(self.input) != float:
            self.__pushToPipeline("isNumber", False)
            return self
        self.__pushToPipeline("isNumber", True)

        return self

    def isNumeric(self):
        # if input is a string try to convert to number
        try:
            float(self.input)
            self.__pushToPipeline("isNumeric", True)
            return self
        except Exception as e:
            try:
                int(self.input)
                self.__pushToPipeline("isNumeric", True)
                return self
            except ValueError:
                self.__pushToPipeline("isNumeric", False)
                return self
   
        

    def isNone(self) -> Self:
        if self.input == None:
            self.__pushToPipeline("isNone", True)
            return self
        self.__pushToPipeline("isNone", False)

        return self

    def isLowerCase(self) -> Self:
        if type(self.input) != str:
            self.__pushToPipeline("isLower", False)
            return self

        if self.input.islower()== True: 
            self.__pushToPipeline("isLower", True)
        else:
            self.__pushToPipeline("isLower", False)
        return self

    def isUpperCase(self) -> Self:
        if type(self.input) != str:
            self.__pushToPipeline("isUpper", False)
            return self
        if self.input.isupper() == True:
            self.__pushToPipeline("isUpper", True)
        else:
            self.__pushToPipeline("isUpper", False)
        return self
    def isCapitalized(self) -> Self:
        if type(self.input) != str:
            self.__pushToPipeline("isCapitalized", False)
            return self
        if self.input[0].isupper():
            self.__pushToPipeline("isCapitalized", True)
        else:
            self.__pushToPipeline("isCapitalized", False)
        return self
    def isEveryWordCapitalized(self) -> Self:
        if type(self.input) != str:
            self.__pushToPipeline("isEveryWordCapitalized", False)
            return self
        for word in self.input.split():
            if not word[0].isupper():
                self.__pushToPipeline("isEveryWordCapitalized", False)
                return self
        self.__pushToPipeline("isEveryWordCapitalized", True)
        return self

    def atStart(self, val: Any):
        # check if len exists for input
        try:
            len(self.input)
        except TypeError:
            self.__pushToPipeline("atStart", False)
            return self

        if self.input[0] != val:
            self.__pushToPipeline("atStart", False)
            return self

        self.__pushToPipeline("atStart", True)
        return self

    def atEnd(self, val: Any):
        # check if len exists for input
        try:
            len(self.input)
        except TypeError:
            self.__pushToPipeline("atEnd", False)
            return self

        if self.input[-1] != val:
            self.__pushToPipeline("atEnd", False)
            return self

        self.__pushToPipeline("atEnd", True)
        return self

    def isEmptyString(self) -> Self:
        if type(self.input) != str:
            self.__pushToPipeline("isEmptyString", False)
            return self
        if len(self.input) > 0:
            self.__pushToPipeline("isEmptyString", False)
            return self
        self.__pushToPipeline("isEmptyString", True)
        return self

   
    def isEmpty(self) -> Self:
        # check if len exists for input
        try:
            len(self.input)
        except TypeError:
            self.__pushToPipeline("isEmpty", False)
            return self

        if len(self.input) > 0:
            self.__pushToPipeline("isEmpty", False)
            return self
        self.__pushToPipeline("isEmpty", True)
        return self
   

    def isMinLength(self, val: int) -> Self:
         # check if len exists for input
        try:
            len(self.input)
        except TypeError:
            self.__pushToPipeline("isMinLength", False)
            return self
        
        if len(self.input) < val:
            self.__pushToPipeline("isMinLength", False)
            return self
        self.__pushToPipeline("isMinLength", True)
        return self

    def isMaxLength(self, val: int) -> Self:
         # check if len exists for input
        try:
            len(self.input)
        except TypeError:
            self.__pushToPipeline("isMaxLength", False)
            return self
        
        if len(self.input) > val:
            self.__pushToPipeline("isMaxLength", False)
            return self
        self.__pushToPipeline("isMaxLength", True)
        return self
    
    def isInBetweenLength(self, min: int, max: int) -> Self:
            # check if len exists for input
            try:
                len(self.input)
            except TypeError:
                self.__pushToPipeline("isInBetweenLength", False)
                return self
        
            if len(self.input) < min or len(self.input) > max:
                self.__pushToPipeline("isInBetweenLength", False)
                return self
            self.__pushToPipeline("isInBetweenLength", True)
            return self
   
    

    def isInBetween(self, min: int, max: int) -> Self:
        if type(self.input) != int and type(self.input) != float:
            self.__pushToPipeline("isInBetween", False)
            return self
        if self.input <= min or self.input >= max:
            self.__pushToPipeline("isInBetween", False)
            return self
        self.__pushToPipeline("isInBetween", True)
        return self

    def isLessThan(self, val: int) -> Self:
        if type(self.input) != int and type(self.input) != float:
            self.__pushToPipeline("isLessThan", False)
            return self
        if self.input >= val:
            self.__pushToPipeline("isLessThan", False)
            return self
        self.__pushToPipeline("isLessThan", True)
        return self

   

    def isGreaterThan(self, val: int) -> Self:
        if type(self.input) != int and type(self.input) != float:
            self.__pushToPipeline("isGreaterThan", False)
            return self
        if self.input <= val:
            self.__pushToPipeline("isGreaterThan", False)
            return self
        self.__pushToPipeline("isGreaterThan", True)
        return self

   

    def isNegative(self) -> Self:
        if type(self.input) != int and type(self.input) != float:
            self.__pushToPipeline("isNegative", False)
            return self
        if self.input >= 0:
            self.__pushToPipeline("isNegative", False)
            return self
        self.__pushToPipeline("isNegative", True)
        return self

    def isPositive(self) -> Self:
        if type(self.input) != int and type(self.input) != float:
            self.__pushToPipeline("isPositive", False)
            return self
        if self.input <= 0:
            self.__pushToPipeline("isPositive", False)
            return self
        self.__pushToPipeline("isPositive", True)
        return self


    def isEven(self) -> Self:
        if type(self.input) != int:
            self.__pushToPipeline("isEven", False)
            return self
        if self.input % 2 != 0:
            self.__pushToPipeline("isEven", False)
            return self
        self.__pushToPipeline("isEven", True)
        return self

    def isOdd(self) -> Self:
        if type(self.input) != int:
            self.__pushToPipeline("isOdd", False)
            return self
        if self.input % 2 == 0:
            self.__pushToPipeline("isOdd", False)
            return self
        self.__pushToPipeline("isOdd", True)
        return self

    def itIncludes(self, val: Any):
        if type(self.input) != list or type(self.input) != str:
            self.__pushToPipeline("itIncludes", False)
            return self
        if val not in self.input:
            self.__pushToPipeline("itIncludes", False)
            return self
        self.__pushToPipeline("itIncludes", True)
        return self
    def itIncludesNumbers(self):
        # case for string
        if type(self.input) == str:
            for char in self.input:
                if char.isdigit():
                    self.__pushToPipeline("itIncludeNumbers", True)
                    return self
            self.__pushToPipeline("itIncludeNumbers", False)
            return self
        # case for list, sets
        if type(self.input) == list or type(self.input) == set:
            for item in self.input:
                if type(item) == int or type(item) == float:
                    self.__pushToPipeline("itIncludeNumbers", True)
                    return self
            self.__pushToPipeline("itIncludeNumbers", False)
            return self
    def isInt(self):
        if type(self.input) != int:
            self.__pushToPipeline("isInt", False)
            return self
        self.__pushToPipeline("isInt", True)
        return self

    def isFloat(self):
        if type(self.input) != float:
            self.__pushToPipeline("isFloat", False)
            return self
        self.__pushToPipeline("isFloat", True)
        return self

    def itHasSpaces(self):
        if type(self.input) != str:
            self.__pushToPipeline("itHasSpaces", False)
            return self
        if " " not in self.input:
            self.__pushToPipeline("itHasSpaces", False)
            return self
        self.__pushToPipeline("itHasSpaces", True)
        return self

    def itPassedSome(self):
        for item in self.pipeline:
            if item["itPassedSome"] == True:
                return True
        return False

    def isInstance(self, val: Type) -> Self:
        if not isinstance(self.input, val):
            self.__pushToPipeline("isInstance", False)
            return self
        self.__pushToPipeline("isInstance", True)

        return self

    def isType(self, val:Type) -> Self:
        if type(self.input) != val:
            self.__pushToPipeline("isType", False)
            return self
        self.__pushToPipeline("isType", True)

        return self
