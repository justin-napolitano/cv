
//*****************************************************************************//
//Justin Napolitano



//******************************************************************************//

//******************************************************************************//
// Logic:   1. take arguement from terminal.   2.  open file.  3. read line to a buffer.
//           4. Parse buffer for tokens.  5. write tokens to an array.  6. print data.
//***************************DONT FORGET TO FREE MALLOCS************************//



#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "airPdata.h"
#define MAXL 900
#define MAXC 1024
#define MAXT 20

airPdata* loadTransform(char *filename);
void printData(airPdata *airport);
int memMan(airPdata*ptr);                                          		          //testOpen prototype

int main(int argc, char *argv[]){                                               //takes arguments from stdin.  int argc == #of values/strings input into field
  char *filename= argv[1];                                                      // *argv[] == the pointer string.  IE Filename in this case
  airPdata *airporter = NULL;
  //airporter = (airPdata*)malloc(MAXL*MAXC* MAXT);
  //if (NULL == airporter){
  //  fprintf(stderr, "airporter malloc failed -line(33)\n");
  //  exit(1);
  //}
  if (argc !=2){                                                                //If not equal to two input values,  kill
    fprintf(stderr, "Failure\n\nCorrect Usage: ./test inputfile\n");
    exit(1);
  }
  //  fprintf(stdout, "Success testOpen\n\n");                                  //Prints to log file
  airporter = loadTransform(filename);
  if (NULL == airporter){
    fprintf(stderr, "(line 43)- airporter=>airport assignment failure\n");
    exit(1);
  }
  printData(airporter);
//  free (airporter);
  airporter = NULL;
  memMan(airporter);
  return 0;
}

airPdata* loadTransform(char *filename){                                        //Opens and stores data read from csv
//int tokenCount = 0;
//  int a = 0;
//  int j = 0;
  int k = 0;
  int i = 0;
  //  char ***allData;                                                          // ptr arry of an array.   ie *allData[][];  Allows for MALLOC
  airPdata *airport = NULL;
  airport = (airPdata*)malloc(MAXL*MAXC*MAXT);
  if (NULL == airport){
    fprintf(stderr, "(line 73)- airport malloc failed");
    exit(1);
  }                                                                             // Could  also alocate a struct array.  May do for homework three. Avoid n^2 complexity
  //allData = (char ***)malloc (MAXL * MAXC * MAXT);
  //const char s[2]=",";                                                        //parse delim
  //const char s1[2]="\0";
  char *buffer = (char*)malloc(MAXC);
  if (NULL == buffer){
    fprintf(stderr, "(line 81)- buffer malloc failed");
    exit(1);
  }
  char *token = (char*)malloc(MAXT);
  if (NULL == token){
    fprintf(stderr, "(line 86)- token malloc failed");
    exit(1);
  }
  FILE *ifp;
  ifp = fopen(filename, "r");
  if (NULL == ifp){
    //Valid file Test
    fprintf(stderr, "Failure to open csv\n\nConfirm file name\n");
    exit(1);
  }
  //Parses each line. Saves the string to buffer
  for (i=0; fgets(buffer, MAXC, ifp); i++){
    k=0;

    //    allData[i] = malloc(MAXC);
    //    airport[i]= malloc(MAXC);
    char* bufferCpy = (char*) malloc(MAXC);
    if (NULL ==bufferCpy){
      fprintf(stderr, "(line 104)- bufferCpy malloc failed");
      exit(1);
    }
    bufferCpy=strdup(buffer);
    //	printf("buffer=%s:\nbufferCpy=%s\n", buffer, bufferCpy);
    while ((token = strsep(&bufferCpy, ",")) != NULL){


      //**Special For Loop**  occupies an array of alldata with tokens at where i say.
      //** Could be implemented as a structure array instead of a two dimensional
      //** Also could use a single for loop to avoid n^2 complexity.
      //** Will do to play.*/

      //for (k=0; token != NULL; k++){
      //          fprintf(stdout,"token (%d) : %s\n\n",k, token);
      //      allData[i][k] = (char *)malloc(MAXT);
      //      if (strcmp(token, s1) == 0)      allData[i][k]= strdup("Empty");
      //      else allData[i][k] = strdup(token);

      if (k==0){
        airport[i].siteNumber = (char *)malloc(MAXT);
        if (NULL == airport[i].siteNumber){
          fprintf(stderr, "(line 126)- airport[%d].siteNumber malloc failed",i);
          exit(1);
        }
        airport[i].siteNumber = strdup(token);
      }
//    If compares to substring counter.  Then points to token to my command
      if (k==1){
        airport[i].LocID = (char *)malloc(MAXT);
        if (NULL == airport[i].LocID){
          fprintf(stderr, "(line 135)-airport[%d].LocID malloc failed",i);
          exit(1);
        }
        airport[i].LocID = strdup(token);
      }
      if (k==2){
        airport[i].fieldName = (char *)malloc(MAXT);
        if (NULL == airport[i].fieldName){
          fprintf(stderr, "(line 143)-airport[%d].fieldName malloc failed",i);
          exit(1);
        }
        airport[i].fieldName = strdup(token);
      }
      if (k==3){
        airport[i].city = (char *)malloc(MAXT);
        if (NULL == airport[i].city){
          fprintf(stderr, "(line 151)-airport[%d].city malloc failed",i);
          exit(1);
        }
        airport[i].city = strdup(token);
      }
      if (k==4){
        airport[i].state = (char *)malloc(MAXT);
        if (NULL == airport[i].state){
          fprintf(stderr, "(line 159)-airport[%d].state malloc failed",i);
          exit(1);
        }
        airport[i].state = strdup(token);
      }
      if (k==8){
        airport[i].latitude = (char *)malloc(MAXT);
        if (NULL == airport[i].latitude){
          fprintf(stderr, "(line 167)-airport[%d].latitude malloc failed",i);
          exit(1);
        }
        airport[i].latitude = strdup(token);
      }
      if (k==9){
        airport[i].longitude = (char *)malloc(MAXT);
        if (NULL == airport[i].longitude){
          fprintf(stderr, "(line 175)-airport[%d].longitutde malloc failed",i);
          exit(1);
        }
        airport[i].longitude = strdup(token);
      }
      if (k==14){
        airport[i].controlTower = *(char *)malloc(MAXT);
        airport[i].controlTower = *token;

      }
      k++;
  //    if (tokenMAX<k)
  //    tokenMAX=k;                                                             //Sets token to next , , region
    }
    free(bufferCpy);
    bufferCpy = NULL;
    free(token);
    token = NULL;
  }
  fclose(ifp);
  ifp = NULL;
  free (buffer);
  buffer = NULL;
  return (airport);
//  memMan(airport);
}
void printData(airPdata *airport)
{
//****************************************************************************//
// reads pointer airpointer passed from main until null;  Frees struct."" pointers with each pass;
// Then frees entire struct once first null is tapped
// original plans was to pass a line counter to functions, but this methods is better.
//****************************************************************************//
  //int lines = i;
  int a = 0;
  printf("%-12s %-11s %-42s %-34s %-3s %-15s %-16s Tower\n", "FAA Site", "Short Name",
  "Airport Name", "City", "ST", "Latitude", "Longitude");
  printf("%-12s %-11s %-42s %-34s %-3s %-15s %-16s =====\n", "========", "==========",
  "============", "====", "==", "========", "=========");
  for (a=0; airport[a].siteNumber!=NULL; a++){
    printf("%-12s %-11s %-42s %-34s %-3s %-15s %-16s %-1c\n", airport[a].siteNumber, airport[a].LocID, airport[a].fieldName,
    airport[a].city, airport[a].state, airport[a].latitude, airport[a].longitude, airport[a].controlTower);

    free (airport[a].siteNumber);
    airport[a].siteNumber = NULL;
    free (airport[a].LocID);
    airport[a].LocID = NULL;
    free (airport[a].fieldName);
    airport[a].fieldName = NULL;
    free (airport[a].city);
    airport[a].city = NULL;
    free (airport[a].state);
    airport[a].state = NULL;
    free (airport[a].latitude);
    airport[a].latitude = NULL;
    free (airport[a].longitude);
    airport[a].longitude = NULL;
  }
  free (airport);
  airport = NULL;
  memMan(airport);
}

int memMan(airPdata *ptr){
if(ptr ==NULL)
  return 0;
  free (ptr);
  ptr = NULL;
  return 0;
}




//*********************************References**********************************//
//title: strsep(3) Linux Programmer's manual
//author: Michael Kerrisk
//url: http://man7.org/linux/man-pages/man3/strsep.3.html
//*
//title: strtok(3) Linux Programmer's manual
//author: Michael Kerrisk
//url: http://man7.org/linux/man-pages/man3/strtok.3.html
//****************************************************************************//


//   for(j=0; j<tokenCount; j++){
//     if (allData[a][j] != NULL)
//     fprintf(stdout,"(allData[%d][%d]); %s\n\n", a, j, allData[a][j]);
//     //            if (allData[a][j] == NULL)
//     //               fprintf(stdout,"(allData[%d][%d]): Empty Field\n\n", a, j);
//     free (allData[a][j]);                                                                //Frees Data with each pass and sets null
//     allData[a][j] = NULL;
//   }
// }
//  free (allData);
//  allData = NULL;
