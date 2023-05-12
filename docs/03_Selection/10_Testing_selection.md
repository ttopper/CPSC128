# Testing Selection

-   We did some rough testing of our grade conversion program logic
    using a couple of **typical values**, 65 and 93. While it
    is_necessary_to test with common values like these, it is *not
    sufficient*. When programs break it is usually on **uncommon
    values**, i.e. values at the edge of the range of allowable values,
    or even outside the range. What uncommon values should we use to
    test this program?*

-   Will this program work if the grades entered are real values, e.g.
    75.3. If not, what happens? What changes are necessary to make it
    work with real values?

------------------------------------------------------------------------

* We should try 0, 100 as they are at the edges of the range, and
values off each edge of the range, e.g. -1 and 101, since they are
outside the allowable range.
