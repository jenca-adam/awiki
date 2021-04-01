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

         This is a timely contribution in the rather new and fast developing field of dynamical resource theories. It is
concentrated on the PPT entanglement which is more tractable and not so complicated as considering LOCC superchannels or
combs. Nevertheless, it brings numerous open questions and  research directions, certainly of interest for the audience, 
in dynamical resource theories but also in entanglement theory of states.    

         [gour2019theentanglement](gour2019theentanglement), [gour2020dynamical](gour2020dynamical)   
     
    2.   Ryuji Takagi. Optimal resource cost for error mitigation (57)


         The results on resource theories for quantum channels are applied to the problem of the optimal cost of
probabilistic error cancellation method. The main idea is to view the set of implementable channels as free resources
in a convex quantum resource theory. The optimal cost, obtained from optimal linear decomposition in terms of
implementable devices, is then directly related to the standard robustness measure and
one can use the tools of convex resource theories. As a result, the exact cost is computed in some cases and lower and
upper bounds are provided for more general noise models.

         The fact that the standard robustness is related to optimal linear decomposition seems known. 
I like the idea of its application in the setting of error mitigation, but I am not sure if the results are strong enough or significant given the high treshold of TQC. Besides, it is somewhat similar to submission (155) (including the present author).

         [arxiv:2006.12509](https://arxiv.org/abs/2006.12509)

    3.   Bartosz Regula, Ludovico Lami, Giovanni Ferrari and Ryuji Takagi. Operational quantification of  infinite-dimensional resources in quantum mechanics and beyond (85)

         The robustness measure of finite dimensional resource theories is extended to infinite dimensional systems. In particular, it is proved that it provides a faithful resource monotone in any infinite dimensional convex resource theory. It is shown that the robustness represents the advantage of the given state in channel discrimination tasks over the set of free states. Convex duality is used to obtain an alternative expression, showing that if finite, robustness can be evaluated by measuring a suitable observable. Moreover, conditions for strong duality are given. The results are applied to several important  continuous variable resource theories.

         In this contribution, some of the technical problems are solved that need to be tackled before continuous
variable resource theories can be treated in an unified manner. This is an important step towards this goal and I
support its acceptance to TQC.

         [arxiv:2009.11313](https://arxiv.org/abs/2009.11313), [arxiv:2009.11302](https://arxiv.org/abs/2009.11302)
	

    1.   Bartosz Regula, Ryuji Takagi and Mile Gu. Operational applications of the diamond norm and related measures in quantifying the non-physicality of quantum maps (155)

         A non-physical map is Hermitian and possibly trace preserving, but not completely positive. This submission
considers the problem of simulating such a map by physically implementable, i.e. cptp, maps. The results are as follows:

         - robustness measures R, R' are defined and it is proved that they are related to the diamond norm and have  an operational characterization.
         - The authors propose an interesting method for the simulation: the map in question is written as Phi(.)= Lambda( .\otimes X), where Lambda is a cptp map and X is a Hermitian operator with unit trace. The simulation uses a quasiprobability representation of X, while the channel Lambda remains fixed. This has some advantage over the standard approach, where a number of different operations has to be realized.
         - The simulation cost, evauated as the trace norm of X, is proved to be exactly given by the robustness measure R. It is also proved that the robustness R' characterizes the advantage of Phi over all physical maps in certain quantum games.
         - Applications include simulation of positive maps, evaluating the non-Markovianity of an evolution and cost of error mitigation. The author prove some advantages of their methods over existing ones in some cases and show that the
measures can be efficiently computed by SDP.

         This is a neat contribution, with some interesting results. However, there seem to be other sumbissions concerned with similar problems and ideas. Given this fact and the high treshold in TQC, I tend to only weak accept.

         [REF_regula2021](REF_regula2021)

* **Quantum state/channel discrimination/estimation**

    1.   Jessica Bavaresco, Mio Murao and Marco Túlio Quintino. Strict hierarchy between parallel, sequential, and indefinite-causal-order strategies for channel discrimination (5)

         Two new contributions to the problem of quantum channel discrimination are presented:

         - new strategies for discrimination using n-copies of the channel are introduced - called 
separable and general. In contrast to the parallel and sequential strategies, the new strategies involve an indefinite
causal order
         - a strict hierarchy of the four types of strategies is presented on the example of 2 copies of pairs of qubit channels: amplitude damping and bit-flip, with appropriate parameters.

         To compute the success probabilities, a unified formalism of quantum testers is developed describing the
different classes of strategies, the optimal probability P^S for each class S of strategies is computable by SDP. A method is developed to obtain exact bounds on P^s from numerical results. (The authors call this ''computer assisted proof'', but 
that expression means something different).

         This is an important step in the problem of quantum channel discrimination, but it is not clear whether this is the first time indefinite causal order strategies were considered. The established strict hierarchy is interesting,
especially that it shows that the separable strategies are more than just a convex combination of (differently ordered)
sequetial ones. This shows that the structure of the general strategies is quite complicated and intriguing, however,
not much further insight is obtained.

         [arxiv:2011.08300](https://arxiv.org/abs/2011.08300)

    1.   Simon Becker, Nilanjana Datta, Ludovico Lami and Cambyse Rouze. Energy-constrained discrimination of unitaries, quantum speed limits and a Gaussian Solovay--Kitaev theorem (96)

         The problem of discrmination of unitary channels is considered in the energy constrained (EC) setting of continuous variable systems, where only the energy of the input states is constrained. Basic results known for finite dimensional
systems are extended to this setting:

         - no entanglement is needed in discrimination of unitaries
         - perfect discrimination is possible in a finite number of rounds at some energy level

         Using these results, a new kind of EC speed limit is obtained, quantifying the speed at which two time evolutions (under some reasobable constraints) drift apart in time. Furthermore, a version of the Solovay-Kitaev theorem for Gaussian
unitaries is obtained, showing that any such unitary can be approximated by a reasonably short sequence of Gaussian
unitaries from some base set.

         Studying these problems in the proposed seting is well motivated and highly relevant. The extensions from the
finite dmensional setting are rather nontrivial and technically involved, although the results and the basic ideas are similar. This would be a nice talk for TQC.

         [arxiv:2006.06659](https://arxiv.org/abs/2006.06659)


    1.   Farzin Salek, Masahito Hayashi and Andreas Winter. When are Adaptive Strategies in Asymptotic Quantum Channel Discrimination Useful? (229)

         Various adaptive and parallel strategies for quantum channel discrimination are compared in the asymptotic regime: parallel strategies with or without quantum memory, adaptive strategies with only classical feed-forward with or without entangled inputs or general sequential strategies. There seem to be two main results:

         - it is shown that the non adaptive  vs. adaptive separation in the well known example of Harrow et al. is present also in the symmetric asymptotic setting, thus completing the previously obtained non-asymptotic and asymetric results
         - in the case of classical-quantum channels, it is proved that the adaptive strategies bring no advantage in
both symmetric and asymetric settings. This is done by relating to the problem of classical channel discrimination.

         The previous result is applied to show that adaptive strategies with only classical feed-forward and product inputs do not offer any advantage in the asymptotic settings. As an application, the discrimination power of quantum channels is investigated.

         These are interesting results, but not really unexpected. Discrimination of cq-channels is somewhat close to discrimination of states and adaptive strategies do not seem to offer much power. Likewise, it is not surprising that adaptive strategies with only classical memory effects do not bring any advantage. This contribution has its merits and fills some gaps in the theory of asymptotic  quantum channel discrimination, however, it might be not strong enough.

         [arxiv:2011.06569](https://arxiv.org/abs/2011.06569)


    1.   Vishal Katariya and Mark Wilde. RLD Fisher Information Bound for Multiparameter Estimation of Quantum Channels (72)

         A Cramer-Rao bound for multiparameter estimation of quantum channels is given, in terms of the RLD Fisher
informaton. The bound applies to all quantum channels and all sequential strategies. Moreover, it is single-letter and can be efficiently computed by SDP. The result is proved using a chain rule for the RLD Fisher information, which can be applied to prove an amortization collapse. This means that the sequential strategies have no advantage over paralel ones for the RLD Fisher information of n channel uses. The obtained CR bound has the important consequence that if the Fisher information is finite, then the Heisenberg scaling of the mean square error is unattainable. 

         The results of this contribution are of fundamental importance, giving an effectively computable CR bound and
providing conditions under which advantages over the fundamental limit with classical resources are attainable for
quantum channel estimation. I strongly support acceptance to TQC.

         [arxiv:2008.11178](https://arxiv.org/abs/2008.11178)

    1.   Milán Mosonyi, Zsombor Szilágyi and Mihály Weiner. On the error exponents of binary quantum state discrimination with composite hypotheses (162)

         Error exponents for the binary quantum hypothesis testing in the asymptotic iid setting are considered, for composite null and alternative hypothesis. The error exponent (Chernoff, Stein or direct) is upper bounded by the worst-case error exponent over all pairs and it is known that there are cases when this bound is attainable and cases when it is not. The main contributions are that there are instances when the worst-case exponents are not attainable:

         - already in the simple case when the null hypothesis is simple and the alternative consists of two states
         - even for commuting states (i.e. in the classical case), on an infinite dimensional system and with countably infinite alternative.

         It is further proved that the worst-case exponents are attainable in some specific cases (semi-classical and
when both hypotheses consist of finite sets of pure states).

         This question is of importance since if the worst-case exponents are attainable, the error exponents have an
explicit expression in terms of divergence distances of the two hypotheses. This contribution provides some further
information and seems to indicate that this perhaps  happens less frequently than previously thought. This could be a nice talk, although the results are not very strong.

         [arxiv:2011.04645](https://arxiv.org/abs/2011.04645)



* **Combs, superchannels**

    1.   Wataru Yokojima, Marco Túlio Quintino, Akihito Soeda and Mio Murao. Consequences of preserving reversibility in
       quantum superchannels (12)

         Quantum superchannels represent physical transformations that map  causally independent  quantum operations  into a quantum operation. Quantum superchannels are called pure if they transform  unitary channels into a unitary channel. It is proved that a bipartite superchannel (i.e. with two slots) is pure if and only if it is:

         - a quantum comb (causally ordered superchannel) that can be represented as a concatenation of unitary channels
           (without discarding a subsystem)
         - a direct sum of two pure combs (of the above form) with opposite causal order, this is a generalization of
           the quantum switch.

         The relevance of the studied question is in its relation to the purification postulate in Ref. [8]. The conclusion shows that the pure bipartite superchannels have a special form and a similar physical interpretation as the quantum switch. This result is of interest, but I am not sure that it is significant enough to meet the standards of TQC.

         [arxiv:2003.05682](https://arxiv.org/abs/2003.05682)

    1.   Qingxiuxiong Dong, Marco Túlio Quintino, Akihito Soeda and Mio Murao. Success-or-draw: A strategy allowing
       repeat-until-success in quantum computation (42)

         A construction of a success-or-draw realization of a given probabilistic supermap on unitary channels. Such a
realization has a lower success probability but the input state is preserved in the case of a failure, so that it can be
reused until success is obtained. The constructed scheme is a quantum comb with 2 slots, using d-copies of the unitary
channel (d being the dimension). In the case of unitary inversion, the optimal success probability of such a strategy is
computed by SDP.

         This is a very neat idea, of theoretical value but perhaps also in applications. It could be a nice talk for TQC.

         [arxiv:2011.01055](https://arxiv.org/abs/2011.01055)


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
to be fullfilled only on average over the rounds. So this is a reasonable setting to study. This idea seems similar to smooth entropies, especially the smooth min-entropy in the case of state discrimination. It would be interesting to know whether these settings are related. Another question is whether classical measurements (post-processing of a single projective measurement) could be replaced  by compatibility of measurements (post-processings of a single POVM) in the third point listed above. 

         This is a reasonable proposal for a semi-device independent framework, which has some advantages over existing
ones. The results are interesting, but limited to performances of some particular protocols, which may not be of overal
interest for TQC audience.
  


    1.   Harshank Shrotriya, Kishor Bharti and Leong Chuan Kwek. Robust Self Testing of All Pure Bipartite Maximally Entangled States via Quantum Steering (84)

         A semi-device independent scenario for self-testing of all pure entangled states is proposed, based on quantum steering. An ideal steering assemblage is found that self-tests any pure entangled qudit state.  For maximally entangled states robustness bounds are found.

         The method in the first part resembles the one used in the device-independent setting [17], with tilted steering inequalities instead of tilted CHSH. The second part adopts the methods of [28] where robust asemblage-based self-testing of qubit maximally entangled states is considered. The steering based approach has the advantage over device independent self-testing that exact robustness bounds can be found.

         This is a solid piece of work, largerly extending previous results. However, it seems that no really new techniques or methods are introduced here.

         [arxiv:2007.04020](https://arxiv.org/pdf/2007.04020.pdf)
         

* **Foundations, Bell inequalities (?)**

    1.   Patricia Contreras Tejada, Giannicola Scarpa, Aleksander M. Kubicki, Adam Brandenburger and Pierfrancesco La Mura. Agreement between observers: a physical principle? (52)

         A new property of no-signalling boxes is introduced, called common certainty of disagreement. This notion is
based on a result from classical probability theory, the classical agreement theorem, which states that two Bayesian agents cannot agree to disagree. The boxes with this property are characterized and it is proved that for local or quantum boxes, common certainty of disagreement is not possible.  A related notion called singular disagreement is introduced and is again proved possible in no-signaling setting, but impossible for local or quantum boxes.

         
         The authors propose some interesting properties of no-signaling boxes, which may serve as  simple tests for quantum correlations. However, the usefulness of such  tests is unclear. There are some almost-quantum correlations that can be ruled out, but others that cannot. There is no further investigation (yet) into performance of such tests and their relations to other properties of no-signalling boxes. So this may be worth of further research, but there are not enough for a talk.  

  

    1. Ravishankar Ramanathan, Michal Banacki, Ricard Rodriguez and Pawel Horodecki. Single trusted qubit is necessary and  sufficient for quantum realisation of extremal no-signaling correlations  (165)


* Continuous variables

    1. Giovanni Ferrari, Ludovico Lami, Thomas Theurer and Martin Plenio. Asymptotic state transformations of continuous
       variable resources (92)

    1. Ludovico Lami. Quantum data hiding with continuous variable systems (238)


* Relative entropy

    1. Nicholas Laracuente. Quasi-factorization and Multiplicative Comparison of Subalgebra-Relative Entropy (209)


* Cojaviem

    1. Seiichiro Tani. Quantum Algorithm for Finding the Optimal Variable Ordering for Binary Decision Diagrams (44)

         (subreviewer: Daniel Nagaj)

    1. Soumya Das, Goutam Paul and Anindya Banerji. Hyper-hybrid entanglement and the fidelity of quantum teleportation
       limit each other (156)

    1. Kai Meinerz, Chae-Yeun Park and Simon Trebst. Scalable Neural Decoder for Topological Surface Codes (164)

    1. Angelo Lucia, David Pérez-García and Antonio Pérez-Hernández. Thermalization in Kitaev’s quantum double models
       via Tensor Network techniques (220)




