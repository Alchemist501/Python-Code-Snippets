# Functions

Block of statements that perform a specific task

Function Definition

    def functionName(param1,param2....):
        # some work
        return val

Function Call

    functionName(arg1,arg2,....)

Example

    # function definition
    def calc_area(l,b):
        area = l*b
        print(area)
        return area

    # function call
    calc_area(1,2)

    # output
    2

#### Function reduces redundancy in programming

#### Functions with no return value returns None

## BUILT IN FUNCTIONS

#### print() => Prints the values to a stream, or to sys.stdout by default.

#### len() => Returns the number of items in a container.

#### type() => Returns the object type name.

#### range() => Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.

## USER DEFINED FUNCTIONS

#### User defines......

## Default Parameters

##### Default values indicate that the function argument will take that value if no argument value is passed during the function call. The default value is assigned by using the assignment(=) operator of the form keywordname=value.

#### Syntax:

    def function_name(param1, param2=default_value2, param3=default_value3)
