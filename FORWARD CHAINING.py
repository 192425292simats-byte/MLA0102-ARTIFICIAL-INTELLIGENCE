facts = {"computer_not_starting", "power_light_off"}

rules = [
    ({"computer_not_starting", "power_light_off"}, "power_supply_problem"),
    ({"power_supply_problem"}, "check_power_cable"),
    ({"check_power_cable"}, "computer_needs_service")
]

for conditions, conclusion in rules:
    if conditions <= facts:
        facts.add(conclusion)
        print("Derived:", conclusion)

print("\nFinal Facts:", facts)
