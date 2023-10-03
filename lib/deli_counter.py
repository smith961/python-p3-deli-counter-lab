# Initialize an empty list to represent the deli line
katz_deli = []

# Function to display the current line
def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for i, person in enumerate(katz_deli, 1):
            line_str += f" {i}. {person}"
        print(line_str)

# Function to add a customer to the line
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

# Function to serve the next person in line
def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")

# Example usage:
if __name__ == "__main__":
    take_a_number(katz_deli, "Alice")
    take_a_number(katz_deli, "Bob")
    take_a_number(katz_deli, "Charlie")
    line(katz_deli)
    now_serving(katz_deli)
    line(katz_deli)
    now_serving(katz_deli)
    now_serving(katz_deli)
    line(katz_deli)