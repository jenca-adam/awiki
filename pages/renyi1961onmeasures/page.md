title: renyi1961onmeasures
---
## Reference

A. Rényi, On measures of entropy and information, In: Proceedings of the Symposium on Mathematical Statistics and Probability, pp. 547–561. University of
California Press (1961) 


[file](renyi1961onmeasures/renyi1961onmeasures.pdf)

## Content

**Postulates for Rényi entropies** (for generalized probability distributions: $w(P)=\sum_i p_i\le 1$):
 
1. symmetry
1. continuity of $p\mapsto H({p})$, $p\in (0, 1]$
1. normalization:  $H(\{1/2\})=1$
1. additivity: $H(P\otimes Q)=H(P)+H(Q)$
1. generalized mean value: there is a continuous strictly monotone function $g$ such that 
$$
H(P\cup Q)= g^{-1}\left(\frac{w(P)g(H(P))+w(Q)g(H(Q))}{w(P)+w(Q)}\right)
$$
if $w(P)+w(Q)\le 1$

Shannon entropy if $g$ is linear, $H_\alpha$, $1\ne \alpha>0$ obtained if $g=g_\alpha$, $g_\alpha(x)=2^{(\alpha-1)x}$.

**Postulates for Rényi relative entropies**:  *amount of info obtained if observing $P$ instead of $Q$*

(generalized probability distributions $P=(p_1,\dots,p_n)$, $p_i>0$, $Q=(q_1,\dots, q_n)$)

1. symmetry
2. order: if $p_i\le q_i$ $\forall i$, then $I(Q|P)\ge 0$; if $p_i\ge q_i$ $\forall i$, then $I(Q|P)\le 0$
1. normalization: $I(\{1\}|\{1/2\})=1$
1. additivity: $I(P_1\otimes P_2| Q_1\otimes Q_2)=I(P_1|Q_1)+ I(P_2|Q_2)$
1. generalized mean value: there is a continuous strictly monotone function $g$ such that if $w(Q_1)+w(Q_2)\le1$, $w(P_1)+w(P_2)\le 1$
$$
I(Q_1\cup Q_2|P_1\cup P_2)= g^{-1}\left(\frac{w(Q_1)g(I(Q_1|P_1))+w(Q_2)g(I(Q_2|P_2))}{w(Q_1)+w(Q_2)}\right)
$$

Then $g_\alpha$, $1\ne \alpha>0$  and $g_1$ linear are the only possible functions and then $I=I_\alpha$,  where
$$
I_\alpha(Q|P)=\frac{1}{\alpha-1}\log\left(\frac{\sum_i q_i^\alpha p_i^{1-\alpha}}{\sum q_i}\right),\qquad I_1(Q|P)=\sum_i q_i \log\left(\frac{q_i}{p_i}\right)
$$