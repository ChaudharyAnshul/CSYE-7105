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

```

5. To request two nodes in interactive mode, each with 10 tasks per node and 2 CPUs per task (a total of 40 CPUs), 2 GB of memory, for 30 minutes on the “short” partition (or any available partition).             6pts

6. Please use squeue with the flag related users to show all your jobs.             2pts

7, Cancel the job by using jobid in Q4.             2pts

8. Then use squeue to check your job status and explain the meaning of the state name.        4pts

9. In your $HOME, create a new directory: tmp7105; then create a sub-directory: hands-on-test in one command line.               4 pts

10. Show all modules available on Discovery.          2pts

11. Load module of gcc/11.1.0 and show the version of gcc compiler.         4 pts