# RECURSION IN PYTHON

### When a function calls repeatedly itself.

Example

    def print_fact(num, fact=1):
    if num == 1 or num == 0:  # base case
        return fact
    return num * print_fact(num - 1) # recurison
