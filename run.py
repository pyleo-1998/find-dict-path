from find_dict_path import Find_Dict_Path

search_key_from_dict = {"full name":"Brendan Stiedemann","address":{"street":{"colony":"Reinger Inc","extra_info":[{"date":"2023-05-06"},{"uuid":"6eca8033-ba89-4db2-bdb1-c2e0a4f6e0e6"},{"phone":"615-335-1131"}]}}} 

search_key = 'phone'

search_path_finder_from_dict = Find_Dict_Path()

full_path = search_path_finder_from_dict.get_full_path(search_key_from_dict,'propEmbed')

print(full_path)

full_path = search_path_finder_from_dict.get_full_path(search_key_from_dict,'propEmbed',find_first_occurance=False)

print(full_path)