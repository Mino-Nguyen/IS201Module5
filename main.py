from Module import helperFunction
import time

prompt = 'Your option are: Show, Add, Edit, Complete, Exit:'
flag = True

while flag:
    time_now = time.strftime('%b %d, %Y %H:%M:%S')
    print(f'It is now {time_now}')
    userInput = input(prompt)
    userInput = userInput.strip().title()
    match userInput:
        case "Show":
            currentList = helperFunction.getCurrentList()
            filterList = [item.strip('\n') for item in currentList]
            for idx, item in enumerate(filterList):
                print(f'{idx+1} {item}')
            if len(currentList) <=0:
                print("None to do Items")
        case "Add":
            addtodo = input('Add this to do list') + '\n'
            currentList = helperFunction.getCurrentList()
            currentList.append(addtodo)
            helperFunction.writeCurrentList(currentList)
        case "Edit":
            currentList = helperFunction.getCurrentList()
            editIdx = int(input('Edit number: ')) -1
            newTodo = input('New Todo Item: ') + '\n'
            currentList[editIdx] = newTodo
            helperFunction.writeCurrentList(currentList)
        case "Complete":
            currentList = helperFunction.getCurrentList()
            removeTodo = input("Index or todo name to remove: ")
            if str.isdigit(removeTodo):
                removeTodo = int(removeTodo)
                if removeTodo > len(currentList)  or removeTodo < 1:
                    print("Index must be  between 1 to", len(currentList))
                else:
                    removeTodo = removeTodo-1
                    print('Remove: ', currentList.pop(removeTodo))
            else:
                currentList.remove(removeTodo)
            helperFunction.writeCurrentList(currentList)
        case "Exit":
            flag = False