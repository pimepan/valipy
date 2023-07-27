## Valipy

The chainable and composable data validation library for python.

### Inspiration

Valipy is heavily inspired on [v8n.js](https://github.com/imbrn/v8n) and is aimed to be almost a 1:1 replica of the library.

### Chainable

valipy was created to be composable

```python
Valipy('test text 22').isType(str).isMinLength(5).itHasSpaces().itIncludesNumbers().validate() # returns True
```

### validations strategies

Validate currently supports 2 validation strategies: Booleand based and Exception Based

##### Boolean Based

convenient for quick validations inside a condition

example:

```python
if Valipy('some text').isType(int).validate() == True:
	print('this validation passed')
```


##### Exception Based

Better for cases where you have to validate data from APIs requests

example:

```python
some_data_from_api = {...}

try:
   Valipy(some_data_from_api['fieldX']).isType(int).tryValidate()

except: InputValidationException as e:
	# handle your error here...
```

### caveats

The pipeline doesn't check itself for invalid combinations of validation rules

### Exceptions

valipy ships each rule with a specific exception

you can import them by following the next pattern:

`InputI[RuleName]Exception`

#### Example:

```python
try:
   Valipy('myText').isEqual('MyText').isMinLength(12).tryValidate()
except: InputIsEqualException as e:
	# handle equality exception here
except: InputIsMinLengthException as e:
	# handle length exception here
```

#### Note about exceptions

All Valipy exceptions derive InputValidationException so avoid putting InputValidationException on top of your try, except chain since it will catch it automatically

### RoadMap

* [X] Release minimal version for personal use
* [ ] Cover all API cases
* [ ] Create website
* [ ] add regex based validation rules
* [ ] add a schema validator so you can validate dicts and JSON schemas



## API

Coming soon... You can read the source code. the library is written in a way that all methods are pretty self explanatory and is writter in a typed style
