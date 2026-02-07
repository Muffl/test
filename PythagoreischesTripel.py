# Pythagoreiches Tripel mit x + y + z = 'eingebene Zahl' finden
# Ein pythagoreiches Tripel (x, y, z) erfüllt: x < y < z und x**2 + y**2 = z**2

def find_pythagorean_triplet():
    """
    Findet das pythagoreiches Tripel (x, y, z), für das x + y + z = 'eingebene Zahl' gilt.
    Berechnet dann x * y * z.
    """
    # Wir iterieren über alle möglichen Werte von x und y
    # Da x + y + z = 'eingebene Zahl' und z > y > x, gilt: z = 'eingebene Zahl' - x - y
    # Aus x**2 + y**2 = z**2 folgt:
    # x**2 + y**2 = ('eingebene Zahl' - x - y)**2
    triple = input("Gib die Triple Zahl ein: ")
    triple = int(triple)
    for x in range(1, triple):
        for y in range(x + 1, triple):
            z = triple - x - y
            
            # Überprüfe ob z > y und das pythagoreiches Tripel erfüllt ist
            if z > y and x**2 + y**2 == z**2:
                print(f"Gefunden: x = {x}, y = {y}, z = {z}")
                print(f"Überprüfung: x + y + z = {x + y + z}")
                print(f"Überprüfung: x**2 + y**2 = {x**2 + y**2}, z**2 = {z**2}")
                
                result = x * y * z
                print(f"\nDas Produkt x * y * z = {result}")
                return result
    
    
    return None


if __name__ == "__main__":
    find_pythagorean_triplet()
