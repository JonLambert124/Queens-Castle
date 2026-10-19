"""IT 140 Project Two text-based adventure game."""

# Jonathan Lambert


def show_instructions():
    """Display the game goal and valid player commands."""
    print("\nQueen's Castle")
    print("Collect all six royal items before entering the Throne Room.")
    print("If you enter early, The Crown's Shadow will stop your mission.")
    print("Move commands: go north, go south, go east, go west")
    print("Item command: get <item name>")


def show_status(current_room, inventory, rooms):
    """Display the current room, inventory, and any available item."""
    print("\n----------------------")
    print(f"You are in the {current_room}.")
    print(f"Inventory: {inventory}")

    room_item = rooms[current_room].get("item")
    if room_item and room_item not in inventory:
        print(f"You see a {room_item}.")

    print("----------------------")


def get_item(requested_item, current_room, inventory, rooms):
    """Validate an item request, update inventory, and remove a collected item."""
    for collected_item in inventory:
        if requested_item == collected_item.lower():
            print("That item is already in your inventory.")
            return

    room_item = rooms[current_room].get("item")
    if room_item and requested_item == room_item.lower():
        inventory.append(room_item)
        del rooms[current_room]["item"]
        print(f"{room_item} added to inventory.")
    else:
        print("That item is not available in this room.")


def main():
    """Run the complete text-based adventure game."""
    # Each room lists valid directions and, except for the start and villain
    # rooms, one collectible item.
    rooms = {
        "Great Hall": {"north": "Throne Room", "west": "Club Cellar"},
        "Royal Library": {
            "south": "Diamond Gallery",
            "east": "Queen's Path",
            "item": "Ace of Insight",
        },
        "Diamond Gallery": {
            "north": "Royal Library",
            "east": "Throne Room",
            "south": "Club Cellar",
            "item": "Diamond Seal",
        },
        "Royal Armory": {
            "west": "Queen's Path",
            "south": "Spade Courtyard",
            "item": "Jack's Shield",
        },
        "Club Cellar": {
            "north": "Diamond Gallery",
            "east": "Great Hall",
            "item": "Club Key",
        },
        "Queen's Path": {
            "west": "Royal Library",
            "east": "Royal Armory",
            "south": "Throne Room",
            "item": "Queen's Compass",
        },
        "Spade Courtyard": {
            "north": "Royal Armory",
            "west": "Throne Room",
            "item": "Spade Standard",
        },
        "Throne Room": {
            "north": "Queen's Path",
            "south": "Great Hall",
            "east": "Spade Courtyard",
            "west": "Diamond Gallery",
        },
    }
    villain_room = "Throne Room"
    required_item_count = 6
    current_room = "Great Hall"
    inventory = []

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip().lower()
        command_parts = command.split(maxsplit=1)

        if len(command_parts) != 2:
            print("Invalid command. Use 'go <direction>' or 'get <item name>'.")
            continue

        action, value = command_parts

        if action == "go":
            if value not in ("north", "south", "east", "west") or value not in rooms[current_room]:
                print("You cannot go that way.")
                continue

            current_room = rooms[current_room][value]

            if current_room == villain_room:
                if len(inventory) == required_item_count:
                    print("\nCongratulations! You collected all royal items and defeated The Crown's Shadow!")
                else:
                    print("\nThe Crown's Shadow catches you before your mission is complete. GAME OVER!")
                print("Thanks for playing Queen's Castle.")
                break

        elif action == "get":
            get_item(value, current_room, inventory, rooms)

        else:
            print("Invalid command. Use 'go <direction>' or 'get <item name>'.")


if __name__ == "__main__":
    main()
