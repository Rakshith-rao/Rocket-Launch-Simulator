# Initialize rocket state
stage = "Pre-Launch"
fuel = 100
altitude = 0
speed = 0

# Function to update rocket parameters
def update_rocket_parameters():
    global stage, fuel, altitude, speed

    # Define parameters for each stage (you may need to adjust these values)
    stages = {
        "Pre-Launch": {"fuel_depletion_rate": 0.0, "altitude_increase_rate": 0.0, "speed_increase_rate": 0.0},
        "Stage 1": {"fuel_depletion_rate": 10.0, "altitude_increase_rate": 10.0, "speed_increase_rate": 1000.0},
        "Stage 2": {"fuel_depletion_rate": 5.0, "altitude_increase_rate": 15.0, "speed_increase_rate": 1500.0},
    }

    if stage in stages:
        # Update parameters based on the current stage
        stage_data = stages[stage]
        fuel -= stage_data["fuel_depletion_rate"]
        altitude += stage_data["altitude_increase_rate"]
        speed += stage_data["speed_increase_rate"]

# Function to display rocket parameters
def display_parameters():
    print(f"Stage: {stage}, Fuel: {fuel}%, Altitude: {altitude} km, Speed: {speed} km/h")

# Function to check for stage separation
def check_stage_separation():
    global stage

    # Define conditions for stage separation (you may need to adjust these)
    if stage == "Stage 1" and altitude >= 30:  # Example condition
        print("Stage 1 complete. Separating stage. Entering Stage 2.")
        stage = "Stage 2"

# Function to check if orbit is achieved
def check_orbit_achieved():
    global stage

    # Define conditions for orbit achievement (you may need to adjust these)
    if altitude >= 200 and speed >= 2000:  # Example conditions
        print("Orbit achieved! Mission Successful.")
        stage = "Orbit"

# Function to handle mission result
def handle_mission_result():
    global stage

    if stage == "Orbit":
        print("Mission Successful.")
    else:
        print("Mission Failed due to insufficient fuel.")

# Main simulation loop
while True:
    user_input = input("Enter a command: ")

    if user_input == "start checks":
        # Check all systems and report if 'Go' for launch
        print("All systems are 'Go' for launch.")

    elif user_input == "launch":
        # Start the mission and enter the simulation loop
        while stage != "Orbit" and fuel > 0:
            # Update rocket parameters
            update_rocket_parameters()
            # Display updated parameters
            display_parameters()
            # Check for stage separation or orbit
            check_stage_separation()
            check_orbit_achieved()
        # Handle mission success or failure
        handle_mission_result()

    elif user_input.startswith("fast forward "):
        try:
            seconds = int(user_input.split()[2])
            for _ in range(seconds):
                update_rocket_parameters()
                display_parameters()
                check_stage_separation()
                check_orbit_achieved()
                if stage == "Orbit" or fuel <= 0:
                    handle_mission_result()
                    break
        except ValueError:
            print("Invalid input for fast forward.")