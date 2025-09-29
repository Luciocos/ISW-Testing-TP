# test_scripts.py
import pytest
import pricing_calculator as pc

# ---------- Boundary Value Tests for Weight ----------
@pytest.mark.parametrize("weight,expected", [
    (0.09, False),      # below min
    (0.1, 0.1),         # at min
    (0.11, 0.11),       # just above min
    (19.99, 19.99),     # just below max
    (20.0, 20.0),       # at max
    (20.1, False)       # above max
])
def test_check_weight_bva(weight, expected):
    assert pc.check_weight(weight) == expected

# ---------- Boundary Value Tests for Zone ----------
@pytest.mark.parametrize("zone,expected", [
    ("A", True),
    ("B", True),
    ("C", True),
    ("a", True),   # lowercase
    ("D", False),
    ("", False),
])
def test_check_zone(zone, expected):
    assert pc.check_zone(zone) == expected

# ---------- Decision Table: Valid weights x valid zones ----------
@pytest.mark.parametrize("weight,zone,expected_cost", [
    # weight 0.1 kg in each zone
    (0.1, "A", 2.00 + (0.1*1000*0.005*1.0)),  # Zone A
    (0.1, "B", 2.00 + (0.1*1000*0.005*1.5)),  # Zone B
    (0.1, "C", 2.00 + (0.1*1000*0.005*2.0)),  # Zone C

    # weight 20.0 kg in each zone
    (20.0, "A", 2.00 + (20.0*1000*0.005*1.0)),
    (20.0, "B", 2.00 + (20.0*1000*0.005*1.5)),
    (20.0, "C", 2.00 + (20.0*1000*0.005*2.0)),
])
def test_calculate_shipping_cost_decision(weight, zone, expected_cost):
    assert pc.calculate_shipping_cost(weight, zone) == pytest.approx(expected_cost, rel=1e-6)

# ---------- Decision Table: Invalid zone should raise ----------
@pytest.mark.parametrize("zone", ["D", "Z", ""])
def test_calculate_shipping_cost_invalid_zone(zone):
    with pytest.raises(ValueError):
        pc.calculate_shipping_cost(1.0, zone)
