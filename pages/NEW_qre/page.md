
title: Rényi relative entropy in von Neumann algebras
---


## 1. $\alpha-z$ - Renyi relative entropies

**With: Fumio Hiai, Shinya Kato, Yoshimichi Ueda**   


### Paper versions

* [February 24](NEW_qre/alphaz.pdf) AJ  
* [February 28](NEW_qre/alphaz-1.pdf) FH    
* [my current version](NEW_qre/alphaz-2.pdf) AJ

### Notes

* [My note on DPI](NEW_qre/notes.pdf) November 23, 2023    
* [Kato's note on variational expression](NEW_qre/note_kato.pdf) November 26, 2023    
* [Fumio's note with questions](NEW_qre/note_hiai.pdf) November 29, 2023    
* [Fumio's note with martingale convergence](NEW_qre/note_hiai2.pdf) December 2, 2023    
* [My notes on $\alpha-z$](NEW_qre/notes2.pdf) December 7, 2023      
* [Fumio's note with monotonicity in $z$](NEW_qre/note_hiai3.pdf) December 3-8, 2023    
* [My note on the limit $\alpha\searrow 1$](NEW_qre/notes3.pdf) December 19, 2023    
* [Fumio's note on the limits $\alpha\to 1$](NEW_qre/note_hiai5.pdf) December 23, 2023    
* [Fumio's note on $\lim_{\alpha\searrow 1}$, ${1/2 < z<1}$](NEW_qre/note_hiai4.pdf) December 27, 2023    
* [My note on sufficiency and DPI, $\alpha>1$](NEW_qre/notes4.pdf) December 30, 2023    
* [Fumio's note on monotonicity in $\alpha$](NEW_qre/note_hiai6.pdf) December 31, 2023   
* [Fumio's note on monotonicity in $\alpha$, finite dimensional case](NEW_qre/note_hiai7.pdf) January 6, 2024    
* [My note on monotonicity in $\alpha$](NEW_qre/notes5.pdf) January 10, 2024    
* [Fumio's note on monotonicity in $\alpha\in (0,1)$](NEW_qre/note_hiai8.pdf) January 12, 2024    
* [My notes on monotonicity in $z$ for $1<\alpha\le 2z$](NEW_qre/notes6.pdf)  January 18 (<span style=color:red> mistake! </span>)    
* [My notes on monotonicity in $z$, $\alpha$ and the limit $\alpha\searrow 1$](NEW_qre/notes7.pdf) January 23    
* [Fumio's note on equality in DPI, $\alpha<1$](NEW_qre/note_hiai9.pdf) (2/21/2024)     
* [Fumio's note on variational expression, $\alpha>1](NEW_qre/note_hiai10.pdf) (2/26/2024)    


### Questions

1. *Variational expressions*: solved for $\alpha<1$ and $1<\alpha\le 2z$ in [kato2023onrenyi](kato2023onrenyi) and  [Kato Nov. 26](NEW_qre/note_kato.pdf)    
1. *DPI*: solved in [kato2023onrenyi](kato2023onrenyi) and [Anna Nov. 23](NEW_qre/notes.pdf)    
1. *Martingale convergence*: solved in [Fumio Dec. 2](NEW_qre/note_hiai2.pdf) and a remark in [Anna Dec. 7](NEW_qre/notes2.pdf)    
1. *Monotonicity in $z$*:

    - solved for $\alpha<1$ in [kato2023onrenyi](kato2023onrenyi).     
    - For $\alpha>1$, solved for finite von Neumann algebras in [Fumio Dec. 3-8](NEW_qre/note_hiai3.pdf). In the general case, the use of Haagerup reduction still needs the restriction $\max\{\alpha/2,\alpha-1\}\le z\le\alpha$, then monotonicity holds for $z\le z'$, this is discussed in [Fumio Dec. 3-8](NEW_qre/note_hiai3.pdf), [Anna Dec. 19](NEW_qre/notes3.pdf)    
    - <span style='color:green'> Try to improve this using the variational formulas? </span> - <span style='color:red'> does not work outside the DPI bounds!</span>    
    - <span style='color:green'> Try using complex interpolation as in monotonicity in $\alpha$. Hm? </span> Done in [Anna Jan. 18](NEW_qre/notes6.pdf)    

1. *The limit $\alpha\nearrow 1$*:  solved for all $z> 0$, [Fumio Dec. 3-8](NEW_qre/note_hiai3.pdf), [Anna Dec. 7](NEW_qre/notes2.pdf)   
1. *The limit $\alpha\searrow 1$*: 

    - solved for $z\ge 1$ in  [Fumio Dec. 3-8](NEW_qre/note_hiai3.pdf), [Fumio Dec. 23](NEW_qre/note_hiai5.pdf), [Anna Dec. 19](NEW_qre/notes3.pdf).     
    - The case $1/2< z<1$ solved in [Fumio Dec. 27](NEW_qre/note_hiai4.pdf) under the restrictions $\lambda^{-1}\varphi\le \psi\le \lambda\varphi$ for some $\lambda>0$, using state perturbation theory (in fact, analyticity of the Connes cocycle). Can we extend this to $\psi\le\lambda\varphi$?     
    - <span style='color:green'> Can we prove this for $z=\alpha/2$ (the left Kosaki $L_p$-spaces)? The result would follow.</span>   

1. *Monotonicity in $\alpha$*: 
    
    - proved for $1<\alpha\le2z$ in [Fumio Dec. 31](NEW_qre/note_hiai6.pdf) + a further note on the reiteration theorem  theory using the paper [cwikel1978complex](cwikel1978complex) (also Pisier book on Hardy spaces?)     
    - proved for $\alpha\in (0,1)$, $z>0$ using [fack1986generalized](fack1986generalized). For  $z>1/2$ proved using complex interpolation [Anna Jan. 10](NEW_qre/notes5.pdf).     
    - In finite dimensional case, proved for all values of $\alpha$ and $z$ in [Fumio Jan. 6](NEW_qre/note_hiai7.pdf)    
    - <span style='color:green'> Can we extend values of $\alpha$ and $z$ using complex interpolation for $p<1$ as in [gu2019interpolation](gu2019interpolation)?</span>

1. *Reversibility and DPI equality*

    - proved for $\alpha>1$, $z$ in DPI bounds in [Anna Dec. 30](NEW_qre/notes4.pdf)    
    - <span style='color:green'> Try the case $\alpha<1$ using the variational formula, as in [jencova2021renyi](jencova2021renyi) </span>



### References

Finite dimensional

* [audenaert2015alpha](audenaert2015alpha) introduction of $\alpha-z$-Renyi relative entropies    
* [lin2015investigating](lin2015investigating) limit to 1, derivative at 1    
* [zhang2020fromwyd](zhang2020fromwyd) proof of DPI in bounds       

The $B(\mathcal H)$ case

* [mosonyi2023thestrong](mosonyi2023thestrong)


In von Neumann algebras:

* [kato2023onrenyi](kato2023onrenyi) $\alpha-z$ Renyi divergences in von Neumann algebra setting    
* [kato2023aremark](kato2023aremark) tensor product of Haagerup $L_p$-spaces    
* [gu2019interpolation](gu2019interpolation) interpolation of Haagerup $L_p$-spaces for $p<1$.    
* [berta2018renyi](berta2018renyi) sandwiched Renyi divergence via Araki-Masuda $L_p$-spaces    
* [BOOK_hiai2021quantum](BOOK_hiai2021quantum) Hiai's book on quantum divergences     
* [hiai2018quantum](hiai2018quantum) Hiai's paper on standard divergences    

Tools

* [BOOK_bergh1976interpolation](BOOK_bergh1976interpolation)   interpolation theory    
* [calderon1964intermediate](calderon1964intermediate) complex interpolation method    
* [cwikel1978complex](cwikel1978complex)  reiteration theorem     
* [kosaki1984applications](kosaki1984applications), [kosaki1984applicationsuc](kosaki1984applicationsuc) noncommutative $L_p$-spaces   
* [terp1981lpspaces](terp1981lpspaces) Haagerup $L_p$-spaces   
* [haagerup1979lpspaces](haagerup1979lpspaces) Haagerup $L_p$-spaces    
* [fack1986generalized](fack1986generalized) measurable operators   
* [haagerup2010areduction](haagerup2010areduction) Haagerup reduction theorem   
* [junge2003noncommutative](junge2003noncommutative) conditional expectations extended to Haagerup $L_p$-spaces   
* [BOOK_ohya1993quantum](BOOK_ohya1993quantum) quantum entropy and its use     
* [choi1974aschwarz](choi1974aschwarz)   Choi inequality   
* [zalinesco2002convex](BOOK_zalinescu2002convex) Uniform convexity and smoothness...

General von Neumann algebra theory

* [BOOK_takesaki123theory](BOOK_takesaki123theory)






Myown 

* [jencova2021renyi](jencova2021renyi) sandwiched Rényi rel. entropies, $1/2\le \alpha<1$  
* [jencova2018renyi](jencova2018renyi) sandwiched Rényi rel. entropies, $\alpha>1$           
* [jencova2017preservation](jencova2017preservation) sandwiched RRE and sufficiency, $\alpha>1$  (matrix algebras)    
* [jencova2006sufficiencyfirst](jencova2006sufficiencyfirst) with D. Petz, sufficiency     
* [jencova2006sufficiency](jencova2006sufficiency) with D. Petz, sufficiency, review with examples2
     


---


## Further topics



### Operational interpretation of  Rényi divergence (infinite dimensions)



* [mosonyi2014strongconverse](mosonyi2014strongconverse) operational interpretation (strong converse) for $\alpha>1$, finite dimension     
* [mosonyi2023thestrong](mosonyi2023thestrong) strong converse, infinite dimensional (type I)    
* [hiai2021quantum](hiai2021quantum) strong converse, injective von Neumann algebras




### Approximate sufficiency (recoverability)

* [wilde2015recoverability](wilde2015recoverability) recoverability via RED and interpolation (finite dimensional)
* [sutter2016strengthened](sutter2016strengthened) recoverability via pinching map (finite dim)    
* [junge2018universal](junge2018universal) recoverability via RED and interpolation, universal recovery map (finite dim)    
* [faulkner2022approximate2](faulkner2022approximate2) approximate sufficiency for 2-positive (von Neumann)
* [faulkner2022approximate](faulkner2022approximate) approximate sufficiency for subalgebras (von Neumann)   


(RED- relative entropy difference)

### Petz

* [petz1985quasi](petz1985quasi) quasi entropies, (von Neumann)    
* [petz1986quasi](petz1986quasi) quasi entropies (finite dim)    
* [petz1986sufficient](petz1986sufficient) sufficient subalgebras and relative entropy (von Neumann)    
* [petz1988sufficiency](petz1988sufficiency) sufficient channels, petz dual  (von Neumann)   





