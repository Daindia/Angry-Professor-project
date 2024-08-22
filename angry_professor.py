def angry_professor(attendancy_threshold, attendancy):
    
    get_early_attendees = list(filter(lambda integer: integer <= 0, attendancy))
    
    if len(get_early_attendees) >= attendancy_threshold:
        return 'NO'
    
    else:
        return 'YES'
    