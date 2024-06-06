# Save this script as initialize_directories.py in Prismals-Game-Form-A directory
import os

directories = [
    "Version_Control/Deadlained",
    "Version_Control/Deadlained/Celestial",
    "Version_Control/Deadlained/Deadlock",
    "Version_Control/Deadlained/entities",
    "Version_Control/Deadlained/entities4D",
    "Version_Control/Deadlained/GodHeads",
    "Version_Control/Deadlained/GodHeadVoices",
    "Version_Control/Deadlained/higherentities",
    "Version_Control/Deadlained/highestentities",
    "Version_Control/Deadlained/LVX",
]

# Create directories if they do not exist
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create __init__.py files in the directories
for directory in directories:
    init_file = os.path.join(directory, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, 'w') as f:
            pass

print("All directories and __init__.py files are ensured to exist.")
