# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:46:14 2018

@author: Weber
"""
import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Please enter a city from Chicago, New york city, Washington: ")).lower()
        if city in CITY_DATA:
            break
        else:
            print("Oops,Since the city you input is not in Chicago, New york city, Washington, please enter again!")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    while True:
        month = str(input("Please enter a month from January to June.\n You can also enter 'all' if you want to extract all months data: ")).lower()
        if month in months:
            break
        else:
            print("Oops,Since the month you input is not 'all' or is not including in January to June. Please enter again!")
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = str(input("Please enter a day in a week like 'Friday'\n You can also enter 'all' if you want to extract all days data: ")).lower()
        if day in days:
            break
        else:
            print("Oops,Since the day you input is not 'all' or is not in a proper format. Please enter again!")
            continue

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

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day:', common_day)

    # TO DO: display the most common start hour
    common_start_hour =  df['Start Time'].dt.hour.mode()[0]
    print('Most Popular Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_stat = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start_stat)

    # TO DO: display most commonly used end station
    common_end_stat = df['End Station'].mode()[0]
    print('Most commonly used end station',common_end_stat )
    # TO DO: display most frequent combination of start station and end station trip
    df['Station_Combination'] = df['Start Station']+df['End Station']
    print('Most frequent combination of start station and end station trip', df['Station_Combination'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total travel time:', total_trip_duration)

    # TO DO: display mean travel time
    avg_trip_duration = df['Trip Duration'].mean()
    print('Total travel time:', avg_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('counts of user types:', user_types_count)

    # TO DO: Display counts of gender
    # washington.csv doesn't have gender variable
    # so we have to create a statement to solve it
    if "Gender" not in df:
        print('\nSorry, but the dataset of city you extract is lack of "Gender" variable QAQ"\n We cannot provide the data of Gender...\n')
    else:
        gender_count = df['Gender'].value_counts()
        print('Counts of gender:', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    # washington.csv doesn't have birth variable
    # so we have to create a statement to solve it
    if "Birth Year" not in df:
        print('\nSorry, but the dataset of city you extract is lack of "Birth Year" variable QAQ"\n We cannot provide the data of Birth...\n')  
    else:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth:', earliest_birth)
        print('Most recent birth:', recent_birth)
        print('Most common year of birth:', common_birth)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        count = -5
        while True:
            count += 5
            extract = input('\nWould you like to see individual trip data? Enter yes or no.\n')
            if extract.lower() != 'yes':
                break
            else:
                print(df[count:count+5])
                
                
                
                
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
            


if __name__ == "__main__":
	main()

