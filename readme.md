Overview
========

astronomy_picture.py
--------------------

Fetches NASA's Astronomy Picture of the Day. Can be set to run daily (via cron or your preferred scheduling program), allowing the user to have a diverse and ever-growing collection of astronomy-related desktop backgrounds! Science!

group.add_argument("-d", "--date", help="The date of the APoD to fetch, in "
                   "YYYY MM DD format.", type=int, nargs=3, metavar=("YYYY",
                   "MM", "DD"), default=datetime.date.today())
group.add_argument("-n", "--new", help="Downloads all new APoDs since the "
                   "most recent APoD on file.", action="store_true")
parser.add_argument("-r", "--dir", help="Downloads APoDs to the specified "
                    "directory. Defaults to ~/Pictures/NASA/.", type=str,
                    default=DESTINATION)

### Arguments

Options:
* -d, --date: Downloads the astronomy picture for the specified date (in YYYY MM DD format). Defaults to today. (Cannot be used with -n.)
* -r, --dir: Downloads the astronomy picture(s) to the specified directory. Defaults to ~/Pictures/NASA/.

Flags:
* -n, --new: Downloads all new pictures of the day since the most recent picture on file. (Cannot be used with -d.)

Bugs and Feature Requests
=========================

Feature Requests
----------------

* None

Known Bugs
----------

* None

Astronomy Picture of the Day
============================

NASA's Astronomy Picture of the Day can be found at:
http://apod.nasa.gov/apod/

License Information
===================

Written by Gem Newman.
http://www.startleddisbelief.com

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
