""" This code was developed by 'Ahmed Rabia' for the FDW Data Analysis Professional Nano Degree  """


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

""" These 3 lists are provided to validate the user's inputs   """

city_names = ['chicago', 'new york city', 'washington']
months_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days_names = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


""" This function asks the user to specify a city, month, and day to be analyzed.
It returns:    (str) city - name of the city to analyze
               (str) month - name of the month to filter by, or "all" to apply no month filter
               (str) day - name of the day of week to filter by, or "all" to apply no day filter
"""
def get_filters():

    print('\n Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington).
    while True:
        city = str(input('\n Please choos a city to explore its data: Chicago, New York City, Washington: ')).lower()
        if city not in city_names:
            print('\n This not a valid city name, please write the city name correctly')
        else:
            break
	
    # get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('\n Which month would you like to filter by: all, January, February, March, April, May, or June: ')).lower()
        if month not in months_names:
            print('\n This not a valid month name, please write the month name correctly')
        else:
            break


	
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('\n Which day would you like to filter by: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday: '))
        if day not in days_names:
            print('\n This not a valid day name, please write the day name correctly')
        else:
            break

    print('-'*40)
    return city, month, day


""" This function loads data for the specified city and filters by month and day if applicable.
Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
Returns:
    df - Pandas DataFrame containing city data filtered by month and day
"""
def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

""" This function ask the user if he\she would like to explore the firts 5 rows of the raw data? ."""
def explore_data(df):

    i = 0
    Loop_stop = df.shape[0]
    # get user input if he\she would like to explore the firts 5 rows of the raw data?
    while True:
        data_head = input('\n Would you like to explore the first 5 rows of the raw data? Please enter yes or no.\n')

        # if the answer is not yes, the function will be terminated, otherwise, the function will print 5 rows.
        if data_head.lower() != 'yes':
            break
        else:
            for i in range(i, Loop_stop, 5):
                data_rows = df.iloc[i:i+5]
                print(data_rows)
                i+= 5
                break

""" This function calculates the statistics of the most frequent times of travel."""
def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month =  df['month'].value_counts().idxmax()
    print('Most Frequent month:', popular_month)

    # display the most common day of week
    popular_day_of_week =  df['day_of_week'].value_counts().idxmax()
    print('Most Frequent day of week:', popular_day_of_week)


    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    popular_hour =  df['hour'].value_counts().idxmax()
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


""" This function calculates the statistics of the most popular stations and trip."""
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station =  df['Start Station'].value_counts().idxmax()
    print('Most Frequent Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station =  df['End Station'].value_counts().idxmax()
    print('Most Frequent End Station:', popular_end_station)

    # Generate a trip combination column that joins the start station and end station columns
    df['station combination'] = df['Start Station'] + ' with ' + df['End Station']

    # display most frequent combination of start station and end station trip
    popular_station_combination =  df['station combination'].value_counts().idxmax()
    print('Most Frequent Station Combination:', popular_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

""" This function calculates the statistics of the total and average trip duration."""
def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time_sum = df['Trip Duration'].sum()
    print("The Total Travel Time in Seconds :", travel_time_sum)

    # display mean travel time
    travel_timea_mean = df['Trip Duration'].mean()
    print("The Mean Travel Time in Seconds :", travel_timea_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

""" This function calculates the statistics of the bikeshare user types."""
def user_Types_stats(df):

    print('\nCalculating User Types Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("The Counts of User Types :", user_types_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

""" This function calculates the statistics of the bikeshare users gender and birht year."""
def gender_birhtyear_stats(df):

    print('\nCalculating Users\' Gender and Birth Year Stats...\n')
    start_time = time.time()

    # Display counts of gender
    gender_count = df['Gender'].dropna(axis = 0).value_counts()
    print("The Counts of User Gender :", gender_count)
    # Display earliest, most recent, and most common year of birth
    earliest_birthyear = df['Birth Year'].dropna(axis = 0).min()
    print("The Earliest Year of Birth :", earliest_birthyear)

    most_recent_birthyear = df['Birth Year'].dropna(axis = 0).max()
    print("The Most Recent Year of Birth :", most_recent_birthyear)

    most_common_birthyear =  df['Birth Year'].dropna(axis = 0).value_counts().idxmax()
    print("The Most Common Year of Birth :", most_common_birthyear)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        """ This IF statment to check if the selected city is not washington - in this case
        the 'gender_birhtyear_stats' function will be called, otherwise, if the selected city is
        washington, the 'gender_birhtyear_stats' function will not be called because there are no
        records of Gender or Birth Year in the washington.csv file """
        if city != 'washington':
            explore_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_Types_stats(df)
            gender_birhtyear_stats(df)

        else:
            explore_data(df)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_Types_stats(df)
            print('\n Washington City Data does not have Gender or Birth Year Records')


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
