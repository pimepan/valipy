# API Reference

## Core

### Valipy

* **Signature**: `Valipy()`
* **Arguments**
  * `input:Any`
* **Usage:**

This function is the entry point for your Valipy pipeline. Once you call it you can start chaining validations rules on it

```python
Valipy('some text').isType(str).validate() # True
```

## Validation Strategies

### validate

* **Signature**: `validate()`
* **returns:**

  * **`bool`**
* **Usage:**

This function is the end part of a validation pipeline and it returns either true if all stages passed or false if any of the stages of the pipeline failed (unless you are using [itPassedSome](#itPassedSome) rule)

```python
Valipy('some text').isType(str).validate() # True
```

### tryValidate

* **Signature**: `tryValidate()`
* **returns:**

  * `<str,InputValidationException> `
* **Usage:**

This function is the end part of a validation pipeline and is used inside a try, except block. it returns the **input or** an **InputValidationException**

```python
try:
    Valipy('some text').isType(str).tryValidate() # True
except InputValidationException as e:
    print(e)
    # handle error here
```



## Built In Rules

### isEqual

* **Signature**: `isEqual(Expected)`
* **Arguments**
  * `val:Any`
* **Usage:**
  This rule performs an equality check on the input agains passed argument

```python
Valipy('some text').isEqual('some text').validate() # True

Valipy('some text').isEqual('different text').validate() # False
```

### isNumber

* **Signature**: `isNumber()`
* **Usage:**
  This rule verifies that the input is a valid **int** or **float**

> Note:  this method check the **input type**

```python
Valipy(10).isNumber().validate() # True

Valipy(10.5).isNumber().validate() # True

Valipy('10').isNumber().validate() # False
```

### isNumeric

* **Signature**: `isNumeric()`
* **Usage:**
  Unlike [isNumber()](#isNumber), this method will cast number strings and accept them as number inputs

```python
Valipy(10).isNumeric().validate() # True

Valipy(10.5).isNumeric().validate() # True

Valipy('10').isNumeric().validate() # True

Valipy('10.5').isNumeric().validate() # True

Valipy('text').isNumeric().validate() # False

```

### isUpperCase

### isInt

* **Signature**: `isInt()`
* **Usage:**
  This rule verifies if the input is of int type

!> Warning: this rule will fail if the input is not of a number

```python
Valipy(10).isInt().validate() # True

Valipy(10.5).isInt().validate() # False
```

### isFloat

* **Signature**: `isFloat()`
* **Usage:**
  This rule verifies that the input is a valid  **float**

!> Warning: this rule will fail if the input is not of a number

```python
Valipy(10).isInt().validate() # True

Valipy(10.5).isInt().validate() # False
```

```python
Valipy(10).isFloat().validate() # False

Valipy(10.5).isFloat().validate() # True
```

* **Signature**: `isUpperCase()`
* **Usage:**
  It checks if the whole input is upper cased.

> Note: This pipeline will fail if the input is not of string type

```python
Valipy('SOME TEXT HERE').isUpperCase().validate() # True

Valipy('SOME text Here').isLowerCase().validate() # False
```

### isLowerCase

* **Signature**: `isLowerCase()`
* **Usage:**
  It checks if the whole input is lower cased.

> Note: This pipeline will fail if the input is not of string type

```python
Valipy('some text here').isLowerCase().validate() # True

Valipy('SOME text Here').isLowerCase().validate() # False
```

### isEveryWordCapitalized

* **Signature**: `isEveryWordCapitalized()`
* **Usage:**
  It checks if the first letter of every word in the input is capitalized

> Note: This pipeline will fail if the input is not of string type

```python
Valipy('Some Text Here').isEveryWordCapitalized().validate() # True

Valipy('Some text here').isEveryWordCapitalized().validate() # False

```

### isEmptyString

* **Signature**: `isEmptyString()`
* **Usage:**
  It checks if the input is an emptu string (**''**)

> Note: This pipeline will fail if the input is not of string type

!> Warning: This pipeline will fail if the string has spaces. Ex: String(' ')

```python
Valipy('').isEmptyString().validate() # True

Valipy(' ').isEmptyString().validate() # False

```

### itHasSpaces

* **Signature**: `itHasSpaces()`
* **Usage:**
  It checks if the input string has spaces

!> Warning: This pipeline will fail if input is not of string type

```python
Valipy('Hello World').itHasSpaces().validate() # True

Valipy('HelloWorld').itHasSpaces().validate() # False

```

### isEmpty

* **Signature**: `isEmpty()`
* **Usage:**
  It performs an equality check on the first element of the input

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy('').isEmptyString().validate() # True

Valipy(' ').isEmptyString().validate() # False

Valipy([]).isEmptyString().validate() # True

Valipy([1,2,3]).isEmptyString().validate() # False

```

### atStart

* **Signature**: `atStart()`
* **Arguments**
  * `val:Any`
* **Usage:**
  It performs an equality check on the first element of the input

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy('Some Text Here').atStart('S').validate() # True

Valipy('Some text here').atStart('N').validate() # False

Valipy([0,2,4,6]).atStart(0).validate() # True

Valipy([0,2,4,6]).atStart(1).validate() # False


```

### atEnd

* **Signature**: `atEnd()`
* **Arguments**
  * `val:Any`
* **Usage:**
  It performs an equality check on the last element of the input

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy('Some Text Here').atEnd('e').validate() # True

Valipy('Some text here').atEnd('N').validate() # False

Valipy([0,2,4,6]).atEnd(6).validate() # True

Valipy([0,2,4,6]).atEnd(4).validate() # False


```

### isMinLength

* **Signature**: `isMinLength()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a less than **(<) on the input againts the passed minimun val**

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy('Some Text Here').isMinLength(4).validate() # True

Valipy('Some text here').isMinLength(25).validate() # False

Valipy([0,2,4,6]).isMinLength(2).validate() # True

Valipy([0,2,4,6]).isMinLength(10).validate() # False


```

### isMaxLength

* **Signature**: `isMaxLength()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a greater than **(>) on the input againts the passed maximun val**

> Note: This pipeline only works with objects that contain a **len** method. Ex: **strings, lists, tuples, dicts, sets**

```python
Valipy('Some Text Here').isMaxLength(4).validate() # True

Valipy('Some text here').isMaxLength(25).validate() # False

Valipy([0,2,4,6]).isMaxLength(2).validate() # False

Valipy([0,2,4,6]).isMaxLength(10).validate() # True


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
Valipy('Some Text Here').isInBetweenLength(0,20).validate() # True

Valipy('Some text here').isInBetweenLength(20,30).validate() # False



```

### isLessThan

* **Signature**: `isLessThan()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a less than **(<) on the input againts the passed minimun val**

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy(2).isLessThan(4).validate() # True


Valipy(7).isLessThan(4).validate() # False
```

### isGreaterThan

* **Signature**: `isGreaterThan()`
* **Arguments**
  * `val:int`
* **Usage:**
  It performs a greater than **(>) on the input againts the passed maximun val**

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy(2).isLessThan(4).validate() # True


Valipy(7).isLessThan(4).validate() # False
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
Valipy(2).isInBetween(0,4).validate() # True


Valipy(7).isInBetween(8,9).validate() # False
```

### isPositive

* **Signature**: `isPositive()`
* **Usage:**
  It checks if the input is over 0

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy(2).isPositive().validate() # True


Valipy(-2).isPositive().validate() # False
```

### isNegative

* **Signature**: `isNegative()`
* **Usage:**
  It checks if the input is under 0

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy(2).isNegative().validate() # False


Valipy(-2).isNegative().validate() # True
```

### isOdd

* **Signature**: `isOdd()`
* **Usage:**
  It checks if the input is an even number

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy(2).isOdd().validate() # False


Valipy(3).isOdd().validate() # True
```

### isEven

* **Signature**: `isEven()`
* **Usage:**
  It checks if the input is an odd number

!> Warning: This pipeline will fail if the input is not an int or float

```python
Valipy(2).isTrue().validate() # True


Valipy(3).isTrue().validate() # False
```

### itPassedSome

* **Signature**: `itPassedSome()`
* **Usage:**
  It checks if the input passed atleast one stage of the pipeline

```python
Valipy(2).isOdd().isInt().itPassedSome().validate # true


Valipy(3).isOdd().isGreaterThan(5).itPassedSome().validate() # False
```

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
Valipy(2).isType(int) # true

Valipy('hello').isType(str) # true

Valipy(True).isType(bool) # true
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
Valipy(x).isInstance(Foo) # true

```
