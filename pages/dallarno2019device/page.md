title: dallarno2019device
---

## Reference

M. Dall'Arno, Device-independent tests of quantum states, Phys. Rev. A 99, 052353 (2019) 

[arxiv:1702.00575](https://arxiv.org/abs/1702.00575)

## Comments

*Tento článok je podobný ako  (a snáď ešte hlúpejší než) [dallarno2017device](dallarno2017device)*


##  Contents

Given a  family of $m$ quantum states $\rho=\\{\rho_x\\}$, the set $\mathcal S(\pi)$ of all input-output correlations (conditional probabilities) obtained by performing an $n$-outcome measurement is described:
$$
S_n(\rho_x):=\\{p | p_{y|x}=\mathrm{Tr}[\pi_y\rho_x],\ \mbox{for an $n$-outcome POVM }\pi\\}
$$
The problem is restricted to $n=2$, where $S_2(\rho_x)$ is a set of vectors in $\mathbb R^m$, given as
$$
S_2(\rho_x)=\\{p\in \mathbb R^m| p_x=\mathrm{Tr}[\rho_x\pi],\ 0\le \pi\le I\\}.
$$

### Results

1. Measurements producing correlations on the boundary of $S_2(\rho_x)$ are those maximizing $p^Tw$ for $w\in \mathbb
   R^m$ and the corresponding effects are the projections onto the positive part of $\sum_xw_x\rho_x$ (Prop. 1)

1. For qubits, the set $S_2(\rho_x)$ is characterized as the convex hull of $0$, $u=(1,1,\dots,1)$ and an embedding of an ellipsoid (possibly degenerate)  centered at $\frac12 u$ in $\mathbb R^m$. This embedded ellipsoid is described by a system of equalities and inequalities.

1. This is applied to pairs of pure states  and to $m$ pure states uniformly distributed in te Bloch equatorial plane
### Remarks

1. The function $W(\rho_x,w)=\max_{p\in S_2} p^Tw$ is the support functional of $S_2(\rho_x)$, which is the conjugate of the
   indicator function 
   $$
   \chi_{S_2}(x)=\left\\{ \begin{array}{cc} 0 & \mbox{ if } x\in S_2\\\
                          \infty & \mbox{ otherwise}
			  \end{array}\right.
$$
The maximization in Eq. (4) is $\chi_{S_1}^{\*\*}=\chi\_{S\_2}$ (see [ekeland]()), so that the inequality in Eq. (4) 
can be put to equality. 

1. The results, in fact, are obtained as follows:  Using the Pauli operators $\\{\sigma_k\\}\_{k=1}^3$, we
   write for all $x$ and for any qubit effect $0\le \pi\le I$:
$$
\rho_x=\frac12 I+\sum_{k=1}^3 S_{x,k}\sigma_k,  \qquad \pi= tI+\sum_{k=1}^3 \alpha_k\sigma_k,
$$
here 
$\\|\alpha\\|\_2\le t\le 1-\\|\alpha\\|\_2$. Then $p(\pi)=\\{\mathrm{Tr}[\rho_x\pi]\\}= tu + 2S\alpha$,
$\alpha=\\{\alpha_k\\}$, $S=\\{S\_{x,k}\\}$ is the $m\times 3$-matrix. It is clear that $S_2(\rho_x)$ is the convex hull of
$E_2:=\\{p(\pi),\ \pi \mbox{ is a projection}\\}$ (since projections are the extreme points of $[0,I]$). Moreover, $\pi$ is a
projection iff $t=\\|\alpha\\|\_2=\frac12$, so that 
$$
E_2=\\{0,u\\}\cup \frac12 u+SB_1(\mathbb R^3)\qquad (B_1(\mathbb R^3) \mbox{ is the unit sphere in }\mathbb R^3).
$$
and it is easy to se that $co(E_2)=co(\\{0,u\\}\cup (\frac12 u+ SB(\mathbb R^3))\\},\qquad (B(\mathbb R^3) \mbox{ is the unit ball in }\mathbb R^3).
$$

1. *I would say that the system of (in)equalities describing the set of the form $a+SB(\mathbb R^3)$ is something
   standard.*


 

