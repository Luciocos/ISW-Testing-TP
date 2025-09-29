from typing import Any


fixed_cost = 2.00
price_per_gram = 0.005
zone_coefficients = {
    "A": 1.0,
    "B": 1.5,
    "C": 2.0
}

def check_weight(arg: Any) -> bool | float:

    if isinstance(arg, float):
        if 0.1 <= arg and arg <= 20:
            return arg
        else: 
            return False
    else: 
        return False


def check_zone(arg: Any) -> bool:
    if isinstance(arg, str):
        if str.upper(arg) in ["A", "B", "C"]:
            return True
        else:
            return False


def calculate_shipping_cost(weight: float, zone: str) -> float:


    weight_in_grams = weight * 1000
    base_variable_cost = weight_in_grams * price_per_gram

    if str.upper(zone) in zone_coefficients:
        zone_multiplier = zone_coefficients[str.upper(zone)]
    else:
        raise ValueError("Invalid zone. Please choose from 'A', 'B', or 'C'.")

    variable_cost = base_variable_cost * zone_multiplier
    total_cost = fixed_cost + variable_cost

    return total_cost