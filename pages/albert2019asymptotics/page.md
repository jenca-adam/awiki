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

* **Asymptotic projection**: 
$\quad \mathcal{P}\_{\mathcal{A}}\equiv \lim\_{m\to\infty} \mathcal{A}^{\alpha\_m}$
     * projection onto the eigenspace of peripheral spectrum
     * expression in rotating points:  
$$\quad \mathcal{P}\_{\mathcal{A}}(\rho)=
\sum\_{\Delta,\mu} \Psi\_{\Delta\mu}\mathrm{Tr}(J^{\Delta\mu\dagger}\rho),\qquad 
e^{i\Delta} \mbox{ peripheral spectrum},\ \mu \mbox{ degeneracies}$$
     * $J^{\Delta\mu},\ \Psi_{\Delta\mu}$ can be made biorthogonal:
       $\quad \mathrm{Tr}(J^{\Delta\mu\dagger}\Psi_{\Theta\nu})=\delta_{\Delta\Theta}\delta_{\mu\nu}$.

* **Faithful channels**:   with a faithful invariant state

      >  *Equivalently, $\langle\psi|\mathcal{P}\_{\mathcal E}(|\psi\rangle\langle \psi|)|\psi\rangle> \ne 0$ for all
 $|\psi\rangle$.*
