#.     "Shipping Cost Calculator"
#e-commerce application with a feature that calculates shipping costs based on the weight of a package and the destination zone. 

# The Rules for the Shipping Cost Calculator:
# Package Weight: The system accepts package weights between 0.1 kg and 20.0 kg.
# Destination Zones: There are three shipping zones:
#   Zone A: Urban areas
#   Zone B: Rural areas
#   Zone C: Remote areas
# Shipping Costs: The cost is determined by a combination of weight and destination zone.


# Fixed Cost: A flat rate of $2.00 is applied to every shipment, regardless of weight or destination. This fee covers basic handling and administrative costs.

# Price per Gram: The base variable cost is $0.005 per gram. This rate is applied to the weight of the package before the zone-specific multiplier.

# Zone Coefficients: These multipliers adjust the variable cost based on the shipping destination:
#   Zone A (Urban): 1.0 (No additional cost)
#   Zone B (Rural): 1.5 (50% increase over the base variable cost)
#   Zone C (Remote): 2.0 (100% increase over the base variable cost)

import pricing_calculator as pc
import os

os.system('clear')

print("Bienvenido a la Calculadora de Costos de Envío \nEl peso aceptado de los paquetes es entre 0.1 kg y 20.0 kg \nLas zonas de envío son: Zona A (Áreas Urbanas), Zona B (Áreas Rurales), Zona C (Áreas Remotas)")  

peso = input("Ingrese el peso del paquete en kg: ")
zona = input("Ingrese la zona de destino: ")

if pc.check_weight(float(peso)) > 0 and pc.check_zone(zona) == True:
    costo = pc.calculate_shipping_cost(float(peso), zona)
    print(f"El costo de envío para un paquete de {peso} kg a la zona {zona.upper()} es: ${costo:.2f}")
else:
    print("Entrada inválida. Asegúrese de que el peso esté entre 0.1 kg y 20.0 kg y que la zona sea A, B o C.")
