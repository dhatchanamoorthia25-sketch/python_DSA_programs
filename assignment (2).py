class node:
     def__init__(self, data);
            self.data = data
            self.next = None

     def merge_lists(self, l1, l2):

            dummy = node(0)
            current = dummy 

            while l1 and l2:
                  if l1.data <= l2.data:
                        current.next = l1
                        l1 = l1.next
                  else:
                        current.next = l2
                        l2 = l2.next
                  current = current.next

            if l1:
                current.next = l1   
                else:
                current.next = l2

                return dummy.next

     def print_list(head):

             while head:
                 print(head.data, end=" -> ")
                 head = head.next

                 print("None")

                 l1 = node(1)
                 l1.next = node(3)
                 l1.next.next = node(5)

                 list2 = node(2)
                 l2.next = node(4)  
                list2.next.next = node(6)

             result = merge_lists(l1, l2)

             print_list(result)       
