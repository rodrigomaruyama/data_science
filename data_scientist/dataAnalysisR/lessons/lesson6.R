install.packages('ggplot2')
library(ggplot2)
data(diamonds)

# Quiz 1, 2
ggplot(data=diamonds, aes(x=price, y=x)) +
  geom_point()

# Quiz 3
cor.test(diamonds$price, diamonds$x)
cor.test(diamonds$price, diamonds$y)
cor.test(diamonds$price, diamonds$z)

# Quiz 4, 5, 6
ggplot(data=diamonds, aes(y=price, x=depth)) +
  geom_point(alpha= 1/100) +
  scale_y_continuous(breaks = seq(0, 20000, by = 2000)) +
  scale_x_continuous(breaks = seq(40, 70, by = 1))

# Quiz 7
cor.test(diamonds$price, diamonds$depth)

# Quiz 8
p1 <- ggplot(aes(y=price, x=carat), data=diamonds) +
  geom_point()

p2 <- ggplot(aes(y=price, x=carat), data=subset(diamonds, (price <= 18635 & carat <= 4.96))) +
  geom_point()

install.packages('gridExtra')
library(gridExtra)

grid.arrange(p1, p2, ncol=2)

# Quiz 9
diamonds$volume <- diamonds$x*diamonds$y*diamonds$z
ggplot(aes(y=price, x=volume), data=diamonds) +
  geom_point()

# Quiz 10
subset(diamonds, volume == 0)

# Quiz 11: Correlations on Subsets
s_diamonds <- subset(diamonds, volume <= 800 & volume != 0)
cor.test(s_diamonds$price, s_diamonds$volume)

# Quiz 12: Adjustments - price vs. volume
# https://ggplot2.tidyverse.org/reference/geom_smooth.html
ggplot(aes(y=price, x=volume), data=s_diamonds) +
  geom_point(alpha = 1/50) +
  geom_smooth(method = lm)

# Quiz 13: Mean Price by Clarity
# https://rpubs.com/profversaggi/lesson_four_problem_set
install.packages('dplyr')
library(dplyr)
diamondsByClarity <- diamonds %>%
  group_by(clarity) %>%
  summarise(mean_price = mean(price),
            median_price = median(price),
            min_price = min(price),
            max_price = max(price),
            n = n())

# Quiz 14: Bar Charts of Mean Price
diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))

diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))

p1 <- ggplot(data=diamonds_mp_by_clarity, aes(clarity, mean_price)) + geom_col()

p2 <- ggplot(data=diamonds_mp_by_color, aes(color, mean_price)) + geom_col()

grid.arrange(p1, p2, ncol=1)

# Quiz 15: 

# Quiz 16:
setwd("C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/")
bt <- read.csv('../dsNanodegree/data_scientist/dataAnalysisR/data/indicator who bad_teeth.csv')
c <- read.csv('../dsNanodegree/data_scientist/dataAnalysisR/data/countries.csv')
gdp <- read.csv('../dsNanodegree/data_scientist/dataAnalysisR/data/gdp2016.csv')
# https://www.theguardian.com/news/datablog/2010/dec/07/world-education-rankings-maths-science-reading
education <- read.csv('../dsNanodegree/data_scientist/dataAnalysisR/data/education.csv')
education$education_mean_score <- ((education$reading+education$math+education$science)/3)


names(bt)[1] <- paste('name')
names(bt)[2] <- paste('bad_teeth_indice')
names(gdp)[2] <- paste('gdp')

new_c <- c[,c('name', 'region', 'sub.region')]

# https://www.statmethods.net/management/merging.html
final_df <- merge(bt, new_c, by='name')
final_df <- merge(final_df, gdp, by='name')
names(final_df)[4] <- 'sub_region'
final_df$gdp <- gsub(',', '', final_df$gdp)
final_df$gdp <- as.numeric(final_df$gdp)

final_df <- merge(final_df, education, by = 'name')

# https://www.statmethods.net/input/missingdata.html
# mean(final_df$gdp, na.rm=TRUE)

# Plots
ggplot(data=final_df, aes(x=region, y=bad_teeth_indice)) +
  geom_boxplot()

# https://stackoverflow.com/questions/1330989/rotating-and-spacing-axis-labels-in-ggplot2
# http://www.sthda.com/english/wiki/ggplot2-box-plot-quick-start-guide-r-software-and-data-visualization
# 
ggplot(data=final_df, aes(x=sub_region, y=bad_teeth_indice)) +
  geom_boxplot() +
  #theme(axis.title.x=element_blank(),
  #      axis.text.x=element_blank(),
  #      axis.ticks.x=element_blank())
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

region <- final_df %>%
  group_by(region) %>%
  summarise(mean_indice = mean(bad_teeth_indice),
            median_indice = median(bad_teeth_indice),
            min_indice = min(bad_teeth_indice),
            max_indice = max(bad_teeth_indice),
            n = n())

p1 <- ggplot(data=region, aes(x=region, y=mean_indice)) +
  geom_col(fill='blue')

p2 <- ggplot(data=region, aes(x=region, y=median_indice)) +
  geom_col(fill='blue')

p3 <- ggplot(data=region, aes(x=region, y=min_indice)) +
  geom_col(fill='blue')

p4 <- ggplot(data=region, aes(x=region, y=max_indice)) +
  geom_col(fill='blue')

grid.arrange(p1, p2, p3, p4, ncol=2)

sub_region <- final_df %>%
  group_by(sub_region) %>%
  summarise(mean_indice = mean(bad_teeth_indice),
            median_indice = median(bad_teeth_indice),
            min_indice = min(bad_teeth_indice),
            max_indice = max(bad_teeth_indice),
            n = n())

p1 <- ggplot(data=sub_region, aes(x=sub_region, y=mean_indice)) +
  geom_col(fill='blue') +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

p2 <- ggplot(data=sub_region, aes(x=sub_region, y=median_indice)) +
  geom_col(fill='blue') +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

p3 <- ggplot(data=sub_region, aes(x=sub_region, y=min_indice)) +
  geom_col(fill='blue') +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

p4 <- ggplot(data=sub_region, aes(x=sub_region, y=max_indice)) +
  geom_col(fill='blue') +
  theme(axis.text.x = element_text(angle = 90, hjust = 1))

grid.arrange(p1, p2, p3, p4, ncol=2)

cor.test(final_df$bad_teeth_indice, final_df$gdp)

p_educa_teeth <- ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = sub_region)) +
  #labs(title = "Education x Bad Teeth Indicator x GDP x World Sub Region", y = "Education Mean Score", x = "Bad Teeth Indicator") +
  geom_point(na.rm=TRUE) 
#  scale_y_continuous(seq(0, 101000, by = 20000))
  #theme(axis.text.x = element_text(angle = 90, hjust = 1))

# https://cdr.ibpad.com.br/htmlwidgets.html
install.packages('plotly', dependencies = TRUE)
install.packages('devtools')
devtools::install_github("ropensci/plotly")

ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = sub_region)) +
  geom_point() +
  ggtitle("Education x Bad Teeth Indicator x GDP x World Sub Region") +
  labs(x="Bad Teeth Indicator",y="Education Mean Score") + 
  theme(plot.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=15, hjust=0)) +
  theme(axis.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=18, hjust = 0)) +
  theme(legend.position="right")

ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = sub_region)) +
  geom_point() +
  ggtitle('Education x Bad Teeth Indicator x GDP x World Sub Region') +
  labs(x = 'Bad Teeth Indicator', y = 'Education Mean Score')

# Plot the Education x Bad Teeth Indicator x GDP x World Sub Region
p_educa_teeth <- ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = sub_region)) +
  geom_point() +
  ggtitle("Education x Bad Teeth Indicator x GDP x World Sub Region") +
  labs(x="Bad Teeth Indicator",y="Education Mean Score") + 
  theme(plot.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=15, hjust=10)) +
  theme(axis.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=18, hjust = 5)) +
  theme(legend.position="right")

ggplotly(p_educa_teeth) + 
  layout(title = "Education x Bad Teeth Indicator x GDP x World Sub Region",
         #xaxis = list(showticklabels = FALSE),
         legend = list(orientation = "v",
                       y = 0, x = 10))


### Final Plot

install.packages('ggplot2')
install.packages('plotly')
library(ggplot2)
library(plotly)

# Set the directory
setwd("C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/")

# Load the datasets
bt <- read.csv('indicator who bad_teeth.csv') # https://www.gapminder.org/tools/#%24state%24time%24value=2004&delay:188.1419354838712;&entities%24filter%24;;&marker%24axis_x%24domainMin:null&domainMax:null&zoomedMin=194&zoomedMax=96846;&axis_y%24which=bad_teeth_per_child_12_yr&domainMin:null&domainMax:null;&color%24which=world_6region;;;&ui%24chart%24trails:false;;&chart-type=bubbles
c <- read.csv('countries.csv') #https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv
gdp <- read.csv('gdp2016_f.csv') #https://unstats.un.org/unsd/snaama/selbasicFast.asp

# https://www.theguardian.com/news/datablog/2010/dec/07/world-education-rankings-maths-science-reading
# https://docs.google.com/spreadsheets/d/1Rm4gr_BMteklQGIy1NapooVqSOWD9AxlhUmYFk73jHk/edit?hl=en&hl=en#gid=1
education <- read.csv('education.csv')

# Add a education mean score column
education$education_mean_score <- ((education$reading+education$math+education$science)/3)

# Change columns names
names(bt)[1] <- paste('name')
names(bt)[2] <- paste('bad_teeth_indice')

# Getting just what I want
new_c <- c[,c('name', 'region', 'sub.region')]

# Merging the dataframes
final_df <- merge(bt, new_c, by='name')
final_df <- merge(final_df, gdp, by='name')

# Change column name
names(final_df)[4] <- 'sub_region'

# Converting the gdp column value to numeric
final_df$gdp <- gsub(',', '', final_df$gdp)
final_df$gdp <- as.numeric(final_df$gdp)

# Merging the final dataframe
final_df <- merge(final_df, education, by = 'name')

# Plot the Education x Bad Teeth Indicator x GDP x World Sub Region
p_educa_teeth <- ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = sub_region)) +
  geom_point() +
  ggtitle("Education x Bad Teeth Indicator x GDP x World Sub Region") +
  labs(x="Bad Teeth Indicator",y="Education Mean Score") 

ggplotly(p_educa_teeth) %>% 
  layout(title = "Education x Bad Teeth Indicator x GDP x World Sub Region",
         #xaxis = list(showticklabels = FALSE),
         legend = list(orientation = "v",
                       y = 0, x = 10))

ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = sub_region)) +
  geom_point() +
  ggtitle("Education x Bad Teeth Indicator x GDP x World Sub Region") +
  labs(x="Bad Teeth Indicator",y="Education Mean Score")

ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = region)) +
  geom_point() +
  ggtitle("Education x Bad Teeth Indicator x GDP x World Sub Region") +
  labs(x="Bad Teeth Indicator",y="Education Mean Score")

