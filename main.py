from time import sleep
import twitter_tweet

if __name__ == '__main__':

    country = (
        'Cairo',
        'Chicago',
        'Costa Rica',
        'Los Angeles',
        'Mexico City',
        'New York',
        'Panama',
        'Bankok',
        'India',
        'Dubai',
        'Hon Kong',
        'Kuwait',
        'Singapore',
        'Japan',
        'Melbourne',
        'Sydney',
        'Canada',
        'Germany',
        'England',
        'Luxembourg',
        'Moscow',
        'Rome',
        'Alaska',
        'Poland'
                )

    while True:

        for i in country:
            twitter_tweet.TweetContent(i).tweet()
            sleep(3600)
