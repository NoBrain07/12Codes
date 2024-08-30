# 15	Write a function in Python , Push(Vehicle) where, Vehicle is a dictionary containing details of vehicles–{Car_Name: Maker}.
# The function should push the name of car manufactured by 'TaTA’ (including all the possible cases like Tata,TaTa, etc.) to the stack. For example
# If the dictionary contains the following data:
# Vehicle={'Santro' : 'Hyundai', 'Nexon': 'Tata', 'Safari': 'Tata'}
# The stack should contain
# Safari
# Nexon

stack = []

vehicles = {"Santro": "Hyundai", "Nexon": "Tata", "Safari": "Tata"}


def push(vehicle):
    stack.extend([x for x, y in vehicle.items() if y.lower() == "tata"][::-1])


def show_all():
    print("\n".join(stack))


push(vehicles)
