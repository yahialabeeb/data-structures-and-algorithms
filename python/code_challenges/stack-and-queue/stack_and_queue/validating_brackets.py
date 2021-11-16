from stack_and_queue.stack_and_queue import Stack

def validate_brackets(str:str):
    stack = Stack()
    for i in str :
        if i == "{" or i== "(" or i== "[":
            stack.push(i)
        elif  i=="}" or i == ")" or i == "]":
            if stack.top:
                a = stack.pop() + i
                if a != "{}" and a != "[]" and a != "()":
                    return False             
            else:
                 return False
    if stack.top:
        return False    
    if str:
        return True
    raise Exception ("Empty String")
# print(validate_brackets("{{}{()"))