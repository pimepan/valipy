# API Reference

## Core

### Valipy

* **Signature**: `Valipy()`
* **Usage:**

This function is the entry point for your Valipy pipeline. Once you call it you can start chaining validations rules on it

```python
Valipy('some text').isType(str).validate('some text') # True
```

## Validation Strategies

### validate

* **Signature**: `validate()`
* **Arguments**

  * `input:Any`
* **returns:**

  * **`bool`**
* **Usage:**

This function is the end part of a validation pipeline and it returns either true if all stages passed or false if any of the stages of the pipeline failed (unless you are using [itPassedSome](#itPassedSome) rule)

```python
Valipy('some text').isType(str).validate() # True
```

### tryValidate

* **Signature**: `tryValidate()`
* **Arguments**

  * `input:Any`
* **returns:**

  * `[input<Any>,InputValidationException] `
* **Usage:**

This function is the end part of a validation pipeline and is used inside a try, except block. it returns the **input or** an **InputValidationException**

```python
try:
    Valipy().isType(str).tryValidate('some text') # True
except InputValidationException as e:
    print(e)
    # handle error here
```

### validateSchema

* **Signature**: `tryValidate()`
* **Arguments**

  * `data: dict`
  * `strict : bool`
  * `useExcept : bool`
* **returns:**

  * `[input<Any>,InputValidationException] `
* **Usage:**

Validate a data model with multiple fields. Good for validating data before sending it to a database.

```python
personModel = {
    "name": Valipy().isType(str).isInBetweenLength(3, 20),
    "age": Valipy().isType(int).isInBetween(18, 100),
}

testData = {
    "name": "John Doe",
    "age": 20,
}
# validate
Valipy().schema(personModel).validateSchema(testData)
```

#### Strict Mode

if the strict flag is set to true, the input data keys must exactly match the schema keys.

#### useExcept 

If the useExcept flag is set to true, you can use validateSchema with the [tryValidate](#tryValidate) strategy.

## Built In Rules

### isValidPattern

* **Signature**: `isValidPattern(regex)`
* **Arguments**
  * `regex: Literal`
* **Usage:**
  This rule performs an equality check on the input agains passed argument

```python
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

Valipy().isValidPattern(email_pattern).validate('email@domain.com') # True

Valipy().isValidPattern(email_pattern).validate('email@') # False

```

### isEqual

* **Signature**: `isEqual(Expected)`
* **Arguments**
  * `val:Any`
* **Usage:**
  This rule performs an equality check on the input agains passed argument

```python
Valipy().isEqual('some text').validate('some text') # True

Valipy().isEqual('different text').validate('some text') # False
```

### isNumber

* **Signature**: `isNumber()`
* **Usage:**
  This rule verifies that the input is a valid **int** or **float**

> Note:  this method check the **input type**

```python
Valipy().isNumber().validate(10) # True

Valipy().isNumber().validate(10.5) # True

Valipy().isNumber().validate('10') # False
```

### isNumeric

* **Signature**: `isNumeric()`
* **Usage:**
  Unlike [isNumber()](#isNumber), this method will cast number strings and accept them as number inputs

```python
Valipy().isNumeric().validate(10) # True

Valipy().isNumeric().validate(10.5) # True

Valipy().isNumeric().validate('10') # True

Valipy().isNumeric().validate('10.5') # True

Valipy().isNumeric().validate('text') # False

```

### isUpperCase

### isInt

* **Signature**: `isInt()`
* **Usage:**
  This rule verifies if the input is of int type

!> Warning: this rule will fail if the input is not of a number

```python
Valipy().isInt().validate(10) # True

Valipy().isInt().validate(10.5) # False
```

### isFloat

* **Signature**: `isFloat()`
* **Usage:**
  This rule verifies that the input is a valid  **float**

!> Warning: this rule will fail if the input is not of a number

```python
Valipy().isInt().validate(10) # True

Valipy().isInt().validate(10.5) # False
```

```python
Valipy().isFloat().validate(10) # False

Valipy().isFloat().validate(10.5) # True
```

* **Signature**: `isUpperCase()`
* **Usage:**
  It checks if the whole input is upper cased.

> Note: This pipeline will fail if the input is not of string type

```python
Valipy().isUpperCase().validate('SOME TEXT HERE') # True

Valipy().isLowerCase().validate('SOME text Here') # False
```

### isLowerCase

* **Signature**: `isLowerCase()`
* **Usage:**
  It checks if the whole input is lower cased.

> Note: This pipeline will fail if the input is not of string type

```python
Valipy().isLowerCase().validate('some text here') # True

Valipy().isLowerCase().validate('SOME text Here') # False
```

### isEveryWordCapitalized

* **Signature**: `isEveryWordCapitalized()`
* **Usage:**
  It checks if the first letter of every word in the input is capitalized

> Note: This pipeline will fail if the input is not of string type

```python
Valipy().isEveryWordCapitalized().validate('Some Text Here') # True

Valipy().isEveryWordCapitalized().validate('Some text here') # False

```

### isEmptyString

* **Signature**: `isEmptyString()`
* **Usage:**
  It checks if the input is an emptu string (**''**)

> Note: This pipeline will fail if the input is not of string type

!> Warning: This pipeline will fail if the string has spaces. Ex: String(' ')

```python
Valipy().isEmptyString().validate('') # True

Valipy().isEmptyString().validate(' ') # False

```

### itHasSpaces

* **Signature**: `itHasSpaces()`
* **Usage:**
  It checks if the input string has spaces

!> Warning: This pipeline will fail if input is not of string type

```python
Valipy().itHasSpaces().validate('Hello World') # True

Valipy().itHasSpaces().validate('HelloWorld') # False

```

### isEmpty

* **Signature**: `isEmpty()`
* **Usage:**
  It performs an equality check on the first element of the input

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy().isEmptyString().validate('') # True

Valipy().isEmptyString().validate(' ') # False

Valipy().isEmptyString().validate([]) # True

Valipy().isEmptyString().validate([1,2,3]) # False

```

### atStart

* **Signature**: `atStart()`
* **Arguments**
  * `val:Any`
* **Usage:**
  It performs an equality check on the first element of the input

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy().atStart('S').validate('Some Text Here') # True

Valipy().atStart('N').validate('Some text here') # False

Valipy().atStart(0).validate([0,2,4,6]) # True

Valipy().atStart(1).validate([0,2,4,6]) # False


```

### atEnd

* **Signature**: `atEnd()`
* **Arguments**
  * `val:Any`
* **Usage:**
  It performs an equality check on the last element of the input

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy().atEnd('e').validate('Some Text Here') # True

Valipy().atEnd('N').validate('Some text here') # False

Valipy().atEnd(6).validate([0,2,4,6]) # True

Valipy().atEnd(4).validate([0,2,4,6]) # False


```

### isMinLength

* **Signature**: `isMinLength()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a less than **(<) on the input againts the passed minimun val**

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy().isMinLength(4).validate('Some Text Here') # True

Valipy().isMinLength(25).validate('Some text here') # False

Valipy().isMinLength(2).validate([0,2,4,6]) # True

Valipy().isMinLength(10).validate([0,2,4,6]) # False


```

### isMaxLength

* **Signature**: `isMaxLength()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a greater than **(>) on the input againts the passed maximun val**

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy().isMaxLength(4).validate('Some Text Here') # True

Valipy().isMaxLength(25).validate('Some text here') # False

Valipy().isMaxLength(2).validate([0,2,4,6]) # False

Valipy().isMaxLength(10).validate([0,2,4,6]) # True


```

### isInBetweenLength

* **Signature**: `isInBetweenLength()`
* **Arguments**
  * `min:int`
  * `max:int`
* **Usage:**
  It checks if the input len is between a range

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy().isInBetweenLength(0,20).validate('Some Text Here') # True

Valipy().isInBetweenLength(20,30).validate('Some text here') # False



```

### isLessThan

* **Signature**: `isLessThan()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a less than **(<) on the input againts the passed minimun val**

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy().isLessThan(4).validate(2) # True


Valipy().isLessThan(4).validate(7) # False
```

### isGreaterThan

* **Signature**: `isGreaterThan()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a greater than **(>) on the input againts the passed maximun val**

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy().isLessThan(4).validate(2) # True


Valipy().isLessThan(4).validate(7) # False
```

### isInBetween

* **Signature**: `isInBetween()`
* **Arguments**
  * `min:int`
  * `max:int`
* **Usage:**
  It checks if the input is between a min and max val

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy().isInBetween(0,4).validate(2) # True


Valipy().isInBetween(8,9).validate(7) # False
```

### isPositive

* **Signature**: `isPositive()`
* **Usage:**
  It checks if the input is over 0

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy().isPositive().validate(2) # True


Valipy().isPositive().validate(-2) # False
```

### isNegative

* **Signature**: `isNegative()`
* **Usage:**
  It checks if the input is under 0

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy().isNegative().validate(2) # False


Valipy().isNegative().validate(-2) # True
```

### isOdd

* **Signature**: `isOdd()`
* **Usage:**
  It checks if the input is an even number

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy().isOdd().validate(2) # False


Valipy().isOdd().validate(3) # True
```

### isEven

* **Signature**: `isEven()`
* **Usage:**
  It checks if the input is an odd number

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy().isTrue().validate(2) # True


Valipy().isTrue().validate(3) # False
```

### itPassedSome

* **Signature**: `itPassedSome()`
* **Usage:**
  It checks if the input passed atleast one stage of the pipeline

```python
Valipy().isOdd().isInt().itPassedSome().validate(3) # true


Valipy().isOdd().isGreaterThan(5).itPassedSome().validate(3) # False
```

### isSchema

* **Signature**: `itPassedSome()`
* arguments:
  * `dict[Valipy]`
* **Usage:**
  this saves internally a schema for a complex data type for later validation. Good for validating data from APIs or Databases

> Note: Check also [validateSchema](#validateSchema) strategy

```python
personModel = {
    "name": Valipy().isType(str).isInBetweenLength(3, 20),
    "age": Valipy().isType(int).isInBetween(18, 100),
}

testData = {
    "name": "John Doe",
    "age": 20,
}
# validate
Valipy().schema(personModel).validateSchema(testData)
```

> Note: isSchema should be used in isolation since the validation strategies cannot be further chained.

## Type Checking Rules

These rules are suited to check typing and even works for custom types!

* isType: suited for validating built in python types
* isInstance: suited for validating custom types made from classes

### isType

* **Signature**: `isType()`
* **Arguments**
  * `val:Type`
* **Usage:**
  good for checking if the input is a valid **buit in python type**

> Note: You can pass all built in python types: **str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType**

```python
Valipy().isType(int).validate(2) # true

Valipy().isType(str).validate('hello') # true

Valipy().isType(bool).validate(True) # true
```

Note that we pass literally the type and is not wrapped between quotes

### isInstance

* **Signature**: `isInstance()`
* **Arguments**
  * `val:Type`
* **Usage:**
  good for checking if the input is an instance of a custom class / type

> Note: This would be usefull if you are using classes as types


```python
class Foo:
	x:str = 'hello world'
	y:int = 25

x = Foo()
Valipy().isInstance(Foo).validate(x) # true

```

## Exceptions

Valipy ships with an specific exception for each built in rule. You can either catch them all with InputValidationException or you can catch each rule respectively giving you extra control in your error handling workflow.

### InputValidationException

* **Signature**: `InputValidationException()`
* **Extends:**
  * **`Exception`**
* **Arguments**
  * `input:str`
  * `message:str`
  * `rule:str`
  * `natural_language_message:str`
* **Returns:**
  * str
* **Usage:**
  import it and use it inside a try excep block

```python
from valipy import Valipy, InputValidationException
try:
     Valipy().isType(str).validate('some text') 
   # success flow here

except InputValidationException as e:
	print(e)
	# handle your error here...
```

#### InputValidationException.to_dict() {to_dict}

* **Signature**: `InputValidationException.to_dict()`
* **Returns:**
  * dict[str]
* **Usage:**
  Access specific info from the error

```python
from valipy import Valipy, InputValidationException
try:
     Valipy().isType(str).validate('some text') 
   # success flow here

except InputValidationException as e:
	print(e.to_dict())
	'''
	{
          input:str, # the input you are validating
          message:str, # a full text message of the error
          rule:str, # at which rule it failed
	   natural_language_message:str # a natural language error message that non developers could understand (could be used as an API error return message)
	}
	'''
	# handle your error here...
```

!> Warning: the **natural_language_message** is only available in english and currently there is no plan of adding **i18n** support


### Granular Exceptions

* **Extends:**
  * **`InputValidationException`**
* **Arguments**
  * `input:str`
  * `message:str`
  * `rule:str`
  * `natural_language_message:str`
* **Returns:**
  * str
* **Usage**

Valipy ships for a specific exception for each rule so you can have further granularity for each rule failure

Example:

```python
from valipy import Valipy, InputValidationException, InputIsTypeException
try:
     Valipy().isType(str).isEqual('some text').validate() 
   # success flow here

except InputIsTypeException as e:
	print(e)
	# handle error for isType() rule failure
except InputValidationException as e:
	print(e)
	# this exception serve as a catch all.



```

Each built in rule in Valipy has its own Exception.

You can import them by following the next  pattern:

`Input<RuleName>Exeption`

Example:

isEqual() Exception

```python
from valipy import InputIsEqualException
```

isInt() Exception

```python
from valipy import InputIsIntException
```

#### Considerations

make sure to place **InputValidationException** at the bottom of your exception stack since all Valipy rules exceptions derive from it so it is basically a **catch all** exceptions
