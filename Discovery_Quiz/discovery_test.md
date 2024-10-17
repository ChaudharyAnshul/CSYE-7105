1. Use sinfo to show the node list, nodes, state (compact), number of CPUs and features of the “debug” partition.                         6 pts
```
sinfo -p debug --Format='nodelist,nodes,statecompact,cpus,features'
```

2. Use sinfo to show the partition, state (complete), memory, time limit of the node “c0165”.                               4 pts
```
sinfo -n c0165 --Format='partition,statecomplete,memory,time'
```

3. Show all nodes of the ‘idle’ state of the “short” partition.        2 pts
```
sinfo -p short -t idle
```

4. To request one node from “courses” partition in interactive mode, 10 tasks for 30 minutes with X11 forwarding.         6pts
```
srun --partition=courses --nodes=1 --ntasks=10 --time=00:30:00 --x11 --pty /bin/bash
```

5. To request two nodes in interactive mode, each with 10 tasks per node and 2 CPUs per task (a total of 40 CPUs), 2 GB of memory, for 30 minutes on the “short” partition (or any available partition).             6pts
```
srun --partition=short --nodes=2 --ntasks-per-node=10 --cpus-per-task=2 --mem=2G --time=00:30:00 --pty /bin/bash
```

if short is busy
```
srun --nodes=2 --ntasks-per-node=10 --cpus-per-task=2 --mem=2G --time=00:30:00 --pty /bin/bash
```

6. Please use squeue with the flag related users to show all your jobs.             2pts
```
squeue -u chaudhary.ans
```

7, Cancel the job by using jobid in Q4.             2pts
```
scancel <jobid>
```

8. Then use squeue to check your job status and explain the meaning of the state name.        4pts
```
squeue -u chaudhary.ans
```

9. In your $HOME, create a new directory: tmp7105; then create a sub-directory: hands-on-test in one command line.               4 pts
```
mkdir tmp7105 tmp7105/hands-on-test
```

10. Show all modules available on Discovery.          2pts
```
module avail
```

11. Load module of gcc/11.1.0 and show the version of gcc compiler.         4 pts
```
module load gcc/11.1.0
```

12. In HW1, the csye7105_ex1.c has been parallelized according to the requirements. Implement the following operations:             28 pts
    1. Transfer csye7105_ex1.c from your local machine to your $HOME/tmp7105/hands-on-test on Discovery.      2 pts
    ```
    use - ood.discovery.neu.edu
    ```
    2. On login node, compile the parallelized C program csye7105_ex1.c with OpenMP flag and get the executable file: csye7105_ex1.         4 pts
    ```
    gcc -fopenmp -o csye7105_ex1 csye7105_ex1.c
    ```
    3. Request a node in a simple way (debug or express or short) and request a node on courses partition with 1 task and 8 CPUs per task on two terminals. [students should open 2 terminals].          6 pts
    ```
    srun -p short -N 1 --pty /bin/bash
    ```
    ```
    srun -p courses -N 1 -c 8 --pty /bin/bash
    ```
    4. Now, you are on 2 compute nodes. Please use Linux commands to show the number of CPUs and memory size of these two nodes.      2 pts
    ```
    lscpu
    lsmem <or> free -h
    ```
    5. On these two nodes, directly run $ ./csye7105_ex1, and explain what different the results are on these two nodes.       6 pts
    ```
    ./<filename>
    ```
    6. On these two nodes, use the environment variable to set the number of threads to 4, then repeat step (5) and explain what different the results are on these two nodes and with step (5).      8 pts
    ```
    export OMP_NUM_THREADS=4
    ```

13. Conda module and environment:        4 pts
    1. Load module of anaconda3/2022.05 and check available modules in your environment.         2 pts
    ```
    module load anaconda3/2022.05
    ```
    2. List your conda environments.                 1 pts
    3. List the software packages within your conda environment.      1 pts