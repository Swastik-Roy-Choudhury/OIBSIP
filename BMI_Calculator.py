# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m)^2)
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to classify BMI into categories
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main function to prompt user input and display the result
def bmi_calculator():
    # Prompt user for weight (in kilograms) and height (in meters)
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify BMI
        category = classify_bmi(bmi)

        # Display the BMI and category to the user
        print(f"\nYour BMI is: {bmi}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

# Run the BMI calculator
bmi_calculator()
