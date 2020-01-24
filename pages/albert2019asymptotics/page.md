title: albert2019asymptotic
---

## Reference

Victor V. Albert, Asymptotics of quantum channels: conserved quantities, an adiabatic limit, and matrix product states, Quantum 3, 151 (2019)


[arxiv:1803.00109](https://arxiv.org/abs/1803.00109)

## Contents

* A **quantum channel** $\\mathcal{A}$ on $B(\\mathcal{H})$ in finite dimensions, $\mathcal{A}^\ddagger$ the adjoint. 
<dl>
  <dt> right rotating points</dt>
  <dd> $\mathcal{A}(\Psi)=e^{i\Delta}\Psi, \ \Delta\in \mathbb R$</dd> 
  <dt> fixed points (invariant ''states'')</dt>
  <dd> $\mathcal{A}(\Psi)=\Psi\    (\Delta=0)$ </dd>
  <dt> conserved quantities (left rotating points)</dt>
  <dd> $\mathcal{A}^\ddagger(J)=e^{-i\Delta}J, \ \Delta\in \mathbb R$</dd>
</dl>
<div style="background-color:rgba(0, 0, 0, 0.0470588);  text-align:center; vertical-align: middle; padding:10px 0;">
   *Only trivial Jordan blocks for peripheral eigenvalues??* See Prop. 6.2. in [MMW Guided
Tour](http://www-m5.ma.tum.de/foswiki/pub/M5/Allgemeines/MichaelWolf/QChannelLecture.pdf) and 
[wolf2010theinverse](wolf2010theinverse)
</div>
* **Asymptotic projection**: 
$\quad \mathcal{P}\_{\mathcal{A}}\equiv \lim\_{m\to\infty} \mathcal{A}^{\alpha\_m}$
     * projection onto the eigenspace of peripheral spectrum
     * expression in rotating points:  
$$\quad \mathcal{P}\_{\mathcal{A}}(\rho)=
\sum\_{\Delta,\mu} \Psi\_{\Delta\mu}\mathrm{Tr}(J^{\Delta\mu\dagger}\rho),\qquad 
e^{i\Delta} \mbox{ peripheral spectrum},\ \mu \mbox{ degeneracies}$$
     * $J^{\Delta\mu},\ \Psi_{\Delta\mu}$ can be made biorthogonal:
       $\quad \mathrm{Tr}(J^{\Delta\mu\dagger}\Psi_{\Theta\nu})=\delta_{\Delta\Theta}\delta_{\mu\nu}$.

* **Faithful channels**:  a channel $\mathcal E$  with a faithful invariant state
<div style="background-color:rgba(0, 0, 0, 0.0470588);  text-align:center; vertical-align: middle; padding:10px 0;">
 *Equivalently, $\langle\psi|\mathcal{P}\_{\mathcal E}(|\psi\rangle\langle \psi|)|\psi\rangle> \ne 0$ for all
 $|\psi\rangle$*.
</div>
       *  **Prop. 1**: If $\mathcal{E}^\ddagger(J)=e^{-i\Delta}J$ for some $\Delta\in \mathbb R$, then the Kraus
	  operators satisfy: 
	  $$
		JE\_\ell=e^{-i\Delta}E\_\ell J
	  $$
	  The proof is exactly as for the fact that the fixed points of $\mathcal E^\ddagger$ commute with all
	     $E_\ell$
	
	* **Prop. 2**: Spectral restrictions: since $\mathcal E^\ddagger(J_1J_2)=e^{-i(\Delta_1+\Delta_2)}J_1J_2$ for
	  conserved quantities $J_1,J_2$ and $\mathcal E^\ddagger$ has finitely many eigenvalues, a conserved quantity
	  is either nilpotent $(J_{nil})$ or there is some $n\in \mathbb N$ such that
	  $$
		\Delta=\frac{2\pi}{N}n,\qquad \mbox{for some } N\le \vert J\vert_1
	  $$
          Proof: by number of eigenvalues in finite dimension 
<div style="background-color:rgba(0, 0, 0, 0.0470588);  text-align:center; vertical-align:middle; padding:10px 0;"> 
  *The bound on $N$ seems rather strange, since any constant multiple of a conserved quantity is a conserved quantity. The proof is 
  somewhat confusing.*
</div>

	* **Partial Noether-type theorem**: unitary conserved quantities are symmetries of the channel:
	$$
	J\mathcal E(\rho)J^\dagger =\mathcal E(J\rho J^\dagger)
	$$
        The other direction is not true.

* **Extension to general channels**: Any faithful channel $\mathcal E$ can be extended to a channel $\mathcal A$  with a decaying (transient)  subspace,  such that $\mathcal E$ acts on the largest invariant subspace for $\mathcal A$. Kraus operators for $\mathcal A$:
$$
A^\ell=\begin{pmatrix} E\_\ell & A\_1^\ell\\\
                             0 & A\_2^\ell 
        \end{pmatrix},\qquad \sum_\ell E_\ell=P,\quad \sum_\ell E_\ell^\dagger A_1^\ell=0,\quad \sum_\ell \left(A_1^{\ell\dagger}A_1^\ell+ A_2^{\ell\dagger}A_2^\ell\right)=I-P      $$
<div style="background-color:rgba(0, 0, 0, 0.0470588);  text-align:center; vertical-align:middle; padding:10px 0;"> 
  *Conversely, any quantum channel $\mathcal A$ has such a block decomposition, where $\mathcal E$ acts on the largest
invariant subspace for $\mathcal A$ ??*
</div>
<div style="background-color:rgba(0, 0, 0, 0.0470588);  text-align:center; vertical-align:middle; padding:10px 0;"> 
  *The largest invariant subspace can be determined via an algorithm [Cirillo and Ticozzi, J.Phys. A Mat. Theor.
48:085302, 2015](cirillo)*
</div>


