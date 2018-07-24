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
library(ggbiplot)
library(e1071)
library(rpart)

wdf <- read.csv('data/wineQualityWhites.csv')
wdf$X <- NULL
wdf$quality <- as.factor(wdf$quality)

################################################################################
# PCA
################################################################################
wdf.pca <- prcomp(wdf[,1:11], center = TRUE, scale. = TRUE)


################################################################################
# Random Forest
################################################################################
set.seed(123)
samp <- sample(nrow(wdf), 0.4 * nrow(wdf))
# Creating train and test datasets
train <- wdf[samp, ]
test <- wdf[-samp, ]
# Fitting the model
model <- randomForest(quality ~ . - quality, data = train)
# Predicting the quality of wine with test dataset
pred <- predict(model, newdata = test)

print('Random Forest')

# Comparing the predictions with the correct answer
table(pred, test$quality)
classAgreement(table(pred, test$quality))


################################################################################
# Random Forest - PCA
################################################################################
new_wdf.pca <- data.frame(wdf.pca$x)
new_wdf.pca <- data.frame(new_wdf.pca[,1:8], quality = wdf$quality)

# Creating train and test datasets
set.seed(123)
samp <- sample(nrow(wdf), 0.8 * nrow(wdf))
train.pca <- new_wdf.pca[samp, ]
test.pca <- new_wdf.pca[-samp, ]

# Fitting the model
model <- randomForest(quality ~ . - quality, data = train.pca)

# Predicting the quality of wine with test dataset
pred <- predict(model, newdata = test.pca)

print('Random Forest PCA')

# Comparing the predictions with the correct answer
table(pred, test.pca$quality)
classAgreement(table(pred, test.pca$quality))


################################################################################
# Random Forest - PCA
################################################################################
set.seed(123)
samp <- sample(nrow(wdf), 0.5 * nrow(wdf))

# Creating train datasets
train <- wdf[samp, ]
#train_x <- train[,1:11]       # data
#train_y <- train[,'quality']  # label

# Creating test datasets
test <- wdf[-samp, ]
#test_x <- test[,1:11]   # data
#test_y <- test[,12]     # label

# Transforming the variable to a factor
train$quality <- as.factor(train$quality)
test$quality <- as.factor(test$quality)

################################################################################
# SVM
################################################################################
svm.model  <- svm(quality ~ ., data = train, cost = 4, gamma = 0.5)
svm.pred <- predict(svm.model,test[,-12])

print('SVM')
table(svm.pred,test[,12])
classAgreement(table(pred = svm.pred,true = test[,12]))

################################################################################
# Rpart
################################################################################
rpart.model <- rpart(quality ~ ., data = train)
rpart.pred <- predict(rpart.model, test[,-12], type = 'class')

print('rpart')
table(rpart.pred,test[,12])
classAgreement(table(pred = rpart.pred,true = test[,12]))

