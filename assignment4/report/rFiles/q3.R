data <- read.table('C:/Users/kahmed/Desktop/q3/uri20.txt', sep="\t", colClasses=c("POSIXct", "numeric"))
png('C:/Users/kahmed/Desktop/q3/uri20.png')
p1 <- plot(data, type="l", col='blue', main="Relative Jaccard Distance vs. Time", xlab="Time", ylab="Jaccard Distance", xaxt="n", ylim=c(0,1))
axis.POSIXct(side=1, data$V1, format="%Y-%m-%d")