from datetime import datetime

def ordinal(day):
    """Returns the ordinal suffix for a given day of the month."""
    if 10 <= day % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    return f"{day}{suffix}"

def get_date(year = int(datetime.today().strftime('%Y')), month = int(datetime.today().strftime('%m')), day = int(datetime.today().strftime('%d'))):

    # Create a specific date
    specific_date = datetime(year, month, day)

    # Format the date
    day = specific_date.day
    month = specific_date.strftime("%B")
    year = specific_date.year

    # Combine into the desired format
    return f"{ordinal(day)} {month} {year}"


def format_event_date(event_date):
    """Converts a date string in 'YYYY-MM-DD' format to '26th August 2024' format."""
    
    event_date_obj = datetime.strptime(event_date, "%Y-%m-%d")
    
    day = event_date_obj.day
    month = event_date_obj.strftime("%B")
    year = event_date_obj.year
    
    # Use the ordinal function to add the correct suffix to the day
    formatted_date = f"{ordinal(day)} {month} {year}"
    
    return formatted_date
