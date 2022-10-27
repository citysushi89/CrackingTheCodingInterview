# animal_shelter.py 

class Queue:
    def __init__(self):
        self.animals = []
        self.size = 0


    def enqueue(self, animal_type):
        self.animals.append(animal_type)


    # dequeue any
    def dequeue(self):
        del self.animals[0]
        
    # dequeueDog
    def dequeue_dog(self):
        self.animals.remove("Dog")
                

    # dequeueCat
    def dequeue_cat(self):
        self.animals.remove("Cat")

    def see_animals(self):
        return self.animals

q = Queue()

q.enqueue('Cat')
q.enqueue('Cat')
q.enqueue('Dog')
q.enqueue('Dog')
q.enqueue('Cat')
# q.dequeue()
q.dequeue_dog()

print(q.see_animals())