import array


class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.size_max = size_max
        
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))
    
    def empty(self):
        return self.size == 0
    
    def full(self):
        return self.size == self.size_max
    
    def enqueue(self, element):
        if self.size == self.size_max:
            return False
        self.data[self.tail] = element
        self.tail += 1
        self.size += 1
        if self.tail == self.size_max:
            self.tail = 0
        return True
    
    def dequeue(self):
        if self.size == 0:
            return None
        element = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.size_max:
            self.head = 0
        return element


def test1():
    queue = Queue(3)
    
    is_empty = queue.empty()
    if not is_empty: return False
    
    is_added_1 = queue.enqueue(1)
    if not is_added_1: return False
    
    is_added_2 = queue.enqueue(2)
    if not is_added_2: return False
    
    element_1 = queue.dequeue()
    if element_1 != 1: return False
    
    element_2 = queue.dequeue()
    if element_2 != 2: return False
    
    is_empty = queue.empty()
    if not is_empty: return False
    
    return True


def test2():
    queue = Queue(2)
    
    is_empty = queue.empty()
    if not is_empty: return False
    
    was_added_1 = queue.enqueue(1)
    if not was_added_1: return False
    
    was_added_2 = queue.enqueue(2)
    if not was_added_2: return False
    
    if queue.tail != 0: return False
    
    was_added_3 = queue.enqueue(3)
    if was_added_3: return False
    
    return True


def test3():
    queue = Queue(2)
    
    is_empty = queue.empty()
    if not is_empty: return False
    
    element_0 = queue.dequeue()
    if element_0: return False
    
    was_added_1 = queue.enqueue(1)
    was_added_2 = queue.enqueue(2)
    
    element_1 = queue.dequeue()
    if not element_1: return False
    
    element_2 = queue.dequeue()
    if not element_2: return False
    
    if queue.head != 0: return False
    
    element_3 = queue.dequeue()
    if element_3: return False
    
    return True


def main():
    q = Queue(2)
    is_added_1 = q.enqueue(6)
    is_added_2 = q.enqueue(7)
    is_added_3 = q.enqueue(8)
    element_added_1 = q.dequeue()
    element_added_2 = q.dequeue()
    element_added_3 = q.dequeue()
    
    print(is_added_1, is_added_2, is_added_3,
          element_added_1, element_added_2, element_added_3)
    
    result_test1 = test1()
    result_test2 = test2()
    result_test3 = test3()
    
    print('test1 OK' if result_test1 else 'test1 NOT OK')
    print('test2 OK' if result_test2 else 'test2 NOT OK')
    print('test3 OK' if result_test3 else 'test3 NOT OK')


if __name__ == '__main__':
    main()
