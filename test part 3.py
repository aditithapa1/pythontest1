def convertSalary(salary, country):
    conversion_rates = {
        "Canada": 1.0,
        "USA": 1.18,
        "Cambodia": 4847.38,
        "United Kingdom": 0.91
    }
    converted_salary = salary / conversion_rates[country]
    return converted_salary

# Ask the user for their salary in Euros
salary_euros = float(input("Please enter your salary in Germany: "))

# Ask the user for their desired country of migration
country = input("Enter the country you want to migrate to: ")

# Check if the user input is valid
if country not in ["Canada", "USA", "Cambodia", "United Kingdom"]:
    print("Invalid country input")
else:
    # Convert the user's salary to the currency of the desired country using the function convertSalary()
    converted_salary = convertSalary(salary_euros, country)

    # Compare the user's salary with the average salary of the desired country
    average_salaries = {
        "Canada": 64000,
        "USA": 56516,
        "Cambodia": 5649856,
        "United Kingdom": 35423
    }
    currency_name = "CAD" if country == "Canada" else "US Dollars" if country == "USA" else "Cambodian riel" if country == "Cambodia" else "Pound Sterling"
    if converted_salary < average_salaries[country]:
        print("You will be poor in {} with a salary of {:.2f} {}".format(country, converted_salary, currency_name))
    else:
        print("You will be rich in {} with a salary of {:.2f} {}".format(country, converted_salary, currency_name))
