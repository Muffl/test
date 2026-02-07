# Alle pythagoreiches Tripel zwischen 1 und 100 berechnen
# Ein pythagoreiches Tripel (x, y, z) erfüllt: x < y < z und x**2 + y**2 = z**2

def find_all_pythagorean_triplets(max_value=100):
    """
    Findet alle pythagoreiches Tripel (x, y, z) mit 1 <= x < y < z <= max_value.
    """
    triplets = []
    
    for x in range(1, max_value):
        for y in range(x + 1, max_value):
            for z in range(y + 1, max_value + 1):
                if x**2 + y**2 == z**2:
                    triplets.append((x, y, z))
    
    return triplets


def main():
    print("Alle pythagoreiches Tripel zwischen 1 und 100:\n")
    
    triplets = find_all_pythagorean_triplets(100)
    
    if triplets:
        for i, (x, y, z) in enumerate(triplets, 1):
            print(f"{i}. Tripel: ({x}, {y}, {z})")
            print(f"   Überprüfung: {x}² + {y}² = {x**2} + {y**2} = {x**2 + y**2} = {z}² = {z**2}")
            print(f"   Produkt: {x} * {y} * {z} = {x * y * z}\n")
        
        print(f"Insgesamt {len(triplets)} pythagoreiches Tripel gefunden.")
    else:
        print("Keine pythagoreiches Tripel gefunden.")


if __name__ == "__main__":
    main()
