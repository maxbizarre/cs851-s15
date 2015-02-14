age <- read.csv("C:/Users/kahmed/Desktop/age.txt",stringsAsFactors=F,header=FALSE)
data = age[,1]

png("C:/Users/kahmed/Desktop/tweetAge.png")
hist(data,main="Tweet Age vs. Frequency",freq=T,xlab="Tweet Age",ylab="Frequency",xlim=c(1,8000),ylim=c(0,5000))

se <- function(x) sqrt(var(x)/length(x))
write("Mean", file = "C:/Users/kahmed/Desktop/meanMedMode.txt")
write(mean(data), file = "C:/Users/kahmed/Desktop/meanMedMode.txt",
      append = TRUE, sep = "\t")
write("Median", file = "C:/Users/kahmed/Desktop/meanMedMode.txt",
      append = TRUE, sep = "\t")
write(median(data, na.rm = FALSE), file = "C:/Users/kahmed/Desktop/meanMedMode.txt",
      append = TRUE, sep = "\t")
write("Standard Deviation", file = "C:/Users/kahmed/Desktop/meanMedMode.txt",
      append = TRUE, sep = "\t")
write(sd(data, na.rm = FALSE), file = "C:/Users/kahmed/Desktop/meanMedMode.txt",
      append = TRUE, sep = "\t")
se <- function(data) sd(data)/sqrt(length(data))
write("Standard Error", file = "C:/Users/kahmed/Desktop/meanMedMode.txt",
      append = TRUE, sep = "\t")
write(se(data), file = "C:/Users/kahmed/Desktop/meanMedMode.txt",
      append = TRUE, sep = "\t")
