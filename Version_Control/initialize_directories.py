# Version_Control/initialize_directories.py

import os

directories = [
    'Version_Control/Deadlained',
    'Version_Control/Deadlained/Celestial',
    'Version_Control/Deadlained/Deadlock',
    'Version_Control/Deadlained/entities',
    'Version_Control/Deadlained/entities4D',
    'Version_Control/Deadlained/GodHeads',
    'Version_Control/Deadlained/GodHeadVoices',
    'Version_Control/Deadlained/higherentities',
    'Version_Control/Deadlained/highestentities',
    'Version_Control/Deadlained/LVX',
    'Version_Control/Time',
    'Version_Control/'
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)
    init_file = os.path.join(directory, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w') as f:
            f.write('')

print("All directories and __init__.py files are ensured to exist.")
