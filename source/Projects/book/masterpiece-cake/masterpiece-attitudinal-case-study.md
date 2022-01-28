(attitudinal-case-study)=
# Attitudinal Model Case Study
Write an intro.  Facts, text, 

## Methodology

To build a model that takes into account the subjective attitudes of the Supreme Court Justices. I use the Washington University Law Database (Spaeth, Epstein, et al. 2017) that takes into account the individual decisions of each justice in order to determine their ideological value across time.   I then test these values against the facts, including attitudinal objects, and attitudinal situations, of Masterpiece Cake LTD. v. Colorado Civil Rights Commission (2018)

### Ideological Score by Justice 
To determine a justice’s ideological score I test their votes across time to determine whether they vote conservatively or liberally.  A simple mean value between one and two is then generated.  The closer to one a justice votes the more conservative.  Alternatively, the closer to two the value, the more liberal.  The results for the individual justices are included in 
the chart below.  


```{eval-rst}

.. csv-table:: Ideological Score by Justice Figure 1.0
    :header-rows: 1
    :widths: 5, 5, 5, 5, 5
    :file: tables/id-score-justice.csv
```

### Ideological Score by Justice First Ammendment 
Similarly, I derive ideological values according to voting patterns relating to first amendment cases.  The results are printed in the following chart.  


```{eval-rst}

.. csv-table:: Ideological Score by Justice by First Ammendment Figure 1.1
    :header-rows: 1
    :widths: 5, 5, 5, 5, 5, 5
    :file: tables/id-first-ammendment.csv
```

### Ideological Score by Justice by Individual Issue Area
Finally, ideological scores are derived by issue area.  For the purpose of this discussion this is equivalent to an evaluation of the individual attitude-situations as they relate to the facts of the case.  The results are below:

```{eval-rst}

.. csv-table:: Ideological Score by Justice by Issue Area Figure 1.2
    :header-rows: 1
    :widths: 5, 5, 5, 5, 5, 5, 5
    :file: tables/id-issue-area.csv
```


## Expected Results

In an attempt to replicate the results of Masterpiece Cakeshop Ltd. v. Chicago Civil Rights Commission (2018) I will simply consult the three ideological values above.  If a justice scores below a 1.5 in any area, then they will be expected to vote conservatively.  Conversely if a score above 1.5 is observed the justice is expected to vote liberally.  


In context, A liberal vote will found in favor of the Mr. Charlie Craig and his partner, Mr. Dave Mullins.  The following variables describe liberal voting preferences as they relate to the case.  Pro-civil liberties or civil rights, pro-neutrality in establishment clause cases, pro-underdog, anti-owner, anti-business, pro-government, pro-exercise of judicial action, and pro-judicial activism. A conservative vote is in favor of Mr. Philips, the Colorado baker. Conservatism in context is described as opposite the above liberal values.  


### Justice Vote According to General Ideological Score

```{eval-rst}

.. csv-table:: Justice Vote by General Ideological Score Figure 4
    :header-rows: 1
    :widths: 5, 5, 5
    :file: tables/justice-vote-id-score.csv
```
### Justice Votes by First Amendment 


```{eval-rst}

.. csv-table:: Justice Vote by Amendment Figure 5
    :header-rows: 1
    :widths: 5, 5, 5, 5
    :file: tables/justice-vote-amendment.csv
```

### Justice Votes by Issue Area


```{eval-rst}

.. csv-table:: Justice Vote by Issue Area Figure 6
    :header-rows: 1
    :widths: 5, 5, 5, 5, 5
    :file: tables/justice-vote-issue-area.csv
```

## Prediction Summary


The general ideological value scores predict a 5-4 split along the usual lines (figure 5 include a ref).  The conservative majority coalition consists of Justices, Kennedy, Thomas, Roberts, Alito, and Gorsuch.  The liberal minority is of Justices Ginsberg, Breyer, Sotomayor, and Kagan.  

	
The ideological scores by the first amendment issue area, predicts a very different outcome.  For instance, a 7-2 liberal majority is expected.  Kennedy, is expected to vote with the conservative coalition, along with Gorsuch.  The Liberal majority consists of, Thomas, Ginsberg, Breyer, Roberts, Alito, Sotomayor, and Kagan.  


Testing again for individual issue areas, the results seem spurious.  When controlling for just the establishment clause, there is a 5-4 majority conservative coalition comprised of Justices Kennedy, Thomas, Roberts, Alito and Gorsuch.  The minority coalition consists of Justices, Ginsberg, Breyer, Sotomayor, Kagan.  However, when controlling for Free Exercise, a 9-0 liberal majority is the expected outcome.  
