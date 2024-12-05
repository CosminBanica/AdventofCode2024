"""
Solver for day 5: Print Queue
"""
from src.day_management.day_solver import DaySolver


class Day5Solver(DaySolver):
    """
    Solver for day 5: Print Queue
    """
    def get_rules_updates(self):
        rules = {}
        updates = []

        getting_rules = True
        for line in self.input_data:
            if line.strip() == "":
                getting_rules = False
                continue

            if getting_rules:
                rule = line.split("|")
                rule = (int(rule[0]), int(rule[1]))
                if rule[0] in rules:
                    rules[rule[0]].append(rule[1])
                else:
                    rules[rule[0]] = [rule[1]]
            else:
                update = line.split(",")
                updates.append([int(x) for x in update])

        return rules, updates

    def get_middle_pages_correct(self, rules, updates):
        middle_pages = []

        for update in updates:
            past_pages = [update[0]]
            update_correct = True

            for i in range(1, len(update)):
                for page in past_pages:
                    # print(f"Checking if {update[i]} is in {rules}")
                    if update[i] in rules:
                        # print(f"Checking if {page} is in {rules[update[i]]}")
                        if page in rules[update[i]]:
                            update_correct = False
                            break
                if not update_correct:
                    break
                past_pages.append(update[i])

            if update_correct:
                # print(f"Correct update: {update}")
                middle_pages.append(update[int(len(update) / 2)])

        return middle_pages

    def get_middle_pages_incorrect(self, rules, updates):
        middle_pages = []

        for j in range(0, len(updates)):
            past_pages = [updates[j][0]]
            update_correct = True

            for i in range(1, len(updates[j])):
                for k in range(0, len(past_pages)):
                    if updates[j][i] in rules:
                        if past_pages[k] in rules[updates[j][i]]:
                            # print(f"Wrong step: curr_nr:{updates[j][i]} vs past_nr:{past_pages[k]} vs rule:{rules[updates[j][i]]}")
                            update_correct = False
                            incorrect_page = updates[j][i]
                            updates[j].pop(i)
                            updates[j].insert(k, incorrect_page)
                            past_pages.insert(k, incorrect_page)
                            # print(f"After update: {updates[j]}")
                            break
                else:
                    past_pages.append(updates[j][i])

            if not update_correct:
                # print(f"Incorrect update: {updates[j]}")
                middle_pages.append(updates[j][int(len(updates[j]) / 2)])

        return middle_pages

    def solve_part_one(self):
        """
        Solves part one
        """
        rules, updates = self.get_rules_updates()

        # print(rules)
        # print(updates)

        middle_pages = self.get_middle_pages_correct(rules, updates)

        return sum(middle_pages)

    def solve_part_two(self):
        """
        Solves part two
        """
        rules, updates = self.get_rules_updates()

        # print(rules)
        # print(updates)

        middle_pages = self.get_middle_pages_incorrect(rules, updates)

        return sum(middle_pages)
