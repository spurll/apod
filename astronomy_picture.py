import argparse, urllib2, datetime, re, os


DESTINATION = "/Users/gem/Pictures/NASA/"


# Features to add:
#   Make it less Gem-centric by adding the ability to specify the target
#   directory or something.


"""
Default: Grab today's APoD.
Options:
    Provide a date in "yyyy mm dd" format, and grab that day's APoD.
    Provide the "new" flag to catch up on all missing APoDs.
"""

parser = argparse.ArgumentParser(description="Fetches NASA's Astronomy "
                                 "Picture of the Day.")
parser.add_argument("-d", "--date", help="The date of the APoD to fetch, in "
                    "YYYY MM DD format.", type=int, nargs=3, metavar=("YYYY",
                    "MM", "DD"), default=datetime.date.today())
parser.add_argument("-n", "--new", help="Downloads all new APoDs since the "
                    "most recent APoD on file.", action="store_true")
args = parser.parse_args()

if args.new:
    # Catch up on all missing APoDs since the latest one we have.
    # Generate a list of all of these dates, then get them one by one.
    ls = os.listdir(DESTINATION)
    pattern = re.compile(r"NASA (\d{4}) (\d{2}) (\d{2})\.\w+")
    ls = filter(pattern.match, ls)
    ls.sort()   # Since everything is stored in YYYY MM DD, this will do.

    if ls:
        # Grab everything since the last item.
        last_image = ls[len(ls) - 1]
        match = pattern.search(last_image)
        last_date = datetime.date(int(match.group(1)), int(match.group(2)),
                int(match.group(3)))
        days = (datetime.date.today() - last_date).days
        dates = [last_date + datetime.timedelta(d) for d in range(1, days + 1)]
        if not dates:
            print "Stored Astronomy Pictures of the Day appear to be "        \
                  "up-to-date."

    else:
        # No current items exist.
        print 'Error: No Astronomy Pictures of the Day found in {}. Please '  \
              'fetch at least one individually before using the "new" '       \
              'flag.'.format(DESTINATION)

else:
    # Put the date in a list.
    if isinstance(args.date, datetime.date):
        dates = [args.date]
    else:
        dates = [datetime.date(*args.date)]

# Actually download the appropriate files.
pattern = re.compile(r'<a href="(image/.+(\.\w+))"')
for date in dates:
    print "Date:        {}".format(date)
    url = "http://apod.nasa.gov/apod/ap{:%y%m%d}.html".format(date)
    print "URL:         {}".format(url)

    # Grab the HTML that points to this day's image.
    response = urllib2.urlopen(url)
    html = response.read()

    # Identify the URL of the image.
    match = pattern.search(html)
    if match:
        image = match.group(1)
        ext = match.group(2)
        print "Image:       {}".format(image)

        url = "".join(["http://apod.nasa.gov/apod/", image])
        try:
            response = urllib2.urlopen(url)

            file_name = "NASA {:%Y %m %d}{}".format(date, ext)
            destination = "".join([DESTINATION, file_name])
            print "Destination: {}".format(destination)
            local_file = open(destination, "w")

            # Write the remote data to the local file.
            local_file.write(response.read())
            local_file.close()
        except urllib2.HTTPError:
            print "Error: File not found on server! Blame NASA!"
    else:
        print "Warning: No image found for today."

    print ""
