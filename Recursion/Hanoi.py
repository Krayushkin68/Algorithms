def move_tower(height, from_pole, to_pole, help_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, help_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, help_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):
    print("moving disk from", from_pole, "to", to_pole)


move_tower(64, "A", "B", "C")
