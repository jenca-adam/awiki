title: guerini2017operational
---

## Reference

Leonardo Guerini, Jessica Bavaresco, Marcelo Terra Cunha, Antonio Acín, Operational framework for quantum measurement
simulability, ournal of Mathematical Physics 58, 092102 (2017)


[arxiv:1705.06343](https://arxiv.org/abs/1705.06343)



## Contents

Simulability of a quantum measurement (POVM) $A$ by a set $\mathcal B=\\{B^{(j)}\\}$ of POVMs (finite dimensional, finite outcomes) 

* **Classical manipulations** of a set $\\{B^{(j)}\\}$ of POVMs consist of
    * pre-processing (mixing): choice of some POVM $B^{(j)}$ with probability $p(j)$
    * post-processing (relabelling): by conditional probabilities $q(i|j,i)$
* $A$ is **$\mathcal B$-simulable** if it can be obtained by classical manipulations from $\mathcal B$

* Robustness: $\max\\{t\in [0,1],\ tA+(1-t)\mathrm{Tr}(A)/d I\mbox{ is }\mathcal B-\mbox{simulable}\\}$ 
* Simulability of a set of POVMs by a single measurement: **joint measurability** (compatibility)
    * robustness - usual 
    * SDP
* Simulability by $k$- POVMs: $k$-POVM simulability
    * **Prop.1**: If $\\{A^{(j)}\\}$ is $\mathcal B$-measurable and all $A^{(j)}$ have the same pre-processing step
      $p(j)$, then $\\{A^{(j)}\\}$ is jointly measurable
    * A qubit example: 4 projective qubit measurements, various notions of simulability and joint measurability are
      compared
* Simulability by a set of POVMS with $k$ outcomes: $k$-outcome simulability
    * the number of simulators is not restricted - can always assume *deterministic* post-processings
    * **Lemma 2**: An $n$-outcome POVM $A$ is $k$-outcome simulable iff there are at most $\begin{pmatrix} n\\\
      k\end{pmatrix}$ POVMs $B^{(j)}$, with at most $k$ nonzero effects such that 
      $$
A=\sum_j p_j B^{(j)}
      $$
    one $B^{(j)}$ for each possible choice of $k$-nonzero effects among $n$.
    * Example: tetrahedral qubit measurement: $A_i=(I+v_i\sigma)$, $v_i\in \mathbb R^3$ form the vertices of a regular
      tetrahedron.
    * relation of $k$-outcome simulability to joint measurability: $A, pI$ have a joint measurement with 'many zeros'
    * antipodal measurements
* **projective-simulabilility** simulability by a set of PVMs:
    $ every 2-outcome measurement is PS
    * **Thm. 1**: A qubit POVM $A$ is projective-simulable iff $A$, $\tilde A$ are jointly measurable, $\tilde A$
      antipodal
* Measurement simulability as a **resource theory**: for any type of simulators
    * free objects: sets of POVMs of the given type and simulable from them
    * free operations: classical processing
    * simulability is transitive (**Prop. 4**) so it works
    * resource quantifiers: white noise robustness: monotone w.r. to classical processings (**Prop. 5**)
    
