Tesi: $$\large \forall q \in R, \; \beta \in N - \{0, 1\} \quad \exists! \; b \in Z \mid q \in (\beta^{b-1}, \beta^b]$$ Dimostrazione:

Osserviamo intanto che
$$ \lim_{ b \to -\infty } \beta^b = 0$$
il che implica, per definizione di limite, che
$$\forall \epsilon > 0 \quad \exists c \mid \forall b < c \quad \beta^b < \epsilon$$
Se poniamo $\epsilon = q$, otteniamo
$$\exists c \mid \forall b < c \quad \beta^b < q$$
Se scegliamo $d = max \{c \mid \forall b < c \quad \beta^b < q\}$, sappiamo per certo che 
$$\beta^d < q \leq \beta^{d+1}$$
in quanto $d$ è il massimo tra gli esponenti che permettono alla potenza di essere minore di $q$. Abbiamo così dimostrato l'esistenza dell'esponente desiderato, la sua unicità segue dal fatto che ogni insieme finito ha un solo massimo.
														 $\square$

