import random
"""----------------------------DEFINITIONS-----------------------------------"""
"""
class Definition
A class in Python is a blueprint/template for creating objects. 
Classes group related data and functions (methods) together, 
providing a way to model complex objects in a structured way.

__init__ Method
The __init__ method is a special method that initializes a new instance of a class.
This method is automatically called when you create a new object from a class.
Purpose: In Event, __init__ initializes each event with a description (what happens) 
and damage (the level of damage it causes).


self Keyword
self is a reference to the current instance of the class. 
It allows the instance to access its own attributes and methods. 
When defining instance methods, self is always the first parameter, although it’s not passed when the method is 
called.


.strip
Return a copy of the string with leading and trailing whitespace removed.


"""


class Event:
    """
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
        self.damage = damage  # "Slightly Damaged", "Severely Damaged", "Totaled".
        self.tires_upgraded = False
        #Initializes a tires_upgraded attribute, as a flag for whether upgraded tires are available to reduce damage.


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
        # This line creates a dictionary called choices that maps each direction ('left', 'straight', 'right')
        # to its corresponding event.
        # This setup allows the program to retrieve the appropriate event when the player chooses a direction.


    def get_event(self, choice):
        """
        :description: Retrieves the event based on the player’s choice.
        :param choice: A string representing the player's choice ('left', 'straight', or 'right').
        :return:Uses choice.lower() to ensure case-insensitive matching and retrieves the corresponding
                Event object from choices. Returns None if the choice isn’t valid.
        """
        return self.choices.get(choice.lower())
        # Ensures that the player's choice is case-insensitive.
        # self.choices.get Retrieves the Event instance that corresponds to the player's direction choice.
        # If the choice is not in the dictionary, it will return None.


class Level:
    # This segment completes the Turn class, which allows the game to handle a player’s directional choice
    # by mapping each option to a unique event.
    def __init__(self, name, turns,random_event_chance):
        #The __init__ method sets these attributes for each Level instance.

        """
        :param name: String
        :param turns: List, The list of turn objects
        """
        self.name = name
        # The name of the level (a string), like "Suburban Roads", "Countryside Roads" or "Mountain Roads".
        self.turns = turns
        # A list of Turn objects, which represents the sequence of choices the player will encounter in the level.
        self.random_event_chance = random_event_chance
        #A float (e.g., 0.1 or 0.2) that determines the likelihood of a random event occurring within this level.


class Game:

    SLIGHT_DAMAGE_COST = 250
    # The cost in $ when the car suffers slight damage.
    SEVERE_DAMAGE_COST = 500
    # The cost in $ when the car suffers severe damage.
    TOTAL_DAMAGE_COST = 2000
    # The cost in $ when the car suffers total damage.


    def __init__(self):
        """
        Attributes:
            1.levels: An empty list that will hold all levels in the game. Each level can include multiple turns.
            2.current_level: Tracks which level the player is on.
        Purpose: Manages the player's progression through levels, holding the game structure.
        :description: Initializes a new game instance for a specific player.
        """
        self.levels = self.create_levels()
        # Stores all levels in the game, generated by calling self.create_levels()
        self.current_level_index = 0
        # Tracks which level the player is currently on, starting at 0.
        self.current_turn_index = 0
        #  Tracks the current turn within a level, also starting at 0.
        self.car_status = "Healthy"
        # Represents the current condition of the car, initially set to "Healthy".
        self.money_lost = 2000
        # Stores the initial amount of money lost at the mechanic, set to 2000.
        self.tires_upgraded = False
        # A boolean flag indicating whether the player has upgraded their tires.


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
            # Shuffles each level’s turns for added variability in gameplay.

        return levels
        # Returns the list of levels to be stored in self.levels in the game’s __init__ method.


    def reset_game(self):
        """
        :return: Resets the game state to its initial conditions, simulating a restart after a total car loss.
        """
        print("\n--- Whoa! Your car just took a one-way trip to the junkyard! ---")
        print("--- It’s now officially a metal pancake! ---")
        print("--- You’re going back to MrMecanique1994, who’s probably trying to figure out "
            "if he can use the parts for a new coffee table. ---")
        self.current_level_index = 0
        # Reset to 0, ensuring the game restarts from the first level and first turn.
        self.current_turn_index = 0
        # Reset to 0, ensuring the game restarts from the first level and first turn.
        self.car_status = "Healthy"
        # Set back to "Healthy".
        self.money_lost = 2000
        # Reset to $2000 as if the player is starting fresh with the Samsarica_Gelu14’s initial fee.
        self.tires_upgraded = False
        # Set to False, indicating the player must choose the tire upgrade option again in the new game.
        input("Please press Enter to try again...")
        # Prompts the player to press Enter, pausing the game until they’re ready to restart,
        # adding a small interactive element before resetting.


    def random_event(self):
    # Defines a method that returns a favorable event where there’s no damage.
        return Event("Clear path! No issues this turn.", "Healthy")
        # This event is returned when the player encounters a random event chance that results in no obstacles.


    def offer_tire_upgrade(self):
    # Offer the upgrade only if tires are not upgraded yet.
        if not self.tires_upgraded:
        # Checks if the tires haven’t been upgraded yet to prevent re-offering the option.
            while True:
                upgrade_choice = input("Would you like to upgrade tires for $500 to reduce "
                                       "pothole damage risk? (yes/no): ").strip().lower()
                # Loop until a valid input is given
                if upgrade_choice == "yes":
                    self.money_lost += 500
                    # Adds $500 to self.money_lost, recording the upgrade cost.
                    self.tires_upgraded = True
                    print("Tires upgraded! Pothole damage risk reduced.")
                    # Sense of comfort added. Just a trick mwuhaha!
                    break  # Exit the loop after the upgrade.
                elif upgrade_choice == "no":
                    print("You chose not to upgrade tires.")
                    # Prints this message if input is "no".
                    break
                    # Exit the loop if they decline the upgrade.
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    # Print for invalid inputs.
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
            #  Checks if it’s the first turn in the level, offering a tire upgrade.

        print(f"\nLevel: {level.name} | Turn: {turn_number + 1}/{len(level.turns)}")
        # Displays the level name and the current turn number out of the total turns in the level.

        while True:
        # Ensures that the player provides a valid path choice.
            choice = input("Choose your path (Left / Straight ahead / Right): ").strip().lower()
            # Asks the player to choose between left, straight, or right.
            if choice in ['left', 'straight', 'right']:
                break
                # Exit the loop if the choice is valid.
            else:
                print("Invalid choice. Please choose 'left', 'straight', or 'right'.")
                # If not valid, prints this message prompting the player to enter a correct choice.

        if random.random() < level.random_event_chance:
            # Generates a random number and compares it to the level’s random event chance.
            event = self.random_event()
            # Calls self.random_event() to generate a no-issue event
            print("Event:", event.description)
            # Prints "Event: <description>" (e.g., "Clear path! No issues this turn.").
        else:
            event = turn.get_event(choice)
            # Calls get_event() on turn with the player’s choice to fetch the corresponding event for the path.
            print("Event:", event.description)
            # Prints the event description (e.g., "A pedestrian suddenly walks out. You swerve to avoid.").

        print(f"Car status: {event.damage}")
        # Process the selected event.

        if event.damage == "Totaled":
            # If the damage attribute of the event is "Totaled" :
            self.reset_game()
            # Calling the reset_game() method to reset the game state.
            return False
            # After resetting, it returns False to indicate that the turn (and effectively the level)
            # could not be completed due to the car being totaled.
        elif event.damage == "Severely Damaged":
        # If the event’s damage level is "Severely Damaged":
            self.car_status = "Severely Damaged"
            # Sets self.car_status to "Severely Damaged" to keep track of the car's current condition.
            self.money_lost += self.SEVERE_DAMAGE_COST
            # Increases self.money_lost by SEVERE_DAMAGE_COST, a fixed cost defined earlier,
            # to account for the additional repair expense due to severe damage.
            print(f"You lost an additional ${self.SEVERE_DAMAGE_COST} for repairs.")
            # Prints a message indicating the repair cost lost for severe damage.
        elif event.damage == "Slightly Damaged":
        # If the event’s damage level is "Slightly Damaged":
            if self.car_status != "Severely Damaged":
            # If the car status is not already set to "Severely Damaged."
                self.car_status = "Slightly Damaged"
                # If the car isn’t already "Severely Damaged," it updates the car status to "Slightly Damaged."
            self.money_lost += self.SLIGHT_DAMAGE_COST
            # Adds the cost associated with slight damage to self.money_lost.
            print(f"You lost an additional ${self.SLIGHT_DAMAGE_COST} for repairs.")
            # Printing a message indicating the cost added due to slight damage.

        print(f"Total Money Lost: ${self.money_lost}")
        # Displays the total amount of money lost due to repairs so far.
        input("Press Enter to continue...")
        # Pauses the game until the player presses Enter.
        # This provides a moment to process the information before moving to the next turn.
        return True
        # Indicates that this turn was completed successfully and allows the game to proceed to the next one.


    def play_level(self, level):
        """
        :param level:
        :return: If success is False, the method returns that the level was not completed successfully.
        If all turns are successfully completed, the method returns that the level was completed without any issues.
        """
        for turn_number, turn in enumerate(level.turns):
        # Loops through each turn in the level by iterating over level.turns, which is a list of turn objects.
            success = self.play_turn(level, turn_number, turn)
            # Calls the play_turn method for each turn, passing in the current level, turn number, and turn object.
            # Stores the result (True or False) in success.
            if not success:
                # Checks if success is False.
                # If play_turn returns False (indicating a "Totaled" car status),
                # it breaks out of this level by returning False
                return False
                # Car was totaled, restart the game
        return True
        # If all turns are completed without totaling the car, the level is considered successfully completed,
        # so it returns True.


    def start_game(self):
    # Defines the start_game method, which initiates and runs the entire game sequence across all levels.
        print("=== The Road Wrecker's Adventure! ===")
        print("""This is a game where every turn is a gamble with potholes, pedestrians, and stray shopping carts.
Your journey begins after purchasing your car for $2000.
Get ready to laugh, lose money, and dodge your way through the ultimate test of driver’s luck.
But beware of treacherous roads ahead!""")

        while self.current_level_index < len(self.levels):
        # loop runs as long as there are more levels to play, determined by checking if
        # self.current_level_index is less than the number of levels in the game.

            current_level = self.levels[self.current_level_index]
            # Retrieves the current level to play based on self.current_level_index.
            print(f"--- Starting Level {self.current_level_index + 1}: {current_level.name} ---")
            # Prints the current level’s name and number to indicate the beginning of a new level.
            quit_choice = input("Press Enter to start the level, or type 'quit' to exit the game: ").strip().lower()
            # Giving the option to the player to quit/start before each level if they want to.
            if quit_choice == 'quit':
            # Checks if the player entered "quit."
                print("Thanks for playing! Goodbye!")
                # Prints a farewell message if the player chooses to quit.
                exit()

            level_completed = self.play_level(current_level)
            #  Calls the play_level method for the current level.
            #  The result (True or False) is stored in level_completed.

            if level_completed:
            # If play_level returned True, the level was completed.
                print(f"--- Completed Level {self.current_level_index + 1}: {current_level.name} ---\n")
                # Prints a message indicating successful completion of the level.
                self.current_level_index += 1
                # Increments current_level_index to move to the next level.
            else:
                return self.start_game()
                # If the level wasn’t completed (car was "Totaled"), it restarts the game by calling start_game() again.

        print("=== Congratulations! You've made it home safely! ===")
        print(f"Total Money Lost: ${self.money_lost}")
        print("Thank you for playing!")


game = Game()
# Creates a new instance of the Game class, initializing the game.
game.start_game()
# Calls the start_game method on the game instance to begin the game sequence.



