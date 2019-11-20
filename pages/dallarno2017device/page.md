title: dallarno2017device
---

## Reference

M. Dall'Arno, S. Brandsen, F. Buscemi, V. Vedral, Device-independent tests of quantum measurements, Phys. Rev. Lett. 118, 250501 (2017)

[arxiv:1609.07846](https://arxiv.org/abs/1609.07846)

## Comments

*Tento článok mi pripadá dosť slabý na PRL*


##  Contents

Given a POVM $\pi=\\{\pi_y\\}$, the set $\mathcal S(\pi)$ of all input-output correlations (conditional probabilities) compatible with $\pi$  is characterized:
$$
\mathcal S(\pi)=\\{p_{y|x}=\mathrm{Tr}[\pi_y\rho_x],\ \mbox{for a family of quantum states }\\{\rho_x\\}\\}
$$

### Results

1. A conditional probability distribution $p\in \mathcal S(\pi)$ if and only if $p\_{\cdot|x}\in \mathcal S(\pi)$ for all
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


 

