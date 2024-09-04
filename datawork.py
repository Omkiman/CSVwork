import pandas as pd 
from enum import Enum
import os

# menu items
class actions(Enum):
    ADD = 1
    REMOVE = 2
    EDIT = 3
    DISPLAY = 4
    CLEAR = 5
    EXIT = 6

# exit protocol
def exitprog():
    print("Exiting program...")
    exit()

# clear terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#load a specifiv CVS file
def loadCSV(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except:
        print("Error: Unable to load CSV file.")

# display menu
def menu():
    for i in actions:
        print(f"{i.value} - {i.name}")
    return actions(int(input("your selection? ")))

def csvInDir(directory):
    csv_files = []
    for file in os.listdir(directory):
        if file.endswith(".csv"):
            csv_files.append(file)  # Add only the file name
    return csv_files

# path to directory
script_dir = os.path.dirname(os.path.abspath(__file__))

def choosefile():
    print(f"Choose a file to work with:")
    csvfiles = csvInDir(script_dir)
    for file in csvfiles:
        print(file)
    answer = input("Enter file name (without .csv): ")
    for file in csvfiles:
        if f"{answer}.csv" in file:
            return f"C:/Users/omror/OneDrive/Desktop/python/classwork/CSVwork/{answer}.csv"
    print("file not found")
    return

def add_item(df):
    # Get the list of columns from the DataFrame
    columns = df.columns
    
    # Dictionary to hold new row data
    new_data = {}
    
    # Prompt user for each column
    print("Please provide the following information:")
    for column in columns:
        value = input(f"Enter value for {column}: ")
        new_data[column] = value
    
    # Create a DataFrame from the new row data
    new_row_df = pd.DataFrame([new_data], columns=columns)
    
    # Append the new row to the existing DataFrame
    df = pd.concat([df, new_row_df], ignore_index=True)
    
    return df

def delete_row_by_name(df):
    name_to_delete = input("Enter name: ")
    # Find the index of the row(s) where 'Name' matches name_to_delete
    indices_to_delete = df[df['Name'] == name_to_delete].index

    # Convert index to a list and get the first element
    indices_list = indices_to_delete.tolist()

    if indices_list:
        # Extract the integer value (assuming there is at least one index)
        index_value = indices_list[0]
        # Drop the row(s) by index and reset the index
        df = df.drop(index_value).reset_index(drop=True)
        print(f"Row with index {index_value} and name '{name_to_delete}' has been removed.")
    else:
        print(f"No item found with the name '{name_to_delete}'.")
    
    return df






if __name__ == "__main__":
    df = []
    while True:
        if len(df) > 0:
            selection = menu()
            if selection == actions.EXIT:
                exitprog()
            elif selection == actions.ADD:
                df = add_item(df)
            elif selection == actions.CLEAR:
                clear()
            elif selection == actions.DISPLAY:
                print(df)
            elif selection == actions.EDIT:
                pass
            elif selection == actions.REMOVE:
                df = delete_row_by_name(df)
            else:
                pass
        else:
            df = pd.read_csv(choosefile())
            print(df)
