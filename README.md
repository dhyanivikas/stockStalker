This is a simple stock tracker Python project.
It is supposed to keep track of your stocks of interest and notify you 
through Notifications (right now configured only for MacBook) and 
alarm the sound alerts whenever given stock(s) meet a certain 
drop/gain criteria set by the user.

In future, I want to automate the tracking from a database and 
add more sophisticated trackers, e.g. price < 50% of 52 week high, 
volume increase alert etc.

You'll need to add the secrets.yaml file in resources folder by yourselves
and put following entries:
{"x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
"x-rapidapi-host": "YOUR_CHOSEN_RAPIDAPI_HOST"}

I've put that file into gitignore list for obvious reasons. 
