import random

def random_hex_color():
    """Generate a random hex color."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def refresh_sunbird():
    """Predict a new hex color for the sunbird feather."""
    new_hex_color = random_hex_color()
    return new_hex_color

# Example usage
if __name__ == "__main__":
    hex_color = refresh_sunbird()
    print("The new hex color for the sunbird feather is:", hex_color)
