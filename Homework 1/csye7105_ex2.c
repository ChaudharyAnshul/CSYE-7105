/* CSYE7105 HW1 Q2: totals 16 points*/

#include <omp.h>
#define N 1000
#define N_THREADS 4

main () 
{
  int tid, i, chunk;
  double a[N], b[N], c[N];

  chunk = N/N_THREADS;

/* Please complete the data scope in the OpenMP parallel directive line: 8 points */

/* Use clause to define the number of threads using N_THREADS: 4 points 
   and put this in the second line: 2 points */
   
#pragma omp parallel num_threads(N_THREADS) private(tid) shared(a, b, c, chunk)

  {
  tid = omp_get_thread_num();         // get the thread number, 2 points
  for (i = tid * chunk; i < (tid+1) * chunk; i++)
    {
      c[i] = a[i] + b[i];
    }

  }  /* end of parallel section */   

}