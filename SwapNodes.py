class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    # Базовий випадок: якщо вузлів немає або є лише один
    if head is None or head.next is None:
        return head
    
    # Отримуємо два перші вузли
    first_node = head
    second_node = head.next
    
    # Обмін місцями першої пари
    first_node.next = swapPairs(second_node.next)
    second_node.next = first_node

    # Повертаємо нову голову списку (другий вузол стає головою)
    return second_node

# Функція для створення зв'язаного списку зі списку значень
def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Функція для друку списку
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Приклади тестування
print("Input: [1, 2, 3, 4]")
head = create_list([1, 2, 3, 4])
new_head = swapPairs(head)
print("Output:", end=" ")
print_list(new_head)

print("\nInput: []")
head = create_list([])
new_head = swapPairs(head)
print("Output:", end=" ")
print_list(new_head)

print("\nInput: [1]")
head = create_list([1])
new_head = swapPairs(head)
print("Output:", end=" ")
print_list(new_head)
