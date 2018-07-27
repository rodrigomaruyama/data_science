---
output:
  html_document: default
  pdf_document: default
editor_options: 
  chunk_output_type: console
---
TITLE by Rodrigo P Maruyama
========================================================
# Table of contents

1. Initial Setup
  + Working Directory 
  + Package Installation
  + Libraries
  
2. Introduction
  
3. Data Structure:
  + Size
  + Summary

4. Univariate Plots Section
  + Bar plot for each variable
  + Outliers
  + Replot - Bar plot for each variable 
  + Density plot for each variable
  + Quality.2 feature creation
  + Univariate analysis

5. Bivariate Plots Section
  + ggpairs plot
  + corrplot
  + Positive, Negative and Zero Correlation Table
  + Bivariate Boxplots
  + Bivariate Scatter plots with linear regression
  + Bivariate analysis

6. Multivariate Plots Section
  + Highest Correlated features plots
  + Multivariate analysis


7. Machine Learning
  + Random Forest model
  + Tuning SVM parameters
  + SVM
  + Rpart
  + Pricipal component analysis - PCA
  + Load new Dataset
  + Random Forest
  + Tuning SVM parameters
  + SVM
  + Rpart
  + Accuracy Average

8. Final Plots and Summary
  + Plot One
  + Plot two
  + Plot Three

9. Reflection

10. Resources

# Initial Setup

## Working directory


```r
setwd("D://Documents/ead/Udacity/dsNanodegree/dataAnalysisR/project/")
```

## Package Instalation


```r
install.packages("markdown", dependencies = TRUE)
install.packages("knitr", dependencies = TRUE)
install.packages("ggplot2", dependencies = TRUE)
install.packages("knitr", dependencies = TRUE)
install.packages("dplyr", dependencies = TRUE)
install.packages('GGally', dependencies = TRUE)
install.packages('tidyverse')
install.packages('ggthemes', dependencies = TRUE)
install.packages('corrplot', dependencies = TRUE)
install.packages('e1071', dependencies = TRUE)
install.packages('rpart', dependencies = TRUE)
install.packages('randomForest', dependencies = TRUE)
install.packages('ggfortify')
install.packages('ROCR', dependencies = TRUE)
```

## Libraries 


```r
library(ROCR)
library(ggfortify)
library(ggplot2)
library(knitr)
library(dplyr)
library(GGally)
library(tidyverse)
library(ggthemes)
library(gridExtra)
library(corrplot)
library(grid)
library(lattice)
library(e1071)
library(rpart)
library(randomForest)
library(knitr) 
library(markdown)
library(htmlTable)
```

## Loading Dataset


```r
# Load the Data
wdf <- read.csv('data/wineQualityWhites.csv')
wdf$X <- NULL
```

# Introduction

We will study a white wine dataset with 4898 observations and 12 features. One
of then is the quality of the wine from 0 to 10, and the others are chemical
information. You can find a summary regarding the features in the table below.

Dataset link: [here](https://archive.ics.uci.edu/ml/datasets/wine+quality) <br>
Article link: [here](https://www.semanticscholar.org/paper/Modeling-wine-preferences-by-data-mining-from-Cortez-Cerdeira/977eda794ec436d20b22296ed5f3b4e2f72cb086)

# The Dataset Structure

## Dataset size


```r
dim(wdf)
```

```
## [1] 4898   12
```


## Summary of the Dataset:


```r
swdf <- summary(wdf)
swdf <- t.data.frame(swdf)
write.csv(swdf, file = 'summary.csv')
```


| Feature              | unit                         | Min  | 1st Qu. | Median | Mean   | 3rd Qu. | Max    |
|----------------------|------------------------------|------|---------|--------|--------|---------|--------|
| fixed.acidity        | [g(tartaric acid)/dm^3]      | 3.80 | 6.30    | 6.80   | 6.86   | 7.30    | 14.20  |
| volatile.acidity     | [g(acetic acid)/dm^3]        | 0.08 | 0.21    | 0.26   | 0.28   | 0.32    | 1.10   |
| citric.acid          | [g/dm^3]                     | 0.00 | 0.27    | 0.32   | 0.33   | 0.39    | 1.66   |
| residual.sugar       | [g/dm^3]                     | 0.60 | 1.70    | 5.20   | 6.39   | 9.90    | 65.80  |
| chlorides            | [g(acetic acid)/dm^3]        | 0.01 | 0.04    | 0.04   | 0.05   | 0.05    | 0.35   |
| free.sulfur.dioxide  | [mg/dm^3]                    | 2.00 | 23.00   | 34.00  | 35.31  | 46.00   | 289.00 |
| total.sulfur.dioxide | [g/cm^3]                     | 9.00 | 108.00  | 134.00 | 138.40 | 167.00  | 440.00 |
| density              | [g/cm^3]                     | 0.99 | 0.99    | 0.99   | 0.99   | 1.00    | 1.04   |
| pH                   |                              | 2.72 | 3.09    | 3.18   | 3.19   | 3.28    | 3.82   |
| sulphates            | [g(potassium sulphate)/dm^3] | 0.22 | 0.41    | 0.47   | 0.49   | 0.55    | 1.08   |
| alcohol              | [% vol.]                     | 8.00 | 9.50    | 10.40  | 10.51  | 11.40   | 14.20  |
| quality              |                              | 3.00 | 5.00    | 6.00   | 5.88   | 6.00    | 9.00   |

# Univariate Plots Section

## Histogram for each feature


```r
p1 <- ggplot(aes(x=fixed.acidity), data = wdf) +
  geom_bar(fill='#99CCFF')
p2 <- ggplot(aes(x=volatile.acidity), data = wdf) +
  geom_bar(fill='#99CCFF')
p3 <- ggplot(aes(x=citric.acid), data = wdf) +
  geom_bar(fill='#99CCFF')
p4 <- ggplot(aes(x=residual.sugar), data = wdf) +
  geom_bar(fill='#99CCFF')
p5 <- ggplot(aes(x=chlorides), data = wdf) +
  geom_bar(fill='#99CCFF')
p6 <- ggplot(aes(x=free.sulfur.dioxide), data = wdf) +
  geom_bar(fill='#99CCFF')
p7 <- ggplot(aes(x=total.sulfur.dioxide), data = wdf) +
  geom_bar(fill='#99CCFF')
p8 <- ggplot(aes(x=density), data = wdf) +
  geom_bar(fill='#99CCFF')
p9 <- ggplot(aes(x=pH), data = wdf) +
  geom_bar(fill='#99CCFF')
p10 <- ggplot(aes(x=sulphates), data = wdf) +
  geom_bar(fill='#99CCFF')
p11 <- ggplot(aes(x=alcohol), data = wdf) +
  geom_bar(fill='#99CCFF')
p12 <- ggplot(aes(x=quality), data = wdf) +
  geom_bar(fill='#99CCFF')

u1 <- grid.arrange(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, ncol = 4, top = textGrob("Histograms for all features",gp=gpar(fontsize=15,font=3)))

ggsave(file = 'pictures/1_univariate.png', u1)
```

![Histogram](pictures/1_univariate.png)

Histogram for all features in the dataset. We can observe that most of the
graphic have a normal distribution with a tendency for a positive skeew. The next section we will remove the outliers based on our observation on the plots below and re-plot the Histograms again.

## Removing Outliers


```r
wdf.outliers <- data.frame(wdf)

wdf.outliers <- subset(wdf.outliers, wdf.outliers$fixed.acidity < 11)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$volatile.acidity < 0.75)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$citric.acid < 1)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$residual.sugar < 30)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$chlorides < 0.10)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$free.sulfur.dioxide < 125)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$total.sulfur.dioxide < 350)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$density < 1.005)

# 139 removed
```


## Histogram without outliers

![Histogram without outliers](pictures/1_univariate_outliers.png)

Histograms re-ploted without outliers.

## Density plot for each feature with stat lines


```r
# Using a for loop for better programming practice and to save lines of code :)

feature.list <- names(wdf.outliers)
p <- list()
a <- 0
for (var in feature.list) {
  a <- a + 1

  p[[a]] <- ggplot(data = wdf.outliers, aes_string(x=var)) +
    geom_density(fill='#99CCFF') +
    geom_vline(aes_string(xintercept=mean(wdf.outliers[, var])),
               color='blue', size=0.5) +
    geom_vline(aes_string(xintercept=median(wdf.outliers[, var])),
               color='red', size=0.5) +
    geom_vline(aes_string(xintercept=quantile(wdf.outliers[, var], 0.25)),
               linetype='dashed', size=0.5) +
    geom_vline(aes_string(xintercept=quantile(wdf.outliers[, var], 0.75)),
               linetype='dashed', size=0.5) +
    ylab(NULL)

}

ggsave(file = 'pictures/density_univariate_outliers.png', do.call(grid.arrange, p))
```

Density plots for each feature with stats lines

![univariate density plots without outliers](pictures/density_univariate_outliers.png)

In this plot and from the histograms above we can see the mean, median, 1st quantile and 3rd quantile over each density distribution and a very normal distribution for all features except for residual.sugar that have a very slightly positve skeew.

## Quality.2 feature creation


```r
# | classification | Criterion       |
# |----------------|-----------------|
# | Bad            | quality < 6     |
# | Normal         | quality = 6     |
# | Good           | quality > 6     |


wdf.outliers$quality.2 <- ifelse(wdf.outliers$quality < 6, 'bad', ifelse(wdf.outliers$quality == 6, 'normal', 'good'))
wdf.outliers$quality.2 <- as.factor(wdf.outliers$quality.2)

table(wdf.outliers$quality.2)
```

```
## 
##    bad   good normal 
##   1565   1055   2139
```

```r
wdf.outliers$quality.2 <- NULL
```

| Quality.2 | raw  dataset | outliers removed dataset | removed |
|-----------|--------------|--------------------------|---------|
| bad       |     1640     |           1565           |   75    |
| normal    |     2198     |           2139           |   59    |
| good      |     1060     |           1055           |    5    |



```r
# Pie plot creation with percent legend

rating = as.numeric(c(1565, 2139, 1055))
percent <- round(100*rating/sum(rating), 1)
colors = c("red", "orange", "blue")
lable <- c('Bad', 'Normal', 'Good')
pie(rating, labels = lable, main = 'Wine quality Pie chart distribution', col = colors)
```

![Pie chart](pictures/pie_outlier.png)

## Univariate Analysis

### What is the structure of your dataset?

See Dataset Structure above.

### What is/are the main feature(s) of interest in your dataset?

The quality is the main feature of interest.

### What other features in the dataset do you think will help support your investigation into your feature(s) of interest?

From [Wine specialists](https://winefolly.com/review/wine-characteristics/) the basics characteristics are:

1. Sweetness
2. Acidity
3. Tannin
4. Alcohol
5. Body

Tannin is correlated with phenolic compounds however we don't have this variable in our dataset, and Body is a mix from all characteristics mentioned above. Then, I will focusing on the following variables:

1. quality
2. pH
3. residual.sugar
4. alcohol

### Did you create any new variables from existing variables in the dataset?

Yes, I created a new variable called quality.2 from quality as in the table below:

 classification |    Criterion
----------------|-----------------
 Bad            |   quality < 6
 Normal         |   quality = 6
 Good           |   quality > 6

### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?

No. I didn't change the original data.

# Bivariate Plots Section

## GGPAIRS plot


```r
ggpairs(wdf.outliers, title = 'GGPAIRS') + 
  theme(panel.grid.minor = element_blank(), panel.grid.major = element_blank(),         
  axis.line=element_blank(), axis.text=element_blank())
```

![Ggpairs](pictures/ggpairs_plot_outliers.png)

## CORRPLOT


```r
cor.wdf.outliers <- cor(wdf.outliers)
corrplot.mixed(cor.wdf.outliers, tl.pos = 'lt', mar=c(2,0,2,0), title = 'CORRPLOT graphic') 
```

![Corrplot](pictures/corrplot_outliers.png)

Looking at the "ggpairs" and "corrplot" plots result it is easy to have a good idea
about the correlations between the features. In the table below there is a list with a few pairs with a positive, negative and zero correlation. The positive correlation
have 4 rows but we will discharge the number 2 because those features have similar
properties.

## Positive, Negative and Zero Correlation Table

|    | Positive correlation                       | correlation | correlation outliers |
|----|--------------------------------------------|-------------|----------------------|
| 1  | density x residual.sugar                   | 0.84        | 0.84                 |
| 2  | total.sulfur.dioxide x free.sulfur.dioxide | 0.62        | 0.61                 |
| 3  | density x total.sulfur.dioxide             | 0.53        | 0.55                 |
| 4  | quality x alcohol                          | 0.44        | 0.44                 |

|    | Negative correlation                       | correlation | correlation outliers  |
|----|--------------------------------------------|-------------|-----------------------|
| 1  | density x alcohol                          | -0.78       | -0.81                 |
| 2  | total.sulfur.dioxide x alcohol             | -0.45       | -0.46                 |
| 3  | alcohol x residual.sugar                   | -0.45       | -0.48                 |

|    | Zero correlation                           | correlation | correlation outliers  |
|----|--------------------------------------------|-------------|-----------------------|
| 1  | quality x citric.acid                      | ~ 0         | ~ 0                   |
| 2  | sulphates x chlorides                      | ~ 0         |  0.06                 |
| 3  | density x volatily.acidity                 | ~ 0         | -0.03                 |

## Bivariate Boxplots


```r
# Removing outliers for density and residual.sugar for better visualization

# Positive correlation plots
p1 <- ggplot(data = wdf.outliers, aes(x = density, y = residual.sugar)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  scale_y_continuous(limits = c(0, 25)) +
  ggtitle('density X residual.sugar')

p2 <- ggplot(data = wdf.outliers, aes(x = density, y = total.sulfur.dioxide)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  ggtitle('density X total.sulfur.dioxide')

p3 <- ggplot(data = wdf.outliers, aes(x = quality, y = alcohol)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  ggtitle('quality X alcohol')

# Negative correlation plots
p4 <- ggplot(data = wdf.outliers, aes(x = density, y = alcohol)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  ggtitle('density X alcohol')

p5 <- ggplot(data = wdf.outliers, aes(y = total.sulfur.dioxide, x = alcohol)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  ggtitle('total.sulfur.dioxide X alcohol')

p6 <- ggplot(data = wdf.outliers, aes(x = alcohol, y = residual.sugar)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  scale_y_continuous(limits = c(0, 30)) +
  ggtitle('alcohol X residual.sugar')

# Zero correlation
p7 <- ggplot(data = wdf.outliers, aes(x = quality, y = citric.acid)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  scale_y_continuous(limits = c(0, 1)) +
  ggtitle('quality X citric.acid')

p8 <- ggplot(data = wdf.outliers, aes(y = sulphates, x = chlorides)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  ggtitle('sulphates X chlorides')

p9 <- ggplot(data = wdf.outliers, aes(x = density, y = volatile.acidity)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  scale_y_continuous(limits = c(0, 0.9)) +
  ggtitle('density X volatile.acidity')

grid1 <- grid.arrange(p1, p2, p3, ncol = 3, top = textGrob("Bivariate Boxplots with Positive Correlation",gp=gpar(fontsize=15,font=3)))

grid2 <- grid.arrange(p4, p5, p6, ncol = 3, top = textGrob("Bivariate Boxplots with Negative Correlation",gp=gpar(fontsize=15,font=3)))

grid3 <- grid.arrange(p7, p8, p9, ncol = 3, top = textGrob("Bivariate Boxplots with Zero Correlation",gp=gpar(fontsize=15,font=3)))

ggsave(file = 'pictures/1_boxplot_bivariate_outliers.png', grid1)
ggsave(file = 'pictures/2_boxplot_bivariate_outliers.png', grid2)
ggsave(file = 'pictures/3_boxplot_bivariate_outliers.png', grid3)
```

![Bivariate Boxplots](pictures/1_boxplot_bivariate_outliers.png)

![Bivariate Boxplots](pictures/2_boxplot_bivariate_outliers.png)

![Bivariate Boxplots](pictures/3_boxplot_bivariate_outliers.png)


## Bivariate Scatter plots with linear regression line


```r
# Removing outliers for better visualization

# Solution for Warning message: "Continuous x aesthetic -- did you forget aes(group=...)? "
# https://ggplot2.tidyverse.org/reference/geom_boxplot.html

# Positive correlation plots
p1 <- ggplot(data = wdf.outliers, aes(x = density, y = residual.sugar)) +
  geom_point() +
  geom_smooth(method='lm',formula=y~x) +
  scale_x_continuous(limits = c(0.98, 1.01)) +
  scale_y_continuous(limits = c(0, 30))

p2 <- ggplot(data = wdf.outliers, aes(x = density, y = total.sulfur.dioxide)) +
  geom_point() +
  geom_smooth(method='lm',formula=y~x) +
  scale_x_continuous(limits = c(0.98, 1.01))

p3 <- ggplot(data = wdf.outliers, aes(x = quality, y = alcohol)) +
  geom_point()

# Negative correlation plots
p4 <- ggplot(data = wdf.outliers, aes(x = density, y = alcohol)) +
  geom_point() +
  geom_smooth(method='lm',formula=y~x) +
  scale_x_continuous(limits = c(0.98, 1.01))

p5 <- ggplot(data = wdf.outliers, aes(y = total.sulfur.dioxide, x = alcohol)) +
  geom_point() +
  geom_smooth(method='lm',formula=y~x)

p6 <- ggplot(data = wdf.outliers, aes(x = alcohol, y = residual.sugar)) +
  geom_point() +
  geom_smooth(method='lm',formula=y~x) +
  scale_y_continuous(limits = c(0, 30))

# Zero correlation
p7 <- ggplot(data = wdf.outliers, aes(x = quality, y = citric.acid)) +
  geom_point()

p8 <- ggplot(data = wdf.outliers, aes(y = sulphates, x = chlorides)) +
  geom_point() +
  geom_smooth(method='lm',formula=y~x) +
  scale_x_continuous(limits = c(0, 0.2))

p9 <- ggplot(data = wdf.outliers, aes(x = density, y = volatile.acidity)) +
  geom_point() +
  geom_smooth(method='lm',formula=y~x) +
  scale_y_continuous(limits = c(0, 0.9)) +
  scale_x_continuous(limits = c(0.98, 1.01))

grid1 <- grid.arrange(p1, p2, p3, ncol = 3, top = textGrob("Bivariate Scatter plot with Positive Correlation",gp=gpar(fontsize=15,font=3)))

grid2 <- grid.arrange(p4, p5, p6, ncol = 3, top = textGrob("Bivariate Scatter plot with Negative Correlation",gp=gpar(fontsize=15,font=3)))

grid3 <- grid.arrange(p7, p8, p9, ncol = 3, top = textGrob("Bivariate Scatter plot with Zero Correlation",gp=gpar(fontsize=15,font=3)))

ggsave(file = 'pictures/1_scatterplot_bivariate_outliers.png', grid1)
ggsave(file = 'pictures/2_scatterplot_bivariate_outliers.png', grid2)
ggsave(file = 'pictures/3_scatterplot_bivariate_outliers.png', grid3)
```

![Positive COrrelation Bivariate Scatterplot](pictures/1_scatterplot_bivariate_outliers.png)

![Negative Correlation Bivariate Scatterplot](pictures/2_scatterplot_bivariate_outliers.png)

![Zero Correlation Bivariate Scatterplot](pictures/3_scatterplot_bivariate_outliers.png)



## Bivariate Analysis

### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?

- Strong Positive correlation

In the density_X_residual.sugar plot we can observe a strong correlation. The
amount of wines with lower density and residual.sugar is bigger than high values.
In density_X_total.sulfur.dioxide the plot have a eclipse format where the amount
of wines have a concentration in the midle for both features but fot total.sulfur.dioxide they are spread much more.


- Strong Negative correlation

In the density_X_alcohol plot we can see the expected behaivour once the alcohol
density is lower than the water density.
For both second and third plots they have a negative tendency nad for alcohol_X_residual.sugar they are a concentration of wines with lower residual.sugar quantities.

- Zero Correlation

Those plots we can check what was expected from the correlation value. They don't
have any strong tendency.

### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?

No.

### What was the strongest relationship you found?

|    | Positive correlation                       | correlation | correlation outliers |
|----|--------------------------------------------|-------------|----------------------|
| 1  | density x residual.sugar                   | 0.84        | 0.84                 |
| 2  | total.sulfur.dioxide x free.sulfur.dioxide | 0.62        | 0.61                 |
| 3  | density x total.sulfur.dioxide             | 0.53        | 0.55                 |
| 4  | quality x alcohol                          | 0.44        | 0.44                 |

In this table we can see the correlation using a raw dataset and the dataset
without oultliers we can't see difference between them. We can disconsidering
total.sulfur.dioxide x free.sulfur.dioxide beacuse one is part of the others.

# Multivariate Plots Section

## Highest Correlated features plots


```r
# Multivariate plots with Linear Regression

p1 <- ggplot(data = wdf.outliers, aes(x = density, y = residual.sugar, colour = quality)) +
  geom_point(alpha = 0.3) +
  geom_smooth(method='lm',formula=y~x) +
  scale_colour_gradientn(colours=rainbow(10)) +
  ggtitle('density X residual.sugar X quality')

p2 <- ggplot(data = wdf.outliers, aes(x = density, y = alcohol, colour = quality)) +
  geom_point(alpha = 0.3) +
  geom_smooth(method='lm',formula=y~x) +
  scale_colour_gradientn(colours=rainbow(10)) +
  ggtitle('density X alcohol X quality')

p3 <- ggplot(data = wdf.outliers, aes(y = sulphates, x = chlorides, colour = quality)) +
  geom_point(alpha = 0.3) +
  geom_smooth(method='lm',formula=y~x) +
  scale_colour_gradientn(colours=rainbow(10)) +
  ggtitle('sulphates X chlorides X quality')

p4 <- ggplot(data = wdf.outliers, aes(x = density, y = volatile.acidity, colour = quality)) +
  geom_point(alpha = 0.3) +
  geom_smooth(method='lm',formula=y~x) +
  scale_colour_gradientn(colours=rainbow(10)) +
  ggtitle('density X volatile.acidity X quality')


grid_multivariate <- grid.arrange(p1, p2, p3, p4, ncol = 2, top = textGrob("Multivariate Plots",gp=gpar(fontsize=15,font=3)))

ggsave(file = 'pictures/2_multivariate_outliers.png', grid_multivariate)
```

![Multivariate scatter plot](pictures/2_multivariate_outliers.png)

## Multivariate Analysis

### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?

We can confirm the correlation between density and residual.sugar in the ggpairs
 plot and linear regression line over the previous one. I all of the 4
 multivariate graphics we can observe a concentration for good wines instead
 normal and bad ones.

# Machine Learning Models

## Creating Training and Test Datasets for Raw Data


```r
# Loading wdf.raw dataset
wdf.raw <- read.csv('data/wineQualityWhites.csv')
wdf.raw$X <- NULL
wdf.raw$quality <- as.factor(wdf$quality)

# Creating train.raw and test.raw datasets
set.seed(13)
samp <- sample(nrow(wdf.raw), 0.4 * nrow(wdf.raw))
train.raw <- wdf.raw[samp, ]
test.raw <- wdf.raw[-samp, ]
```

## Creating Training and Test Datasets for Outliers


```r
# Loading wdf.outliers dataset
wdf.outliers <- data.frame(wdf.raw)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$fixed.acidity < 11)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$volatile.acidity < 0.75)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$citric.acid < 1)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$residual.sugar < 30)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$chlorides < 0.10)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$free.sulfur.dioxide < 125)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$total.sulfur.dioxide < 350)
wdf.outliers <- subset(wdf.outliers, wdf.outliers$density < 1.005)

# Creating Train.outliers and Test.outliers datasets
set.seed(13)
samp <- sample(nrow(wdf.outliers), 0.4 * nrow(wdf.outliers))
train.outliers <- wdf.outliers[samp, ]
test.outliers <- wdf.outliers[-samp, ]
```


## Random Forest Model


```r
# Random Forest Raw
a <- 0
while (a < 10){
  a <- a + 1
  model <- randomForest(quality ~ . - quality, data = train.raw)
  rf.pred <- predict(model, newdata = test.raw)
  acc.rf <- classAgreement(table(rf.pred, test.raw$quality))[1]
  time <- Sys.time() 
  str <- paste('rf', time, as.numeric(acc.rf), sep = ',')
  write(str, file = 'data/accuracy_models.csv', append = TRUE)
}

# Random Forest Raw
a <- 0
while (a < 10){
  a <- a + 1
  model <- randomForest(quality ~ . - quality, data = train.outliers)
  rf.pred <- predict(model, newdata = test.outliers)
  acc.rf <- classAgreement(table(rf.pred, test.outliers$quality))[1]
  time <- Sys.time() 
  str <- paste('rf.out', time, as.numeric(acc.rf), sep = ',')
  write(str, file = 'data/accuracy_models.csv', append = TRUE)
}
```


## Tuning the parameters SVM


```r
# Tune with raw dataset
obj.raw <- tune.svm(quality~., data = train.raw, gamma = 2^(-1:1),cost = 2^(2:4))
summary(obj.raw)
p.tune.svm.raw <- (plot(obj.raw))
# tune with outliers dataset
obj.outliers <- tune.svm(quality~., data = train.outliers, gamma = 2^(-1:1),cost = 2^(2:4))
summary(obj.outliers)
p.tune.svm.outliers <- (plot(obj.outliers))
```

![SVM tune raw](pictures/svm_tune_raw.png) 

![SVM tune outliers](pictures/svm_tune_outliers.png)

## Supported Vector Machines


```r
# SVM raw
df.list <- list(data.frame(train.raw), data.frame(test.raw))
a <- 0
while (a < 10){
  a <- a + 1
  svm.model  <- svm(quality ~ ., data = train.raw, cost = 4, gamma = 0.5)
  svm.pred <- predict(svm.model,test.raw[,-12])
  acc.svm <- classAgreement(table(svm.pred, test.raw$quality))[1]
  time <- Sys.time() 
  str <- paste('svm', time, as.numeric(acc.svm), sep = ',')
  write(str, file = 'data/accuracy_models.csv', append = TRUE)
}

# SVM outliers
df.list <- list(data.frame(train.outliers), data.frame(test.outliers))
a <- 0
while (a < 10){
  a <- a + 1
  svm.model  <- svm(quality ~ ., data = train.outliers, cost = 16, gamma = 0.5)
  svm.pred <- predict(svm.model,test.outliers[,-12])
  acc.svm <- classAgreement(table(svm.pred, test.outliers$quality))[1]
  time <- Sys.time() 
  str <- paste('svm.out', time, as.numeric(acc.svm), sep = ',')
  write(str, file = 'data/accuracy_models.csv', append = TRUE)
}
```

## Rpart


```r
# rpart raw
a <- 0
while (a < 10){
  a <- a + 1
  rpart.model <- rpart(quality ~ ., data = train.raw)
  rpart.pred <- predict(rpart.model, test.raw[,-12], type = 'class')
  table(rpart.pred,test.raw[,12])
  classAgreement(table(pred = rpart.pred,true = test.raw[,12]))
  acc.rpart <- classAgreement(table(rpart.pred, test.raw$quality))[1]
  time <- Sys.time() 
  str <- paste('rpart', time, as.numeric(acc.rpart), sep = ',')
  write(str, file = 'data/accuracy_models.csv', append = TRUE)
}

# rpart outliers
a <- 0
while (a < 10){
  a <- a + 1
  rpart.model <- rpart(quality ~ ., data = train.outliers)
  rpart.pred <- predict(rpart.model, test.outliers[,-12], type = 'class')
  table(rpart.pred,test.outliers[,12])
  classAgreement(table(pred = rpart.pred,true = test.outliers[,12]))
  acc.rpart <- classAgreement(table(rpart.pred, test.outliers$quality))[1]
  time <- Sys.time() 
  str <- paste('rpart.out', time, as.numeric(acc.rpart), sep = ',')
  write(str, file = 'data/accuracy_models.csv', append = TRUE)
}
```

## The Accuracy average for each Model


```r
# load the dataset
acc.df <- read.csv(file = 'data/accuracy_models.csv')

# Random Forest
mean.acc.rf <- mean(subset(acc.df, acc.df$model == 'rf')$accuracy)
mean.acc.rf <- format(mean.acc.rf, digits = 4)
mean.acc.rf <- as.numeric(mean.acc.rf)*100

mean.acc.rf.out <- mean(subset(acc.df, acc.df$model == 'rf.out')$accuracy)
mean.acc.rf.out <- format(mean.acc.rf.out, digits = 4)
mean.acc.rf.out <- as.numeric(mean.acc.rf.out)*100

# SVM
mean.acc.svm <- mean(subset(acc.df, acc.df$model == 'svm')$accuracy)
mean.acc.svm <- format(mean.acc.svm, digits = 4)
mean.acc.svm <- as.numeric(mean.acc.svm)*100

mean.acc.svm.out <- mean(subset(acc.df, acc.df$model == 'svm.out')$accuracy)
mean.acc.svm.out <- format(mean.acc.svm.out, digits = 4)
mean.acc.svm.out <- as.numeric(mean.acc.svm.out)*100

# Rpart
mean.acc.rpart <- mean(subset(acc.df, acc.df$model == 'rpart')$accuracy)
mean.acc.rpart <- format(mean.acc.rpart, digits = 4)
mean.acc.rpart <- as.numeric(mean.acc.rpart)*100

mean.acc.rpart.out <- mean(subset(acc.df, acc.df$model == 'rpart.out')$accuracy)
mean.acc.rpart.out <- format(mean.acc.rpart.out, digits = 4)
mean.acc.rpart.out <- as.numeric(mean.acc.rpart.out)*100
```


```r
# Print the results
paste('Random Forest Mean Accuracy: ', mean.acc.rf, '%', sep = '')
```

```
## [1] "Random Forest Mean Accuracy: 62.13%"
```

```r
paste('SVM Mean Accuracy: ', mean.acc.svm, '%', sep = '')
```

```
## [1] "SVM Mean Accuracy: 59.34%"
```

```r
paste('Rpart Mean Accuracy: ', mean.acc.rpart, '%', sep = '')
```

```
## [1] "Rpart Mean Accuracy: 52.19%"
```

```r
paste('Random Forest Mean Accuracy: ', mean.acc.rf.out, '%', sep = '')
```

```
## [1] "Random Forest Mean Accuracy: 62.38%"
```

```r
paste('SVM Mean Accuracy: ', mean.acc.svm.out, '%', sep = '')
```

```
## [1] "SVM Mean Accuracy: 58.02%"
```

```r
paste('Rpart Mean Accuracy: ', mean.acc.rpart.out, '%', sep = '')
```

```
## [1] "Rpart Mean Accuracy: 50.81%"
```

```r
acc.matrix <- matrix(c(mean.acc.rf, mean.acc.svm, mean.acc.rpart, mean.acc.rf.out, mean.acc.svm.out, mean.acc.rpart.out), ncol = 3, byrow = TRUE)
```


```r
htmlTable(acc.matrix,
          css.cell = ("padding-left: 1em; padding-right: 1em;"), 
          header =  c('Random Forest', 'SVM', 'Rpart'),
          rnames = c('RAW Data', 'Outliers Data'),
          caption="Accuracy Mean (%)")
```

<table class='gmisc_table' style='border-collapse: collapse; margin-top: 1em; margin-bottom: 1em;' >
<thead>
<tr><td colspan='4' style='text-align: left;'>
Accuracy Mean (%)</td></tr>
<tr>
<th style='border-bottom: 1px solid grey; border-top: 2px solid grey;'> </th>
<th style='border-bottom: 1px solid grey; border-top: 2px solid grey; text-align: center;'>Random Forest</th>
<th style='border-bottom: 1px solid grey; border-top: 2px solid grey; text-align: center;'>SVM</th>
<th style='border-bottom: 1px solid grey; border-top: 2px solid grey; text-align: center;'>Rpart</th>
</tr>
</thead>
<tbody>
<tr>
<td style='text-align: left;'>RAW Data</td>
<td style='padding-left: 1em; padding-right: 1em; text-align: center;'>62.13</td>
<td style='padding-left: 1em; padding-right: 1em; text-align: center;'>59.34</td>
<td style='padding-left: 1em; padding-right: 1em; text-align: center;'>52.19</td>
</tr>
<tr>
<td style='border-bottom: 2px solid grey; text-align: left;'>Outliers Data</td>
<td style='padding-left: 1em; padding-right: 1em; border-bottom: 2px solid grey; text-align: center;'>62.38</td>
<td style='padding-left: 1em; padding-right: 1em; border-bottom: 2px solid grey; text-align: center;'>58.02</td>
<td style='padding-left: 1em; padding-right: 1em; border-bottom: 2px solid grey; text-align: center;'>50.81</td>
</tr>
</tbody>
</table>


## Pricipal component analysis - PCA

To better understand how the features are correlated I ran a PCA algorithm and
I did the plot for the PCA Components and a graphic with Variance x Number of
Component to decide how many Components I will use in the following models.


```r
# PCA
wdf.pca <- prcomp(wdf.outliers[,1:11], center = TRUE, scale. = TRUE)
```


```r
# Variance plot
plot(wdf.pca, type = "l")
abline(h=0.55, v=8, col="blue")

# PCA components plots
g <- autoplot(wdf.pca, loadings = TRUE, loadings.colour = 'blue', loadings.label = TRUE, loadings.label.size = 5, alpha = 0.3, main = 'PCA')
ggsave(file = 'pictures/pca_outliers.png', g)
```

![PCA Variance](pictures/variance_pca_outliers.png)

Looking at this graphic it is easy to indentify that we can run the models with
8 components without loosing accuracy in our model.

![PCA components](pictures/pca_outliers.png)

In this graphic we can confirm some teories about the correlation between the
variables. For example we expect negative correlation with alcohol and residual.sugar
once the alcohol needs sugar to be produced. pH and citric.acid and fixed.acidity
also need to have negative correlation once the lowest pH means very acid solution.

## New PCA Datasets


```r
# New dataframe
new.wdf.pca <- data.frame(wdf.pca$x)
new.wdf.pca <- data.frame(new.wdf.pca[,1:8], quality = wdf.outliers$quality)

# Creating train and test datasets
set.seed(123)
samp <- sample(nrow(new.wdf.pca), 0.8 * nrow(new.wdf.pca))
new.train.pca <- new.wdf.pca[samp, ]
new.test.pca <- new.wdf.pca[-samp, ]
```

## Random Forest Model after PCA


```r
# Random Forest Raw
a <- 0
while (a < 10){
  a <- a + 1
  model <- randomForest(quality ~ . - quality, data = new.train.pca)
  rf.pred <- predict(model, newdata = new.test.pca[, -9])
  acc.rf <- classAgreement(table(rf.pred, new.test.pca$quality))[1]
  time <- Sys.time() 
  str <- paste('rf', time, as.numeric(acc.rf), sep = ',')
  write(str, file = 'data/accuracy_models_pca.csv', append = TRUE)
}
```

## Mean Random Forest Accuracy


```r
# load the dataset
acc.df <- read.csv(file = 'data/accuracy_models_pca.csv')

# Random Forest
mean.acc.rf <- mean(subset(acc.df, acc.df$model == 'rf')$accuracy)
mean.acc.rf <- format(mean.acc.rf, digits = 4)
mean.acc.rf <- as.numeric(mean.acc.rf)*100
```


```r
htmlTable(mean.acc.rf,
          css.cell = ("padding-left: 1em; padding-right: 1em;"), 
          header =  c('Random Forest'),
          rnames = c('Outliers Data'),
          caption="Accuracy Mean (%)")
```

<table class='gmisc_table' style='border-collapse: collapse; margin-top: 1em; margin-bottom: 1em;' >
<thead>
<tr><td colspan='2' style='text-align: left;'>
Accuracy Mean (%)</td></tr>
<tr>
<th style='border-bottom: 1px solid grey; border-top: 2px solid grey;'> </th>
<th style='border-bottom: 1px solid grey; border-top: 2px solid grey; text-align: center;'>Random Forest</th>
</tr>
</thead>
<tbody>
<tr>
<td style='border-bottom: 2px solid grey; text-align: left;'>Outliers Data</td>
<td style='padding-left: 1em; padding-right: 1em; border-bottom: 2px solid grey; text-align: center;'>66.45</td>
</tr>
</tbody>
</table>

We could increase the accuracy in more than 4% with Random Forest and PCA.

# Final Plots and Summary

## Plot One


```r
# PCA
wdf.pca <- prcomp(wdf.outliers[,1:11], center = TRUE, scale. = TRUE)
# PCA components plots
autoplot(wdf.pca, loadings = TRUE, loadings.colour = 'blue', loadings.label = TRUE, loadings.label.size = 5, alpha = 0.3, main = 'PCA')
```

![PCA components](pictures/pca_outliers.png)

### Description One

THe PCA component plot is a very ilustrative way to see the correlation between the features. As we expected quality is very negative correlated with residual.sugar as pH and Acidty as well.

## Plot Two

```r
good.wine <- median(subset(wdf.outliers, quality > 6)$alcohol)
normal.wine <- median(subset(wdf.outliers, quality == 6)$alcohol)
bad.wine <- median(subset(wdf.outliers, quality < 6)$alcohol)

ggplot(data = wdf.outliers, aes(x = quality, y = alcohol)) +
  geom_boxplot(aes(group = cut_width(quality, 1)), fill = '#99CCFF') +
  ggtitle('quality X alcohol') +
  geom_hline(yintercept = good.wine, color = 'blue') +
  geom_hline(yintercept = normal.wine, color = 'orange') +
    geom_hline(yintercept = bad.wine, color = 'red')
```

### Description Two

In this Graphic we can see that the Very Good wines (quality = 9) have a very low variance. If we look the Median lines for each class (Good, Normal, Bad) we can see that the main Wine Qualities are 5, 6 and 7 because those lines are matching with their respective Medians. This is just another way we saw in the Density graphics where we plot the Mean and Median over the distribution for each feature. 



## Plot Three

```r
wdf.outliers$quality <- as.numeric(wdf.outliers$quality)

p1 <- ggplot(data = wdf.outliers, aes(x = density, y = residual.sugar, colour = quality)) +
    geom_point(alpha = 0.3) +
    geom_smooth(method='lm',formula=y~x) +
    scale_colour_gradientn(colours=rainbow(10))

p2 <- ggplot(data = wdf.outliers, aes(x = density, y = alcohol, colour = quality)) +
    geom_point(alpha = 0.3) +
    geom_smooth(method='lm',formula=y~x) +
    scale_colour_gradientn(colours=rainbow(10))


p3 <- ggplot(data = wdf.outliers, aes(y = sulphates, x = chlorides, colour = quality)) +
    geom_point(alpha = 0.3) +
    geom_smooth(method='lm',formula=y~x) +
    scale_colour_gradientn(colours=rainbow(10))

p4 <- ggplot(data = wdf.outliers, aes(x = density, y = volatile.acidity, colour = quality)) +
    geom_point(alpha = 0.3) +
    geom_smooth(method='lm',formula=y~x) +
    scale_colour_gradientn(colours=rainbow(10))

grid.arrange(p1, p2, p3, p4, ncol = 2, 
  top = textGrob("Outliers Dataset",gp=gpar(fontsize=15,font=3)))
```

![Multivariate scatter plot](pictures/2_multivariate_outliers.png)

### Description Three

In this Multivariate Scatter plot it is easy to note that the even the correlation is positive, negative or zero, the Good Wines have  clear tendency in each case. For Positive and Negative correlation plots, the Good wines are above the Linear Regression Line and For Zero COrrelation plots they are in left, which means low Density and low Chlorides.

------

# Reflection

The models I made didn't perform well as I expected. The accuracy with PCA
was a good choice to try to eliminate useless information in the dataset and we
could see in the results some accuracy improvement, around 4%.

# General resources

## Articles

- Modeling wine preferences by data mining from physicochemical properties by Paulo Cortez,Ant?nio Cerdeira, Fernando Almeida, Telmo Matos, Jos? Reis. (2009) 547-553 <br>
- Support Vector Machines, The Interface to libsvm in package e1071 by David Meyer <br>
- A Practical Guide to Support Vector Classification by Chih-Wei Hsu, Chih-Chung Chang, and Chih-Jen Lin (2016)

## R
Remove the column X from Dataframe:  https://stackoverflow.com/questions/6286313/remove-an-entire-column-from-a-data-frame-in-r/30620946 <br>
Write function: https://stat.ethz.ch/R-manual/R-devel/library/base/html/write.html <br>
Get current Date and Time: https://stat.ethz.ch/R-manual/R-devel/library/base/html/Sys.time.html <br>
Concatenate Strings: https://stat.ethz.ch/R-manual/R-devel/library/base/html/paste.html <br>
Format function: https://www.rdocumentation.org/packages/base/versions/3.5.1/topics/format <br>
htmlTable: https://cran.r-project.org/web/packages/htmlTable/vignettes/tables.html <br>
ROCR: https://cran.r-project.org/web/packages/ROCR/ROCR.pdf <br>

## Style and Markdown tools and cheatsheet

Marktable generator: https://www.tablesgenerator.com/markdown_tables <br>
markdown table formater: http://markdowntable.com/ <br>
Markdown basics: https://rmarkdown.rstudio.com/authoring_basics.html <br>
Style guide: http://adv-r.had.co.nz/Style.html <br>
Histogram colors: https://www.r-bloggers.com/how-to-make-a-histogram-with-ggplot2/ <br>

## Wine related articles
Sulfite regulation USA: https://www.ecfr.gov/cgi-bin/text-idx?c=ecfr&sid=33fc0c0194b58b6fe95208945b5c637a&rgn=div5&view=text&node=27:1.0.1.1.2&idno=27 <br>
Wine Characteristics: https://winefolly.com/review/wine-characteristics/ <br>

## GGplot, GGPAIRS, Corrplot and other Visualizations tips and tricks
Colors in ggplot: http://www.cookbook-r.com/Graphs/Colors_(ggplot2)/ <br>
More COlors in ggplot: http://www.sthda.com/english/wiki/ggplot2-colors-how-to-change-colors-automatically-and-manually <br>
Insert a line in plot: http://www.sthda.com/english/wiki/abline-r-function-an-easy-way-to-add-straight-lines-to-a-plot-using-r-software <br>
Corrplot: https://cran.r-project.org/web/packages/corrplot/vignettes/corrplot-intro.html <br>
aes_string in the geom_vline: https://www.biostars.org/p/234142/ <br>
Pie color reference link: http://www.r-tutor.com/elementary-statistics/qualitative-data/pie-chart <br>
Legend and percent reference link: https://www.tutorialspoint.com/r/r_pie_charts.htm <br>
GGpairs: https://www.rdocumentation.org/packages/GGally/versions/1.4.0/topics/ggpairs <br>
Ggpairs with background: https://stackoverflow.com/questions/48104455/ggpairs-correlation-values-without-gridlines <br>
ggbipplot documentation: https://www.rdocumentation.org/packages/ggbiplot/versions/0.55 <br>

## PCA and Machine Learning Models
PCA: https://www.r-bloggers.com/computing-and-visualizing-pca-in-r/ <br>
Random Forest Predictor: https://datascienceplus.com/predicting-wine-quality-using-random-forests/ <br>
Random Forest + PCA: https://www.analyticsvidhya.com/blog/2016/03/practical-guide-principal-component-analysis-python/ <br>