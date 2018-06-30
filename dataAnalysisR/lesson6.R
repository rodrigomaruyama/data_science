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
p1 <- ggplot(aes(x=price, y=carat), data=diamonds) +
  geom_point()

p2 <- ggplot(aes(x=price, y=carat), data=diamonds[0:53400,]) +
  geom_point()

install.packages('gridExtra')
library(gridExtra)

grid.arrange(p1, p2, ncol=2)
