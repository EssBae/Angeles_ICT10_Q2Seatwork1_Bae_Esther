from pyscript import document, display

teachers_name = [ "Danica Perez", "Winmhar Salazar", "Bianca Franco", "Rogelio Alegrid", "Angelina Cristobal", "Louise Garcia", "Ailene Galang", "Heidi Mamangon", "Ian Lumboy", "Ruel Roquel", "Sean Mercado", "Amelia Aguirre", "Mark Layug", "Roselle Sarmiento", "Luisito Balajadia", "Randy Santos" ] # List of confirmed names

def verify(event):
    first = document.getElementById("first_name").value.strip().title() # Gets the first name entered
    last = document.getElementById("last_name").value.strip().title() # Gets the last name entered
    message = document.getElementById("result") # Result of verification message

    fullname = first + " " + last # Combine the entered first name and second name 
    
    results = {
        True: "Confirmed! This teacher is a part of the Junior High School Department",
        False: "Name not found"
    }

    message.innerHTML = results[fullname in teachers_name] # Checks whether or not the fullname exists within the list
