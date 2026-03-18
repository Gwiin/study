#include "queue.h"

void initQueue(Queue *pq){
    pq->front = pq->queue;
    pq->rear = pq->queue;
}


void push(Queue *pq, int data){
    if(pq->rear == QUEUESIZE){
        pq->rear = pq->queue;
    }
    if(pq->rear+1 == pq->front){
        fprintf(stderr, "stack is full\n");
        exit(1);
    }
    *(pq->rear++) = data;
   
}

int pop(Queue *pq){
    if(pq->front == QUEUESIZE){
        pq->front = pq->queue;
    }
    if(pq->front == pq->rear){
        fprintf(stderr, "there is no data\n");
        exit(1);
    }
    return *(pq->front++);
}

