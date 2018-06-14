# Lesson 4: Explore One Variable

# setting the working directory
setwd("C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/")

install.packages('ggplot2')
library('ggplot2')
diamonds

# Quiz 1: Diamonds
nrow(diamonds)
names(diamonds)
levels(diamonds)
diamonds$color

# Quiz 2: Price Histogram
qplot(diamonds$price, geom="histogram", bins="50")

# Quiz 3: Price Histogram Summary
median(diamonds$price)
mean(diamonds$price)

# Quiz 4: Diamond counts
subset(diamonds, price < 500)
subset(diamonds, price < 250)
subset(diamonds, price >= 15000)

# Quiz 5: Cheaper Diamonds
qplot(diamonds$price, geom="histogram", bins="50")
ggsave('dsNanodegree/machine-learning-master/projects/finding_donors/priceAnalysisR/priceHistogram.jpg')
