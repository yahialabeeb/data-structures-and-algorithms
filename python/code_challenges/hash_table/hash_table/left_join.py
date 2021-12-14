from .hash_table import Hash_table

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

    return list_of_key

# hash1 = Hash_table(100)
# hash1.add("diligent", "employed")   
# hash1.add("fond", "enamored")	 	
# hash1.add("guide", "usher")	 	
# hash1.add("outfit", "garb")	 	
# hash1.add("wrath","anger")
# hash2 = Hash_table(100) 	
# hash2.add('diligent', 'idle') 
# hash2.add('fond', 'averse')
# hash2.add('guide', 'follow')
# hash2.add('flow', 'jam')
# hash2.add('wrath', 'delight')
# print(left_joins(hash1,hash2))