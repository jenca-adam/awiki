title: liu2019resource
---

## Reference

Zi-Wen Liu, Andreas Winter, Resource theories of quantum channels and the universal role of resource erasure, arXiv:1904.04201


[arxiv:1904.04201](https://arxiv.org/abs/1904.04201)



## Contents

* **Free channels** minimal requirements:
    * closed under composition and tensor products
    * topologically closed (in diamond norm)
    * contains identity

* further properties (not necessary but can be useful):
    * partial traces are free
    * free states (channels from tricial systems) are free
    * convexity
    * on tensor products, permutations are free

* **Resource transformations:** supercchannels
    * must transform free channels to free channels
    * but not necessarily all such superchannels
    * the choice here: $\mathcal D * \mathcal E$ where $\mathcal E,\mathcal D$ are free 

* **Composition of multiple resources:** tensor products
    * more complicated than states
    * $\mathcal N_1\otimes\dots \mathcal N_n$ can be seen as a cptp map
    * or as a quantum comb (memory channel: ordered tuple)
    * or as a no-signaling map (a collection of channels)
    * corresponding norms: 
        * for combs $\diamond\to$ (or $n\diamond$) norm
        * for ns: $\diamond ns$ norm - ''max trace norm of the output of any generalized supechannels that maps
	  ns-channels to ns-channels'' [arxiv:1909.06655](https://arxiv.org/abs/1809.06655)
    * simulation: for collections of channels: $\alpha=\mathcal N_1\otimes\dots\otimes \mathcal N_n$ simulates 
    $\beta=\mathcal M_1\otimes\dots\otimes \mathcal M_m$ if for any permutation $\pi\in S_m$ there is a permutation
    $\tau\in S_n$ and a quantum comb $C$ such that 
    $$
   \beta^\pi=\mathcal M\_{\pi(1)}\otimes\dots\otimes \mathcal M\_{\pi(m)}=C(\alpha^\tau)
    $$
    * or approximate (in suitable norm)

* **Resource measures:** axiomatic / operational 
    * Conditions for a resource measure $\Omega$ on channels:
        * Normalization: $\Omega(\mathcal N)=0$ if $\mathcal N$ is free and is nonnegative otherwise;
        * Faithful: $\Omega(\mathcal N)=0$ iff $\mathcal N$ is free and is strictly positive otherwise;
        * Monotone: left composition, right composition, tensoring -  with free channels
        * Convex
    * constructions:  for a resource monotone 	$\omega$
        * *Increasing power:* $$\Omega_{ip,\omega}(\mathcal N)=\sup_\rho \\{\omega(\mathcal
	  N(\rho))-\omega(\rho)\\},\qquad 
	\Omega_{ip,\omega}^*(\mathcal N)=\sup_\rho \\{\omega(\mathcal N\otimes id(\rho))-\omega(\rho)\\}$$
	    * *Generating power:* $$\Omega_{gp,\omega}=\sup_{\omega(\rho)=0}\omega(\mathcal N(\rho)), \qquad \Omega_{gp,\omega}^*=\sup_{\omega(\rho)=0}\omega(\mathcal N\otimes id(\rho))$$
	    * *Distance measures*: for a distance measure $\delta$ on channels: $$\Delta_\delta(\mathcal N)=\inf_{\mathcal
	  L\in \mbox{ free}} \delta(\mathcal N,\mathcal L)$$
	    * by lifting a distance $d$ from states: 
	$$\Delta_{(d)}(\mathcal N)=\inf_{\mathcal L\in \mbox{ free}}\sup_\rho d(\mathcal N(\rho),\mathcal L(\rho)),\qquad
	\Delta_{(d)}^*(\mathcal N)=\inf_{\mathcal L\in \mbox{ free}}\sup_\rho d(\mathcal N\otimes id(\rho),\mathcal L\otimes id(\rho))
$$
        * all are normalized and monotone w.r. left and right composition with free channels, complete (starred) versions  are monotone under tensoring with free channels (invariant if free states exist)
	    * *Robustness (and smooth):* 
	    $$R(\mathcal N)=\min\\{s\ge 0: \frac1{1+s}\mathcal N+\frac{s}{1+s}\mathcal N'\in \mbox{ free}, \
	  \mathcal N'\ cptp\\},\qquad R^\epsilon(\mathcal N)= \inf_{\frac12\\|\mathcal N'-\mathcal N\\|_\diamond} R(\mathcal N')$$
	       * *log-robustness (and smooth):* 
	   $$LR(\mathcal N)=\log(1+R(\mathcal N))= \min_{\mathcal M\in \mbox{ free}} D_{max}(\mathcal N\\|\mathcal M),
	   \qquad
LR^\epsilon(\mathcal N)=\inf_{\frac12\\|\mathcal N'-\mathcal N\\|_\diamond} LR(\mathcal N')=
	   \min\_{\mathcal M \in\mbox{ free}}D\_{max}^\epsilon(\mathcal N\\|\mathcal M)
	   $$
	       * Channel max-reletive entropy:	  
	       $$D\_{max}(\mathcal N\\|\mathcal M)=\log\min\\{\lambda:, \mathcal N\le \lambda\mathcal M\\}, \qquad 
	   D\_{max}^\epsilon(\mathcal N\\|\mathcal M)=\inf_{\frac12\\|\mathcal N'-\mathcal N\\|_\diamond}D\_{max}(\mathcal N'\\|\mathcal M)$$
               * $R$, $LR$ are normalized and monotone.

* **One-shot resource erasure:** $\epsilon$-resource-destruction cost:
\\[
\mathsf{COST}^\epsilon(\mathcal N)=\min\\{ \log(k), \ \exists \mbox{ free }\mathcal F,\mathcal M,\  \\{p_i,\mathcal U_i,\mathcal
V_i\\}\mbox{ ensemble of pairs of free reversible channels}, s.t. \frac12\\|\sum_{i=1}^k p_i\mathcal V_i\circ(\mathcal N\otimes
\mathcal F)\mathcal U_i-\mathcal M\\|_\diamond \le \epsilon\\}
\\]
    * **Thm. 10:** some bounds for $\mathsf{COST}^\epsilon$ (in smooth $LR$).

* **QAEP for channel max-relative entropy?** only lower bound in q. realtive entropy of channels:
\\[
\liminf_{n\to \infty} D\_{max}^\epsilon(\mathcal N^{\otimes n}\\|\mathcal M^{\otimes n})\ge D(\mathcal N\\|\mathcal M)=
\sup_\rho D(\mathcal N\otimes id(\rho)\\|\mathcal M\otimes id(\rho))
\\]

* *Conic convex-split lemma*:

