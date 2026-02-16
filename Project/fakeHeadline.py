import random

subjects = ["Scientists", "Politicians", "Celebrities", "Atheletes", "Teachers"]

actions = ["discover", "invent", "debate", "critisize", "support"]

places_or_thing = ["new planet", "cure for cancer", "climate change", "education reform", "space exploration"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_thing)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    cont = input("Generate another headline? (y/n): ").strip().lower()

time = 34:00