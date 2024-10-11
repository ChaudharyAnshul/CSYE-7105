/* CSYE7105 HW1 Q3: totals 6 points */

#include <stdio.h>
#include <omp.h>

int main ()  
{
   int nthreads = 4;
   /* Please use OpenMP runtime routine to set the number of threads
      4 points  */
   omp_set_num_threads(nthreads);

   #pragma omp parallel
   {
      int id = omp_get_thread_num();   // get the thread number, 2 points

      printf("Hello World from thread = %d", id);
      printf(" with %d threads\n",omp_get_num_threads());
   }  

   printf("all done, with hopefully %d threads\n",nthreads);

}

