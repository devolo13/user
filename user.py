class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points -= amount
        else:
            print("User does not have the required balance")
            return False

devin = User("devin", "lozano", "email@email.com", 26)
devin.enroll()
devin.display_info()

steven = User("steven", "stevenson", "steven@steven.com", 42)
edward = User("edward", "edwards", "edward@edward.com", 67)

devin.spend_points(50)
steven.enroll()
devin.display_info()
steven.display_info()
edward.display_info()
edward.spend_points(40)