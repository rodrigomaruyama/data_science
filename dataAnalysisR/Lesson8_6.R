setwd("C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/")
pf <- read.delim('pseudo_facebook.tsv')
pf$year_joined <- floor(2014 - pf$tenure/365)
pf$year_joined.bucket <- cut(pf$year_joined, breaks=c(2004, 2009, 2011, 2012, 2014))
pf$prop_initiated <- ifelse(pf$friend_count != 0, pf$friendships_initiated / pf$friend_count, 0)

# 1st
ggplot(data = pf, aes(x = tenure, y = prop_initiated), color = 'year_joined.bucket') + geom_line()

# 2nd 
ggplot(data = pf, aes(x = tenure, y = prop_initiated), stat = 'median') + geom_line(aes(color = 'year_joined.bucket'))

# https://discussions.udacity.com/t/problem-set-5-cant-create-line-graph-of-the-median-of-prop-initiated-vs-tenure-and-color-the-line-segment-by-year-joined-bucket/20438/13
# Final but still not perfect
ggplot(data = pf, aes(x = tenure, y = prop_initiated)) + geom_line(aes(colour = year_joined.bucket), stat = 'summary', fun.y = median)
