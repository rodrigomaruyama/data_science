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
qplot(diamonds$price, geom="histogram") + xlim(c(250, 1500))
ggsave('C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/priceHistogram.jpg')

# Quiz 6: Price by Cut Histograms
# https://www.tutorialgateway.org/r-ggplot2-histogram/
ggplot(data = diamonds, aes(x = price, fill = cut)) + 
	geom_histogram(binwidth = 100) +
	facet_wrap(~ cut)

# Quiz 7: Price by cut
# https://discussions.udacity.com/t/problem-set-3-price-by-cut/128116
by(diamonds$price,diamonds$cut,max)
by(diamonds$price,diamonds$cut,min)
by(diamonds$price,diamonds$cut,median)

# Quiz 8: Scales and Multiple Histograms
qplot(x = price, data = diamonds) + facet_wrap(~cut, scales = "free_y")