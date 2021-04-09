title: TQC 2021 
---


* [link]()    

* Duty: program committee    
* deadline: 20.4.2021


### Papers:

* **Resource theories**

    1.   Gilad Gour and Carlo Maria Scandolo. Dynamical entanglement (4) 


         In this contribution, dynamical entanglement, that is, entanglement of bipartite channels, is studied as a
dynamical resource theory. A family of resource measures is defined that completely characterizes bipartite channel
simulation under LOCC. A partial transpose superchannel is introduced to define the dynamical NPT entanglement and 
computable measures are obtained, in particular the max-logarithmic negativity that has an operational interpretation
as the exact asymptotic dynamical entanglement cost under PPT superchannels. Finally, it is proved that no entanglement
can be distilled from a PPT channel, not even if adaptive schemes are used.    

         This is a timely contribution in the recently fast developing field of dynamical resource theories. It is
concentrated on the PPT entanglement which is more tractable and not so complicated as considering LOCC superchannels or
combs. Nevertheless, it brings numerous open questions and  research directions, certainly of interest for the audience, 
in dynamical resource theories but also in entanglement theory of states.    

         [gour2019theentanglement](gour2019theentanglement), [gour2020dynamical](gour2020dynamical)   
     

         **score:2**    



    2.   Ryuji Takagi. Optimal resource cost for error mitigation (57)


         The results on resource theories for quantum channels are applied to the problem of the optimal cost of
probabilistic error cancellation method. The main idea is to view the set of implementable channels as free resources
in a convex quantum resource theory. The optimal cost, obtained from optimal linear decomposition in terms of
implementable devices, is then directly related to the standard robustness measure and
one can use the tools of convex resource theories. As a result, the exact cost is computed in some cases and lower and
upper bounds are provided for more general noise models.

         
         This is a nice application of robustness measure in the setting of error mitigation, however, the results are close to submission (155) and could be included in it (the authors of (155) include the present author). Therefore my suggestion is to reject.

         **score:-2**

         [arxiv:2006.12509](https://arxiv.org/abs/2006.12509)

    3.   Bartosz Regula, Ludovico Lami, Giovanni Ferrari and Ryuji Takagi. Operational quantification of  infinite-dimensional resources in quantum mechanics and beyond (85)

         The robustness measure of finite dimensional resource theories is extended to infinite dimensional systems. In particular, it is proved that it provides a faithful resource monotone in any infinite dimensional convex resource theory. It is shown that the robustness represents the advantage of the given state in channel discrimination tasks over the set of free states. Convex duality is used to obtain an alternative expression, showing that if finite, robustness can be evaluated by measuring a suitable observable. Moreover, conditions for strong duality are given. The results are applied to several important  continuous variable resource theories.

         In this contribution, some of the technical problems are solved that need to be tackled before continuous
variable resource theories can be treated in an unified manner. This is an important step towards this goal. However,
given the rather technical nature of this contribution and the high acceptance level at TQC, I do not support it for
a talk.

         [arxiv:2009.11313](https://arxiv.org/abs/2009.11313), [arxiv:2009.11302](https://arxiv.org/abs/2009.11302)
	

         **score:-1** 

    1.   Bartosz Regula, Ryuji Takagi and Mile Gu. Operational applications of the diamond norm and related measures in quantifying the non-physicality of quantum maps (155)

         A non-physical map is Hermitian and possibly trace preserving, but not completely positive. This submission
considers the problem of simulating such a map by physically implementable, i.e. cptp, maps. The results are as follows:

         - robustness measures R, R' are defined and it is proved that they are related to the diamond norm and have  an operational characterization.
         - The authors propose an interesting method for the simulation: the map in question is written as Phi(.)= Lambda( .\otimes X), where Lambda is a cptp map and X is a Hermitian operator with unit trace. The simulation uses a quasiprobability representation of X, while the channel Lambda remains fixed. This has some advantage over the standard approach, where a number of different operations has to be realized.
         - The simulation cost, evaluated as the trace norm of X, is proved to be exactly given by the robustness measure R. It is also proved that the robustness R' characterizes the advantage of Phi over all physical maps in certain quantum games.
         - Applications include simulation of positive maps, evaluating the non-Markovianity of an evolution and cost of error mitigation. The author prove some advantages of their methods over existing ones in some cases and show that the
measures can be efficiently computed by SDP.

         The robustness-like measures were studied before for different problems in resource theories and elwewhere. This is another application, where the robustness has similar properties and interpretations. The relation to the diamond norm is not really surprising, given the well known fact that the diamond norm coincides with the base norm on the subspace generated by quantum channels.  This a neat contribution, with some nontrivial ideas and interesting results. I especially like the idea of pushing the non-physicality to the ancilla, I wonder whether this technique is really new. There is another submission applying a similar measure to non-cp maps, so there seems to be some competition, but this suggests that the fruit was not hanging too high. 


         [REF_regula2021](REF_regula2021)

         **score:0**

* **Quantum state/channel discrimination/estimation**

    1.   Jessica Bavaresco, Mio Murao and Marco Túlio Quintino. Strict hierarchy between parallel, sequential, and indefinite-causal-order strategies for channel discrimination (5)

         Two new contributions to the problem of quantum channel discrimination are presented:

         - new strategies for discrimination using n-copies of the channel are introduced - called 
separable and general. In contrast to the parallel and sequential strategies, the new strategies involve an indefinite
causal order
         - a strict hierarchy of the four types of strategies is presented on the example of 2 copies of pairs of qubit channels: amplitude damping and bit-flip, with appropriate parameters.

         To compute the success probabilities, a unified formalism of quantum testers is developed describing the
different classes of strategies, the optimal probability P^S for each class S of strategies is computable by SDP. A method is developed to obtain exact bounds on P^S from numerical results. (The authors call this ''computer assisted proof'', but 
that expression means something different).

         This is an important step in the problem of quantum channel discrimination, but it is not clear whether this is the first time indefinite causal order strategies were considered. The established strict hierarchy is interesting,
especially that it shows that the strategies with indefinite causal order have a more complicated and intriguing structure.However, not much further insight is gained and the methods for computing the bounds may be useful but quite technical. Given the acceptance rate at TQC, I recommend that this contribution is presented as a poster.


         [arxiv:2011.08300](https://arxiv.org/abs/2011.08300)


         **score: -1**

    1.   Simon Becker, Nilanjana Datta, Ludovico Lami and Cambyse Rouze. Energy-constrained discrimination of unitaries, quantum speed limits and a Gaussian Solovay--Kitaev theorem (96)

         The problem of discrimination of unitary channels is considered in the energy constrained (EC) setting of continuous variable systems, where only the energy of the input states is constrained. Basic results known for finite dimensional
systems are extended to this setting:

         - no entanglement is needed in discrimination of unitaries
         - perfect discrimination is possible in a finite number of rounds at some energy level

         Using these results, a new kind of EC speed limit is obtained, quantifying the speed at which two time evolutions (under some reasonable constraints) drift apart in time. Furthermore, a version of the Solovay-Kitaev theorem for Gaussian
unitaries is obtained, showing that any such unitary can be approximated by a reasonably short sequence of Gaussian
unitaries from some base set.

         Studying these problems in the proposed setting is well motivated and highly relevant. The extensions from the
finite dimensional setting are rather nontrivial and technically involved, although the results and the basic ideas are similar. This could be a nice talk for TQC.

         [arxiv:2006.06659](https://arxiv.org/abs/2006.06659)

         **score:1**


    1.   Farzin Salek, Masahito Hayashi and Andreas Winter. When are Adaptive Strategies in Asymptotic Quantum Channel Discrimination Useful? (229)

         Various adaptive and parallel strategies for quantum channel discrimination are compared in the asymptotic regime: parallel strategies with or without quantum memory, adaptive strategies with only classical feed-forward with or without entangled inputs, or general sequential strategies. There seem to be two main results:

         - it is shown that the non adaptive  vs. adaptive separation in the well known example of Harrow et al. is present also in the symmetric asymptotic setting, thus completing the previously obtained non-asymptotic and asymmetric results
         - in the case of classical-quantum channels, it is proved that the adaptive strategies bring no advantage in
both symmetric and asymmetric settings. This is done by relating to the problem of classical channel discrimination.

         The previous result is applied to show that adaptive strategies with only classical feed-forward and product inputs do not offer any advantage in the asymptotic settings. As an application, the discrimination power of quantum channels is investigated.

         These are interesting results, but not really unexpected. Discrimination of cq-channels is somewhat close to discrimination of states and adaptive strategies do not seem to offer much power. Likewise, it is not surprising that adaptive strategies with only classical memory effects do not bring any advantage. This contribution undoubtedly has its merits and fills some gaps in the theory of asymptotic  quantum channel discrimination, however, it might be not strong enough for a talk.

         [arxiv:2011.06569](https://arxiv.org/abs/2011.06569)

         **score:-1**


    1.   Vishal Katariya and Mark Wilde. RLD Fisher Information Bound for Multiparameter Estimation of Quantum Channels (72)

         A Cramer-Rao bound for multiparameter estimation of quantum channels is given, in terms of the RLD Fisher
information. The bound applies to all quantum channels and all sequential strategies. Moreover, it is single-letter and can be efficiently computed by SDP. The result is proved using a chain rule for the RLD Fisher information, which can be applied to prove an amortization collapse. This means that the sequential strategies have no advantage over parallel ones for the RLD Fisher information of n channel uses. The obtained CR bound has the important consequence that if the Fisher information is finite, then the Heisenberg scaling of the mean square error is unattainable. 

         The results of this contribution are of fundamental importance, giving an effectively computable CR bound and
providing conditions under which advantages over the fundamental limit with classical resources are attainable for
quantum channel estimation. I strongly support acceptance to TQC.


         **score:3**


         [arxiv:2008.11178](https://arxiv.org/abs/2008.11178)

    1.   Milán Mosonyi, Zsombor Szilágyi and Mihály Weiner. On the error exponents of binary quantum state discrimination with composite hypotheses (162)

         Error exponents for the binary quantum hypothesis testing in the asymptotic iid setting are considered, for composite null and alternative hypothesis. The error exponent (Chernoff, Stein or direct) is upper bounded by the worst-case error exponent over all pairs and it is known that there are cases when this bound is attainable and cases when it is not. The main contributions are that there are instances when the worst-case exponents are not attainable:

         - already in the simple case when the null hypothesis is simple and the alternative consists of two states.
           Such examples are constructed for all types of exponents, using inequalities for operator means,
         - even for commuting states (i.e. in the classical case), on an infinite dimensional system and with countably infinite alternative.

         It is further proved that the worst-case exponents are attainable in some specific cases (semi-classical and
when both hypotheses consist of finite sets of pure states).

         This question is of importance since if the worst-case exponents are attainable, the error exponents have an
explicit expression in terms of divergence distances of the two hypotheses. This contribution provides evidence that
this happens much less frequently than previously thought. This is certainly a material for a nice talk, but the TQC
acceptance level is high and the impact of this contribution is limited.


         [arxiv:2011.04645](https://arxiv.org/abs/2011.04645)

         **score:-1**


* **Combs, superchannels**

    1.   Wataru Yokojima, Marco Túlio Quintino, Akihito Soeda and Mio Murao. Consequences of preserving reversibility in
       quantum superchannels (12)

         Quantum superchannels represent physical transformations that map  causally independent  quantum operations  into a quantum operation. Quantum superchannels are called pure if they transform  unitary channels into a unitary channel. It is proved that a bipartite superchannel (i.e. with two slots) is pure if and only if it is:

         - a quantum comb (causally ordered superchannel) that can be represented as a concatenation of unitary channels
           (without discarding a subsystem)
         - a direct sum of two pure combs (of the above form) with opposite causal order, this is a generalization of
           the quantum switch.

         The relevance of the studied question is in its relation to the purification postulate in Ref. [8]. The conclusion shows that the pure bipartite superchannels have a special form, in particular it suggests that the superchannels with two slots with indefinite causal order are close to the quantum switch. This result is of importance, but with a limited impact for the TQC audience, compared to other contributions.


         **score:-1**


         [arxiv:2003.05682](https://arxiv.org/abs/2003.05682)

    1.   Qingxiuxiong Dong, Marco Túlio Quintino, Akihito Soeda and Mio Murao. Success-or-draw: A strategy allowing
       repeat-until-success in quantum computation (42)

         This contribution gives a construction of a success-or-draw realization of a given probabilistic supermap on unitary channels. Such a realization has a lower success probability but the input state is preserved in the case of a failure, so that it can be reused until success is obtained. The constructed scheme is a quantum comb with 2 slots, using d-copies of the unitary channel (d being the dimension). In the case of unitary inversion, the optimal success probability of such a strategy is computed by SDP.

         This is a very neat idea, of theoretical value but perhaps also in applications. It could be a nice talk, but its impact is limited, compared to other contributions.

         [arxiv:2011.01055](https://arxiv.org/abs/2011.01055)

         **score:-1**

* **Device-independent, self-testing**

    1.   Armin Tavakoli. Semi-device-independent framework based on restricted distrust in prepare-and-measure experiment (15)

         Prepare-and-measure experiments are considered when the measurements are fully uncharacterized and the prepared
states are trusted within a given fidelity with respect to given target states. Numerical methods are proposed to compute 
the lower and upper bounds for maximal quantum correlations obtainable for fixed target states and fidelity bound. The results are applied to some tasks:

         - state discrimination
         - efficiency of detectors
         - non-classicality in the measurements
         - random number generator

         This framework has some advantages over other semi-device independent approaches: there is no bound on the
dimension, the fidelity can be assessed by measurement (in contrast to a restriction on dimension) and the condition has
to be fulfilled only on average over the rounds. So this is a reasonable setting to study. It would be interesting to see whether classical measurements (post-processing of a single projective measurement) could be replaced  by compatibility of measurements (post-processings of a single POVM) in the third point listed above. 

         This is a reasonable proposal for a semi-device independent framework, which has some advantages over existing
ones. The results are interesting, but limited to performances of some particular protocols, which may not be of overall
interest for TQC audience. 
  

         **score:-1**


    1.   Harshank Shrotriya, Kishor Bharti and Leong Chuan Kwek. Robust Self Testing of All Pure Bipartite Maximally Entangled States via Quantum Steering (84)

         A semi-device independent scenario for self-testing of all pure entangled states is proposed, based on quantum steering. An ideal steering assemblage is found that self-tests any pure entangled qudit state.  For maximally entangled states robustness bounds are found.

         The method in the first part resembles the one used in the device-independent setting [17], with tilted steering inequalities instead of tilted CHSH. The second part adopts the methods of [28] where robust assemblage-based self-testing of qubit maximally entangled states is considered. The steering based approach has the advantage over device independent self-testing that exact robustness bounds can be found.

         This is a solid piece of work, largely extending previous results. However, it seems that no really new techniques or methods are introduced here.


         (subreviewer: M. Hoban - no answer?)

         [arxiv:2007.04020](https://arxiv.org/pdf/2007.04020.pdf)
         

         **score:0** 

* **Foundations, Bell inequalities (?)**

    1.   Patricia Contreras Tejada, Giannicola Scarpa, Aleksander M. Kubicki, Adam Brandenburger and Pierfrancesco La Mura. Agreement between observers: a physical principle? (52)

         A new property of no-signaling boxes is introduced, called common certainty of disagreement. This notion is
based on a result from classical probability theory, the classical agreement theorem, which states that two Bayesian agents cannot agree to disagree. The boxes with this property are characterized and it is proved that for local or quantum boxes, common certainty of disagreement is not possible.  A related notion called singular disagreement is introduced and is again proved possible in no-signaling setting, but impossible for local or quantum boxes.

         
         The authors propose some interesting properties of no-signaling boxes, which may serve as  simple tests for quantum correlations. However, the usefulness of such  tests is unclear. There are some almost-quantum correlations that can be ruled out, but others that cannot. There is no further investigation (yet) into performance of such tests and their relations to other properties of no-signaling boxes. So this may be worth of further research, but it is not enough for a talk at TQC.  

  
         **score: -2**

    1. Ravishankar Ramanathan, Michal Banacki, Ricard Rodriguez and Pawel Horodecki. Single trusted qubit is necessary and  sufficient for quantum realisation of extremal no-signaling correlations  (165)


         There are two main results in this paper, related to a no-go theorem stating that extremal nonlocal boxes in a Bell scenario cannot be obtained by quantum correlations:

         - it is proved that this remains true also in the sequential Bell nonlocality framework, where each party
           performs measurements in a sequential manner. This leads to a more complicated time-ordered no-signaling
structure. 

         - in a three party scenario with one trusted party steered by the two other parties, it is shown that  nonlocal extremal assemblages can be obtained from any pure genuine three party entangled state. It was previously known that any bipartite steering assemblage of quantum states can be obtained by quantum steering but there are three party assemblages that cannot be.

         This paper extends and completes previous results, important in device-independent and semi-device independent
quantum cryptography. The structure of the sequential bipartite no-signaling polytope and the three party no-signaling assemblages is also elucidated, which is interesting also for quantum foundations. However, the impact of this work does not match other contributions for TQC.

         [arxiv:2004.14782](https://arxiv.org/abs/2004.14782) 

         **score:-1**



  

* **Continuous variables**

    1.   Giovanni Ferrari, Ludovico Lami, Thomas Theurer and Martin Plenio. Asymptotic state transformations of continuous variable resources (92)


         In this work, upper bounds on transformation rates in resource theories are obtained in the continuous variable
setting. This is done by using resource monotones that satisfy certain properties. In contrast to finite dimensional
systems where asymptotic continuity of the measures is employed, this property is typically not available and has to be
replaced with other suitable properties. The results are applied to resource theories of nonclassicality, quantum
entanglement and quantum thermodynamics, obtaining rigorous bounds on the transformation rates for the first time. In
the case of nonclassicality, new resource measures are introduced, their properties are proved and useful bounds are
provided. 


         The results are strong and fundamental for resource theories in infinite dimensional systems. Three important
applications are demonstrated but the results are widely applicable in the framework of CV systems. I strongly support
acceptance for a talk.
  

         [arxiv:2010.00044](https://arxiv.org/abs/2010.00044)


         **score:3**


    1.   Ludovico Lami. Quantum data hiding with continuous variable systems (238)

         
         In this paper, data hiding is investigated in the continuous variable setting. The results can be divided into
two parts:

         - maximum efficiency of data hiding against LOCC measurements is bounded for states satisfying an energy
           constraint. It is shown that in this case, the energy constraint plays a similar role as the dimension in
finite dimensional schemes. The result is obtained by finding an upper bound on the error induced by a continuous variable teleportation protocol.

         - data hiding against GOCC is studied. An explicit scheme is obtained that achieves data hiding with arbitrary
           efficiency. This scheme is achieved for a single mode system. Two other examples are studied, showing that in
some cases the GOCC measurements are reasonably accurate and no data hiding is present.


         I find these results very interesting and timely, given the recent interest and progress in continuous variable
systems. However, it may have a limited impact given the audience of TQC. Taking into account the high number and
quality of other contribution, I tend to weak accept.


         [arxiv:2102.01100](https://arxiv.org/abs/2102.01100)

         **score:1**
     


* **Relative entropy**

    1.   Nicholas Laracuente. Quasi-factorization and Multiplicative Comparison of Subalgebra-Relative Entropy (209)


         This submission studies the subalgebra-relative entropy. Multiplicative inequalities for perturbations of the subalgebra-relative entropy are obtained. A further result is a multiplicative extension of strong subadditivity for noncommuting conditional expectations: a strong (complete) quasi-factorization is proved, improving on results in [GR21] and extending to an arbitrary finite number of conditional expectations. Applications are shown in entropic uncertainty relations
and the merging of (complete) modified logarithmic Sobolev inequalities.


         It is quite difficult to assess the impact of this contribution, especially from the extended abstract provided
by the author. As presented there (and in the paper), I doubt it could be fully appreciated outside a circle of experts.
The paper extends and improves previous results, but it is not clear what are the really new ideas. So given the
number and quality of other contributions, I think this work is not suitable for a talk at TQC.


         [arxiv:1912.00983](https://arxiv.org/abs/1912.00983)

         **score:-1**
 

* Cojaviem

    1. Seiichiro Tani. Quantum Algorithm for Finding the Optimal Variable Ordering for Binary Decision Diagrams (44)

         (subreviewer: Daniel Nagaj)

    1. Soumya Das, Goutam Paul and Anindya Banerji. Hyper-hybrid entanglement and the fidelity of quantum teleportation
       limit each other (156)

         (subreviewer: Marek Kus)


    1.   Kai Meinerz, Chae-Yeun Park and Simon Trebst. Scalable Neural Decoder for Topological Surface Codes (164)

         In this submission, a decoding algorithm for quantum error correcting codes is proposed. The algorithm consists
of two steps: a preprocessing of local error corrections based on machine learning, and a union-find decoder. It is
demonstrated that the algorithm increases the error threshold and reduces the total decoding time, compared to the UF
algorithm itself.

         The algorithm combines two known approaches and benefits from both. This is clearly an interesting result worth
further investigation, but I am not sure about its significance for the wider audience at TQC.

       

         **score:-1**

  
    1. Angelo Lucia, David Pérez-García and Antonio Pérez-Hernández. Thermalization in Kitaev’s quantum double models
       via Tensor Network techniques (220)


         (subreviewer: B. Brown - no answer ) (subreviewer: A. Gendiar)




