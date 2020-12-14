# from Encapsulation.wild_cat_zoo_01E.project.caretaker import Caretaker
# from Encapsulation.wild_cat_zoo_01E.project.cheetah import Cheetah
# from Encapsulation.wild_cat_zoo_01E.project.keeper import Keeper
# from Encapsulation.wild_cat_zoo_01E.project.lion import Lion
# from Encapsulation.wild_cat_zoo_01E.project.tiger import Tiger
# from Encapsulation.wild_cat_zoo_01E.project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        searched = [w for w in self.workers if w.name == worker_name]
        if not searched:
            return f"There is no {worker_name} in the zoo"
        worker = searched[0]  # might be more than 1 with that name
        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        cost = sum([a.get_needs() for a in self.animals])
        if cost > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= cost
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        if lions:
            result += f'----- {len(lions)} Lions:\n'
            for l in lions:
                result += f'{l}\n'
        if tigers:
            result += f'----- {len(tigers)} Tigers:\n'
            for t in tigers:
                result += f'{t}\n'
        if cheetahs:
            result += f'----- {len(cheetahs)} Cheetahs:\n'
            for c in cheetahs:
                result += f'{c}\n'
        return result[:-1]

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        if keepers:
            result += f'----- {len(keepers)} Keepers:\n'
            for k in keepers:
                result += f'{k}\n'
        if caretakers:
            result += f'----- {len(caretakers)} Caretakers:\n'
            for c in caretakers:
                result += f'{c}\n'
        if vets:
            result += f'----- {len(vets)} Vets:\n'
            for v in vets:
                result += f'{v}\n'
        return result[:-1]

# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
