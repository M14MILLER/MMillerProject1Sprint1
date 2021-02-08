import requests
import secrets


def get_data():
    all_data = []
    for page in range(162):
        response = requests.get(f"https://api.data.gov/ed/collegescorecard/v1/schools.json?school.degrees_awarded.predominant=2,3&fields=school.name,school.city,2018.student.size,2017.student.size,2017.earnings.3_yrs_after_completion.overall_count_over_poverty_line,2016.repayment.3_yr_repayment.overall&api_key={secrets.api_key}&page={page}")
        if response.status_code != 200:
            print("error getting data")

        page_of_data = response.json()
        page_of_school_data = page_of_data['results']
        all_data.extend(page_of_school_data)
    return all_data


def main():
    college_data = get_data()

if __name__ == '__main__':
    main()