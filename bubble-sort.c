int bs(int *x, int size, int (*compare)(int x, int y)) {
   int i, j, temp, z;
   if (x == NULL) {
      return -1;
   } else {
      for (i=0; i<size; i++) {
         for (j=i+1; j<size; j++) {
            z = ((*compare)(x[i],x[j]));
            if (z == 0) {
               temp = x[i];
               x[i] = x[j];
               x[j] = temp;
            }
         }
      } return 0;
   }
}

int lt(int x, int y) {
   if (x < y) { return 0; }
   else { return -1; }
}

int gt(int x, int y) {
   if (x > y) { return 0; }
   else { return -1; }
