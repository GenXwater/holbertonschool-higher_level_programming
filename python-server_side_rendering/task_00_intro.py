def generate_invitations(template, attendees):
    # Vérification des types d'entrées
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Vérification des contenus vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Parcours de la liste des participants
    for index, attendee in enumerate(attendees, start=1):
        # Remplacement des valeurs manquantes par "N/A" si nécessaire
        content = template
        content = content.replace("{name}", attendee.get("name", "N/A"))
        content = content.replace("{event_title}", attendee.get("event_title", "N/A"))
        content = content.replace("{event_date}", attendee.get("event_date", "N/A"))
        content = content.replace("{event_location}", attendee.get("event_location", "N/A"))
        
        # Génération du fichier de sortie
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Generated {filename}")
