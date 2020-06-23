is_male = not False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male or is_tall:
    print("You are not a male or tall")
else:
    print("You either not male or not tall or both")

