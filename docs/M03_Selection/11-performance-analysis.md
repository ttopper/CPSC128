# Performance Analysis*

Note that while all three versions of our program work, Version 3 is the
best because it is more efficient, and more readable. (Increased
efficiency does not always go hand in hand with increased readability).
The table below summarizes the relative numbers of comparison made by
each of the versions.

```
  ----------------- ----------------- ----------------- -----------------
                    Number of                           
                    comparison &                        
                    logical                             
                    operations                          

                    Minimum           Average           Maximum

  Version 1         12 if/elifs @ 3 = 12 if/elifs @ 3 = 12 if/elifs @ 3 =
                    36                36                36

  Version 2         3                 (12 if/elifs @ 3  12 if/elifs @ 3 =
                                      )/2 = 18          36

  Version 3         3                 ((1 if @ 3) +\    ((1 if @ 3) + (11
                                      (11 if/elifs @ 1  if/ellifs @ 1 ))
                                      ))/2 = 7          = 14
  ----------------- ----------------- ----------------- -----------------
```

Notes:

1.  We might be able to make the program even faster by by checking for
    the most likely grades first (e.g. C's first, then B's, then A's,
    then F's). This would minimize the number of tests that need to be
    done, but the resulting loss of readability might not be worth the
    performance gain.

2.  The table overstates the numbers of comparisons that will actually
    be made in some cases. The reason is that Python "short circuits"
    test expressions when it can. More on this later.

------------------------------------------------------------------------

* This is a_theoretical_performance analysis in which we are
estimating the expected performance. We will soon also be
doing_empirical_or_experimental_performance analyses in which we
measure actual performance rather than trusting to fallible predictions.
