explanation_text="""
Polya's Urn is a box that initially contains a certain number of black and white balls.
The Urn is updated by drawing a ball randomly from the box, recording whether it is black or white,
and then replacing it in the box <em> along with another ball of the same color</em>.
<br><br>
If X(i) is the random variable that gives the color of the ball that you obtain on the n_th draw,
then the sequence of random variables X(n) for n=1,2,3,... is an example of a sequence that is not
independent but is <em>exchangeable.</em>
<br><br>
<em>Exchangeable</em> means that the probability of obtaining
any particular sequence
of n black and white balls is independent of the order in which the balls are drawn and depends only on the
number of balls of each color. 
<br><br>
DeFinetti's Theorem states that such an exchangeable sequence of random variables arises as a mixture.  One
can reconstruct the probability of a given sequence of black and white balls by
<ol>
<li> drawing a probability p of getting a white ball from a prior probability distribution over the interval [0,1],
<li> and then making a series of independent, identically distributed choices of white vs black balls with probability p.
</ol>

In the particular case of Polya's urn, with two colors, the prior probability distribution is the Beta distribution with parameters
given by the initial number of white and black balls.
"""

explanation_text_2="""
This simulation illustrates the behavior of Polya's Urn.
<ul>
<li>  The controls at the top set the initial number of white and black balls in the urn.  
<li>  The lower graph shows repeated simulations of 50 draws from the urn, showing how the number of white balls evolves for the 
50 draws.  
<li> The upper graph accumulates a histogram of the relative number of times the urn has k white balls in it after 50 draws.  If
the initial numbers of white and black balls are a and b respectively, then this histogram converges to (a good approximation) of
the Beta distribution, appropriately rescaled.
</ul>
To use the simulation, choose your initial number of black and white balls and push Go!
"""
