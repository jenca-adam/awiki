title: liu2019operational 
---

## Reference


Liu, Yunchao, and Xiao Yuan. "Operational resource theory of quantum channels." Physical Review Research 2.1 (2020): 012035


[arxiv:1904.02680](https://arxiv.org/abs/1904.02680)


## Comments

Similar to [liu2019resource](liu2019resource) (lw)

## Content

* **General resource framework for channels**
    
    * *Resource theory of states*: $(\Omega,\Phi,\mu)$, where
         * $\Omega\subset \mathcal D(\mathcal H)$ free states
	     * $\Phi$ free (resource non-generating RNG) channels: $\phi(\Omega)\subseteq \Omega$ for $\phi\in \Phi$ 
	     * $\mu:\mathcal D(\mathcal H)\to \mathbb R^+$ resource measure (*resource monotone*): $\mu(\omega)=0$ for $\omega\in \Omega$ and 
	  $\mu\circ\phi\le \mu$ for $\phi\in \Phi$
	     * $\mu$ can be defined as minimal distance to $\Omega$:
	     $$\mu(\rho)=\min_\omega D(\rho,\omega), \qquad  D(\rho,\omega)\ge 0,\ D(\rho,\rho)=0,\quad D(\mathcal
	     N(\rho),\mathcal N(\sigma))\le D(\rho,\omega),\ \forall \mbox{ channels }\mathcal N $$
	  
    * *Channel resource theory*: $(\mathcal F,\mathcal O,\mathcal R)$, where
         * $\mathcal F$ - set of free channels
	     * $\mathcal O$ - set of free superoperators (superchannels): map $\mathcal F$ to $\mathcal F$
	     * $\mathcal R$ - channels resource measure: $\mathcal R(\mathcal N)\ge 0$, $\mathcal R(\mathcal M)=0$ for
	       all $\mathcal M\in \mathcal F$ (*nonnegative*),  $\mathcal R(\Lambda(\mathcal N))\le \mathcal R(\mathcal N)$ for $\Lambda\in \mathcal O$ (*monotone*)
	     * $\mathcal R$ as minimal distance: $\mathcal R(\mathcal N)=\min_{\mathcal M\in \mathcal F}D(\mathcal
	       N,\mathcal M)$

    * *Interplay*:  
        * given a state resource theory $\mathbf S=(\Omega,\Phi,\mu)$, such that $\phi\otimes id$ is free for free $\phi$
	    * we construct a channel resource theory $\mathbf C=(\mathcal F,\mathcal O,\mathcal R)$:

	         * $\mathcal F$ RNG channels for $\mathbf S$ (= $\Phi$?)
	         * $\mathcal O$ superchannels consisting of free pre and post processing (i.e. $\Lambda(\mathcal N)=\phi_1\circ
	           (\mathcal N\otimes id)\circ\phi_2$, with  $\phi_1,\phi_2\in \Phi$)
	         * different constructions of resource monotones:
	         
            (1) $\mathcal R(\mathcal N)= \min\_{\mathcal M\in \mathcal F}D(\mathcal N,\mathcal M)=\min\_{\mathcal M\in \mathcal F}\max\_\rho D(\mathcal N\otimes id(\rho),\mathcal M\otimes id(\rho))$
	    
	        (2)  $\mathcal R_\Omega(\mathcal N)= \min\_{\mathcal M\in \mathcal F}D_\Omega(\mathcal N,\mathcal M)=\min\_{\mathcal M\in \mathcal F}\max\_{\rho\in \Omega} D(\mathcal N\otimes id(\rho),\mathcal M\otimes id(\rho))$

		    (3) $\mathcal R_g(\mathcal N)=\max\_{\omega\in \Omega} \mu(\mathcal N\otimes id)(\omega))$  (resource
		generating power (lw))

		    (4) $\mathcal R_b(\mathcal N)=\max_{\rho} \mu(\mathcal N\otimes id)(\rho))-\mu(\rho)$   (resource increasing power
		(lw))

	    * If $\mu$ is the minimal distance w.r. to $D$: $\mathcal R\_g\le \mathcal R\_\Omega$, if $D$ satisfies triangle
	      inequality, then also $\mathcal R_b\le \mathcal R$.

* **Distillation and dilution**



		
