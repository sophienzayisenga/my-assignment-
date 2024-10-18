def identify_mushroom(has_gills, grows_in_forest, has_ring, has_convex_cup):
    """Determines the mushroom based on the given characteristics."""
    if not has_gills:  
        return "Cepe de bordeaux"
    if not grows_in_forest: 
        if has_ring:
            return "Coprin chevelu"
        else:
            return "Agaric jaunissant"
    if has_convex_cup:
        if has_ring:
            return "Amanite tue-mouche"
        else:
            return "Pied Bleu"
    else:
        return "Girolle"

def main():
   
    has_gills = input("Does your mushroom have gills? (yes/no): ").strip().lower() == "yes"
    grows_in_forest = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower() == "yes"
    has_ring = input("Does your mushroom have a ring? (yes/no): ").strip().lower() == "yes"
    has_convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower() == "yes"

    
    mushroom = identify_mushroom(has_gills, grows_in_forest, has_ring, has_convex_cup)

    print(f"The mushroom is likely a {mushroom}")

main()
