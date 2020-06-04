#!/usr/bin/env python

import os
import requests
import json
import time
import tweepy as tw
import pandas as pd
import authentication


auth = tw.OAuthHandler(authentication.consumer_key, authentication.consumer_secret)
auth.set_access_token(authentication.access_token, authentication.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)



