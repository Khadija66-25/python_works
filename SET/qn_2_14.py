sachin_friends = ["rahul", "ganguly", "yuvi", "zaheer", "raina", "dhoni"]
dhoni_friends = ["rahul", "ganguly", "yuvi", "zaheer", "raina", "kohli", "sachin"]

# display all users


sachin_frnd = set(sachin_friends)

dhoni_frnd = set(dhoni_friends)


print(sachin_frnd.union(dhoni_frnd))

print(dhoni_frnd.intersection(sachin_frnd))

print(sachin_frnd.difference(dhoni_frnd))