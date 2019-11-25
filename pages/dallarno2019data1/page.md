title: dallarno2019data1
---

## Reference

M. Dall'Arno, F. Buscemi, A. Bisio, A. Tosini, Data-Driven Inference, Reconstruction, and Observational Completeness of Quantum Devices


[arxiv:1812.08470](https://arxiv.org/abs/1812.08470)

## Comments

*Nezaujímavé. Blbo napísané. Strata času.*

## Contents

* **Data-driven inference:** a device (measurement or a set of states) is inferred based on output distributions without any
  knowledge of the testing apparatus. The resulting device is
     * consistent with the data (contains the output distributions in its range)
     * maximally noncommital (consistent device with the range of smallest volume)

* **The setting:**
     * Let $\mathbb S\subset \mathbb R^l$ be the set of states. A measurement with $n$-outcomes is an affine (equivalently, linear)  map $M: \mathbb R^l\to \mathbb R^n$, mapping all states to probability distributions. The tests are sets of states $\mathcal S\subset \mathbb S$.
     * Similarly, let $\mathbb E\subset \mathbb R^l$ be the set of effects. A set of $n$ states is a linear map $R:\mathbb R^l\to
  \mathbb R^n$, mapping all effects to $[0,1]^n$. Test are sets of effects $\mathcal E\subset\mathbb E$.
* **The ddi map:** for $\mathcal X\subseteq \mathbb R^n$, $u=\\{1,\dots,1\\}\in \mathbb R^n$,
$$
ddi(\mathcal X|\mathbb S)=\mathrm{argmin} \\{\mathrm{Vol}(M\mathbb S),\ \mathcal X \subseteq M\mathbb S\subseteq
\mathrm{span}(\mathcal X)\\}\\\
ddi(\mathcal X|\mathbb E)=\mathrm{argmin} \\{\mathrm{Vol}(M\mathbb E),\ \mathcal X\cup\\{0,u\\} \subseteq M\mathbb E\subseteq
\mathrm{span}(\mathcal X\cup\\{u\\})\\}
$$

* **Observational completeness:** 
     * A set of states $\mathcal S\subset \mathbb S$ is OC for a measurement $M$ if
$$
ddi(M\mathcal S|\mathbb S)=\\{M\mathbb S\\}
$$
(with $M$ applied to $\mathcal S$, ddi returns the range of $M$ as the unique result). 

     * A set of effects $\mathcal E\subset \mathbb E$ is OC for a set of states $R\subset \mathbb S$ if
$$
ddi(R\mathcal E|\mathbb E)=\\{R\mathbb E\\}
$$

## Results

1. $ddi(\\{p_x\\}|\mathbb S)$ is a singleton for any set of outcome distributions $\\{p_x\\}\subset \mathbb R^n$ if and only if the state space is
   a (hyper)sphere. 

     *  
