install.packages('ggplot2')
install.packages('plotly')
library(ggplot2)
library(plotly)

# Set the directory
setwd("C:/Users/maru/Documents/dsNanodegree/machine-learning-master/projects/finding_donors/dataAnalysisR/")

# Load the datasets
bt <- read.csv('indicator who bad_teeth.csv')
c <- read.csv('countries.csv')
gdp <- read.csv('gdp2016.csv')
education <- read.csv('education.csv')

# Add a education mean score column
education$education_mean_score <- ((education$reading+education$math+education$science)/3)

# Change columns names
names(bt)[1] <- paste('name')
names(bt)[2] <- paste('bad_teeth_indice')
names(gdp)[2] <- paste('gdp')

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
  labs(x="Bad Teeth Indicator",y="Education Mean Score") + 
  theme(plot.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=15, hjust=10)) +
  theme(axis.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=18, hjust = 5)) +
  theme(legend.position="right")

ggplotly(p_educa_teeth) %>% 
  layout(title = "Education x Bad Teeth Indicator x GDP x World Sub Region",
         #xaxis = list(showticklabels = FALSE),
         legend = list(orientation = "v",
                       y = 0, x = 10))

ggplot(data = final_df, aes(x = bad_teeth_indice, y = education_mean_score, size = gdp, color = sub_region)) +
  geom_point() +
  ggtitle("Education x Bad Teeth Indicator x GDP x World Sub Region") +
  labs(x="Bad Teeth Indicator",y="Education Mean Score") + 
  theme(plot.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=15, hjust=0)) +
  theme(axis.title = element_text(family = "Trebuchet MS", color="#666666", face="bold", size=18, hjust = 0)) +
  theme(legend.position="right")
  