import csv
from io import TextIOWrapper
from zipfile import ZipFile

# opens file.
enrollment_outfile = open("enrollment.csv", 'w' , encoding='UTF8')
enrollment_outwriter = csv.writer(enrollment_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)


####################
#todo - change names
####################
country_outfile = open("country.csv", 'w' , encoding='UTF8')
country_outwriter = csv.writer(country_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

incomegroup_outfile = open("incomegroup.csv", 'w' , encoding='UTF8')
incomegroup_outwriter = csv.writer(incomegroup_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

region_outfile = open("region.csv", 'w' , encoding='UTF8')
region_outwriter = csv.writer(region_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

university_outfile = open("university.csv", 'w' , encoding='UTF8')
university_outwriter = csv.writer(university_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

enrollemnt_year_outfile = open("enrollment_year.csv", 'w' , encoding='UTF8')
enrollemnt_year_outwriter = csv.writer(enrollemnt_year_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

incomegroups = {}
regions = {}
universities = {}
enrollment_years = {}
########################
########################
########################



# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
  with ZipFile('enrollment.zip') as zf:
      with zf.open('enrollment.csv', 'r') as infile:
          reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
          for row in reader:
              # TO DO splits row into the different csv table files
              enrollment_outwriter.writerow(row)
          ##################################
          # todo make the right changes here
          ##################################
          for c in countries:
            country_outwriter.writerow(countries[c])
          country_outfile.close()
          for in_group in incomegroups:
                incomegroup_outwriter.writerow(incomegroups[in_group])
          incomegroup_outfile.close()
          for region in regions:
                region_outwriter.writerow(regions[region])
          region_outfile.close()
          for u in universities:
                university_outwriter.writerow(universities[u])
          university_outfile.close()
          for y in enrollment_years:
                enrollemnt_year_outwriter.writerow(enrollment_years[y])
          enrollemnt_year_outfile.close()
    ########################
    ########################
    ########################
    enrollment_outfile.close()



####################
#todo - change names
####################
# process_row should splits row into the different csv table files
def process_row(row):
    #print(row)
    country = row[0]
    countrycode = row[1]
    region = row[2]
    incomegroup = row[3]
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
    countries[countrycode]=[countrycode,country,incomegroup,region]
    incomegroups[incomegroup]=[incomegroup]
    regions[region]=[region]


universities[iau_id1]=[iau_id1,eng_name,orig_name,foundedyr,yrclosed,private01,latitude,longi tude,phd_granting,divisions,specialized,countrycode]
enrollment_years[iau_id1,year]=[iau_id1,year,students5_estimated]
########################
########################
########################

# return the list of all tables
def get_names():
    return ["enrollment"]
    ##################################
    # todo make the right changes here
    ##################################
    # return ["country", "incomegroup", "region", "university", "enrollemnt_year"]
    ########################
    ########################
    ########################


if __name__ == "__main__":
    process_file()







