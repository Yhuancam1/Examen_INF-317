#include <stdio.h>
#include <string.h>
#include <omp.h>

int main(){
    char string1[20];
    int i, length;
    int flag = 0;
    
    printf("Introdusca Palabra:");
    scanf("%s", string1);
    
    #pragma omp taskwait
    {
    length = strlen(string1);
    }
    
    #pragma omp parallel
    {
    for(i=0;i < length ;i++){
        if(string1[i] != string1[length-i-1]){
            #pragma omp task shared(flag)
            {
            flag = 1;
            }
            break;
           }
        }
     }
    
    if (flag) {
        printf("%s Falso \n", string1);
    }    
    else {
        printf("%s Verdad \n", string1);
    }
    return 0;
} 
