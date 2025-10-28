import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n_incidents = 100
n_responses = 100
n_accesses = 100

occurence_date = [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 180)) for _ in range(n_incidents)]
report_date = [f + timedelta(days=np.random.randint(1, 10)) for f in occurence_date]

consult_date = [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 180)) for _ in range(n_responses)]
response_date = [f + timedelta(days=np.random.randint(1, 50)) for f in consult_date] # Hasta 50 dias desps

access_date = [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 180)) for _ in range(n_accesses)]

incident = {
    "incident_id": range(1, n_incidents+1),
    "occurrence_date": occurence_date,
    "report_date": report_date,
    "severity": np.random.choice(['Low', 'Moderate', 'Critical'], size = n_incidents),
    'mitigated': np.random.choice([True, False], size = n_incidents)
}

response = {
    "response_id": range(1, n_responses+1),
    "consult_date": consult_date,
    "response_date": response_date,
}

access = {
    "access_id": range(1, n_accesses+1),
    "access_date": access_date,
    "justified": np.random.choice([True, False], size=n_accesses)
}


incident_df = pd.DataFrame(incident)
response_df = pd.DataFrame(response)
access_df = pd.DataFrame(access)

#print(incident_df.head())
#print(response_df.head())
#print(access_df.head())

## ------------------------------------------------------------------------- ##

response_df["response_time_days"] = (response_df["response_date"] - response_df["consult_date"]).dt.days
response_mean = response_df["response_time_days"].mean()

response_df["on_term"] = response_df["response_time_days"] <= 30
response_on_term_percentage = (response_df["on_term"].sum() / n_responses) * 100

print(f"Average response time: {response_mean:.2f} days")
print(f"Percentage of responses on term (30 days): {response_on_term_percentage:.2f}%")

## ------------------------------------------------------------------------- ##

incidents_mitigated = ((incident_df['mitigated'] == True).sum() / n_incidents) * 100
incicents_reported_on_term = ((((incident_df['report_date'] - incident_df['occurrence_date']).dt.days <= 2).sum()) / n_incidents) * 100

print(f"Percentage of incidents mitigated: {incidents_mitigated:.2f}%")
print(f"Percentage of incidents reported on term (2 days): {incicents_reported_on_term:.2f}%")

## ------------------------------------------------------------------------- ##

access_justified = ((access_df['justified'] == True).sum() / n_accesses) * 100

print(f"Percentage of justified accesses: {access_justified:.2f}%")