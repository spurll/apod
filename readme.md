Astronomy Picture of the Day
============================

Fetches NASA's Astronomy Picture of the Day. Can be set to run daily (via cron or your preferred scheduling program), allowing the user to have a diverse and ever-growing collection of astronomy-related desktop backgrounds! Science!

Instructions
============

Run `astronomy_picture.py`, which takes the following arguments:

### Arguments

Options:
* -d, --date: Downloads the astronomy picture for the specified date (in YYYY MM DD format). Defaults to today. (Cannot be used with `-n`.)
* -r, --dir: Downloads the astronomy picture(s) to the specified directory. Defaults to ~/Pictures/NASA/.

Flags:
* -n, --new: Downloads all new pictures of the day since the most recent picture on file. (Cannot be used with `-d`.)

Bugs and Feature Requests
=========================

Feature Requests
----------------

None.

Known Bugs
----------

None.

Astronomy Picture of the Day
============================

NASA's Astronomy Picture of the Day can be found [here](http://apod.nasa.gov/apod/).

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
