# from Attributes_and_Methods.gym_04E.project.equipment import Equipment
# from Attributes_and_Methods.gym_04E.project.exercise_plan import ExercisePlan
# from Attributes_and_Methods.gym_04E.project.subscription import Subscription
# from Attributes_and_Methods.gym_04E.project.customer import Customer
# from Attributes_and_Methods.gym_04E.project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if subscription.customer_id == c.id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if trainer.id == p.trainer_id][0]
        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]
        result = f'{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}'
        return result
        # all_objects = [subscription, customer, trainer, equipment, plan]
        # result = ''
        # for idx, obj in enumerate(all_objects):
        #     if idx == len(all_objects) - 1:
        #         result += f'{obj}'
        #     else:
        #         result += f'{obj}\n'
        # return result

# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
