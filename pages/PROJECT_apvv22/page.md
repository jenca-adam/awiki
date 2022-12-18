
title: APVV project 2022
---

*  **Description:**  Priprava na APVV projekt    
*  **People:**  M. Ziman, M. Sedlak, Levi (?), ??     

---

## Topics

* **nonclassicality**: incompatibility, steering, entanglement, contextuality ?    
* **no-go**: no-cloning, no-broadcasting, no-information without disturbance, no-free coffee    
* **relations between the above**: in quantum, in GPTs - relation to the convex structure (no-simplex?), quantifications of non-simplexness?      
* **role in discrimination tasks**: (or other tasks)
* **in quantum**: states, measurements, channels,  testers, higher order maps - characterizations, descriptions, operational (games),     
* **higher order maps**: monoidal structures?, discrimination tasks??, resource theories??, noncausality (switch)??

---

## Causality

### Indefinite causal structure

* [chiribella2013quantum](chiribella2013quantum)     
     - product channels -> no-signalling channels (affine combinations of product channels)    
     - supermaps on no-signaling channels    
     - the **switch**: map $\mathcal S$ of the form $NS(AB\to A'B')\to Chan(CQ\to C')$, where $A,A',B,B',C,C',Q$ are qubits:
     for qubit channels $\mathcal A\in Chan(A\to A')$, $\mathcal B\in Chan(B\to B')$:
     $$
(\mathcal A\otimes \mathcal B)\mapsto \mathcal B\circ\mathcal A\circ(id\_C\otimes \langle 0|\_Q\, \cdot \, |0\rangle\_Q) +
\mathcal A\circ\mathcal B\circ(id\_C\otimes \langle 1|\_Q\, \cdot \, |1\rangle\_Q)
     $$     
     - this is a HOM, but cannot be realized as a quantum circuit (comb)     
     - the Choi matrix of $\mathcal S$: $C_{\mathcal S}=|0\rangle\langle 0|\otimes Z_0+|1\rangle\langle 1|\otimes Z_1$, where
     ($E=C_{id}$):
     $$
Z\_0=E_{C'B'}\otimes E_{BA'}\otimes E_{CA},\qquad Z\_1=E_{C'A'}\otimes E_{AB'}\otimes E_{CB}
     $$
     
     - **Quantum switch**: if $\mathcal A$ has Kraus operators $A_i$ and $\mathcal B$ has Kraus operators $B_j$, we can define a map with Kraus operators 
$$
W_{ij}=|0\rangle\_Q\langle 0|\_Q \otimes A\_i\otimes B\_j+|1\rangle\_Q\langle 1|\_Q\otimes B\_j\otimes A\_i
$$

* [chiribella2016optimal](chiribella2016optimal)  optimizing quantum networks, causal and not causal    
- basically - base sections and duality, max entropy    
- tasks: 



----
## Basic references

[compatibility references](CIT_compatibility)

* compatibility of channels:     
    - 
* contextuality and entanglement: [plavala2022contextuality](plavala2022contextuality), [plavala2022incompatibility](plavala2022incompatibility)
* contextuality and discrimination:     
* entanglement and metrology?: 



---

## Research



### Notes



### Todo



### Ideas

---

## Finished

### Papers


### Talks/posters

---

## Ideas for further research

