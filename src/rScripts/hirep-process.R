knitr::opts_knit$set(progress = TRUE, verbose = TRUE)
library(hicrep)

HiCRep1 <- read.table("/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/Original/hESC-r1-1M.npy.txt", header = FALSE, sep = " ")
HiCRep2 <- read.table("/Users/bcchanaka/PycharmProjects/HiC-DataProcess/Contact-Matrix/Original/hESC-r2-1M.npy.txt", header = FALSE, sep = " ")

Pre_HiC <- prep(HiCRep1, HiCRep2, 1000000, 1, 5000000)

## ---- eval=TRUE----------------------------------------------------------
h_hat <- htrain(HiCRep1, HiCRep2, 1000000, 5000000, 0:2)

h_hat

## ------------------------------------------------------------------------
#check total number of reads before adjustment
sum(HiCRep1[, -c(1:3)])

DS_HiCRep1 <- depth.adj(HiCRep1, 200000, 1000000, out = 0)

#check total number of reads after adjustment
sum(DS_HiCRep1[, -c(1:3)])


## ---- eval=TRUE----------------------------------------------------------
dim(Pre_HiC)
SCC.out <- get.scc(Pre_HiC, 1000000, 5000000)

#SCC score
SCC.out[[3]]

#Standard deviation of SCC
SCC.out[[4]]
sessionInfo()

