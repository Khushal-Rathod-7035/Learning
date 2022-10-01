from datetime import datetime
current_date = datetime.now()
new_date_format = current_date.strftime("%B %d, %Y %I:%M %p")
print(new_date_format)

