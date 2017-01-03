  //#include<iostream>
  #include <stdio.h>
  #include<malloc.h>
  //using namespace std;

  int* spiralOrder(int** matrix, int matrixRowSize, int matrixColSize) {
        int i, j, x=0, y=-1, k=0,l=1;
        int n=matrixRowSize*matrixColSize;
        int d=0,r=matrixRowSize,c=matrixColSize;
        // 0 right 1 down 2 left 3 up
        int dir[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
        int* order = (int *)malloc(sizeof(int)*n);
        // 高矩形, 短边为偶数 /2*4+4
        while (k<n && l>0) {
            if (d&1)
                l = --r;
            else
                l = c--;
            //order[k++] = l;
            //d = (d+1) & 3;
            //continue;
            for (j=0;j<l;j++) {
                x += dir[d][0];
                y += dir[d][1];
                order[k++] = matrix[x][y];
                //cout<<"x:"<<x<<" y:"<<y<<endl;
            }
            d = (d+1) & 3;
         }
         return order;
  }
  int main() {
       int a[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
       int *matrix[3]; 
       int i;
       int *result;
       for (i=0;i<3;i++)
            matrix[i] = &(a[i][0]);
       result = spiralOrder(matrix, 3, 3);
       for (int i=0;i<3*3;i++)
       //  cout<<result[i]<<',';
           printf("%d,", result[i]);
       //cout<<endl;
       printf("\n");
       return 0;
  }
