list_Strings = ['1','5','45','34','343','34',6556,323]



def type_list(items): 
        list_of_type = type(items)           
        return list_of_type


new_list = list(map(type_list, list_Strings))
print(new_list)