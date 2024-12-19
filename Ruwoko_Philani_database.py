def insert(table, data):
    table.append(data)

def remove_by_id(table, record_id):
    global users, teams
    table[:] = [item for item in table if item['id'] != record_id]

def update_player(player_id, new_data):
    for player in player:
        if player['id'] == player_id:
            player.update(new_data)
            return True
    return False

def update_team(team_id, new_data):
    for team in team:
        if team['id'] == team_id:
            team.update(new_data)
            return True
    return False

def display_all(table):
    for item in table:
        print(item)

def display_by_id(table, record_id):
    record = next((item for item in table if item['id'] == record_id), None)
    if record:
        print(record)
    else:
        print("Record not found.")

def safe_input(prompt, data_type):
    while True:
        try:
            player_input = input(prompt)
            return data_type(player_input) if player_input else None
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")

# Tables
players = []
teams = []

# Menu
def menu():
    print("\nMENU")
    print("1. Add Player")
    print("2. Add Team")
    print("3. Print Player ")
    print("4. Print Team")
    print("5. Print Player by ID (or 'ppid')")
    print("6. Print Team by ID (or 'ptid')")
    print("7. Remove Player (or 'rp')")
    print("8. Remove Team (or 'rt')")
    print("9. Update Player ")
    print("10. Update Team ")
    print("Type 'quit' or 'q' to Exit")

p_id = 1
t_id = 1

# Main program loop
while True:
    menu()
    choice = input("Enter your choice: ").lower()
    print(choice)

    if choice in ['quit', 'q']:
        print("Program exited.")
        break
    elif choice == '1':
        name = input("Enter name: ")
        age = safe_input("Enter age: ", int)
        position = input("Enter position: ")
        salary= safe_input("Enter salary: ", float)
        if id is not None:
            insert(players, {'id': p_id, 'name': name, 'age': age, 'position': position, 'salary': salary})
            print("Players added successfully.")
            p_id += 1
    elif choice == '2':
        name = input("Enter product name: ")
        league = safe_input("Enter price: ", float)
        titles = input("Enter category: ")
        colour = safe_input("Enter stock quantity: ", int)
        if id is not None:
            insert(teams, {'id': t_id, 'name': name, 'league': league, 'titles': titles, 'colour': colour})
            print("Players added successfully.")
            p_id += 1
    elif choice in ['3', 'pp']:
        print("\nPlayers:")
        display_all(players, )
    elif choice in ['4', 'pp']:
        print("\nTeams:")
        display_all(teams)
    elif choice in ['5', 'ptid']:
        player_id = safe_input("Enter the Team ID: ", int)
        if player_id is not None:
            display_by_id(players, )
    elif choice in ['6', 'ppid']:
        team_id = safe_input("Enter the Team ID: ", int)
        if team_id is not None:
            display_by_id(teams, team_id)
    elif choice in ['7', 'rp']:
        player_id = safe_input("Enter the ID of the Customer to remove: ", int)
        if player_id is not None:
            remove_by_id(players, player_id)
            print("User removed successfully.")
    elif choice in ['8', 'rp']:
        team_id = safe_input("Enter the ID of the team to remove: ", int)
        if team_id is not None:
            remove_by_id(teams, team_id)
            print("Product removed successfully.")
    elif choice in ['9', 'uu']:
        player_id = safe_input("Enter the user ID to update: ", int)
        player_exists = False
        for p in players:
            if p["id"] == player_id:
                player_exists = True
       
        if player_exists == True:
            new_data = {}
            new_name= input("Enter new name (press enter to skip): ")
            if len(new_name) > 0:
                new_data['name'] = new_name
            new_age = safe_input("Enter new age (press enter to skip): ", int)
                        # Continue updating user
            if new_age is not None:
                new_data['age'] = new_age
            new_position = input("Enter new position (press enter to skip): ")
            if len(new_position) > 0:
                new_data['position'] = new_position
            new_salary = safe_input("Enter new salary (press enter to skip): ", float)
            if new_salary is not None:
                new_data['balance'] = new_salary

            # Update only non-empty fields
            new_data = {k: v for k, v in new_data.items() if v is not None}
            if update_player(player_id, new_data):
                print("Player updated successfully.")
        else:
            print("Player not found.")
    elif choice in ['10', 'up']:
        product_id = safe_input("Enter the user ID to update: ", int)
        product_exists = False
        for t in teams:
            if t["id"] == team_id:
                teams_exists = True
       
        if teams_exists == True:
            new_data = {}
            new_name= input("Enter new name (press enter to skip): ")
            if len(new_name) > 0:
                new_data['name'] = new_name
            new_league = safe_input("Enter new league (press enter to skip): ", int)
                       
            if new_league is not None:
                new_data['league'] = new_league
            new_titles = input("Enter new titles (press enter to skip): ")
            if len(new_titles) > 0:
                new_data['titles'] = new_titles
            new_colour= safe_input("Enter new colour(press enter to skip): ", int)
            if new_colour is not None:
                new_data['colour'] = new_colour

            # Update only non-empty fields
            new_data = {k: v for k, v in new_data.items() if v is not None}
            if update_team(team_id, new_data):
                print("Team updated successfully.")
        else:
            print("Team not found.")

    else:
        print("Invalid choice. Please try again.")