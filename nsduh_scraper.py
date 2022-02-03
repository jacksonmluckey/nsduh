import requests, zipfile, io

# generate a list of all years that SAMHSA has a NSDUH survey for in SAMHDA
years = []
for year in range(1990, 2021):
  years.append(year)
years.append(1988)
years.append(1985)
years.append(1979)

# download the delimited zip file for year year
print("Downloading the NSDUH datasets from SAMHDA...")

for year in years:
  year = str(year)
  print("Now downloading " + year)
  url = "https://www.datafiles.samhsa.gov/sites/default/files/field-uploads-protected/studies/NHSDA-" + year + "/NHSDA-" + year + "-datasets/NHSDA-" + year + "-DS0001/NHSDA-" + year + "-DS0001-bundles-with-study-info/NHSDA-" + year + "-DS0001-bndl-data-tsv.zip"
  r = requests.get(url)
  try:
    z = zipfile.ZipFile(io.BytesIO(r.content))
    destination_path = "data" + "/" + year
    z.extractall(destination_path)
  except:
    print("The zip file for the year " + year + " could not be successfully downloaded and extracted :(")
  finally:
    print("Downloaded and extracted NSDUH data for " + year)
