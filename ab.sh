# !/bin/bash
# day=1
# current_date=`date +%F`
# desired_date=`date --date=$day" day ago" +%F`
# git log --date=iso --pretty=format:'%ad%x08%aN' | awk '$0 >= "`$desired_date`" && $0 <= "`$current_date`"'

# git log --date=iso --pretty=format:'%ad%x08%aN' | awk '$0 >= "2019-12-30" && $0 <= "2020-01-02"'

# git log --date=iso --pretty=format:'%ad%x08%aN' | awk '$0 >= $desired_date && $0 <= $current_date'

# git log --date=iso --pretty=format:'%ad%x08%aN' | awk '$0 >= "2019-12-28" && $0 <= "2020-01-02"'

current_date=2020-01-02
desired_date=2019-12-28

git log --date=iso --pretty=format:'%ad%x08%aN' | awk "$0 >= $desired_date && $0 <= $current_date"