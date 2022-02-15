
Part B
ods graphics on;
ods pdf file="/folders/myfoildrs/sasuser.v94/question1partb";
data bread;
  input tsp h1 -h4;
  height=h1; output;
  height=h2; output;
  height=h3; output;
  height=h4; output;
  keep tsp height;
datalines;
  0.25 11.4 11.0 11.3 09.5
  0.50 27.8 29.2 26.8 26.0
  0.75 47.6 47.0 47.3 45.5
  1.00 61.6 62.4 63.0 63.9
 run;
 proc glm;
  class tsp;
  model height=tsp/solution;
  run;
ods graphics off;
ods pdf close;

Part C
ods graphics on;
ods pdf file="C:\Users\ju849482\Desktop";
proc iml;
t={.25 .5 .75 1.0};
C=orpol(t);
print c;
quit

proc glm data=bread;
  class tsp;
  model height=tsp;
  estimate 'Linear Trend' tsp  -.67082 -0.223607 0.223607 0.67082
  output out=s r=resid p=yhat;
run;
ods graphics off;
ods pdf close;

Part E
ods graphics on;
proc glm plots=diagnostic;
  class tsp;
  model height= tsp/solution;
  run
ods graphics off;

Question 2
part a
  Data Power;
  do r=2 to 10
    nu1=4-1; * df for numerator modified for 4 factor levels.;
    nu2=4*(r-1); * df for denominator modified for four factor levels;
    alpha =.05;
    Fcrit=finv(1-alpha,nu1,nu2);*F critical value;
    nc=2*r;*noncentrality parameter for noncentral F;
    power=1-probf(Fcrit,nu1,nu2,nc);
    output
  end;
  keep r nu1 nu2 nc power;
  title Power Calculation in Data Step
  proc print; run;

part b
  *Power Calculation Using proc glmpower;
  data Case
  input trt meanht;
  datalines
  1 -1
  2 0
  3 0
  4 1
  proc glmpower;
    class trt;
    model meanh=trt;
    power
      stddev=1
      ntotal=8 to 40 by 4
      power = .;
    run;

  proc power;
    OneWayAnova
      Alpha=.05
      GroupMeans = (-1.5 0 1.5)
      StdDev=1.4449
      power = .
      NPerGroup = 2. to 6 by 1;
  run;


*Part d with 2 replicates
*Power Calculation Using proc glmpower;
data class;
input trt meanht;
datalines;
1 1
2 0
proc glmpower;
  class trt;
  model meanht=trt;
  power
    stddev=1
    ntotal=4 to 20 by 2
    power = .;
  run;

  *Part d with 8 replicates
  *Power Calculation Using proc glmpower;
  data MidtermQ2
  input trt meanht;
  datalines
  1 -1
  2 0
  3 0
  4 1
  proc glmpower;
    class trt;
    model meanht=trt;
    power
      stddev=1;
      ntotal=16 to 80 by 8
      power = .;
    run;



Question 3

Part A-b
ods graphics on;
ods pdf file ="C:\Users\ju849482\Desktop\q3.pdf" ;

data toolLife;
input A B C toolLife ;
datalines;
-1 -1 -1 22
-1 -1 -1 32
-1 -1 -1 25
+1 -1 -1 32
+1 -1 -1 43
+1 -1 -1 29
-1 +1 -1 35
-1 +1 -1 34
-1 +1 -1 50
+1 +1 -1 55
+1 +1 -1 47
+1 +1 -1 46
-1 -1 +1 44
-1 -1 +1 45
-1 -1 +1 38
+1 -1 +1 40
+1 -1 +1 37
+1 -1 +1 36
-1 +1 +1 60
-1 +1 +1 50
-1 +1 +1 54
+1 +1 +1 39
+1 +1 +1 41
+1 +1 +1 47
;
run;

proc glm data=toolLife;
model toolLife = A|B|C /solution;
ods output ParameterEstimates=solution;
run;

ods graphics off;
ods pdf close;


ods graphics on;
ods pdf file ="C:\Users\ju849482\Desktop\q3c.pdf" ;

data toolLife;
input A B C toolLife ;
datalines;
-1 -1 -1 22
-1 -1 -1 32
-1 -1 -1 25
+1 -1 -1 32
+1 -1 -1 43
+1 -1 -1 29
-1 +1 -1 35
-1 +1 -1 34
-1 +1 -1 50
+1 +1 -1 55
+1 +1 -1 47
+1 +1 -1 46
-1 -1 +1 44
-1 -1 +1 45
-1 -1 +1 38
+1 -1 +1 40
+1 -1 +1 37
+1 -1 +1 36
-1 +1 +1 60
-1 +1 +1 50
-1 +1 +1 54
+1 +1 +1 39
+1 +1 +1 41
+1 +1 +1 47
;
run;

proc glm data=toolLife;
model toolLife = B C A*C /solution;
ods output ParameterEstimates=solution;
run;

proc print data=solution;
title "Regression model for predicting tool life (in hours) based on factors A B C and AC";
run;

proc glm data=toolLife plot(unpack)=diagnostic ;
	model toolLife = A|B|C;
	output out=out p=yhat r=resid;
run;
quit;
ods graphics off;
ods pdf close;





Question 3
ods graphics on;
ods pdf file ="C:\Users\ju849482\Desktop\q3.pdf" ;


data toolLife;
input A B C toolLife ;
datalines;
-1 -1 -1 22
-1 -1 -1 32
-1 -1 -1 25
+1 -1 -1 32
+1 -1 -1 43
+1 -1 -1 29
-1 +1 -1 35
-1 +1 -1 34
-1 +1 -1 50
+1 +1 -1 55
+1 +1 -1 47
+1 +1 -1 46
-1 -1 +1 44
-1 -1 +1 45
-1 -1 +1 38
+1 -1 +1 40
+1 -1 +1 37
+1 -1 +1 36
-1 +1 +1 60
-1 +1 +1 50
-1 +1 +1 54
+1 +1 +1 39
+1 +1 +1 41
+1 +1 +1 47
;
run;

proc glm data=toolLife;
model toolLife = A|B|C /solution;
ods output ParameterEstimates=solution;
run;

proc glm data=toolLife;
model toolLife = B C A*C /solution;
ods output ParameterEstimates=solution;
run;

proc print data=solution;
title "Regression model for predicting tool life (in hours) based on factors A B C and AC";
run;

proc glm data=toolLife plot(unpack)=diagnostic ;
	model toolLife = A|B|C;
	output out=out p=yhat r=resid;
run;
quit;
ods graphics off;
ods pdf close;



ods graphics on;
ods pdf file ="C:\Users\ju849482\Desktop\q3all3.pdf" ;


data toolLife;
input A B C toolLife ;
datalines;
-1 -1 -1 22
-1 -1 -1 32
-1 -1 -1 25
+1 -1 -1 32
+1 -1 -1 43
+1 -1 -1 29
-1 +1 -1 35
-1 +1 -1 34
-1 +1 -1 50
+1 +1 -1 55
+1 +1 -1 47
+1 +1 -1 46
-1 -1 +1 44
-1 -1 +1 45
-1 -1 +1 38
+1 -1 +1 40
+1 -1 +1 37
+1 -1 +1 36
-1 +1 +1 60
-1 +1 +1 50
-1 +1 +1 54
+1 +1 +1 39
+1 +1 +1 41
+1 +1 +1 47
;
run;

proc glm data=toolLife;
model toolLife = A|B|C /solution;
ods output ParameterEstimates=solution;
run;

proc glm data=toolLife;
model toolLife = B C A*C /solution;
ods output ParameterEstimates=solution;
run;

proc print data=solution;
title "Regression model for predicting tool life (in hours) based on factors B C and AC";
run;

proc glm data=toolLife plot(unpack)=diagnostic ;
	model toolLife = A|B|C;
	output out=out p=yhat r=resid;
run;

proc sort data=out; by resid;
data out; set out;
n=_n_;
run;

data _null_;
call symput('obs'), put(lastobs, best.));
set out nobs=lastobs;
run;

data out; set out;
	nQuant=probit(  ( n-0.375)/(&nobs+0.25) );
run;

proc rank data=out normal= blom out= out1;
	var resid;
	ranks resid_Quant
run;

title 'Q-Q plot for residuals in toolLife Data';
	proc sgplot data=out1;
		scatter y=resid_Quant x=nQuant;
		reg y=resid_Quant x=nQuant;
		xaxis label="Normal Quantiles";
		yaxis label="Residual";
	run;


quit;
ods graphics off;
ods pdf close;
