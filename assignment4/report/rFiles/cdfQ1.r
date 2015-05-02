dp1 <- read.table('c:/users/kahmed/desktop/unigramOutput.txt', header=FALSE)
dp2 <- read.table('c:/users/kahmed/desktop/bigramOutput.txt', header=FALSE)
dp3 <- read.table('c:/users/kahmed/desktop/trigramOutput.txt', header=FALSE)
datapoint1 <- dp1[,1]
datapoint2 <- dp2[,1]
datapoint3 <- dp3[,1]
X1 = rnorm(sort(datapoint1))
X2 = rnorm(datapoint2)
X3 = rnorm(datapoint3)
P1 = ecdf(datapoint1)
P2 = ecdf(X2)
P3 = ecdf(X3)
plot(P1,  col="red", xlab="Number of Mementos", ylab="Probability", main = "Number of Mementos for each URI")
lines(P2, col="blue")
lines(P3, col="green")
legend("bottomright",inset = 0.05, c("unigram","bigram", "trigram"), 
      cex=.8, col=c("red","blue", "green"), lwd=c(1,1.5,2))#pch=c(1,3))
