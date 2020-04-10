pip3 install coursera-dl
sudo apt -y install virtualenv
virtualenv my-coursera
cd my-coursera/
source bin/activate
git clone https://github.com/coursera-dl/coursera-dl
cd coursera-dl
pip3 install -r requirements.txt
./coursera-dl ...
coursera-dl -u amirsaleem1990@hotmail.com -p tradersCoursera sql-for-data-science
