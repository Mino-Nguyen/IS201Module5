FILEPATH = "todo.txt"
def getCurrentList(filepath = FILEPATH):
    with open(filepath, 'r') as todo_file:
        getCurrentList = todo_file.readlines()
    return getCurrentList

def writeCurrentList(todo_list, filepath = FILEPATH):
    with open(filepath, 'w') as todoFile:
        todoFile.writelines(todo_list)

if __name__ == "__main__":
    print('debugging purpose')
    print(getCurrentList('./todos.txt'))