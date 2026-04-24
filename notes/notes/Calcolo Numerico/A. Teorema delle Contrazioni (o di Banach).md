#### Contrazioni

Una *contrazione* è una funzione $g : R^n \to R^n$ che "contrae" lo spazio, o formalmente verifica la seguente proprietà
$$\large \lvert g(x) - g(y) \rvert \leq L\lvert x-y \rvert \quad \forall x,y \in R^n, \;L\in [0,1) $$
dove $L$ si dice *costante di contrazione*.

#### Spazio Completo

Per essere più precisi, la funzione $g$ dovrebbe operare su *spazi metrici*, ossia spazi che sono accompagnati da una funzione di distanza $d$. 
Per una definizione formale del teorema è utile conoscere la definizione di *spazio metrico completo*, intuitivamente uno spazio metrico che non ha "buchi".
Formalmente, uno spazio metrico $M$ è completo se tutte le successioni di Cauchy definite in $M$ hanno limite in $M$. Le successioni di Cauchy sono successioni i cui punti si avvicinano arbitrariamente tra di loro. Può sembrare un sinonimo di "successioni convergenti", ma in realtà lo è solo su spazi metrici completi: se lo spazio è incompleto (pensiamo a $\mathbb{Q}$) una successione può essere di Cauchy ma non essere convergente in quanto il limite non è nello spazio considerato.
Le varie potenze di $R$ su cui lavoriamo sono tutte spazi metrici completi, pertanto possiamo ignorare tranquillamente la questione.

#### Enunciato

Sia $M$ uno spazio metrico e $T$ una sua contrazione.
Allora $T$ ammette un solo *punto fisso* $x^*$ e qualsiasi successione della forma
$$\large x_{k} = T(x_{k-1})$$
con $x_{0} \in M$ *convergerà* sempre a $x^*$.

#### Dimostrazione

Iniziamo col primo punto. Ipotizziamo che ci siano *due* punti fissi $x_{1}$ e $x_{2}$.
Allora applicandovi $T$ si dovrebbe avere
$$\large \lvert T(x_{1}) - T(x_{2}) \rvert \leq L\lvert x_{1} - x_{2} \rvert  $$
ma $x_{1}$ e $x_{2}$ sono punti fissi, perciò vale
$$\large \lvert x_{1} - x_{2} \rvert  \leq L \lvert x_{1} - x_{2} \rvert \tag{1}$$
il che implica $L \geq 1$, un assurdo. Pertanto se il punto fisso di $T$ esiste, è unico.

Prendiamo una successione della forma descritta nell'enunciato. Dato che $T$ è una contrazione, ad ogni applicazione la distanza tra due punti consecutivi diminuisce di $L$, portando ad un'espressione del tipo
$$\large \lvert x_{k+1} - x_{k} \rvert \leq L^k \lvert x_{1} - x_{0} \rvert$$
La successione considerata allora è di Cauchy, in quanto i punti diventano arbitrariamente vicini gli uni agli altri. Ma dato che lo spazio $M$ su cui operiamo è completo, la successione deve ammettere un limite $x^*$ in $M$.
Da qui possiamo scrivere
$$\large x_{k} = T(x_{k-1}) \implies \lim_{ k \to \infty } x_{k} = \lim_{ k \to \infty } T(x_{k-1})$$
e dato che ogni contrazione è continua
$$\large \lim_{ k \to \infty } x_{k} = T \left(\lim_{ k \to \infty}  x_{k}\right) $$$$\large x^* = T(x^*)$$
Quindi la successione converge proprio ad un punto fisso di $T$, che quindi esiste anche. Importante notare che questo ragionamento è *indipendente* dal punto iniziale della successione $x_{0}$.

#### Corollario

Un "corollario" teorico del teorema delle contrazioni che mi fa sempre sorridere è il seguente: se siamo in Italia e stendiamo a terra una mappa dell'italia, c'è sempre e soltanto un punto della mappa che si trova esattamente sopra il punto che rappresenta.
Questo perché la mappa può essere visto come l'immagine di una certa contrazione che opera sull'Italia, e stendendola a terra la stiamo posizionando nello stesso spazio metrico su cui opera. Pertanto il teorema ci assicura l'esistenza di un unico punto fisso.

#### Stime degli errori

Una conseguenza forse più interessante è che il teorema di Banach permette di stimare l'errore che un certo metodo iterativo compie nel calcolare un punto fisso.
Analizzando a priori, vale
$$\large \lvert x_{n} - x^* \rvert \leq \frac{L^{n}}{1 - L} \lvert x_{1} - x_{0} \rvert  $$
mentre a posteriori vale
$$\large \lvert x_{n} - x^* \rvert \leq \frac{L}{1-L}\lvert x_{n}-x_{n-1} \rvert $$

Entrambe le disuguaglianze derivano dalla $(1)$ ottenuta durante la dimostrazione, ma potremmo chiederci cosa c'entri quel fattore $\displaystyle \frac{1}{1-L}$. Esso deriva dallo scrivere 
$$\large x_{n}-x^* = \sum_{i=0}^\infty x_{n+i} - x_{n+i+1}$$
Applicando la disuguaglianza triangolare si può maggiorare il termine a sinistra mentre a destra compare una serie geometrica che converge al fattore considerato.

#### Analisi di non contrazioni

Cosa potrebbe succedere al nostro metodo iterativo quando $T$ non è una contrazione? Ci sono diverse possibilità.
Se la funzione è una "espansione" $(L > 1)$ il punto fisso può esistere ma è instabile. Anche partendo vicinissimo ad esso, finiamo per divergere all'infinito, un po' come un pendolo messo in equilibrio a testa in su. In questo senso, le contrazioni garantisco l'esistenza di punti fissi di equilibrio *stabile*.
Più comunemente le funzioni non sono globalmente né contrazioni né espansioni, ma il loro comportamento varia in base ai punti considerati. Allora bisogna essere accorti nel trovare un punto iniziale che sia vicino al punto fisso e permetta al metodo di convergere.
Per finire, metodi iterativi non basati su contrazioni portano spesso a fenomeni caotici. Si pensi alla mappa logistica.