statusCode <- read.csv("C:/Users/kahmed/Desktop/statusCode.txt",stringsAsFactors=F,header=FALSE)
data = statusCode[,1]
png("C:/Users/kahmed/Desktop/statusCode.png")
hist(data,main="HTTP Status Code vs. Frequency",freq=T,xlab="HTTP Status Code",ylab="Frequency",xlim=c(200,600),ylim=c(0,20000))