def calculate_effective_porosity(specific_capacity):
    """
    Calculates effective porosity (ne) using the Wilkinson power-law formula.
    Formula: ne = 0.1508 * (q/s)^0.0826
    
    Parameters:
    specific_capacity (float): Specific capacity (q/s) in m^2/day.
    
    Returns:
    float: Estimated effective porosity (decimal).
    """
    if specific_capacity <= 0:
        return "Error: Specific capacity must be greater than zero."
    
    # The universal power-law constant and exponent
    constant = 0.1508
    exponent = 0.0826
    
    effective_porosity = constant * (specific_capacity ** exponent)
    return round(effective_porosity, 4)

# Example Usage:
if __name__ == "__main__":
    print("--- Wilkinson Effective Porosity Calculator ---")
    try:
        qs_input = float(input("Enter Specific Capacity (q/s) in m^2/day: "))
        result = calculate_effective_porosity(qs_input)
        
        if isinstance(result, float):
            print(f"Estimated Effective Porosity (ne): {result}")
            print(f"Percentage: {result * 100}%")
        else:
            print(result)
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
