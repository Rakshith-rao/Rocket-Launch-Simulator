# Rocket-Launch-Simulator
This is a simple rocket simulation written in Python. It allows you to launch and control a rocket, and monitor its parameters such as stage, fuel, altitude, and speed.

Usage
To run the simulation, simply run the following command:

python rocket_simulation.py
This will start the simulation in the Pre-Launch stage. You can then use the following commands to control the rocket:

start_checks: Performs pre-launch checks.
launch: Launches the rocket.
fast_forward <seconds>: Fast-forwards the simulation by the specified number of seconds.

Example
python rocket_simulation.py
start_checks

launch
fast_forward 10

# Display rocket parameters
Output

All systems are 'Go' for launch.

Launching...

Stage: Stage 1, Fuel: 90%, Altitude: 10 km, Speed: 1000 km/h
Stage: Stage 1, Fuel: 80%, Altitude: 20 km, Speed: 2000 km/h
Stage: Stage 1, Fuel: 70%, Altitude: 30 km, Speed: 3000 km/h

Stage 1 complete. Separating stage. Entering Stage 2.

Stage: Stage 2, Fuel: 100%, Altitude: 30 km, Speed: 3000 km/h
Stage: Stage 2, Fuel: 90%, Altitude: 45 km, Speed: 4500 km/h
Stage: Stage 2, Fuel: 80%, Altitude: 60 km, Speed: 6000 km/h

Orbit achieved! Mission Successful.

Description
The Rocket Launch Simulator is designed to simulate a rocket launch, taking the user through various stages of the launch process. The simulator operates in discrete time steps, with each second representing one second of the mission. It provides real-time updates on the rocket's stage, fuel, altitude, and speed, and it can simulate both successful missions and mission failures.

Functionalities
The Rocket Launch Simulator includes the following functionalities:

Pre-Launch Checks: Initiates system checks to ensure all systems are 'Go' for launch.
Launch: Begins the rocket launch simulation and updates parameters in real-time.
Fast Forward: Allows users to fast forward the simulation by a specified number of seconds.
Mission Result: Provides mission success or failure feedback based on predefined conditions.
Requirements
To run the Rocket Launch Simulator, you need the following:

Python (3.x recommended)
Installation
Clone the repository to your local machine:
git clone https://github.com/yourusername/rocket-launch-simulator.git
Navigate to the project directory:
cd rocket-launch-simulator
Usage
Start by performing pre-launch checks using the command: start checks.
Launch the rocket using the command: launch.
Use the fast forward X command to advance the simulation by X seconds (e.g., fast forward 10).
Observe the real-time updates and follow the predefined conditions for stage separation, orbit achievement, or mission failure.
