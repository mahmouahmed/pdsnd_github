import time
import pandas as pd
import numpy as np
import math
import logical

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
Days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("enter a city to display bikeshare data for chicago, new york city, washington\n")
    while city.lower() not in CITY_DATA :
                 city = input("invalid input of city. please try again")
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("enter month from \n" + ' '.join(Months) + "\n")
    while month.lower() not in Months :
        month = input("\nvallid input.please try again\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("enter Day from \n" + ' '.join(Days) + "\n")
    while day.lower() not in Days :
        day = input("\nvallid input.please try again\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    city = city.lower()
    df = pd.read_csv(CITY_DATA[city])
    if month == 'All' and day == 'All' :
        df = df
    elif month != 'All' and day == 'All' :
        month_index = Months.index(month)
        df = df.loc[pd.to_datetime(df['Start Time']).dt.month==month_index]
    elif month != 'All' and day != 'All' :
        month_index = Months.index(month)
        day_index = Days.index(day)-1
        df = df.loc[(pd.to_datetime(df['Start Time']).dt.month==month_index) & (pd.to_datetime(df['Start Time']).dt.dayofweek==day_index)]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = pd.to_datetime(df['Start Time']).dt.month
    most_commom_month = common_month.mode()[0]
    print('\nmost common month of travel \n' + str(most_commom_month))

    # TO DO: display the most common day of week
    common_dayofweek = pd.to_datetime(df['Start Time']).dt.dayofweek
    most_commom_dayofweek = (common_dayofweek.mode()[0])
    print('\nmost common month of travel \n'+ str(most_commom_dayofweek))

    # TO DO: display the most common start hour
    common_hour = pd.to_datetime(df['Start Time']).dt.hour
    most_commom_hour = (common_hour.mode()[0])
    print('\nmost common Hour of travel \n' + str(most_commom_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = (df['Start Station'].mode()[0])
    print('\nmost common start station \n {}'.format(most_common_start_station)) 

    # TO DO: display most commonly used end station
    most_common_start_station = (df['End Station'].mode()[0])
    print('\nmost common end station \n' + str(most_common_start_station))


    # TO DO: display most frequent combination of start station and end station trip
    common_combination_station = df['Start Station'] + df['End Station']
    most_common_combination_station = common_combination_station.mode()[0]
    print('\n most common combination of start and end station \n' + str(most_common_combination_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = (df['Trip Duration']).sum()
    print('\n total travel time \n' + str(Total_travel_time)+'s')

    # TO DO: display mean travel time
    Mean_travel_time = (df['Trip Duration']).mean()
    print('\n Mean travel time \n' + str(Mean_travel_time)+'s')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_type = (df['User Type'].value_counts())
    print('\ncount of each user type \n' + str(count_of_user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns :
        count_of_gender =(df['Gender'].value_counts())
        print('\ncount of gender of each user type \n' + str(count_of_gender))
    else :
        print('No gender for selected file')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :
        earliest_birth_year = (df['Birth Year'].min())
        print("\noldest persons birth year \n" + str (earliest_birth_year))
        most_recent_birth_year = (df['Birth Year'].max())
        print("\nyoungest persons birth year \n" + str(most_recent_birth_year))
        most_common_birth_year = (df['Birth Year'].min())
        print("\noldest persons birth year \n" + str(most_common_birth_year))
    else :
        print("NO birth year for selected file")
    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart datashow? or you want to exit  Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	    main()
