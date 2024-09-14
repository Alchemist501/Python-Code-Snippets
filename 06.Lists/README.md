# LISTS IN PYTHON

        A built-in data type that stores set of values.
        It can store elements of different types(int,float,string,etc)
        numbers = [1,2,3,4]
        names = ["Drogon","Vermithor","Cannibel"]
        names[0] = "Balareon" => Allowed in python =>Lists are mutable
        len(names) => returns length

# LIST SLICING

    Similar to String slicing
        list_name[starting_idx:ending_idx] ending_idx not included.
        list[:x] = list[0:x]
        list[x:] = list[x:len(list)]

# LIST METHODS

    list.append(el) => adds el at the end of the list
    list.sort()     => sorts in ascending order
    list.sort(reverse = True) =>sorts in descending order
    list.reverse()  =>reverses list
    list.insert(idx,el) =>Insert el at idx
    list.remove(el) =>Removes first occurence of el
    list.pop(idx)   =>Removes element at idx
