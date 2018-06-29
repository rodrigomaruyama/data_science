install.packages('ggplot2')
library(ggplot2)
data(diamonds)
ggplot(data=diamonds, aes(x=price, y=x)) +
  geom_point()
cor.test(diamonds$price, diamonds$x)
cor.test(diamonds$price, diamonds$y)
cor.test(diamonds$price, diamonds$z)
ggplot(data=diamonds, aes(x=price, y=depth)) +
  geom_point(alpha= 1/100)
