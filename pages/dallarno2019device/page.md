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



conditional probability distribution $p\in \mathcal S(\pi)$ if and only if $p\_{\cdot|x}\in \mathcal S(\pi)$ for all
   fixed $x$ (Prop. 2).  *(This is rather obvious)*

2. The range  of a qubit measurement is characterized (Thm. 1): Using the Pauli operators $\\{\sigma_k\\}\_{k=0}^3$, we
   write for all $y$ and for any state $\rho$:
$$
\pi_y=t_y+\sum_{k=1}^3 S_{y,k}\sigma_k,\quad t_y=\frac12\mathrm{Tr}(\pi_y), \qquad \rho=\sigma_0+\sum_{k=1}^3 \alpha_k\sigma_k.
$$
Let $q\in \mathbb R^n$ be the vector $q_y=\mathrm{Tr}[\pi_y\rho]$, then we have $q=t+S\alpha$, where $t=\\{t_y\\}$ and
$\alpha=\\{\alpha_y\\}$ are $n$-dim. vectors and $S=\\{S_{y,k}\\}$ is an $n\times 3$- matrix. Then
$$
\mathcal S_1(\pi):=\\{ \\{\mathrm{Tr}[\pi_y\rho]\\},\ \rho \mbox{ is a state}\\}= t+ SB(\mathbb R^3),\qquad (B(\mathbb R^3) \mbox{ is the unit ball in }\mathbb R^3).
$$
The last set is some (degenerate)  ellipsoid embedded in $\mathbb R^n$ ($n$ is the number of outcomes of $\pi$). It is characterized using
constrained quadratic optimalization. 

3. This is applied to depolarized SIC POVM and MUB (Coro. 1 and 2).


 

