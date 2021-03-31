users = [
  { "user_id": 1, "first_name": "Margaret", "last_name": "Chicken" },
  { "user_id": 2, "first_name": "Bill", "last_name": "Gates" },
  { "user_id": 3, "first_name": "Steve", "last_name": "Jobs" },
  { "user_id": 4, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 5, "first_name": "Brendan", "last_name": "Eich" },
]

# Created a LOOP to extract information on specific user from the above dictionary.
# First defined the FUNCTION with parameters
# created a FOR loop that takes "user_id" as parameter.
# if "user_id" is correct, user info is returned in the console.
# If incorrect NONE is returned to console.

def find_user(list, user_id):
    for user in list:
        if user["user_id"] == user_id:
            return user

    return "User not found" 

user_real = find_user(users,4)
user_fake = find_user(users,100)

print(user_fake)

print(user_real)



# Experimented with loop this time setting it to return user info on "first_name"
# If first_name exists user info is extracted.
# If user doesn't exist NONE is returned from found_user


def find_user(list, user_name):
      found_user = None
      for name in list:
          if name["first_name"] == user_name:
              found_user = name

      return found_user

print(find_user(users,"Barry"))
print(find_user(users,"Steve"))



