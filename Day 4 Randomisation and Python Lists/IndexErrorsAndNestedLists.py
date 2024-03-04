state_of_america = ["Delaware", "Pennsylvania"]
print(state_of_america[0])
print(state_of_america[-1])
state_of_america.append("Angelaland") #append is used to add the item at the last of the list
print(state_of_america)
state_of_america.extend(["Angelaland", "Jack Bauer Land"]) #adds the additional list to the primary list
print(state_of_america)
num_of_states = len(state_of_america)
print(state_of_america[num_of_states - 1])

#Nested Lists

#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)