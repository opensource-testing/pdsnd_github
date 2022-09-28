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
    city_name = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please sselect the city you want to explore it`s data\n' 'Chicago ,New York City or Washington :\n ').lower()
    while city not in city_name:
        city = input('Please enter a VALID City name as mentioned above !\n')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Select a Month you want to extract data from\n''January , February , ... , June , Enter ''"All"'' to select all .\n').lower()
    while month not in months:
        month = input('Please Enter a VALID month as mentioned above !!\n')
        if month == 'all':
            month = months
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please select a Day\n''Saturday , Monday,...Friday.\n''Or Enter '"ALL "'to select all :').lower()
    while day not in days:
        day = input('Please Enter a Valid Day name !!\n')
        if day.lower() == 'all' :
            day = days
    if (month,day) != 'all':
        print('Filtering Data For :'+ city.capitalize(),',' +month.capitalize(),'on '+day.capitalize(),' :')
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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_statistics(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        common_month = months[df['month'].mode()[0]-1]
        print('Most Common Month:', common_month.capitalize())
    # display the most common day of week
    if day == 'all':
        common_day = df ['day_of_week'].mode()[0]
        print('Most Common Day:', common_day.capitalize())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_statistics(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + '_' + df['End Station']).mode()[0]
    print('Most Common Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def tripDuration_statistics(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    total_in_hrs=time.strftime('%H:%M:%S', time.gmtime(total_travel_time))
    print('Total Travel Time:', total_in_hrs)

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    avg_in_hrs=time.strftime('%H:%M:%S', time.gmtime(avg_time))
    print('Total Travel Time:', avg_in_hrs)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        user_types = df['User Type'].value_counts()
        print('Counts of Each User:', user_types)
    except :
        print('Sorry, No Gender Data for Washington!!')

    # Display counts of gender
    try:
        user_genders = df['Gender'].value_counts()
        print('Counts of User Gender:', user_genders)
    except:
        print('Sorry, No Gender Data for Washington!!')
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year=df['Birth Year'].max()
        print('Earliest Year of Birth:', earliest_year)
        most_recent_year=df['Birth Year'].min()
        print('Most Recent Year of Birth:', most_recent_year)
        most_common_year=df['Birth Year'].mode()
        print('Most Common Year of Birth:', most_common_year)
    except:
        print('Sorry, No Birth Year Data for Washington!!')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def viewing_data(df) :
    viewing_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0
    while viewing_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: Yes OR No \n").lower()
        if view_display== 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_statistics(df, month, day)
        station_statistics(df)
        tripDuration_statistics(df)
        user_stats(df)
        viewing_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()