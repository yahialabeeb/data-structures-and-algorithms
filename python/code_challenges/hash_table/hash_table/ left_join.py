from hash_table import Hash_table

def left_joins(map1:Hash_table,map2:Hash_table):
    list_of_key = []
    for pair in map1.arr:
        if pair:
            current = pair.head
            while current:
                list_of_key.append([current.value[0]])
                current = current.next

    for i in list_of_key:
        i.append(map1.get(i[0]))
        i.append(map2.get(i[0]))

    print(list_of_key)

hass1 = Hash_table(100)
hass1.add("yahia",25)
hass1.add("yahai",25)
hass2 = Hash_table(100) 
hass2.add("yahia",25)
hass2.add("yhaia",25)
left_joins(hass1,hass2)