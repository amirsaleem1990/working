current_date=2020-01-02
desired_date=2019-12-28
awk  "$current_date, $desired_date"
# git log --date=iso --pretty=format:'%ad%x08%aN' | awk "$0 >= $desired_date && $0 <= $current_date"