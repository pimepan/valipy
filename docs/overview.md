# Overview

## Composable API

The main goal of Valipy is to be as simple as possible to use. So Valipy uses method chaining to create a "validation pipeline".

```python
Valipy().isType(str).isMinLength(4).isEqual('some text').validate('some text') # returns True
```

The code abode validate that the string is: Of type String, the min length of the string is of 4 and is exactly equal to the value 'some text'

Note that we end the pipeline with the **validate()** method. this method will return True or False if the valdiation process is successful or not. See more on [Validation Strategies - Boolean Based](#Boolean-Based)

## Validation Strategies

Valipy comes built in with 3 validation strategies.

- Boolean based
- Exception Based
- Schema Validation

### Boolean Based

Boolean is the simplest of all the validation strategies. It will simply return true or false if the validation pipeline passed or not. To use this strategy, simply finish the pipeline using the **validate()** method.

Example:

#### Successful

`Valipy().isType(str).validate(`'some text'`) # returns True`

#### Failed

`Valipy().isType(int).validate(`'some text'`) # returns False`

### Exception Based

Exception based validation is a more powerfull way of validating and knowing exactly where the pipeline failed. To use this strategy we first wrap our validation inside a **Try Except** block and finish the pipeline with the **tryValidate()** method

Example:

```python
from valipy import Valipy, InputValidationException
try:
     Valipy().isType(str).validate('some text') 
   # success flow here

except InputValidationException as e:
	print(e)
	# handle your error here...


```

Note that Valipy ships with a InputValidationException  to have more granularity in your error handling

#### Specific Exception for each rule

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

make sure to place **InputValidationException** at the bottom of your exception stack since all Valipy rules exceptions derive from it

### Schema Validation

usefull when you want to create models for data that comes from APIs and / or Databases

Example:

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
Valipy().isSchema(personModel).validateSchema(testData)
```

As you can see you first need to create a validation model and then pass it to the pipeline to compare against your data