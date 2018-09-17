# load the visualize package
library(ggplot2)
library(dplyr)
library(zoo)

# get the working directory
getwd()

# load the csv data
Taipei <- read.csv("city_data.csv")
Global <- read.csv("global_data.csv")

# === observe and clean the data
# observe data
str(Taipei)
str(Global)
tail(Taipei)
tail(Global)

# drop the redundant data
Taipei <- Taipei[,-(2:3)]

# see if there got missing value 
sapply(Taipei, function(x) {sum(is.na(x))})
sapply(Global, function(x) {sum(is.na(x))})

# === calculate the moving averages
# year data
MA_T <- Taipei[7:173,1]
MA_G <- Global[7:266,1]

# moving average
MA_taipei <- rollapply(Taipei$avg_temp, 7, mean)
MA_global <- rollapply(Global$avg_temp, 7, mean)

# bind year data and moving averages
MA_T <- cbind(MA_T, MA_taipei)
MA_G <- cbind(MA_G, MA_global)
MA_T <- MA_T %>% as.data.frame()
MA_G <- MA_G %>% as.data.frame()

# merge 2 dataframes
colnames(MA_T) <- c('year', 'MA_taipei')
colnames(MA_G) <- c('year', 'MA_global')
all <- merge(MA_T, MA_G, by = 'year', all = TRUE)
head(all)

# === visualization
P1 <- ggplot(MA_T, aes(year_taipei, MA_taipei)) +
  geom_line(aes(y = MA_taipei)) +
  ggtitle("Taipei moving average temperature ")
P1 <- ggplot(MA_G, aes(year_global, MA_global)) +
  geom_line(aes(y = MA_global)) +
  ggtitle("Global moving average temperature ")
P1 <- ggplot(all, aes(year, moving_avg_temp)) + 
  geom_line(aes(y = MA_taipei, colour = "MA_taipei")) +
  geom_line(aes(y = MA_global, colour = "MA_global")) +
  ggtitle("The moving average temperature \n of Taipei and global")
P1
P2
P3




