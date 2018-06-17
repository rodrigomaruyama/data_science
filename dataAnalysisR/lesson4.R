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

# Quiz 9: Price per Carat by Cut
# https://discussions.udacity.com/t/problem-set-3-price-box-plots/158779
qplot(x=clarity,y=price,data=diamonds,geom='boxplot',fill=clarity) +
coord_cartesian(ylim=c(500,6500))
ggsave('C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/boxPlot.jpg')
g1 <- ggplot(aes(x=color, y=price), data=diamonds) + geom_boxplot()
g2 <- ggplot(aes(x=cut, y=price), data=diamonds) + geom_boxplot()
g3 <- ggplot(aes(x=clarity, y=price), data=diamonds) + geom_boxplot()
grid.arrange(g1, g2, g3, ncol=3)

# Quiz 10: Price Box Plots
qplot(x=clarity,y=price,data=diamonds,geom='boxplot',fill=clarity) +
coord_cartesian(ylim=c(500,6500))

# Quiz 11: Interquartile Range - IQR
by(diamonds$price,diamonds$color,IQR)
by(diamonds$price,diamonds$cut,IQR)
by(diamonds$price,diamonds$cut,IQR)

# Quiz 12: Price per Carat Box Plots by Color
# https://www.r-graph-gallery.com/265-grouped-boxplot-with-ggplot2/
ggplot(aes(x=color, y=price, fill=color), data=diamonds) + geom_boxplot()
ggsave('C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/pricePerCaratColor.jpg')

# Quiz 13: Carat Frequency Polygon
# https://discussions.udacity.com/t/carat-frequency-polygon-problem-set-3/21610/13
qplot(x = carat, data = diamonds, binwidth = 0.1, geom = 'freqpoly', binwidth = 0.1) 

# Quiz 15: Gapminder Data
# Instalacao de bibliotecas
install.packages('tidyr')
library('tidyr')
install.packages('dplyr')
library('dplyr')

teeth <- read.csv('indicator who bad_teeth.csv')
countries <- read.csv('countries.csv')
# Changing the column names in teeth dataframe 
colnames(teeth) <- c('name','bad_teeth')

# Merging the 2 dataframes
total <- merge(teeth, countries, by='name')

# bad_teeth histogram
ggplot(data = total, aes(x = bad_teeth)) + geom_histogram(binwidth = 0.1)
ggplot(data = total, aes(y = bad_teeth, x=region, fill=bad_teeth)) + geom_boxplot()

# bad_teeth <= 1 Box plot
df_good_teeth <- subset(total, bad_teeth <= 1)
ggplot(data = df_good_teeth, aes(y = bad_teeth, x=region, fill=bad_teeth)) + geom_boxplot()

# bad_teeth >= 4 Box plot
df_bad_teeth <- subset(total, bad_teeth >= 4)
ggplot(data = df_bad_teeth, aes(y = bad_teeth, x=region, fill=bad_teeth)) + geom_boxplot()

# Max, Min, Median, Mean
max(total$bad_teeth)
min(total$bad_teeth)
median(total$bad_teeth)
mean(total$bad_teeth)

# Quiz 16: Exploring Your Friends' Birthdays
