title: dallarno2019data
---

## Reference

F. Buscemi, M. Dall'Arno, Data-Driven Inference of Physical Devices: Theory and Implementation, New J. Phys. 21, 113029 (2019)

[arxiv:1805.01159](https://arxiv.org/abs/1805.01159)


## Comments

*podobné ako [dallarno2017device](dallarno2017device), [dallarno2019device](dallarno2019device), dosť nezaujímavé.*


## Content

1. Data-driven inference: an unknown device is inferred only from the correlations observed in the data, without any
   assumption on the apparatus.

1. The best reconstruction explains all observed data and as little more as possible.

1. For an (unknown) channel $\mathcal C$, let $\mathcal S(\mathcal C)$ be  the set of all correlations 
$$
\mathcal S(\mathcal C)=\\{ \\{p\_{i|j}=\mathrm{Tr}[\mathcal C(\rho_i) \pi_j]\\},\ \\{\rho_i\\} \mbox{ a set of states },\
\\{\pi_j\\} \mbox{ a POVM}\\}
$$
The data-driven reconstruction, with respect to an a priori given set of states $\mathcal D$,  is defined as
$$
\mathcal C_{DD}:= \mathrm{argmin} \\{\mathrm{Vol}(\mathcal S(\mathcal C)),\ \mathcal C\in \mathcal D,\ \\{p_{i|j}\\}\in \mathcal S(\mathcal C)\\}
$$

1. The set $\mathcal S(\mathcal C)$ is characterized for  $\mathcal C\in \mathcal D$ - the set of qubit
   dihedrally-covariant channels (i.e. such that the first column in Ruskai-King representation of the qubit channel has
   only one nonzero element (except the first 1)). It seems that only binary conditional probability distributions are
   considered. 

1. The methods are similar to those of the above two papers, but some parametrization of the set $\mathcal D$ is derived
   first. Again the double conjugate of the indicator function of $\mathcal S(\mathcal C)$ is used. 
