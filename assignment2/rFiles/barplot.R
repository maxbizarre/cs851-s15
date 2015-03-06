B <- c(83.1,54,0.1537,0.240)
png("C:/Users/kahmed/Desktop/uri3.png")
barplot(B, main="Size for URI#3", xlab="Archive Tool", ylab="Size in MB", names.arg = c("Heritrix", "WARCreate", "webrecorder.io", "wget"))
