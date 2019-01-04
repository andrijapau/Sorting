include <stdio.h>
#include <stdlib.h>

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
   int (*compare)(int x, int y);
} intHeap_T;

int
store(intHeap_T* heap, int value) {
   if (heap->end == (heap->size) - 1) { return -1; }
   else {
      heap->store[heap->end] = value;
      heap->end = (heap->end)+1;

   } return 0;
}

int
retrieve(intHeap_T* heap, int *rvalue) {
   /* Return Heap Value through Function if not Empty */
   *rvalue = heap->store[0];
   return 0;
}

int
hs(int *x, int size, int (*compare)(int x, int y)) {

   int parentIndex = 0;
   int temp;
   int childIndex = 2;
   int status;

   if (size == 2) {
      status = (*compare)(x[0], x[1]);
      if (status == 0) {
         temp = x[0];
         x[0] = x[1];
         x[1] = temp;
      } return 0;
   }

   while (childIndex <= size-1) {

      if ( childIndex < size-1) {
         if ( (*compare) ( (x)[childIndex], (x)[childIndex + 1] ) == 0 ) {
            childIndex++;
         }
      }
      if ( (*compare) ( (x)[parentIndex], (x)[childIndex] ) == 0 ) {
         temp = (x)[parentIndex];
         (x)[parentIndex] = (x)[childIndex];
         (x)[childIndex] = temp;
      }
      parentIndex = childIndex;
      childIndex = childIndex*2;
   } return 0;

}
