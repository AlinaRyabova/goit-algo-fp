from linked_list import LinkedList

if __name__ == "__main__":
    # Приклад використання реверсування списку
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_end(3)
    llist.insert_at_end(4)
    llist.insert_at_end(5)

    print("Список до реверсування:")
    llist.print_list()

    llist.reverse()
    print("\nСписок після реверсування:")
    llist.print_list()

    # Приклад використання сортування злиттям
    llist = LinkedList()
    llist.insert_at_end(5)
    llist.insert_at_end(3)
    llist.insert_at_end(8)
    llist.insert_at_end(1)
    llist.insert_at_end(7)

    print("\nСписок до сортування:")
    llist.print_list()

    llist.merge_sort()
    print("\nСписок після сортування злиттям:")
    llist.print_list()

    # Приклад об'єднання двох відсортованих списків
    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(3)
    llist1.insert_at_end(5)

    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)

    merged_llist = llist1.merge_two_sorted_lists(llist1, llist2)

    print("\nОб'єднаний відсортований список:")
    merged_llist.print_list()
