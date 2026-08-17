facts = {"fever", "cough", "body_pain"}

rules = {
    "flu": {"fever", "cough", "body_pain"},
    "cold": {"cough"},
    "infection": {"fever", "body_pain"}
}

for disease, symptoms in rules.items():
    if symptoms <= facts:
        print("Possible disease:", disease)
