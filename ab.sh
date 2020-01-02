current_date="2020-01-02"
desired_date="2019-12-28"
git log --date=iso --pretty=format:'%ad%x08%aN' | awk '$0 >= "2019-12-28-01-01" && $0 <= "2020-01-02"'
# awk '$0 >= "2013-01-01" && $0 <= "2013-12-01"'
# git log --date=iso --pretty=format:'%ad%x08%aN' | awk "$0 >= $desired_date && $0 <= $current_date" 