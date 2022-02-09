
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Integer40
{
  // a dynamically allocated array to hold a 40
  // digit integer, stored in reverse order
  int *digits;
} Integer40;

void big40Print(Integer40 *p)
{
  int i;

  if (p == NULL)
  {
    printf("(null pointer)\n\n");
    return;
  }
  printf("%p\n", p);
  for (i = 39; i >= 0; i--)
  printf("%x", p->digits[i]);
  printf("\n\n");
}

Integer40 *parseString(char *str)
{
  int i;
  char *strg = NULL;

  strg = (char*)malloc(80*sizeof(char));
  memset((void*)strg, 0, 80);
  if(NULL == strg)
  {
    fprintf(stderr,"Line 42 STRG CALLOC or MEMSET Failure\n");
    exit (1);
  }
  Integer40 *p = NULL;
  p = (Integer40*)malloc(160);
  if(NULL==p)
  {
    fprintf(stderr,"Line 49--Parsing Structure 'p' Failed to Malloc\n");
    exit (1);
  }
  p->digits = (int*)malloc(40*sizeof(int));
  if(NULL==p->digits)
  {
    fprintf(stderr,"Line 45--Parsing Array '(p->digits)' Failed to Malloc\n");
    exit (1);
  }
  if(NULL == str)
  {
    fprintf(stderr,"Null String Passed to parseString Function\n");
    p = NULL;
    return p;
  }
  strcpy(strg,str);
  //strg = strdup(str);
  for(i = 0; i < 40; i++)
  {
    char *tmp = NULL;
    tmp = (char*)calloc(3, sizeof(char));
    if (NULL == tmp)
    {
      fprintf(stderr,"Line 72--tmp Character ARRAY Calloc Failure");
    }
    memcpy(tmp, strg + 39-i , 1);
  //  if(NULL == tmp)
  //  {
  //    fprintf(stderr,"Line 60--memcpy to tmp array Failed");
  //    exit (1);
  //  }
    p->digits[i] = (unsigned int)strtol(tmp, NULL, 16);
   printf("p->digits[%d] = %x\n\n",i, p->digits[i]);
    free(tmp);
  }
  memset((void*)strg, 0, 80);
//  printf("%s\n", strg);
  free (strg);
  return p;
}

Integer40 *i40Destroyer(Integer40 *p)
{
  if (p==NULL)
    return p;
  free(p->digits);
  free(p);
//  printf("P Successfully Neutralized Gentlemen\n\n");
  return p;
}
int main(void)
{
  Integer40 *p;
  p = parseString("0123456789abcdef0123456789abcdef01234567");
  //40 digits
  big40Print(p);
  i40Destroyer(p);

  big40Print(p = parseString("354913546879519843519843548943513179"));
  i40Destroyer(p);
  //>40 digits
  big40Print(p = parseString("012345678901234567890123456789012345678901234567899999"));
  i40Destroyer(p);

  //Null digits
  big40Print(p = parseString(NULL));
  i40Destroyer(p);

  big40Print(p = parseString(""));
  i40Destroyer(p);
}
