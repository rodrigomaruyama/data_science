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
