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

