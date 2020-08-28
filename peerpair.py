#!/usr/bin/python3

# peerpair.py
# Corey Welton <cwelton@redhat.com>
#
# Purpose:
# To create x number of pairs, based on a roster
# wherein a CSV roster contains each of: name, organization, email and,
# whereby no names can be matched with anyone in the same organization.

import csv
import random
import time
roster = open("orgtest.csv")
userorg = []
output = csv.reader(roster, delimiter=",")
for row in output:
    userorg.append(row)

# You obviously can't pair if you have an odd number of participants
if len(userorg) % 2 != 0:
    print("Your user list does not contain an even number of rows.")
    print("Pairing cannot continue.")
    quit()

success = 0
iteration = 0

# Probably won't need to worry about max_attempts, but this gives us a
# hard exit. If you find yourself iterating over a million times without
# matches, there's either something wrong with your data, or you've
# provided enough data as to surpass limitations of this script's 
# simple mind.
max_attempts = 1000000

while (success == 0 and iteration < max_attempts):
    play_data = []
    iteration += 1
    if iteration >= max_attempts:
        print("Giving up, after a maximum number of tries.")
        print("You might want to check your data for feasibility.\n")
        quit()
    print("Attempt #", iteration)
    for i in userorg:
        play_data.append(i)
    my_pairs = []

# Roughly speaking, the steps below:
# 1. Pick pairs at random and remove them from the queue
# 2. Assure they don't match.
# 3. If they do match, we start over
# 4. Continue until everyone is matched.
#
# There's surely a better algorithm to do this, but I'm not that saavy.
# In any case, this method seems to scale OK to at least 50 people
# split evenly across 5 orgs
#
    while len(play_data) > 0:
        pair = []
        p1 = random.choice(play_data)
        play_data.remove(p1)
        p2 = random.choice(play_data)
        play_data.remove(p2)
        pair.append(p1)
        pair.append(p2)
        my_pairs.append(pair)
    for mp in my_pairs:
        a1 = []
        a2 = []
        a1, a2 = mp
        if mp[0][2] == mp[1][2]:
            print("Pairing effort failed, retrying...")
            success = 0
            break
        else:
            success = 1

timestamp = str(int(time.time()))
csv_filename = "output-" + timestamp + ".csv"
print("Success! \nTotal Attempts:", iteration)
print(" Pairings being written to:", csv_filename)
with open(csv_filename, "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["Peer 1 Email", "Peer 1", "Peer 1 Org", "Peer 2 Email",
                     "Peer 2", "Peer 2 Org"])
    for mp in my_pairs:
        writer.writerow([mp[0][0], mp[0][1], mp[0][2], mp[1][0],
                         mp[1][1], mp[1][2]])
#    raw_input("Press Enter to continue...")
