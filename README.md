# User Pairing Script

This script generates random pairings of users, ensuring that users are not paired with the same partner more than once. It reads user data and past pairings from CSV files and outputs new pairings to a CSV file.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install the required packages:**
    Make sure you have Python installed. Then, install the necessary packages using pip:
    ```bash
    pip install pandas
    ```

## Usage

1. **Prepare your data:**
    - Create a `users.csv` file with a column `Name` containing the list of user names.
    - Create a `pastpairings.csv` file with columns `User1`, `User2`, and optionally `Date` to log past pairings.

    Example `users.csv`:
    ```csv
    Name
    Alice
    Bob
    Charlie
    ```

    Example `pastpairings.csv`:
    ```csv
    User1,User2,Date
    Alice,Bob,2023-01-01
    Alice,Charlie,2023-02-01
    ```

2. **Run the script:**
    Execute the script to generate new pairings and update the past pairings:
    ```bash
    python pairing_script.py
    ```

3. **Output:**
    - `new_pairings.csv` will contain the new pairings.
    - `pastpairings.csv` will be updated with the new pairings and dates.
