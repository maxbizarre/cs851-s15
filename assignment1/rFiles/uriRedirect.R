uriDataset <- read.csv("C:/Users/kahmed/Desktop/uriRedirect.txt",stringsAsFactors=F,header=FALSE,sep="\t")
data = uriDataset[,1]
png("C:/Users/kahmed/Desktop/uriRedirect.png")
hist(data,main="URI Redirection vs. Frequency",freq=T,xlab="Number of Redirections",ylab="Frequency",xlim=c(0,12),ylim=c(0,5000))