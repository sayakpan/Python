import pandas as pd
import numpy as np
from tqdm import tqdm

# Load the events data from the excel sheet
events_data = pd.read_excel("events.xlsx")

# Iterate through each event and create a new excel sheet for it
for i, current_event in tqdm(
    events_data.iterrows(), total=len(events_data), colour="cyan"
):
    # Get the number of participants for this event
    num_participants = current_event["number_of_participants"]

    # Get a random sample of students from the 'students' sheet
    students_data = pd.read_excel("students.xlsx")

    if current_event["year"] == 2017:
        eligible_students = students_data.loc[
            (current_event["year"] == students_data["year_of_enrollment"])
        ]
    else:
        eligible_students = students_data.loc[
            (
                (current_event["year"] > students_data["year_of_enrollment"])
                & (current_event["year"] - students_data["year_of_enrollment"] <= 4)
            )
        ]
    selected_students = eligible_students.sample(n=num_participants)

    # Save the selected students to a new excel sheet for this event
    selected_students.to_excel(f"{i+2}_{current_event['eventName']}.xlsx", index=False)
