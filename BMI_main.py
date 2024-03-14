from BMI import CountryStatistic

countryStatistic = CountryStatistic()
#######################################################################################################################################################################
print('\nStep 1\n')
print('Life Expectancy "', countryStatistic.life)
print('Body Mass Index of Men ', countryStatistic.bmi_men)
print('Body Mass Index of Women ', countryStatistic.bmi_women)
#######################################################################################################################################################################
print('\nStep 2\n')
print('Body Mass Index of Neutral ', countryStatistic.bmi_neutral)
#######################################################################################################################################################################
print('\nStep 3\n')
status = True
while status:
    try:
        user_year = int(input('Enter a year from 1980 to 2008 : '))
        if user_year >= 1980 and user_year <= 2008:
            status = False
        else:
            print(f'<error> \'{user_year}\' is not between 1980 and 2008. Please Enter again')
    except ValueError:
        print(f'<error> \'{user_year}\' is not between 1980 and 2008. Please Enter again')
bmi_value = countryStatistic.user_selected_year(user_year)
print(f'Max BMI value of {user_year} is {bmi_value[0]:.3f}')
print(f'Min BMI value of {user_year} is {bmi_value[1]:.3f}')
print(f'Median BMI value of {user_year} is {bmi_value[2]:.3f}')
########################################################################################################################################################################
print('\nStep 4\n')
high_bmi_value = countryStatistic.bmi_highest_countries()
for x in high_bmi_value.keys():
    print(f'***{x}***')
    print(f'Men : {high_bmi_value[x][0]}')
    print(f'Women : {high_bmi_value[x][1]}')
    print(f'Percentage difference : {high_bmi_value[x][2]} \n')
########################################################################################################################################################################
print('\nStep 5\n')
status = True
while status:
    enter_country = input('Enter the country to visualize life expectancy data : ')
    status = countryStatistic.country_bmi(enter_country)
    if status:
        print(f'<error> \'{enter_country}\' is not a valid country.')
########################################################################################################################################################################
print('\nStep 6\n')
print('Plot for average Body Mass Index and Life Expectancy of the world')
countryStatistic.bmi_life()
########################################################################################################################################################################