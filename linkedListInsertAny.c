#include<stdio.h>
#include<stdlib.h>

struct Node{
  int data;
  struct Node* next; 
};

struct Node* head;

void Insert(int position,int x){
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = x;
    struct Node* current_node = head;
    int i,flag = 0;
    i = 0;

    if (position == 0){
        new_node->next = head;
        head = new_node;
        return;
    }

    while(current_node != NULL){
        if(i == position-1){
            flag=1;
            new_node->next = current_node->next;
            current_node->next = new_node;
            break;

        }else{
            ++i;
            current_node = current_node->next;
        }
    }
    if (flag == 0){
        printf("Error\n");
    }    
}

void Print(){
    struct Node* temp = head;
    printf("List is: ");
    while(temp != NULL){
        printf(" %d", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main(){
    head = NULL; // Empty List
    Insert(0,1);
    Insert(100,2);
    
    Print();
    return 0;
}