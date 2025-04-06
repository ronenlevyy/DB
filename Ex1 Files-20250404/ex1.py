import csv
from io import TextIOWrapper
from zipfile import ZipFile

#create files
enrollment_outfile = open("enrollment.csv", 'w' , encoding='UTF8')
enrollment_outwriter = csv.writer(enrollment_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

country_outfile = open("Country.csv", 'w' , encoding='UTF8')
country_outwriter = csv.writer(country_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

incomegroup_outfile = open("IncomeGroup.csv", 'w' , encoding='UTF8')
incomegroup_outwriter = csv.writer(incomegroup_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

region_outfile = open("Region.csv", 'w' , encoding='UTF8')
region_outwriter = csv.writer(region_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

university_outfile = open("University.csv", 'w' , encoding='UTF8')
university_outwriter = csv.writer(university_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

closed_at_outfile = open("ClosedAt.csv", 'w' , encoding='UTF8')
closed_at_outwriter = csv.writer(closed_at_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

acceptance_rate_outfile = open("AcceptanceRate.csv", 'w' , encoding='UTF8')
acceptance_rate_outwriter = csv.writer(acceptance_rate_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

countries ={}
income_groups = {}
regions = {}
universities = {}
closed_at = {}
acceptance_rate = {}




# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
  with ZipFile('enrollment.zip') as zf:
      with zf.open('enrollment.csv', 'r') as infile:
          reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
          for row in reader:
              process_row(row)
          for c in countries:
            country_outwriter.writerow(countries[c])
          country_outfile.close()
          for in_group in income_groups:
                incomegroup_outwriter.writerow(income_groups[in_group])
          incomegroup_outfile.close()
          for region in regions:
                region_outwriter.writerow(regions[region])
          region_outfile.close()
          for u in universities:
                university_outwriter.writerow(universities[u])
          university_outfile.close()
          for y in closed_at:
                closed_at_outwriter.writerow(closed_at[y])
          closed_at_outfile.close()
          for y in acceptance_rate:
              acceptance_rate_outwriter.writerow(acceptance_rate[y])
          acceptance_rate_outfile.close()




# process_row should splits row into the different csv table files
def process_row(row):
    country = row[0]
    countrycode = row[1]
    region = row[2]
    income_group = row[3]
    iau_id1 = row[4]
    eng_name = row[5]
    orig_name = row[6]
    foundedyr = row[7]
    yrclosed = row[8]
    private01 = row[9]
    latitude = row[10]
    longitude = row[11]
    phd_granting = row[12]
    divisions = row[13]
    specialized = row[14]
    year = row[15]
    students5_estimated = row[16]
    countries[countrycode]=[countrycode,country,income_group,region]
    income_groups[income_group]=[income_group]
    regions[region]=[region]
    universities[iau_id1]=[iau_id1,eng_name,orig_name,foundedyr,yrclosed,private01,latitude,longitude,phd_granting,divisions,specialized,countrycode]
    acceptance_rate[iau_id1,year]=[iau_id1,year,students5_estimated]
    closed_at[iau_id1,year]=[iau_id1,year]



# return the list of all tables
def get_names():
    return ["Country", "Income_group", "Region", "University", "Closed_at", "Acceptance_rate"]



if __name__ == "__main__":
    process_file()







