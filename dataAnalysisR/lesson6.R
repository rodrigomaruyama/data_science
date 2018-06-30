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
