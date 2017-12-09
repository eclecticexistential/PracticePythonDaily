def start_shopping():
    print("Add items or say 'show' to see your list, 'delete' to remove an item, 'help' to view options, or 'done' to exit and view list.")

start_shopping()

def help():
    start_shopping()

def show(x):
    print(','.join(x))

def delete(x,y):
    x.remove(y)

def main():
    new_item = ""
    shopping_list = list()
    list_output = "You need to buy: "
    solo_list = "You only need to pick up: "

    while new_item != 'done':

        new_item = input("What do you need at the store?").lower()

        if len(shopping_list) == 0 and new_item == "done":
            print('Goodbye. Have a nice day!')

        elif not new_item.isalpha():
            answer = input("Do you need more than one?").lower()
            if answer == "yes":
                shopping_list.append(new_item)
                print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
            elif answer == "no":
                more_info = input("Is this the name of an item?").lower()
                if more_info == "yes":
                    shopping_list.append(new_item)
                    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
                else:
                    print("That is not a word")

        elif new_item == "help":
            help()

        elif new_item == 'show':
            show(shopping_list)

        elif new_item == 'delete':
            try:
                del_item = input("Which item do you want to delete?").lower()
                delete(shopping_list, del_item)
            except:
                print("Item was not on the list.")

        elif new_item == 'done':
                list_len = len(shopping_list)
                for i in range(0, list_len):
                    if list_len == 1:
                        solo_list += shopping_list[i]
                        solo_list += "."
                        print(solo_list)
                    elif i < len(shopping_list)-1:
                        list_output += shopping_list[i]
                        if list_len == 2:
                            list_output += " and "
                        elif list_len > 2:
                            list_output += ", "
                    else:
                        if list_len > 2:
                            list_output += "and "

                        list_output += shopping_list[i]
                        list_output += "."
                        print(list_output)
        else:
            if new_item in shopping_list:
                answer = input("An item is on the list more than once. Delete it?").lower()
                if answer =="yes":
                    #deletes old new_item
                    delete(shopping_list, new_item)
                    #adds current new_item ...is there a better way to do this?
                    shopping_list.append(new_item)
            else:
                shopping_list.append(new_item)
                print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

main()