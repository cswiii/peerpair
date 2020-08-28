# Peerpair

## Purpose
As you might guess from the name, Peerpair was created in order to create random pairings of people. However, this tool provides the ability to do so when there is another criteria which you want to ensure is satisfied in the pairing. More specifically, if you want to limit certain matches, ensuring no one who shares a specified criteria is matched, PeerPair provides this functionality.

## Requirements
- python 3
- import csv
- import random
- import time

## How it Works
Peerpair is admittedly fairly primitive. It randomly matches peers from an array created by reading a CSV file (see below). If at any point it creates a match where the two peers share the same criteria, it restarts.

As you might guess, this is probably not the most efficient way to do this. However, it does the job for lists of at least 100 people, completing in seconds. It is untested for very large groups, such as 10000 people or more.

By default, Peerpair will give up after a million attempts. It should not take anywhere near that number of attempts for smaller datasets however. If you have a small dataset and you find it is taking an extraordinary period of time to create pairs, you probably need to examine your dataset for feasibility.

Peerpair will fail gracefully if there is an odd number of rows in your data.

## How to Use It
Peerpair reads a csv file, "orgtest.csv", for which each line contains exactly three values:

- Email address
- Name
- Criteria

For the purposes of this document (and as the variable is notated in the code), we'll use "Organization". However, in a practical sense, the third value, used as a differentiator, can be anything you want. 

**Example:**

```
john@example.com,John,Org_1
nikhil@example.com,Nikhil,Org_2
```
*Note:* The CSV filename is currently hard-coded. Parameterization may be added in the future.

To create your pairings, simply ensure the csv is populated and run:

```
./peerpair.py
```
This will result in an 'output' file, where **output-** in the filename is appended with a unix timestamp.

The first line of the output file contains CSV header information, making the data suitable for import into a spreadsheet. Subsequent lines contain all of your peer matches.

```
Peer 1 Email,Peer 1,Peer 1 Org,Peer 2 Email,Peer 2,Peer 2 Org
john@example.com,John,Org_1,nikhil@example.com,Nikil,Org_2
```

