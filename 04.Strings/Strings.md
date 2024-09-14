## Strings

        Data type that stores a sequence of characters

## Operations

        > Concatenation
            "hii" + "ppl" ==> "hii ppl"
        >length of str
            len(str)

## Indexing

        Accessing by position
        Manipulation is not possible
        S T R I N G
        0 1 2 3 4 5  => Starts with 0
        Negative indexing possible only with slicing
        S  T  R  I  N  G
        -6 -5 -4 -3 -2 -1 => Starts with -1 from right to left

## Slicing

        Accessing parts of a string
        str[start_idx:end_idx] ending idx is not included
        str[:x] = str[0:x]    x is an integer value
        str[x:] = str[x:len(str)]

## String Functions

        str.endswith("x")    => Returns true if string ends with substr
        str.capitalize()     => Capitalizes 1st char
        str.replace(old,new) => Replaces all occurences of old
        str.find(word)       => Returns 1st index of first occurer
        str.count("x")        => Counts the occurence of substr
