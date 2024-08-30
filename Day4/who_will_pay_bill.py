import random

ardm_members = ["keerthan", "ahmed", "horit", "abhishek_pandit", "veera", "roshan"]


print(f"Person Who is going to pay for this weekend party is: {ardm_members[random.randint(0, 5)]}")

print(f"Person Who is going to pay for this weekend party is: {random.choice(ardm_members)}")