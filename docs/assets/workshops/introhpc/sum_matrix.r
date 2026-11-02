#!/usr/bin/env Rscript

# Function for shared memory execution
doTask <- function(size_x, size_y, seed, print_progress) {
    suppressPackageStartupMessages(library(doParallel))
    message(sprintf("Summing [ %e x %e ] matrix, seed = '%i'", size_x, size_y, seed))
    set.seed(seed)

    registerDoParallel(num_cpus)

    results_all <- foreach(z = 1:size_x, .combine = "+") %dopar% {
        percent_complete = z * 100 / size_x
        if (print_progress && percent_complete %% 1 == 0) {
            message(sprintf(" %i%% done...\r", percent_complete))
        }
        sum(rnorm(size_y))
    }
    results_all
}

# Get SLURM environment variables
ntasks <- as.integer(Sys.getenv('SLURM_NTASKS', unset = "1"))
seed <- as.integer(Sys.getenv('SLURM_ARRAY_TASK_ID', unset = "0"))
num_cpus <- as.integer(Sys.getenv('SLURM_CPUS_PER_TASK', unset = "1"))

size_x <- 60000 # This on makes memorier
size_y <- 40000 # This one to make longer

print_progress <- TRUE

# Check if we're running with multiple tasks
if (ntasks > 1) {
    message(sprintf("MPI Running on '%s' with %i CPU(s)", Sys.info()["nodename"], num_cpus))
    suppressPackageStartupMessages(library(doMPI))
    cl <- startMPIcluster()
    registerDoMPI(cl)

    results_all <- foreach(z = 1:ntasks, .combine = "+") %dopar% {
        doTask(size_x, ceiling(size_y / ntasks), z + seed, print_progress)
    }

    results <- Reduce("+", results_all)
    closeCluster(cl)
    message(sprintf("MPI Sums to %f", results))
    mpi.quit()
} else {
    message("Running non-MPI task")
    message(sprintf("Shared Memory Running on '%s' with %i CPU(s)", Sys.info()["nodename"], num_cpus))
    results <- doTask(size_x, size_y, seed, print_progress)
    message(sprintf("(Non-MPI) Sums to %f", results))
}
