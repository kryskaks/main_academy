animals = ("bird", "fish", "insect", "bat")

# bird : can fly, has feather
# fish : can't fly, live in the water
# insect: can fly, no feather, not bat
# bat : can fly, no feather, bat


def main():
    can_it_fly = input("Can it fly?")

    if can_it_fly:
        verify_flying()

    else:
        verify_unflying()


def verify_flying():
    has_it_feather = input("Has it feather?")

    bird = "bird"

    if has_it_feather:
        print(f"It's a bird! : {bird}")
    else:
        verify_bat_or_no()


def verify_bat_or_no():
    is_it_bat = input("Is it Bat?")

    if is_it_bat:
        print("It's a Bat!")

    else:
        print("It's insect!")


def verify_unflying():
    print("Someone else")


def to_bool(entered):
    # Y, y, T, t, 1
    # N, n, F, f, 0
    if entered not in ("Y", "N"):
        raise ValueError("Unkown result")

    if entered == "Y":
        return True
    else:
        return False


main()
