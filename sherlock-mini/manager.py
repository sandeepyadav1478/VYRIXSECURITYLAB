from sherlock import spruce
from tetra4 import mailer
import csv

users = ['username8974']

if mailer(spruce(users)):
    print("Succeed.")
else:
    print("Didn't Succeed.")
