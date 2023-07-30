from typing import Any, Self, Union, Type, Callable, Literal
from .exceptions import InputValidationException, InputSchemaNotMatchingKeysException, exception_rules
import inspect

class Valipy:
    def __init__(self, input: Any = None) -> None:
        self.pipeline: list = []
        self.schemaModel: dict = {}


    def __pushToPipeline(self, rule: str, lamb:Callable = None) -> None:
        self.pipeline.append({"rule": rule, "lamb": lamb})
  
    # validation strategies
    def validate(self, input: Any = None) -> bool:
        for validator in self.pipeline:
            if validator['lamb'](input) == False:
                return False
        return True


    def tryValidate(self, input: Any = None) -> Union[Any, InputValidationException]:
        for validator in self.pipeline:
            if validator['lamb'](input) == False:
                if validator["rule"] in exception_rules:
                    raise exception_rules[validator["rule"]](input = input,message=f"{str(input)} failed at rule {validator['rule']}" ,rule=validator["rule"])
                else:
                    raise InputValidationException(input = input, rule=validator["rule"])
        return input
    
    # schema validation
    def __validateSchemaStrict(self, inputData: dict = None) -> Union[bool, InputSchemaNotMatchingKeysException]:
        # check that the input matches exactly the schema keys
        if len(inputData) != len(self.schemaModel):
            raise InputSchemaNotMatchingKeysException(input = inputData,message='Schema does not match' ,rule="schemaStrict")
        for key in inputData:
            if key not in self.schemaModel:
                raise InputSchemaNotMatchingKeysException(input = inputData,message='Schema does not match', rule="schemaStrict")
            



    def isSchema(self, schema: dict[Self]) -> Self:
        self.schemaModel = schema
        return self

    
    def validateSchema(self,data:dict = {}, strict: bool = False, useExcept: bool = False) -> bool:
        if strict == True:
            try:
                self.__validateSchemaStrict(inputData=data)
            except InputSchemaNotMatchingKeysException:
                return False
        # loop the schema
        for key, val in self.schemaModel.items():
            # if the key is not in the input data return false
            if key not in data:
                pass
            # if the key is in the input data but the value is not valid return false
            if useExcept == True:
                return val.tryValidate(data[key])
            else:

                return val.validate(data[key])
        
            
    def isValidPattern(self, pattern: Literal) -> Self:
        import re
        def lamb(x):
            if re.match(pattern, x):
                return True
            return False
        self.__pushToPipeline("isValidPattern", lamb)
        return self
    # validation rules
    def isEqual(self, val: Any) -> Self:
        def lamb(x):
            if x != val:
                return False
            return True

        self.__pushToPipeline("isEqual", lamb)
        return self

    def isNumber(self) -> Self:
        def lamb(x):
            if type(x) != int and type(x) != float:
                return False
            return True

        self.__pushToPipeline("isNumber", lamb)
        return self

    def isNumeric(self):
        # if input is a string try to convert to number
        def lamb(x):
            try:
                float(x)
                return True
            except Exception as e:
                try:
                    int(x)
                    return True
                except ValueError:
                    return False

        self.__pushToPipeline("isNumeric", lamb)
        return self
    
        

    def isNone(self) -> Self:
        def lamb(x):
            if x == None:
                return True
            return False
        self.__pushToPipeline("isNone", lamb)
        return self

    def isLowerCase(self) -> Self:
        def lamb(x):
                

            if type(x) != str:
                return False

            if x.islower()== True: 
                return True
            else:
                return False
        self.__pushToPipeline("isNone", lamb)
        return self

    def isUpperCase(self) -> Self:
        def lamb(x):
            if type(x) != str:
                return False
            if x.isupper() == True:
                return True
            else:
                return False
        self.__pushToPipeline("isUpperCase", lamb)
        return self
    def isCapitalized(self) -> Self:
        def lamb(x):
            if type(x) != str:
                return False
            if x[0].isupper() == True:
                return True
            else:
                return False
        self.__pushToPipeline("isCapitalized", lamb)
        return self
    def isEveryWordCapitalized(self) -> Self:

        def lamb(x):
            if type(x) != str:
                return False
            for word in x.split():
                if not word[0].isupper():
                    return False
            return True
        self.__pushToPipeline("isEveryWordCapitalized", lamb)
        return self
    def atStart(self, val: Any):
        def lamb(x):
            try:
                len(x)
            except TypeError:
                return False
            if x[0] != val:
                return False
            return True
        self.__pushToPipeline("atStart", lamb)
        return self

    def atEnd(self, val: Any):
        def lamb(x):
            try:
                len(x)
            except TypeError:
                return False
            if x[-1] != val:
                return False
            return True
        self.__pushToPipeline("atEnd", lamb)
        return self

    def isEmptyString(self) -> Self:
        def lamb(x):
            if type(x) != str:
                return False
            if len(x) > 0:
                return False
            return True
        self.__pushToPipeline("isEmptyString", lamb)    
        return self

   
    def isEmpty(self) -> Self:
        def lamb(x):
            try:
                len(x)
            except TypeError:
                return False
            if len(x) > 0:
                return False
            return True
        self.__pushToPipeline("isEmpty", lamb)
        return self
   

    def isMinLength(self, val: int) -> Self:
        def lamb(x):
            try:
                len(x)
            except TypeError:
                return False
            if len(x) < val:
                return False
            return True
        self.__pushToPipeline("isMinLength", lamb)
        return self


    def isMaxLength(self, val: int) -> Self:
        def lamb(x):
            try:
                len(x)
            except TypeError:
                return False
            if len(x) > val:
                return False
            return True
        self.__pushToPipeline("isMaxLength", lamb)
        return self
      
    
    def isInBetweenLength(self, min: int, max: int) -> Self:
            def lamb(x):
                try:
                    len(x)
                except TypeError:
                    return False
                if len(x) < min or len(x) > max:
                    return False
                return True
            self.__pushToPipeline("isInBetweenLength", lamb)
            return self
    
    

    def isInBetween(self, min: int, max: int) -> Self:
        def lamb(x):
            if type(x) != int and type(x) != float:
                return False
            if x <= min or x >= max:
                return False
            return True
        self.__pushToPipeline("isInBetween", lamb)
        return self
    

    def isLessThan(self, val: int) -> Self:
        def lamb(x):
            if type(x) != int and type(x) != float:
                return False
            if x >= val:
                return False
            return True
        self.__pushToPipeline("isLessThan", lamb)
        return self
    

   

    def isGreaterThan(self, val: int) -> Self:
        def lamb(x):
            if type(x) != int and type(x) != float:
                return False
            if x <= val:
                return False
            return True
        self.__pushToPipeline("isGreaterThan", lamb)
        return self
    

   

    def isNegative(self) -> Self:
        def lamb(x):
            if type(x) != int and type(x) != float:
                return False
            if x >= 0:
                return False
            return True
        self.__pushToPipeline("isNegative", lamb)
        return self

    def isPositive(self) -> Self:
        def lamb(x):
            if type(x) != int and type(x) != float:
                return False
            if x <= 0:
                return False
            return True
        self.__pushToPipeline("isPositive", lamb)
        return self


    def isEven(self) -> Self:
        def lamb(x):
            if type(x) != int:
                return False
            if x % 2 != 0:
                return False
            return True
        self.__pushToPipeline("isEven", lamb)
        return self
      

    def isOdd(self) -> Self:
        def lamb(x):
            if type(x) != int:
                return False
            if x % 2 == 0:
                return False
            return True
        self.__pushToPipeline("isOdd", lamb)
        return self
    

    def itIncludes(self, val: Any):
        def lamb(x):
            if type(x) != list or type(x) != str:
                return False
            if val not in x:
                return False
            return True
        self.__pushToPipeline("itIncludes", lamb)
        return self
    
    def itIncludesNumbers(self):
        def lamb(x):
            if type(x) == str:
                for char in x:
                    if char.isdigit():
                        return True
                return False
            if type(x) == list or type(x) == set:
                for item in x:
                    if type(item) == int or type(item) == float:
                        return True
                return False
        self.__pushToPipeline("itIncludesNumbers", lamb)
        return self
    
    def isInt(self):
        def lamb(x):
            if type(x) != int:
                return False
            return True
        self.__pushToPipeline("isInt", lamb)
        return self
    

    def isFloat(self):
        def lamb(x):
            if type(x) != float:
                return False
            return True
        self.__pushToPipeline("isFloat", lamb)
        return self
    

    def itHasSpaces(self):
        def lamb(x):
            if type(x) != str:
                return False
            if " " not in x:
                return False
            return True
        self.__pushToPipeline("itHasSpaces", lamb)
        return self
    

    def itPassedSome(self):
        def lamb(x):
            for validator in self.pipeline:
                if validator["passed"] == True:
                    return True
            return False
        self.__pushToPipeline("itPassedSome", lamb)
        return self

    def isInstance(self, val: Type) -> Self:
        def lamb(x):
            if not isinstance(x, val):
                return False
            return True
        self.__pushToPipeline("isInstance", lamb)
        return self
    
    def isType(self, val:Type) -> Self:
        def lamb(x):
            if type(x) != val:
                return False
            return True
        self.__pushToPipeline("isType", lamb)
        return self