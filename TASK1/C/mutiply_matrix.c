#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double matrix_lenght(double ramgb){

  double max = ramgb*pow(10,9)*8; 
  double c = -1*max/64;
  double a, b, delta, x1, x2;
  a = 1.0;
  b = 2.0;
  
  delta = pow(b,2) - 4*a*c;
  if(delta >= 0){
    if(delta == 0){
      x1 = -b / (2 * a);
      return (int) floor(x1);
    }
    x1 = (-b - sqrt(delta)) / (2 * a);
    x2 = (-b + sqrt(delta)) / (2 * a);
    if(x1>x2){
    return (int) floor(x1);
    }
    return (int) floor(x2);
      
  }
  return 0;
}

double *limpaArray(int n) {
    double *vec = (double *)malloc(n * sizeof(double));
    for (int i = 0; i <= n; i++)
        vec[i] = 0;

    return vec;
}

double *multiply_matrix_v1(double **A, double *x, int n) {
    double *b = limpaArray(n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            b[i] += A[i][j] * x[j];
        }
    }

    return b;
}


double *multiply_matrix_v2(double **A, double *x, int n) {
    double *b = limpaArray(n);

    for (int j = 0; j < n; j++) {
        for (int i = 0; i < n; i++) {
            b[i] += A[i][j] * x[j];
        }
    }

    return b;
}


int main(int argc, char *argv[]) {
  system("clear");
  FILE *file = fopen("resultados.csv", "a");
  fprintf(file, "N, GB, t1, t2\n");
  printf("N, GB, t1, t2\n");
  for(int i=1;i<argc;++i){
    double ramgb = strtof(argv[i], NULL);

    int n = matrix_lenght(ramgb);  

    srand(time(NULL));
  
    double **A = (double **)malloc(n * sizeof(double *));
    double *x = (double *)malloc(n * sizeof(double));
    double *b;
    double *b2;
    clock_t start1, finish1, start2, finish2;

    for (int i = 0; i < n; i++) {
      A[i] = (double *)malloc(n * sizeof(double));
      for (int j = 0; j < n; j++) {
        A[i][j] = (double)rand()/(double)(RAND_MAX);
      }
      x[i] = (double)rand()/(double)(RAND_MAX);
    };

    start1 = clock();
    b = multiply_matrix_v1(A, x, n);
    finish1 = clock();
      
    start2 = clock();
    b2 = multiply_matrix_v2(A, x, n);
    finish2 = clock();

    fprintf(file, "%d,%.2f, %.6f, %.6f\n", n, ramgb ,((double)(finish1 - start1)) / CLOCKS_PER_SEC, ((double)(finish2 - start2)) / CLOCKS_PER_SEC);
    printf("%d,%.2f, %.6f, %.6f\n", n, ramgb ,((double)(finish1 - start1)) / CLOCKS_PER_SEC, ((double)(finish2 - start2)) / CLOCKS_PER_SEC);

    free(x);
    free(b);
    free(b2);
    for (int i = 0; i < n; i++) {
      free(A[i]);
    }
  }
  return 0;
}