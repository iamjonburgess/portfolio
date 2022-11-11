import pandas as pd
from google.cloud import bigquery

# we're going to query PM10 since it covers a broader range of pollution.
# for more info, see: https://ww2.arb.ca.gov/resources/inhalable-particulate-matter-and-health

# sample query from:
QUERY = """
		SELECT location, city, country, value, timestamp
		FROM `bigquery-public-data.openaq.global_air_quality`
		WHERE pollutant = "pm10" AND timestamp > "2017-04-01"
		ORDER BY value DESC
		LIMIT 1000
		"""

client = bigquery.Client.from_service_account_json(
			'INSERT .JSON CREDENTIAL FILENAME')

query_job = client.query(QUERY)
df = query_job.to_dataframe()

print(df.head(3))