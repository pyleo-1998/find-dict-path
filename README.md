# Pyhtonic Dictionary Path Generator
A package used to the get the Full Pythonic Dictionary Path of the Search key .

## How to use

To install the package

```Bash
pip install find-dict-path
```

_After installing the package use following import:_ <br>

```Python
from find_dict_path import Find_Dict_Path

search_key_from_dict = {"full name":"Brendan Stiedemann","address":{"street":{"colony":"Reinger Inc","extra_info":[{"date":"2023-05-06"},{"uuid":"6eca8033-ba89-4db2-bdb1-c2e0a4f6e0e6"},{"phone":"615-335-1131"}]}}} 

search_key = 'phone'

search_path_finder_from_dict = Find_Dict_Path()

full_path = search_path_finder_from_dict.get_full_path(search_key_from_dict,search_key)

print(full_path)

#['address']['street']['extra_info'][2]['phone']
 
```

_If you wants to get path in every occurrence of the list within dictionary then we can use `find_first_occurance=False` by default it is set as True_ <br>

```Python
full_path = search_path_finder_from_dict.get_full_path(search_key_from_dict,search_key,find_first_occurance=False)

print(full_path)

#['address']['street']['extra_info'][*]['phone'] 
```

> **_NOTE:_**  In output path [*] represent the List is present.

