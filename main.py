from datetime import datetime
obs_dates = input("Enter observation dates (mm/dd/yyy): ")
dates = datetime
format: str = "%m/%d/%Y"
obs_dates = format
for dates in obs_dates:
  if dates[2] == obs_dates:
    return dates
print("Your observation dates does not exist on the list!")