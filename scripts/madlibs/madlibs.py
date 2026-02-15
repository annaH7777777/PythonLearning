import random

templates = [
    {
        "name": "Hospital Story",
        "text": "It was about {} {} ago when I arrived at the hospital in a {}. "
                "The hospital is a {} place, there are a lot of {} {} here." 
                "There are nurses here who have {} {}. "
                "If someone wants to come into my room I told them that they have to {} first. "
                "I’ve decorated my room with {} {}. "
                "Today I talked to a doctor and they were wearing a {} on their {}. "
                "I heard that all doctors {} {} every day for breakfast. "
                "The most {} thing about being in the hospital is the {} {}!",
        "prompts": [
            "Number",
            "Measure of time",
            "Mode of transportation",
            "Adjective",
            "Adjective",
            "Noun",
            "Color",
            "Part of the body",
            "Verb",
            "Number",
            "Noun",
            "Noun",
            "Part of the body",
            "Verb",
            "Noun",
            "Adjective",
            "Silly word",
            "Noun"
        ]
    },
    {
        "name": "Camping Story",
        "text": "This weekend I am going camping with {}. "
                "I packed my lantern, sleeping bag, and {}. "
                "I am so {} to {} in a tent. "
                "I am {} we might see a(n) {}, I hear they’re kind of dangerous. "
                "While we’re camping, we are going to hike, fish, and {}. "
                "I have heard that the {} lake is great for {}. "
                "Then we will {} hike through the forest for {} {}. "
                "If I see a {} {} while hiking, I am going to bring it home as a pet! "
                "At night we will tell {} {} stories and roast {} around the campfire!!",
        "prompts": [
            "Person's name",
            "Noun",
            "Feeling adjective",
            "Verb",
            "Feeling adjective",
            "Animal",
            "Verb",
            "Color",
            "Verb ending in ing",
            "Adverb ending in ly",
            "Number",
            "Measure of time",
            "Color",
            "Animal",
            "Number",
            "Silly word",
            "Noun"
        ]
    },
    {
        "name": "Enchanted forest",
        "text": "Dear {}, I am writing to you from a {} castle in an enchanted forest. "
                "I found myself here one day after going for a ride on a {} {} in {}. "
                "There are {} {} and {} {} here! "
                "In the {} there is a pool full of {}. I fall asleep each night on a {} "
                "of {} and dream of {} {}. "
                "It feels as though I have lived here for {} {}. "
                "I hope one day you can visit, although the only way to get here now is {} on a "
                "{} {}!!",
        "prompts" : [
            "Proper Noun (Person’s Name)",
            "Adjective",
            "Color",
            "Animal",
            "Place",
            "Adjective2",
            "Magical Creature (Plural)",
            "Adjective3",
            "Magical Creature (Plural)2",
            "Room in a House",
            "Noun",
            "Noun2",
            "Noun(Plural)3",
            "Adjective4",
            "Noun (Plural)4",
            "Number",
            "Measure of time",
            "Verb (ending in ing)",
            "Adjective5",
            "Noun5"
        ]
    }
]


def main():
    print("Choose a template:")
    for i in range(len(templates)):
        print(i + 1, "-", templates[i]["name"])
    print("0 - Random template")

    raw = input("Enter number: ").strip()

    if not raw.isdigit():
        print("Invalid input, using random template")
        selected_template = random.choice(templates)
        choice = -1
    else:
        choice = int(raw) - 1
        if choice == -1:
            selected_template = random.choice(templates)
        elif -1 < choice < len(templates):
            selected_template = templates[choice]
        else:
            print("Out of range, using random template")
            selected_template = random.choice(templates)
    print(choice + 1, "-", selected_template["name"])

    answers = []
    counter = len(selected_template["prompts"])
    print(f"answers type {type (answers)}")
    print(f"selected_template type {type(selected_template)}")
    while counter > 0:
        answer = input(f"Enter {selected_template['prompts'][len(selected_template['prompts']) - counter]}: ")
        answers.append(answer)
        counter -= 1
    print(answers)

    story = selected_template["text"].format(*answers)
    print("\nYour story:\n")
    print(story)


if __name__ == "__main__":
    main()
