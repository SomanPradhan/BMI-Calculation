''' Assignment to find and plot the Statistic of Life Expectancy and Body Mass Index of the world'''
import matplotlib.pyplot as plt


class CountryStatistic():
    life = [] # list for storing the values of life.csv
    years = [] # from year 1980 to 2008. This list contain the years of the data
    country = [] # list containing the names of countries whose data are taken
    bmi_men = {} # contains the dict where key is the country_name and values are the men Body mass index of respective country
    bmi_women = {}# contains the dict where key is the country_name and values are the women Body mass index of respective country
    bmi_neutral = {}# contains the dict where key is the country_name and values are the average Body mass index of respective country

    ''' initialising the object and storing the above variables '''
    def __init__(self):
        ''' First Step Methods '''
        self.open_life_file()#opens life.csv file and stored it in life[]
        self.open_men_file()#opens bmi_men.csv file and stored it in bmi_men[]
        self.open_women_file()#opens bmi_women.csv file and stored it in bmi_women[]
        ''' Second Step Methods '''
        self.neutral()#opens bmi_neutral.csv file and stored it in bmi_neutral[]

    def open_life_file(self):
        with open('life.csv') as f: #opens life.csv file
            state = True#state determines if the it is reading first line or not
            for line in f:
                line_values = line.strip().splitlines()
                if state:#when reading the first line years from 1980 to 2009 stored in 'years' variable
                    self.years = [int(x) for x in line_values[0].split(',') if x != line_values[0].split(',')[0]]#stored years in 'years' variable
                    state = False#changing the state = false as the first line is already stored
                    continue
                floatLineValues = [float(x) if x != line_values[0].split(',')[0] else x for x in
                                   line_values[0].split(',')]#chainging list of values in float except the first value of each line
                self.country.append(floatLineValues[0])#adding each country to the country list
                self.life.append(floatLineValues)#adding changed value in life list

    def open_men_file(self):
        with open('bmi_men.csv') as f:#opens bmi_men.csv file
            state = True#for skiping the first line i.e years
            for line in f:
                if state:
                    state = False#chaning the status to false so that from second line does not get skipped
                    continue
                line_values = line.strip().splitlines()
                floatLineValues = [float(x) for x in line_values[0].split(',')[1:]]#changing the values to float in a list except the country name
                self.bmi_men[line_values[0].split(',')[0]] = floatLineValues#assigning the values to the countries as a key in the dict

    def open_women_file(self):
        with open('bmi_women.csv') as f:#opens bmi_women.csv file
            state = True#for skipping the first line i.e. years
            for line in f:
                if state:
                    state = False#changing the status to false so that from second line, values doesn't get skipped
                    continue
                line_values = line.strip().splitlines()
                floatLineValues = [float(x) for x in line_values[0].split(',')[1:]]#changing the values to float in a list except the country name
                self.bmi_women[line_values[0].split(',')[0]] = floatLineValues#assigning the values to the countries as key in the dict

    def neutral(self):
        for key in self.country:
            data = [round((x + y) / 2, 3) for x, y in zip(self.bmi_men[key], self.bmi_women[key])]#calcualting the average data from bmi_men.csv with respect to bmi_women
            self.bmi_neutral[key] = data#assigning countries name as key to the respective values

    def user_selected_year(self, year):
        ''' Methods for step 3 '''
        if year not in self.years:#To check if the entered year is in the data or not
            raise ValueError(f'Year {year} is not in the list Please enter from 1980 to 2008')#Raise  value error exception
        year_place = year - self.years[0]#To find the position of the entered year since the years are sorted in accending orer
        values = [self.bmi_men[x][year_place] for x in self.country]#adding the values from the bmi_men from enter year of all countries
        values += [self.bmi_women[x][year_place] for x in self.country]#adding the values from the bmi_women from enter year of all countries
        values += [self.bmi_neutral[x][year_place] for x in self.country]#addin the vaues from the bmi_neutral from the enter year of all countries
        values.sort()#sorting the values in 'values' variable in accending order
        max_value = values[-1]#since sorted list have max value at last of the list
        min_value = values[0]#since sorted list have min value of first of the list
        median_pos = len(values) // 2#calculating the position of the median in the list
        median = values[median_pos]#assigning the median value to median variable
        return [max_value, min_value, median]#returning the values as the list.

    def bmi_highest_countries(self):
        ''' Step 4 methods'''
        ''' Finding the bmi of men and women of 3 highest population countries of latest 5 years and their percent difference'''
        start_year = 2004#from latest 5 years (2004 t0 2008)
        value_pos = start_year - self.years[0]#finding the position of the start value
        keys = ['China', 'India', 'United States']#list of highest populated countries
        bmi_of_high = {}#empty dictionary for the inserting the values
        for key in keys:
            val_men = round(sum(self.bmi_men[key][value_pos:]) / 5, 2)#finding the average bmi of men of each countries between 2004 and 2008
            val_women = round(sum(self.bmi_women[key][value_pos:]) / 5, 2)#finding the average bmi of women of ech countries between 2004 and 2008
            percent_diff = round((abs(val_men - val_women) / ((val_men + val_women) / 2)) * 100, 2)#finding percentage difference of men and women
            bmi_of_high[key] = [val_men, val_women, percent_diff]#assigning countries as key for list of each above calculated values
        return bmi_of_high

    def plot_bmi_life(self, avg_bmi, avg_life):
        ''' Ploting the values of average BMI and average Life as y-axis and years as in x-axis'''
        fig = plt.figure()
        ax1 = fig.add_subplot()
        ax1.set_xlabel('Years')
        ax1.plot(self.years, avg_bmi, 'bo-')
        ax1.tick_params(axis='y', labelcolor='b')
        ax1.set_ylabel('Average_BMI', color='b')
        ax2 = ax1.twinx()
        ax2.plot(self.years, avg_life, 'r*-')
        ax2.tick_params(axis='y', labelcolor='r')
        ax2.set_ylabel('Average Life Expectancy', color='r')
        plt.show()

    def plot_country_bmi(self, country_name, y_plot):
        ''' Plotting the enter country's life expectancy as y-axis against years as x-axis'''
        fig = plt.figure()
        ax1 = fig.add_subplot()
        ax1.set_xlabel('Years')
        ax1.plot(self.years, y_plot[0], 'bo-')
        ax1.tick_params(axis='y', labelcolor='b')
        ax1.set_ylabel(country_name + ' Life Expectancy', color='b')
        plt.show()

    def country_bmi(self, country_name):
        ''' step 5 method '''
        country_name = [x for x in self.country if country_name.lower() == x.lower()]#To check if input country is the list of country or not(case insensitive)
        if len(country_name) == 0:#if country_name is not in the list of country then list is empty
            return True#doesn't let below code to execute if above condition is True
        print(f'Plot for \'{country_name[0]}\' opens in new window')
        y_plot = [x[1:] for x in self.life if x[0] == country_name[0]]#assigning the  values of life expectancy of entered country to y
        self.plot_country_bmi(country_name[0], y_plot)#calling the funciton to plot
        return False

    def bmi_life(self):
        ''' Step 6 method '''
        sum_bmi = [0 for x in self.country]#initilising the list sum_bmi
        for x in self.country:
            sum_bmi = [sum_bmi[j] + self.bmi_men[x][j] + self.bmi_women[x][j] + self.bmi_neutral[x][j] for j in
                       range(0, len(self.years))]#sum of each country of all bmi data
            avg_bmi = [round(x / (3 * len(self.country)), 2) for x in sum_bmi]#calculating the average values
        sum_life = [0 for x in self.country]#initilising the the list sum_life
        for x in self.life:
            sum_life = [sum_life[j - 1] + x[j] for j in range(1, len(x))]#sum of each country of all life
        avg_life = [round(x / len(self.country), 2) for x in sum_life]#calculating the average life.
        self.plot_bmi_life(avg_bmi, avg_life)#calling the function to plot the avg bmi and avg life against years.
