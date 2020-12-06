#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  int i, j, k, ii, jj, kk, b_access_count;
  b_access_count = 0;
  int a_access_count = 0;
  int temp = 0;
  int a_stride_count = 0;
  int b_stride_count = 0;
  int tid = 0;
  int ARRAY_SIZE = 4096;
  int number_of_threads = 4;
  int n = 512;
  int VECTOR_WIDTH = 4;

  int max_a = 0;
  int max_b = 0;
  for(i = (ARRAY_SIZE/number_of_threads)*(tid); i < (ARRAY_SIZE/number_of_threads)*(tid+1); i+=ARRAY_SIZE/n)
  {
    for(j = 0; j < ARRAY_SIZE; j+=(ARRAY_SIZE/n))
    {
      for(k = 0; k < ARRAY_SIZE; k+=(ARRAY_SIZE/n))
      {        
         for(ii = i; ii < i+(ARRAY_SIZE/n); ii = ii + 1)
         {
            for(jj = j; jj < j+(ARRAY_SIZE/n); jj+=VECTOR_WIDTH)
            {
                for(kk = k; kk < k+(ARRAY_SIZE/n); kk++)
                {
		  if(ii == 0 && kk ==0){
		    a_access_count = a_access_count + 1;
                    if(a_stride_count > max_a){
                      max_a = a_stride_count;
		    }
	            a_stride_count = 0; 
		  }	
		  else{
                    a_stride_count = a_stride_count + 1;
		  }
		  if(kk == 0 && jj == 0){
    	            b_access_count = b_access_count + 1;
		    if(b_stride_count > max_b){
		      max_b = b_stride_count;
                    }
                    b_stride_count = 0;
		  }	
                  else{
 		    b_stride_count = b_stride_count + 1;
		  }
                }
            }
          }
      }
    }
  }  
  fprintf(stdout, "Access count for b[0][0] is %d, max stride between accesses is %d\n", b_access_count, max_b);
  fprintf(stdout, "Access count for a[0][0] is %d, max stride between accesses is %d\n", a_access_count, max_a);
}
