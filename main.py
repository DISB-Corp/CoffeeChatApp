import pandas as pd
import random
from datetime import datetime

# Load the user list and previous pairings
users_df = pd.read_csv('users.csv')
past_pairings_df = pd.read_csv('pastpairings.csv')

# Convert user list to a list of names
users = users_df['Name'].tolist()

# Convert past pairings to a set of tuples for easy lookup
past_pairings = set(tuple(sorted(pair)) for pair in past_pairings_df[['User1', 'User2']].values.tolist())

# Shuffle the user list to ensure random pairings
random.shuffle(users)

# Function to create new pairings
def create_new_pairings(users, past_pairings):
    new_pairings = []
    unmatched_users = []

    for i in range(0, len(users) - 1, 2):
        pair = tuple(sorted((users[i], users[i + 1])))
        if pair not in past_pairings:
            new_pairings.append(pair)
            past_pairings.add(pair)
        else:
            unmatched_users.extend([users[i], users[i + 1]])

    if len(users) % 2 == 1:
        unmatched_users.append(users[-1])

    # Try to pair the unmatched users
    for i in range(0, len(unmatched_users) - 1, 2):
        pair = tuple(sorted((unmatched_users[i], unmatched_users[i + 1])))
        new_pairings.append(pair)

    if len(unmatched_users) % 2 == 1:
        new_pairings.append((unmatched_users[-1], 'No Pair'))

    return new_pairings

new_pairings = create_new_pairings(users, past_pairings)

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Save the new pairings to an Excel file with the current date
new_pairings_df = pd.DataFrame(new_pairings, columns=['User1', 'User2'])
new_pairings_df['Date'] = current_date
new_pairings_df.to_csv('new_pairings.csv', index=False)

# Update the past pairings DataFrame with new pairings and dates
updated_past_pairings_df = pd.concat([past_pairings_df, new_pairings_df[['User1', 'User2', 'Date']]])
updated_past_pairings_df.to_csv('pastpairings.csv', index=False)

print("New pairings have been saved to new_pairings.csv and pastpairings.csv has been updated")
