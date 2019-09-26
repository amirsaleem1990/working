import os
os.chdir('/home/home/Desktop/my-coursera/')

os.system('source bin/activate')


password = 'tradersCoursera'

os.system('coursera-dl -u amirsaleem1990@hotmail.com -p {} {}'.format(password, input('Enter your course name')))
