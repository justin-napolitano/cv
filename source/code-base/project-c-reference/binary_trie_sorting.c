/******************************************************
assignment hw3
fileName hw3Sort.c
Version 2.0
Name: Justin Napolitano
PID: 4153874
NID: ju849482

I Justin Napolitano(ju849482) affirm that this program is entirely my own work
and that I have neither developed my code together with any another person,
nor copied any code from any other person, nor permitted my code to be copied
or otherwise used by any other person, nor have I copied, modified, or
otherwise used program code that I have found in any external source,
including but not limited to, online sources. I acknowledge that any violation
of the above terms will be treated as academic dishonesty.”

**********************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "airPdata.h"
#define BUFFER_SIZE 500

struct stack *parseLine(char *line, struct stack* apd);
float sexag2decimal(char *degreeString);
struct node *sortByLocID(struct stack *airports, struct node *fieldRoot);
struct node *sortByLatitude(struct stack *airports, struct node *latRoot);
int height(struct node *N);
int max(int a, int b);
struct node* newNode(struct airPdata *data);
struct node *rightRotate(struct node *y);
struct node *leftRotate(struct node *x);
int getBalance(struct node *N);
struct node* latInsert(struct node* node, struct airPdata *data);
struct node* fieldInsert(struct node* node, struct airPdata *data);
void inOrder(struct node *root);
void reverseOrder(struct node *root);
void freeStack(struct stack* pHead);
void postOrderDelete(struct node *root);
void freeStruct(airPdata *apd);
void readStack(struct stack* pHead);

struct node
{
  struct airPdata *data;
  struct node *left;
  struct node *right;
  int height;
};
typedef struct stack
{
  struct airPdata *data;
  struct stack* pNext;
}stack;

int main (int argc, char *argv[]){

  // Declare input buffer and other parameters
  struct node *latRoot = NULL;
  struct node *fieldRoot = NULL;
  struct stack *pHead = NULL;
  FILE *fid;
  char buffer[BUFFER_SIZE];
  int count = 0;


  // Check for command line input and open input file.
  if(argc==3){
    fid = fopen(argv[1], "r");
    if(fid==NULL){
      printf("File %s failed to open. Aborting.\n", argv[1]);
      return 2;
    }
  }
  else{
    printf("Incorect number of input parameters. Please specify the name of the input file only.\n");
    printf("Syntax: ./hw1ecl.exe [input file] [sort parameter]\n");
    return 1;
  }

  char *sort = strdup(argv[2]);

  // Determine length of the file.
  while(fgets(buffer, BUFFER_SIZE, fid) != NULL){
    count++;
  }
  rewind(fid);


  // Declare a struct array and allocate memory.


  // if(data==NULL){
  // 	printf("Memory allocation for airPdata array failed. Aborting.\n");
  // 	return 2;
  //}

  // Read and parse each line of the inputt file.
  for(int i = 0; i<count; i++){
    fgets(buffer, BUFFER_SIZE, fid);

    // fgets() includes the New Line delimiter in the output string.
    // i.e. "This is my string.\n\0"
    // We will truncate the string to drop the '\n' if it is there.
    // Note: There will be no '\n' if the line is longer than the buffer.
    if(buffer[strlen(buffer) - 1] == '\n') buffer[strlen(buffer)-1] = '\0';
    pHead = parseLine(buffer, pHead);
  }

  // close the input file.
  fclose(fid);
  fieldRoot = sortByLocID(pHead, fieldRoot);
  latRoot = sortByLatitude(pHead, latRoot);
  //fieldRoot =
  //readStack(pHead);
  if((strcmp(sort, "A") == 0) || (strcmp(sort, "a") == 0)){
  printf("%-11s %-42s %-34s %-15s %-16s\n","Short Name", "Airport Name", "City", "Latitude", "Longitude");
  printf("%-11s %-42s %-34s %-15s %-16s\n", "==========", "============", "====", "========", "=========");
  inOrder(fieldRoot);
  }
  else if((strcmp(sort, "N") == 0) || (strcmp(sort, "n") == 0)){
    printf("%-11s %-42s %-34s %-15s %-16s\n","Short Name", "Airport Name", "City", "Latitude", "Longitude");
    printf("%-11s %-42s %-34s %-15s %-16s\n", "==========", "============", "====", "========", "=========");
    inOrder(latRoot);
}
  else {
    printf("Incorrect sort parameter\n");
    printf("Correct parameters are:  'a', 'n', 'A', 'N'.\n");
    printf("Syntax: ./hw1ecl.exe [input file] [sort parameter]\n");
    printf("Quitting now.....\n\n S'il vous plait, try again\n\n");
    return 1;
  }
  postOrderDelete(fieldRoot);
  postOrderDelete(latRoot);
  freeStack(pHead);
  return 0;

}
struct stack *parseLine(char *line, stack *pHead){
  struct stack *apd = malloc(sizeof(stack));
  if(apd == NULL){
  printf("malloc failed to initialize airPdata stack\n");
  exit(-1);
  }
  apd->data = malloc(sizeof(airPdata));
  if(apd->data == NULL){
  printf("malloc failed to initialize airPdata structure\n");
  exit(-1);
  }
  int i=0, j=0, commas=0;
  char *token = malloc(sizeof(char)*30);
  if (token == NULL){
    printf("malloc failed to initialize token array\n");
    exit(-1);
  }

  while(commas<15){
    while(*(line+i)!=','){
      i++;
      //printf("Successful read i %d\n", i);
    }

    // strncpy does not append a '\0' to the end of the copied sub-string, so we will
    // replace the comma with '\0'.
    *(line+i) = '\0';
    switch (commas){
      case 1:   //Grab the second "field" - Location ID
      apd->data->LocID = malloc(sizeof(char)*(i-j+1));
      if(apd->data->LocID==NULL){
        printf("malloc failed to initialize airPdata.LocID.\n");
        exit(-1);
      }
      strncpy(apd->data->LocID, line+j, i-j+1);
      break;
      case 2:   //Grab the third "field" - Field Name
      apd->data->fieldName = malloc(sizeof(char)*(i-j+1));
      if(apd->data->fieldName==NULL){
        printf("malloc failed to initialize airPdata.fieldName.\n");
        exit(-1);
      }
      strncpy(apd->data->fieldName, line+j, i-j+1);
      break;
      case 3:   //Grab the fourth "field" - City
      apd->data->city = malloc(sizeof(char)*(i-j+1));
      if(apd->data->city==NULL){
        printf("malloc failed to initialize airPdata.city.\n");
        exit(-1);
      }
      strncpy(apd->data->city, line+j, i-j+1);
      break;
      case 8:
      strncpy(token, line+j, i-j+1);
      apd->data->latitude = sexag2decimal(token);
      break;
      case 9:
      strncpy(token, line+j, i-j+1);
      apd->data->longitude = sexag2decimal(token);
      break;
    }
    j=++i;
    commas++;
  }
  if(apd)
  {
    struct stack* pCurrent = pHead;
    if (pHead== NULL)
    {
      apd->pNext= NULL;
      pHead=apd;
    }
    else
    {
      while(pCurrent->pNext!=NULL)
      {
        pCurrent=pCurrent->pNext;
      }
      pCurrent->pNext= apd;
      apd->pNext= NULL;
    }
  }
  else
  {
    fprintf(stderr,"Stack est mal\n\n");
    fprintf(stderr, "j'ai quitee");
    return (NULL);
  }
  free (token);
  return (pHead);
}

float sexag2decimal(char *degreeString)
{
  char *buffer = degreeString;
  int i = 0, j=0, period =0, dirValue = 0;
  float DD = 0, MM = 0, SSMAS = 0, D = 0, tude = 0;
  char *direction;
  char *token = malloc(sizeof(char)*10);
  if (token ==NULL){
    printf("malloc failed to initialize token array\n");
    exit(-1);
  }
  token = strtok(buffer,"-");
  while (token != NULL){
    switch (period)
    {
      case 0:
      DD = strtof(token, NULL);
      break;
      case 1:
      MM = (strtof(token, NULL)/60);
      break;
      case 2:
      while((*(token+j)!='\0')){
        j++;
      }

      direction = strdup(token+(j-1));
      if (strcmp(direction, "N") == 0)
      D=1;
      if (strcmp(direction, "S") == 0)
      D=-1;
      if (strcmp(direction, "E") == 0)
      D=1;
      if (strcmp(direction, "W") == 0)
      D=-1;
      *(token+j) = '\0';
      SSMAS = (strtof(token,NULL)/3600);
      break;
    }
    token = strtok (NULL, "-");
    period++;
  }
  free (token);
  tude = D*(DD+MM+SSMAS);
  return tude;
}

struct node *sortByLocID(struct stack *airports, struct node *fieldRoot)
{
  stack* pCurrent =  airports;
  if (pCurrent !=NULL)
  {
    while(pCurrent != NULL )
    {
      if ((strpbrk(pCurrent->data->LocID, "0123456789") != 0)){
    //  if (strpbrk(pCurrent->data->LocID, "0123456789") != 0){
        pCurrent=pCurrent->pNext;
      }
      else{
      //  sortByLocID(pCurrent);

        fieldRoot = fieldInsert(fieldRoot,pCurrent->data);
        pCurrent=pCurrent->pNext;
       }
     }
    }

  else
  {
    fprintf(stderr," Stack est mal\n\n");
    return NULL;
  }
  //free (pCurrent);
  return fieldRoot;
}

 struct node *sortByLatitude(struct stack *airports, struct node *latRoot)
{
  stack* pCurrent =  airports;
  if (pCurrent !=NULL)
  {
    while(pCurrent != NULL )
    {
      if ((strpbrk(pCurrent->data->LocID, "0123456789") != 0)){
        pCurrent=pCurrent->pNext;
      }
      else{
        latRoot = latInsert(latRoot,pCurrent->data);
        pCurrent=pCurrent->pNext;
       }
     }
    }
  else
  {
    fprintf(stderr,"Stack est mal\n\n");
    return NULL;
  }
  pCurrent = NULL;
  return latRoot;
 }
//   root = insert(root, airports->data);
//   return root;
// }
void readStack(stack* pHead)
{
  stack* pCurrent =  pHead;
  if (pCurrent !=NULL)
  {
    printf("%-11s %-42s %-34s %-15s %-16s\n","Short Name", "Airport Name", "City", "Latitude", "Longitude");
    printf("%-11s %-42s %-34s %-15s %-16s\n", "==========", "============", "====", "========", "=========");
    while(pCurrent != NULL )
    {
      printf("%-11s %-42s %-34s %-15f %-16f\n",pCurrent->data->LocID,pCurrent->data->fieldName
      ,pCurrent->data->city,pCurrent->data->latitude,pCurrent->data->longitude);
      // printf("\nNumber in forward direction is %f \n",pCurrent->data);
      //root = insert(root, pCurrent->data);
      pCurrent=pCurrent->pNext;
    }
  }
  else
  {
    fprintf(stderr,"Ca me fait chier: Stack est mal\n\n");
    return;
  }
  pCurrent = NULL;
  return;
}



int height(struct node *N)
{
  if (N == NULL)
  return 0;
  return N->height;
}

// A utility function to get maximum of two integers
int max(int a, int b)
{
  return (a > b)? a : b;
}

/* Helper function that allocates a new node with the given key and
NULL left and right pointers. */
struct node* newNode(struct airPdata *data)
{
  struct node* node = (struct node*)
  malloc(sizeof(struct node));
  if (node == NULL){
    printf("malloc failed to initialize node\n");
    exit(-1);
  }
  node->data = (struct airPdata*)malloc(sizeof(struct airPdata));
  if (node->data == NULL){
    printf("malloc failed to initialize node ->data airPdata struct\n");
    exit(-1);
  }
  node->data->latitude  = data->latitude;
  node->data->longitude  = data->longitude;
  node->data->fieldName  = data->fieldName;
  node->data->LocID  = data->LocID;
  node->data->city  = data->city;
  node->left   = NULL;
  node->right  = NULL;
  node->height = 1;  // new node is initially added at leaf
  return(node);
}

// A utility function to right rotate subtree rooted with y
// See the diagram given above.
struct node *rightRotate(struct node *y)
{
  struct node *x = y->left;
  struct node *T2 = x->right;

  // Perform rotation
  x->right = y;
  y->left = T2;

  // Update heights
  y->height = max(height(y->left), height(y->right))+1;
  x->height = max(height(x->left), height(x->right))+1;

  // Return new root
  return x;
}

// A utility function to left rotate subtree rooted with x
// See the diagram given above.
struct node *leftRotate(struct node *x)
{
  struct node *y = x->right;
  struct node *T2 = y->left;

  // Perform rotation
  y->left = x;
  x->right = T2;

  //  Update heights
  x->height = max(height(x->left), height(x->right))+1;
  y->height = max(height(y->left), height(y->right))+1;

  // Return new root
  return y;
}

/*
* RECAP Balance is based on Height
*     Hn = Hl - Hr
* so
*    positive => LEFT HEAVY
*    negative => RIGHT HEAVY
*/
// Get Balance factor of node N
int getBalance(struct node *N)
{
  if (N == NULL)
  return 0;
  return height(N->left) - height(N->right);
}

struct node* latInsert(struct node* node, struct airPdata *data)
{
  if (node == NULL)
//  printf("success insert CALL\n");
  return(newNode(data));

  if (data->latitude< node->data->latitude)
  node->left  = latInsert(node->left, data);
  else
  node->right = latInsert(node->right, data);

  node->height = max(height(node->left), height(node->right)) + 1;

  int balance = getBalance(node);

  if (balance > 1 && data->latitude < node->left->data->latitude)
  return rightRotate(node);

  // Right Right Case in code
  if (balance < -1 && data->latitude > node->right->data->latitude)
  return leftRotate(node);

  if (balance > 1 && data->latitude > node->left->data->latitude)
  {
    node->left =  leftRotate(node->left);
    return rightRotate(node);
  }

  if (balance < -1 && data->latitude < node->right->data->latitude)
  {
    node->right = rightRotate(node->right);
    return leftRotate(node);
  }

  /* return the (unchanged) node pointer */
  return node;
}

struct node* fieldInsert(struct node* node, struct airPdata *data)
{
  if (node == NULL)
//  printf("success insert CALL\n");
  return(newNode(data));

  if (strcmp(data->LocID,node->data->LocID) < 0)
  node->left  = fieldInsert(node->left, data);
  else
  node->right = fieldInsert(node->right, data);

  node->height = max(height(node->left), height(node->right)) + 1;

  int balance = getBalance(node);

  if (balance > 1 && strcmp(data->LocID,node->left->data->LocID) < 0)
  return rightRotate(node);

  // Right Right Case in code
  if (balance < -1 && strcmp(data->LocID, node->right->data->LocID) > 0)
  return leftRotate(node);

  if (balance > 1 && strcmp(data->LocID, node->left->data->LocID) > 0)
  {
    node->left =  leftRotate(node->left);
    return rightRotate(node);
  }

  if (balance < -1 && strcmp(data->LocID, node->right->data->LocID) < 0)
  {
    node->right = rightRotate(node->right);
    return leftRotate(node);
  }

  /* return the (unchanged) node pointer */
  return node;
}

void inOrder(struct node *root)
{
     if (root == NULL)
          return;
     inOrder(root->left);
     printf("%-11s %-42s %-34s %-15f %-16f\n",root->data->LocID,root->data->fieldName
     ,root->data->city,root->data->latitude,root->data->longitude);
    // printf("%2f \n\n",root->key);
     inOrder(root->right);
}
void reverseOrder(struct node *root)
{
     if (root == NULL)
          return;
     reverseOrder(root->right);
     printf("%-11s %-42s %-34s %-15f %-16f\n",root->data->LocID,root->data->fieldName
     ,root->data->city,root->data->latitude,root->data->longitude);
     reverseOrder(root->left);
}

void postOrderDelete(struct node *root)
{
    if (root == NULL) return;
    postOrderDelete(root->left);
    postOrderDelete(root->right);
    free(root->data);
    free(root);
}

void freeStack(stack* pHead)
{
  stack* pCurrent =  pHead;
  if (pCurrent !=NULL)
  {
    while(pCurrent != NULL )
    {
      //root = insert(root, pCurrent->data);
      freeStruct(pCurrent->data);
      free (pCurrent);
      pCurrent=pCurrent->pNext;
    }
  }
  else
  {
    fprintf(stderr,"Ca me fait chier: Stack est mal\n\n");
    return;
  }
  free (pCurrent);
  return;
}

void freeStruct(airPdata *apd){
if (apd !=NULL){
  apd->latitude = 0 ;
  apd->longitude = 0;
	free(apd->city);
	free(apd->fieldName);
	free(apd->LocID);
}
}


// struct node* popStack(stack* pHead, struct node *root)
// {
//   stack* pCurrent =  pHead;
//   if (pCurrent)
//   {
//     while(pCurrent != NULL )
//     {
//       //  printf("\nNumber in forward direction is %f \n",pCurrent->data);
//       root = insert(root, pCurrent->data);
//       pCurrent=pCurrent->pNext;
//     }
//   }
//   else
//   {
//     fprintf(stderr,"Ca me fait chier: Stack est mal\n\n");
//     exit (1);
//   }
//   free (pCurrent);
//   return (root);
// }

// void printData(int length, airPdata *data){
// 	printf("%-12s %-11s %-42s %-34s %-3s %-15s %-16s Tower\n", "FAA Site", "Short Name", "Airport Name", "City", "ST", "Latitude", "Longitude");
// 	printf("%-12s %-11s %-42s %-34s %-3s %-15s %-16s =====\n", "========", "==========", "============", "====", "==", "========", "=========");
// 	for(int i=0; i<length; i++){
// 		printf("%-12s %-11s %-42s %-34s %-3s %-15s %-16s %s\n",(data+i)->siteNumber,(data+i)->LocID,(data+i)->fieldName,
// 		  (data+i)->city,(data+i)->state,(data+i)->latitude,(data+i)->longitude,(data+i)->controlTower);
// 	}
// }
