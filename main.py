import random
"""----------------------------DEFINITIONS-----------------------------------"""
"""
class Definition
A class in Python is a blueprint for creating objects. Classes group related data and functions (methods) together, 
providing a way to model complex objects in a structured way.

__init__ Method
The __init__ method is a special method that initializes a new instance of a class.
This method is automatically called when you create a new object from a class.
Purpose: In Event, __init__ initializes each event with a description (what happens) 
and damage (the level of damage it causes).


self Keyword
self is a reference to the current instance of the class. 
It allows the instance to access its own attributes and methods. 
When defining instance methods, self is always the first parameter, although it’s not passed when the method is called.

"""
class Event:
    """
    Attributes: description and damage.
    Purpose: Represents a specific event that can happen in the game, with details on what the event is and the damage
    it causes.
    """
    def __init__(self, description, damage):
        """
        :param description: A string that describes the event (e.g., "You hit a pothole").
        :param damage: A string indicating the damage level ("Slightly Damaged", "Severely Damaged", or "Totaled").
        :function: Sets 'self.description' and 'self.damage' for each Event instance.
        """
        self.description = description
        self.damage = damage  # "Slightly Damaged", "Severely Damaged", "Totaled"
        self.tires_upgraded = False

class Turn:
    """
    Attributes: choices, a dictionary that maps the player's options to Event objects.
    Methods: get_event() retrieves an event based on the player’s choice (left, straight, or right).
    """
    def __init__(self, left_event, straight_event, right_event):
        """
        :description: Initializes a Turn instance by setting up options for left, straight, and right events.
        :param left_event, straight_event, right_event : Each is an Event object that will be stored in a dictionary
                                                        called choices, mapping the direction to the specific event.
        :function: Sets up choices in the form of a dictionary, so the player can choose a direction,
                    and the game can retrieve the corresponding event.
        """
        self.choices = {
            'left': left_event,
            'straight': straight_event,
            'right': right_event
        }

    def get_event(self, choice):
        """
        :description: Retrieves the event based on the player’s choice.
        :param choice: A string representing the player's choice ('left', 'straight', or 'right').
        :return:Uses choice.lower() to ensure case-insensitive matching and retrieves the corresponding
                Event object from choices. Returns None if the choice isn’t valid.
        """
        return self.choices.get(choice.lower())

class Level:
    def __init__(self, name, turns,random_event_chance):
        """
        :param name: String
        :param turns: List, The list of turn objects
        """
        self.name = name
        self.turns = turns  # List of turn objects
        self.random_event_chance = random_event_chance
class Game:
    """
    Attributes:
        1.levels: An empty list that will hold all levels in the game. Each level can include multiple turns.
        2.current_level: Tracks which level the player is on.
    Purpose: Manages the player's progression through levels, holding the game structure.
    """
    SLIGHT_DAMAGE_COST = 250
    SEVERE_DAMAGE_COST = 500
    TOTAL_DAMAGE_COST = 2000

    def __init__(self):
        """
        :description: Initializes a new game instance for a specific player.
        """
        self.levels = self.create_levels()
        self.current_level_index = 0
        self.current_turn_index = 0
        self.car_status = "Healthy" # Represents the current condition of the car, initially set to "Healthy"
        self.money_lost = 2000# Stores the initial amount of money lost at the mechanic, set to 2000
        self.tires_upgraded = False # A boolean flag indicating whether the player has upgraded their tires

    def create_levels(self):
        suburban_turns = [
            Turn(
                Event("You hit a pothole the size of a golf ball.", "Slightly Damaged"),
                Event("A pedestrian suddenly walks out. You swerve to avoid.", "Slightly Damaged"),
                Event("Narrow road with parked cars, you clip a side mirror.", "Severely Damaged"),
            ),
            Turn(
                Event("A speed bump ahead, your car bottoms out.", "Slightly Damaged"),
                Event("Construction zone with debris.", "Severely Damaged"),
                Event("You rear-end someone at a sudden traffic stop.", "Totaled")
            ),
            Turn(
                Event("A dog runs across the road. You swerve to avoid.", "Slightly Damaged"),
                Event("Skid on a wet road.", "Severely Damaged"),
                Event("Avoided a cyclist just in time.", "Slightly Damaged")
            ),
            Turn(
                Event("Hit a parked truck's tailgate.", "Totaled"),
                Event("You swerve to avoid debris.", "Slightly Damaged"),
                Event("Clip a pothole, damaging the suspension.", "Slightly Damaged")
            ),
            Turn(
                Event("A fallen tree blocks the road.", "Severely Damaged"),
                Event("Lost control on a sharp turn.", "Severely Damaged"),
                Event("Your tires blow out unexpectedly.", "Slightly Damaged")
            ),
            Turn(
                Event("Hit a pothole, damaging the tires.", "Slightly Damaged"),
                Event("A sudden hailstorm damages the windshield.", "Severely Damaged"),
                Event("Collision with a stray shopping cart.", "Totaled")
            ),
            Turn(
                Event("Minor scrape with a parked car.", "Slightly Damaged"),
                Event("Failed to brake in time, causing minor damage.", "Slightly Damaged"),
                Event("Overturned on a slippery road.", "Severely Damaged")
            ),
            Turn(
                Event("Hit a small curb.", "Slightly Damaged"),
                Event("Side mirror knocked off.", "Severely Damaged"),
                Event("Total loss in a minor collision.", "Totaled")
            ),
            Turn(
                Event("Broken headlight from a minor bump.", "Slightly Damaged"),
                Event("Damage to the car's bumper.", "Slightly Damaged"),
                Event("Engine trouble from hitting a pothole.", "Severely Damaged")
            ),
            Turn(
                Event("Lost a tire on a rough patch.", "Severely Damaged"),
                Event("Minor fender bender.", "Slightly Damaged"),
                Event("Total loss from a major collision.", "Totaled")
            )
        ]

        countryside_turns = [
            Turn(
                Event("You hit a pothole the size of a golf ball.", "Slightly Damaged"),
                Event("A pedestrian suddenly walks out. You swerve to avoid.", "Slightly Damaged"),
                Event("Narrow road with parked cars, you clip a side mirror.", "Severely Damaged")
            ),
            Turn(
                Event("A speed bump ahead, your car bottoms out.", "Slightly Damaged"),
                Event("Construction zone with debris.", "Severely Damaged"),
                Event("You rear-end someone at a sudden traffic stop.", "Totaled")
            ),
            Turn(
                Event("A dog runs across the road. You swerve to avoid.", "Slightly Damaged"),
                Event("Skid on a wet road.", "Severely Damaged"),
                Event("Avoided a cyclist just in time.", "Slightly Damaged")
            ),
            Turn(
                Event("Hit a parked truck's tailgate.", "Totaled"),
                Event("You swerve to avoid debris.", "Slightly Damaged"),
                Event("Clip a pothole, damaging the suspension.", "Slightly Damaged")
            ),
            Turn(
                Event("A fallen tree blocks the road.", "Severely Damaged"),
                Event("Lost control on a sharp turn.", "Severely Damaged"),
                Event("Your tires blow out unexpectedly.", "Slightly Damaged")
            ),
            Turn(
                Event("Hit a pothole, damaging the tires.", "Slightly Damaged"),
                Event("A sudden hailstorm damages the windshield.", "Severely Damaged"),
                Event("Collision with a stray shopping cart.", "Totaled")
            ),
            Turn(
                Event("Minor scrape with a parked car.", "Slightly Damaged"),
                Event("Failed to brake in time, causing minor damage.", "Slightly Damaged"),
                Event("Overturned on a slippery road.", "Severely Damaged")
            ),
            Turn(
                Event("Hit a small curb.", "Slightly Damaged"),
                Event("Side mirror knocked off.", "Severely Damaged"),
                Event("Total loss in a minor collision.", "Totaled")
            ),
            Turn(
                Event("Broken headlight from a minor bump.", "Slightly Damaged"),
                Event("Damage to the car's bumper.", "Slightly Damaged"),
                Event("Engine trouble from hitting a pothole.", "Severely Damaged")
            ),
            Turn(
                Event("Lost a tire on a rough patch.", "Severely Damaged"),
                Event("Minor fender bender.", "Slightly Damaged"),
                Event("Total loss from a major collision.", "Totaled")
            )
        ]

        mountain_turns = [
            Turn(
                Event("Loose rocks hit the windshield.", "Slightly Damaged"),
                Event("Sharp cliff edge causes you to lose control.", "Totaled"),
                Event("Sudden drop in the road surface.", "Severely Damaged")
            ),
            Turn(
                Event("Small landslide, need to reverse.", "Slightly Damaged"),
                Event("Brake failure on a downhill slope.", "Totaled"),
                Event("Narrow path with overhanging branches.", "Severely Damaged")
            ),
            Turn(
                Event("Clip the guardrail on a narrow path.", "Severely Damaged"),
                Event("Avalanche warning, you make it through.", "Slightly Damaged"),
                Event("Rock slide debris on the road.", "Severely Damaged")
            ),
            Turn(
                Event("Minor damage from loose gravel.", "Slightly Damaged"),
                Event("Severely damaged from hitting a large rock.", "Severely Damaged"),
                Event("Total loss from falling off a cliff.", "Totaled")
            ),
            Turn(
                Event("Worn-out tires slip on icy road.", "Severely Damaged"),
                Event("Minor scrape with a mountain sign.", "Slightly Damaged"),
                Event("Total loss after collision with a large boulder.", "Totaled")
            ),
            Turn(
                Event("Minor damage from a loose stone.", "Slightly Damaged"),
                Event("Severely damaged suspension from rough terrain.", "Severely Damaged"),
                Event("Total loss from a major accident.", "Totaled")
            ),
            Turn(
                Event("Hit a small branch.", "Slightly Damaged"),
                Event("Side mirror damaged from a collision.", "Severely Damaged"),
                Event("Total loss from rolling off the path.", "Totaled")
            ),
            Turn(
                Event("Minor fender bender with a fellow traveler.", "Slightly Damaged"),
                Event("Severely damaged from hitting a large rock.", "Severely Damaged"),
                Event("Totaled after sliding off the road.", "Totaled")
            ),
            Turn(
                Event("Minor damage from hitting a small hill.", "Slightly Damaged"),
                Event("Severely damaged from scraping the undercarriage.", "Severely Damaged"),
                Event("Total loss from a severe collision.", "Totaled")
            ),
            Turn(
                Event("Swerve to avoid a goat blocks the road and fall off the cliff.", "Totaled"),
                Event("Minor damage from a loose rock.", "Slightly Damaged"),
                Event("Severely damaged from hitting a tree.", "Severely Damaged")
            )
        ]
        levels = [
            Level("Suburban Roads", suburban_turns, random_event_chance=0.1),
            Level("Countryside Roads", countryside_turns, random_event_chance=0.2),
            Level("Mountain Roads", mountain_turns, random_event_chance=0.3)
        ]
        for level in levels:
            random.shuffle(level.turns)

        return levels

    def reset_game(self):
        """
        :return: Resets the game state to its initial conditions, simulating a restart after a total car loss.
        """
        print("\n--- Whoa! Your car just took a one-way trip to the junkyard! ---")
        print("--- It’s now officially a metal pancake! ---")
        print("--- You’re going back to MrMecanique1994, who’s probably trying to figure out "
            "if he can use the parts for a new coffee table. ---")
        self.current_level_index = 0
        self.current_turn_index = 0
        self.car_status = "Healthy"
        self.money_lost = 2000
        self.tires_upgraded = False  # Reset tire upgrade status
        input("Please press Enter to try again...")

    def random_event(self):
        return Event("Clear path! No issues this turn.", "Healthy")

    def offer_tire_upgrade(self):
        if not self.tires_upgraded:  # Offer the upgrade only if tires are not upgraded yet
            while True:  # Loop until a valid input is given
                upgrade_choice = input("Would you like to upgrade tires for $500 to reduce "
                                       "pothole damage risk? (yes/no): ").strip().lower()

                if upgrade_choice == "yes":
                    self.money_lost += 500  # Add $500 to the money instead of deducting it
                    self.tires_upgraded = True
                    print("Tires upgraded! Pothole damage risk reduced.")
                    break  # Exit the loop after the upgrade
                elif upgrade_choice == "no":
                    print("You chose not to upgrade tires.")
                    break  # Exit the loop if they decline the upgrade
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")  # Handle invalid inputs
        else:
            print("Tires are already upgraded.")

    def play_turn(self, level, turn_number, turn):
        """
        Description: Plays a single turn within a specified level, displaying level and turn information,
        and prompting the player to make a directional choice.
        :param level: Level, The current level object that contains information about the level.
        :param turn_number: Integer, The index of the current turn within the level, starting from 0.
        :param turn: turn : Turn, The current turn object that contains information about the specific turn.
        :return: Level: City Streets | Turn: 2/3, Choose your path (Left / Straight ahead / Right):
        """
        if turn_number == 0:
            self.offer_tire_upgrade()

        print(f"\nLevel: {level.name} | Turn: {turn_number + 1}/{len(level.turns)}")

        while True:
            choice = input("Choose your path (Left / Straight ahead / Right): ").strip().lower()
            if choice in ['left', 'straight', 'right']:
                break  # Exit the loop if the choice is valid
            else:
                print("Invalid choice. Please choose 'left', 'straight', or 'right'.")

        if random.random() < level.random_event_chance:  # Use the level's random event chance
            event = self.random_event()  # Random event instead of a path-based event
            print("Event:", event.description)
        else:
            event = turn.get_event(choice)  # Use the event from the chosen path
            print("Event:", event.description)

        print(f"Car status: {event.damage}") # Process the selected event

        if event.damage == "Totaled":
            self.reset_game()
            return False
        elif event.damage == "Severely Damaged":
            self.car_status = "Severely Damaged"
            self.money_lost += self.SEVERE_DAMAGE_COST
            print(f"You lost an additional ${self.SEVERE_DAMAGE_COST} for repairs.")
        elif event.damage == "Slightly Damaged":
            if self.car_status != "Severely Damaged":
                self.car_status = "Slightly Damaged"
            self.money_lost += self.SLIGHT_DAMAGE_COST
            print(f"You lost an additional ${self.SLIGHT_DAMAGE_COST} for repairs.")

        print(f"Total Money Lost: ${self.money_lost}")
        input("Press Enter to continue...")
        return True

    def play_level(self, level):
        """
        :param level:
        :return: If success is False, the method returns that the level was not completed successfully.
        If all turns are successfully completed, the method returns that the level was completed without any issues.
        """
        for turn_number, turn in enumerate(level.turns):
            success = self.play_turn(level, turn_number, turn)
            if not success:
                return False  # Car was totaled, restart the game

        return True  # Level completed

    def start_game(self):
        print("=== The Road Wrecker's Adventure! ===")
        print("""
This is a game where every turn is a gamble with potholes, pedestrians, and stray shopping carts.
Your journey begins after purchasing your car for $2000.
Get ready to laugh, lose money, and dodge your way through the ultimate test of driver’s luck.
But beware of treacherous roads ahead!
                """)

        while self.current_level_index < len(self.levels):
            current_level = self.levels[self.current_level_index]
            print(f"--- Starting Level {self.current_level_index + 1}: {current_level.name} ---")
            level_completed = self.play_level(current_level)
            if level_completed:
                print(f"--- Completed Level {self.current_level_index + 1}: {current_level.name} ---\n")
                self.current_level_index += 1
            else:
                # Car was totaled, reset to start
                return self.start_game()

        print("=== Congratulations! You've made it home safely! ===")
        print(f"Total Money Lost: ${self.money_lost}")
        print("Thank you for playing!")


if __name__ == "__main__":
    game = Game()
    game.start_game()
