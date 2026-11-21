# Class List Manager - Group9
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====
# Written by: Leena (task 3)
def sort_names(names):
    return sorted(names)

# Written by: Ranya (task 6)
def to_upper(names):
    upper_names = []                        # variable: a new empty list
    for name in names:                      # loop: go through every name
        upper_names.append(name.upper())    # add the name in capital letters
    return upper_names

# Written by: Shaden (task 2)
def search_name(names, name):
    for n in names:              # loop: check every name in the list
        if n == name:            # if: found the name
            return True
    return False                 # the name was not found


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))
    print("Names in capital letters:", to_upper(names))


main()
