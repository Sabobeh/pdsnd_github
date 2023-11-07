#This is the code file

import time
import pandas as pd
import numpy as np

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
    while True:
        city = input('Select a city to explore from the following: [chicago] [new york city] [washington]\n')
        if (city.lower() in CITY_DATA.keys()):
            print('You just selected {}, smart Choice!'.format(city.lower()))
            break
        print("Please make sure to choose one of the listed cities with the correct SPELLING and SPACING!")
            
           
   

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nSelect a month to explore from the following: [January] [February] [March] [April]] [May] [June] or all of them [ALL]\n')
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if (month.lower() in months) or (month.lower() == 'all'):
            print('You just selected {}'.format(month.lower()))
            break
        print("Please make sure to choose one of the listed options with the correct SPELLING and SPACING!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nSelect a day to explore from the following: [sunday] [monday] [tuesday] [wednesday] [thursday] [friday] [saturday] or all of them [ALL]\n')
        days = ['sunday', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday']
        if (day.lower() in days) or (day.lower() == 'all'):
            print('You just selected {}'.format(day.lower()))
            break
        print("Please make sure to choose one of the listed options with the correct SPELLING and SPACING!")


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
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
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

    # TO DO: display the most common month
    print('The most Frequent Month is: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most frequent Day of the Week: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most frequent Hour is: ',df['hour'].mode()[0])

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # TO DO: display most commonly used start station
    print('The most popular Start Station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most popular Start Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combinations are:\n',  (df['Start Station'] + '     To     '  + df['End Station']).mode()[0] )

    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    # TO DO: display total travel time
    print('Total Travel Time during the Selected Period is: ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travel Time during the Selected Period is: ', df['Trip Duration'].mean())

    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # TO DO: Display counts of user types
    print('User Types counts:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if (city.lower() != 'washington'):
        print(('Gender counts:\n', df['Gender'].value_counts()))
    else:
        print('Gender data is not available for the city of Washington')


    # TO DO: Display earliest, most recent, and most common year of birth
    if (city.lower() != 'washington'):
        print('Earliest year of birh: ', df['Birth Year'].min())
        print('Latest year of birh: ', df['Birth Year'].max())
        print('Most Common year of birh: ', df['Birth Year'].mode()[0])
    else:
        print('Birth Year data is not available for the city of Washington')

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        ans = input('Would you like to print 5 rows of raw data? type [yes]\n')
        if ans.lower() == 'yes':
            for i in range(0, len(df. index), 5):
                print(df.iloc[i:i+5])
                answer = input('Would you like to print 5 more rows of raw data? type [yes]\n')
                if answer.lower() != 'yes':
                    break

        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
