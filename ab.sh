# current_date='2020-01-02'
# desired_date='2019-12-28'
current_date=`date +%F`
git log --pretty='format:%H %an %ae %ai' | grep $current_date | wc -l