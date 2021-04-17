import time_remaining
import tweepy
from os import environ


CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)


class TweetContent:

    def __init__(self, continent):
        self.continent = continent

    def tweet(self):

        a = time_remaining.TimeOfTimezone(self.continent).time_of_different_zone()
        if a.days == 6 or a.days == 5:
            api.update_status(f'Hurray..! you made it {self.continent} enjoy the weekend!\n'
                              f'next weekend in {a}\n\n'
                              f'#programmer #programming #coding #developer #coder #programmerslife '
                              f'#softwareengineer #development #engineering #hacker #cybersecurity #programmerlife')

        else:
            api.update_status(f"Hello {self.continent} you've gotta work more {a} until next weekend \n"
                              f"or {a.total_seconds()} seconds.\n\n"
                              f"#programmer #programming #coding #developer "
                              f"#programmerslife #developerlife #programmingisfun "
                              f"#developers #coders #ai")
        return a


if __name__ == '__main__':
    pass
