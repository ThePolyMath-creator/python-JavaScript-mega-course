print("####### DAY THREE 3 ############")

def welcome_message():  # Example usage
        print("Welcome to the European countries checker!")
        
welcome_message()


countries = [
    "spain", "france", "germany", "italy", "portugal",
    "poland", "sweden", "norway", "finland", "denmark",
    "croatia", "greece", "turkey", "russia", "ukraine",
    "belgium", "netherlands", "switzerland", "austria",
    "ireland", "bosnia", "serbia", "bulgaria", "romania",
    "hungary", "czech republic", "slovakia", "slovenia",
    "lithuania", "latvia", "estonia", "luxembourg",
    "malta", "cyprus",

    "albania", "andorra", "belarus", "iceland",
    "liechtenstein", "moldova", "monaco", "montenegro",
    "north macedonia", "san marino", "vatican city",
    "kosovo",

    "georgia", "armenia", "azerbaijan", "kazakhstan"
]

# Print numbered list
for number, country in enumerate(countries, start=1):
    print(f"{number}- {country}")

# Count countries
print("\nTotal European countries:", len(countries))


def is_european_country(country_name):   
    """Check if a country is in the list of European countries."""
    return country_name.lower() in countries    

print(is_european_country("Germany"))
    


