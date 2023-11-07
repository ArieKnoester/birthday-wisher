# birthday-wisher

A small program created as part of a Python course to introduce the
smtplib module. 

This program automates emailing people on their birthday. Birthday 
data is stored in a csv file. The program checks to see if there are
any birthdays today, selects an email template at random, then
emails them.

### Notes: For this program to work
- Constants in main.py need to be filled in.
- You'll need an 'App Password' for the sending address which is 
less secure. It is recommended to setup a separate email account 
for this.
- birthdays.csv needs to be modified.
- You may want to modify or add more email templates.
- It would be best to create a bash script and schedule it to run
this program daily.