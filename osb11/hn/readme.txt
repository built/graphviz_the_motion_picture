This is the Graphviz "movie" from my talk at Open Source Bridge 2011.

It is a trivial example but all of the mechanics are there 
for you to copy and play with using data of your own.

This data was drawn from the Hacker News website. Every fifteen
minutes the front page of HN was downloaded. This went on for a 
few days until there was enough data to work with.

The movie that is created shows the domains where each story 
came from on HN. The domains are colored based on their
TLD. The coloring effect wasn't as useful as I'd hoped, but
by leaving it in you can see how to do it yourself and maybe
do a better job.

Remember to have Graphviz displaying in "Energy Minimized" mode,
otherwise the display you see will be confusing.

To play the "movie", run the play script like so:

./play


And then open the hnmovie.dot file with Graphviz. I use 
Graphviz 1.13 because I had trouble with stability with
newer versions. (Lots of core dumps.)

What you will see is the top 5 domains listed on HN. This 
will update every few seconds. With each update you move
15 minutes forward in time. The domains will change over time.

