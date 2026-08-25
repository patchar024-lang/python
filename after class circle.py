def calculate_circumference(radius):
    """
    Calculates the circumference of a circle given its radius.
    
    Formula: C = 2 * π * r
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
        
    return 2 * math.pi * radius

# Example usage:
if __name__ == "__main__":
    test_radius = 5
    circumference = calculate_circumference(test_radius)
    
    print("The circumference of a circle with radius {test_radius} is: {circumference:.2f}")
