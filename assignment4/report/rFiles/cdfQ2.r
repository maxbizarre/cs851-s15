dp1 <- read.table('c:/users/kahmed/desktop/mementoCount.txt', header=FALSE)
datapoint1 <- dp1[,1]
X1 = rnorm(sort(datapoint1))
P1 = ecdf(datapoint1)
plot(P1,  col="red", xlab="Number of Mementos", ylab="Probability", main = "Number of Mementos for each URI")
