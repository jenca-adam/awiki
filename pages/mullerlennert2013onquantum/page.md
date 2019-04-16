title: mullerlennert2013onquantum
---
## Reference

M. M\" uller-Lennert et al, On quantum Rényi entropies: a new generalization and some properties, J. Math. Phys. 54, 122203 (2013)


[arXiv:1306.3142](https://arxiv.org/abs/1306.3142)


## Content

* Axiomatic approach to quantum Rényi entropies: for subnormalized density matrices ($0\ne Tr \rho \le 1$), $\rho<<\sigma$
      1. continuity: $(\rho,\sigma)\mapsto D(\rho\|\sigma)$
      1. unitary invariance
      1. normalization: $D(1\|1/2)= \log 2$
      1. order: if $\rho\ge \sigma$, then $D(\rho\|\sigma)\ge 0$; if $\rho\le\sigma$, then $D(\rho\|\sigma)\le 0$
      1. additivity
      1. general mean: there is a continuous and strictly monotone function $g$ such that (whenever well defined):
       $$
        D(\rho\oplus \tau\|\sigma\oplus\omega)=g^{-1}\left( \frac{Tr (\rho)}{Tr (\rho+\tau)} g(D(\rho\|\sigma))+\frac{Tr (\tau)}{Tr (\rho+\tau)} g(D(\tau\|\omega))\right)
       $$ 

 
   By [renyi1961onmeasures](renyi1961onmeasures), $g$ must be linear or exponential. The postulates **do not** determine a unique quantum divergence.
   
   A question: do the axioms imply **data processing inequality?** (in the non-commutative case). Equivalence to joint convexity (concavity) (Prop. 1)

* standard quantum Rényi relative entropy (from Petz quasi entropies): the axioms and DPI **only** for $\alpha\in (0,1)\cup (1,2]$    
* sandwiched quantum Rényi relative entropy: definition, properties:
      1. satisfies axioms for $\alpha\in [1/2)\cup (1,\infty)$
      1. positive definite (for normalized states)
      1. dominance: $\rho, \sigma,\sigma'$, $\sigma\le \sigma'$, then $D(\rho\|\sigma)\ge D(\rho\|\sigma')$ 
      1. limit values: $\alpha\to \infty$: relative max-entropy
                       $\alpha\to^\pm 1$: quantum relative entropy
      1. DPI
* conditional entropies: $H(A|B)\_\rho =\sup\_{\sigma_B} D(\rho\_{AB}\| id\_{A}\otimes \sigma\_B)$  
  supremum over subnormalized densities   
 
