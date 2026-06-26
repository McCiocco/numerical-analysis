# 1. Rappresentazione dei numeri e teoria degli errori

L'obbiettivo di questo capitolo è arrivare a definire un metodo formale di rappresentazione tramite cifre dei numeri, che siano naturali o reali, al fine di eseguire operazioni sugli stessi tramite un calcolatore. In seguito, studieremo metodi per maggiorare gli errori che compiamo nell'eseguire suddette operazioni.

### 1.1 Rappresentazione dei Naturali

Questa sezione l'ho scritta per provare latex quindi è skippabile.
Scelto un certo $\beta \in N$ detto *base della rappresentazione* ed un insieme finito  di cifre $\mathbf{C} = \{ {c_{1}, c_{2}, .., c_{n}} \}$ t.c. $\forall i \:c_{i} \in [0, \beta - 1]$,  possiamo associarvi un naturale $k$ secondo la seguente legge: 

$$ \large k = \sum_{i=0}^{n-1} \: c_{i} \: \beta^{i}$$
Che intervallo di numeri naturali stiamo rappresentando tramite questa legge? Per rispondere è sufficiente individuare il più piccolo ed il più grande dei numeri rappresentabili, in quanto se è possibile rappresentare un certo k, sarà possibile rappresentare anche k + 1 (purché k non sia il massimo numero rappresentabile) (dimostrazione lasciata al lettore :) ).

Il più piccolo numero rappresentabile è 0, che corrisponde al caso in cui tutte le cifre sono nulle.
Il più grande numero rappresentabile, indicato con $g$, va invece calcolato: 
$$ \begin{aligned} 
       g &= \sum_{i=0}^{n-1} \: (\beta - 1)  \: \beta^i \\ 
       &= (\beta - 1) \sum_{i=0}^{n-1} \beta^i \\
       &= (\beta - 1) \: \frac{\beta^{n} - 1}{\beta - 1} \\
       &= \beta^{n} - 1 \quad .
\end{aligned} $$
Dunque questa mappatura è una funzione $R : [0, \beta-1]^n \to [0, \beta^n - 1]$. Facciamo due osservazioni:
- il dominio ha cardinalità $\beta^n$
- il codominio ha cardinalità $\beta^n$
Dato che le cardinalità sono uguali ed è facile verificare che la funzione è iniettiva possiamo concludere che essa è bigettiva, dunque ogni numero naturale nell'intervallo di rappresentabilità ammette una e una sola rappresentazione. 
Per convincerci di questo fatto, descriviamo anche un algoritmo che permette di risalire dal numero alla sua rappresentazione in base $\beta$.

##### Algoritmo 1.1.0

Input: base $\beta$, naturale $k$ da rappresentare.
Output: la rappresentazione di k in base $\beta$.

1. Poniamo $i = 1, \: a = k$
2. Poniamo $c_{i} = a \: \% \: \beta \:, \: a = a / \beta \:, \: i = i + 1$
3. Se $a = 0$, vai al punto 4. Altrimenti vai al punto 2.
4. La rappresentazione decimale di $k$ è su $i$ cifre e consiste dei vari $c_{i}$ ottenuti. Termina.

### 1.2 Rappresentazione normalizzata in virgola mobile

Descriviamo qui un metodo per rappresentare un numero reale $x$ con un numero infinito di cifre.
Scelti una base $\beta$ e una successione di naturali $\{\alpha_{i}\} \mid \forall i \; \: \alpha_{i} \in [0, \beta-1] \wedge \alpha_{1} \neq 0$ possiamo associarvi un reale $x$ secondo la seguente legge:

$$ \large x = \sum_{i=1}^{\infty} \: \alpha_{i} \: \beta^{-i}$$

Assomiglia molto alla legge usata per la rappresentazione dei naturali ed in effetti ne è sostanzialmente un'estensione, differendo solamente per la quantità infinita di cifre necessaria per rappresentare l'infinità dei numeri reali e l'esponente negativo che permette la convergenza della serie ad un valore finito.
Cerchiamo di capire quali numeri vengono rappresentati da questa legge.
Il minimo numero rappresentabile $m$ si ottiene per $\alpha_{1}=1 \wedge \alpha_{i} = 0$ e vale:
$$m = \sum_{i=1}^{\infty}\alpha_{i}\beta^{-i} = \beta^{-1} $$
mentre il massimo numero rappresentabile $M$ si ottiene per $\alpha_{i}=\beta-1$ e vale:
$$ \begin{aligned}
        M &= \sum_{i=1}^\infty (\beta-1)\beta^{-i} \\
        &= (\beta-1)\sum_{i=1}^\infty \beta^{-i} \\
        &= (\beta-1) \left( \frac{1}{1-\beta^{-1}} - 1 \right) \\
        &= (\beta-1) \left( \frac{\beta}{\beta-1} -1 \right) \\
        &= \beta - \beta + 1 \\
        &= 1 \;.

\end{aligned}

$$
Dunque l'intervallo di rappresentabilità è $[\beta^{-1}, 1]$. Il termine "normalizzata" nel nome di questo genere di rappresentazioni si riferisce proprio al fatto che la serie, detta *mantissa* del numero normalizzato, ha valore assoluto compreso tra 0 e 1.
Come possiamo fare a estendere questa rappresentazione a tutti i numeri reali? Basta notare che moltiplicando la mantissa per $\beta^b$, dove $b \in Z$, l'intervallo di rappresentabilità diventa $[\beta^{b-1}, \beta^b]$. Ogni numero reale $x$ deve necessariamente cadere in un intervallo di questo tipo, quindi possiamo rappresentarlo a patto di aggiungere alla rappresentazione anche il parametro $b$. ([[Dimostrazione 1.2.1]])

Ricapitolando, scelti una base $\beta$, una successione di cifre $\alpha_{i}$ e un esponente $\beta$, il numero reale corrispondente è:
$$ \large x = \beta^b \: \sum_{i=1}^{\infty} \: \alpha_{i} \: \beta^{-i}$$
Per dimostrare che una tale rappresentazione esiste per ogni numero reale $x$ ed è unica, tipicamente vi si applicano due restrizioni:
- la prima, già vista, impone che $\alpha_{i} \neq 0$. Se così non fosse, potremmo aggiungere zeri in coda e perderemmo l'unicità della rappresentazione.
- la seconda, apparentemente più stramba, impone che $\nexists k \mid \forall j > k \quad \alpha_{j} = \beta - 1$.  Questo sempre per evitare di perdere l'unicità, in quanto sta sostanzialmente vietando che  $0.99\overline{9}$ sia una valida rappresentazione per il numero 1 e tutti i casi simili.

Con queste condizioni, dato un certo esponente $b$, l'intervallo di rappresentabilità non è più $[\beta^{b-1}, \beta^b]$ ma diviene $[\beta^{b-1}, \beta^b)$, dato che non è possibile porre tutte le cifre pari a $\beta-1$ come abbiamo fatto noi per costruire l'estremo superiore. Questa perdita di rappresentabilità non è davvero un problema in quanto il numero $\beta^b$ è rappresentabile nell'intervallo successivo con esponente $b+1$.

Date queste condizioni, descriviamo un algoritmo per ricavare la rappresentazione in virgola mobile normalizzata di un reale.
Questo l'ho aggiunto io quindi è skippabile.

##### Algoritmo 1.2.2

Input: base $\beta$, reale $x \neq 0$
Output: esponente $b$, successione $\{\alpha_{i}\}$

1. Trovo l'esponente b. Una formula funzionante è $b = \lceil \log_{\beta}x \rceil + 1$.
2. Normalizzo $x$, quindi pongo $\displaystyle x = \frac{x}{\beta^b}$.
3. Definiamo una successione ausiliaria $\displaystyle r_{j} = \sum_{i=1}^{j} \: \alpha_{i} \: \beta^{-i}$.
4. Pongo $j = 1, r_{0} = 0$
5. Scelgo $\alpha_{j} = max \{c \in [0, \beta-1] \mid r_{j-1} + \alpha_{j} \beta^{-j} \leq x\}$.
6. Pongo $j = j+1$. Ripeto il passo 5.

Chiaramente l'algoritmo descritto non termina, in quanto servono infinite cifre per rappresentare un generico reale $x$. Per convincervi della sensatezza di questo algoritmo potete leggere [[Convergenza di 1.2.2]].

Quindi ad ogni numero reale $x$ possiamo far corrispondere una rappresentazione in virgola mobile normalizzata. Ma è unica? La risposta è sì e possiamo enunciarla in questo teorema.

#### Teorema di unicità ed esistenza della rappresentazione in virgola mobile normalizzata (1.2.3)

*Data una base $\beta$ e un reale $x \neq 0$, ne esiste un'unica rappresentazione in base $\beta$, identificata dall'esponente $b$ e dalla successione $\alpha_{i}$ tale che:
- *$\alpha_{1} \neq 0$*
- *$\nexists k \mid \forall j > k \quad \alpha_{j} = \beta - 1$*

### 1.3 Rappresentazione nel calcolatore

All'interno di un calcolatore è possibile rappresentare solo un certo numero $m$ di cifre della mantissa di $x$. Tipicamente, la rappresentazione corrisponde a una delle due seguenti funzioni:
$$\large tr(x) = sign(x) \; \beta^b \; \sum_{i=1}^m \alpha_{i}\beta^{-i}$$
![[Screenshot from 2026-04-17 17-45-07.png]]

Si può dimostrare che:

$$\large |tr(x) - x| < \beta^{b - m}$$
$$\large |rd(x) - x| < \frac{1}{2}\beta^{b - m}$$
Il che è anche abbastanza intuitivo. Dunque l'arrotondamento è una migliore approssimazione.

##### 1.3.1 Numeri di Macchina

Con $M$ si indica l'insieme dei *numeri di macchina*, ossia l'insieme di tutti i reali rappresentabili all'interno di un calcolatore. 
Fissati $\beta$ e $m$, supposto $b \in [L, U]$, la cardinalità di M risulta essere

$$\large |M| = 2\beta^{m-1}(\beta - 1)(U - L + 1) + 1$$
Intuitivamente, questa formula si ricava nel seguente modo:
- il 2 perché abbiamo sia i numeri positivi che negativi
- Considerando **solo** la mantissa, la cardinalità di $M$ sarebbe $\beta^{m-1}(\beta-1)$, dato che dobbiamo scegliere $m$ cifre tra le $\beta$ disponibili di cui la prima diversa da 0.
- Possiamo scegliere anche $b$ nell'intervallo di sopra, dunque moltiplichiamo per $U - L + 1$
- Il +1 viene dall'aggiunta dello zero, altrimenti non rappresentabile.

Si può dimostrare il seguente risultato:

$$\large \forall z \in M, |rd(x) - x|< |x - z|$$
che implica che $rd(x)$ è la migliore approssimazione del numero reale $x$ tra i numeri di macchina (se vi appartiene. Altrimenti, si hanno *overflow* o *underflow*).

##### 1.3.2 Errore e precisione

Si definisce *errore assoluto* della rappresentazione di $x$ il valore:

$$\large \delta_{x} = |rd(x) - x|$$

e si definisce *errore relativo* della rappresentazione di $x$ il valore:

$$\large \epsilon_{x} = \frac{\delta_{x}}{x}$$
Da precedenti considerazioni si [[1.3.2 limiti degli errori| ricavano]] le limitazioni:

$$\large \delta_{x} \leq \frac{1}{2} \beta^{b-m}$$
$$\large \epsilon_{x} < \frac{1}{2}\beta^{1-m}$$
Notiamo che l'errore relativo è limitato da un valore che dipende solo da $m$, che quindi è costante per tutti i numeri di macchina: tale valore è detto *precisione di macchina*. Si può dimostrare che una tale precisione di macchina implica che le rappresentazioni siano corrette fino alla *m-esima* cifra significativa. Questo, intuitivamente, significa che se dovessimo scrivere precisamente tutte le infinite cifre della rappresentazione di $x$ (ad esempio con l'algoritmo 1.2.2), le prime $m-1$ (l'ultima è arrotondata) sarebbero uguali a quelle di $rd(x)$.

##### 1.3.4 Operazioni di macchina

Nel calcolatore non eseguiamo esattamente la somma, la sottrazione, ecc. tra due numeri dati, in quanto il risultato deve essere ricondotto ad un numero di macchina. Pertanto si usa parlare di *operazioni di macchina*, indicandole con i seguenti simboli: $\displaystyle \oplus, \ominus, \otimes, \oslash$. Si tenga a mente che le operazioni di macchina non godono delle stesse proprietà delle operazioni standard.

### 1.4 Errore nel calcolo di una funzione

L'obiettivo di questa sezione è rispondere alla seguente domanda.

*Data una funzione $\displaystyle \phi : R^{n} \to R$, possiamo stimare gli errori assoluti e relativi derivanti dal suo calcolo approssimato all'interno del calcolatore?*

Globalmente, nel calcolare $\phi$ commettiamo tre tipi di errori che contribuiscono all'errore totale $\delta_{f}$:
- *errore di troncamento*: se $\phi$ è una funzione non razionale, nel calcolatore sarà sempre approssimata da una funzione razionale $f$. Da questo punto in poi, immaginiamo di lavorare con l'equivalente razionale $f$.
- *errore algoritmico* $\delta_{a}$: Le operazioni che compongono $f$ devono essere sostituite dalle corrispondenti operazioni di macchina e organizzate in qualche ordine in un algoritmo. Ciò equivale a sostituire la funzione $f$ con un'altra funzione approssimata $f_{a}$.
- *errore di trasmissione dei dati* $\delta_{d}$: vogliamo valutare $f$ in un certo punto $P_{0}$, tuttavia nel calcolatore non possiamo rappresentare esattamente le sue coordinate. Pertanto, stiamo in realtà valutando la funzione in un certo punto $P_{1}$, e questo è fonte di errore.

L'obiettivo delle seguenti sezioni è capire come l'errore totale (relativo e assoluto) dipenda da $\delta_{d}$ e $\delta_{a}$.
##### 1.4.1 Errore assoluto

Dato un certo punto $P_{0} \in R^n$ di coordinate $x_{0i}$ nel quale si vuole valutare $f$, definiamo il suo *insieme di indeterminazione* come:
$$\large D = \{P \in R^n \mid a_{i} \leq x_{i} \leq b_{i}\}$$
Nel calcolatore stiamo effettivamente sostituendo il calcolo di $f(P_{0})$ con il calcolo di $f_{a}(P_{1})$, con $P_{1} \in D$. Pertanto, possiamo scrivere:
$$\delta_{f} = f_{a}(P_{1}) - f(P_{0}) = f_{a}(P_{1}) -f(P_1) + f(P_1) - f(P_0) =\delta_{a} + \delta_{d}$$
L'errore algoritmico è facilmente stimabile una volta fissato l'algoritmo da utilizzare. Per l'errore trasmesso, se $f \in C^1(D)$ (tipo sempre), si può usare la formula di Taylor al primo ordine per ottenere delle stime:
$$f(P_0 + h) \approx f(P_{0}) + h \nabla f(P_{0}) $$
$$ h = P_{1} - P_0 \implies f(P_{1}) - f(P_{0}) = \delta_{d} \approx (P_{1} -P_{0})\nabla f(P_{0})$$
Possiamo indicare con $R$ il gradiente di $f$ calcolato in $P_{0}$ e le sue componenti con $\rho_{i}$, mentre possiamo indicare con $\Delta P$ la differenza tra $P_{1}$ e $P_{0}$ e con $\delta_{x_{i}}$ le sue componenti. I $\rho_{i}$ vengono chiamati *coefficienti di amplificazione* per i corrispondenti $\delta_{x_{i}}$.

Per ottenere una limitazione superiore di $\delta_{d}$, basta osservare che $\displaystyle \rho_{i} \leq \sup_{x \in D} \left| \frac{ \partial f }{ \partial x_{i} } \right|$ e sostituire nella formula di sopra insieme ad una maggiorazione di $\Delta P$.

##### 1.4.2 Errore relativo

Iniziamo col definire *l'errore relativo* $\epsilon_{f}$, *l'errore relativo algoritmico* $\epsilon_{a}$ e *l'errore relativo trasmesso dai dati* $\epsilon_{d}$.
$$\epsilon_{f} = \frac{\delta_{f}}{f(P_{0})}, \quad \epsilon_{a} = \frac{\delta_{a}}{f(P_{1})}, \quad \epsilon_{d} = \frac{\delta_{d}}{f(P_{0})}$$
La relazione tra questi tre termini deriva dal  seguente formulozzo

![[Screenshot from 2026-04-18 13-26-34.png|697]]

Da cui si ricava facilmente dalle definizioni la relazione 
$$\large \epsilon_{f} = \epsilon_{a} + \epsilon_{d} + \epsilon_a \epsilon_{d}$$
in cui tipicamente si trascura il termine $\epsilon_{a}\epsilon_{d}$ perché di ordine superiore.
Abbiamo già delle definizioni degli errori relativi che sono abbastanza al fine di calcolarli, tuttavia sarebbe comodo arrivare anche per $\epsilon_{d}$ ad una formula simile a quella ottenuta per $\delta_{d} = \Delta P \cdot R$. Pertanto, a furia di riscritture, si giunge alla seguente scrittura:
$$\epsilon_{d} = G \cdot E_{x_{i}}$$
in cui i termini di $G$ sono $\displaystyle \gamma_{i} = \frac{x_{i0}}{f(P_{0})} \frac{ \partial f }{ \partial x_{i} }(P_{0})$ e i termini di $E_{x_{i}}$ sono $\displaystyle \epsilon_{x_{i}} = \frac{\delta_{x_{i}}}{x_{i0}}$. 
I $\gamma_{i}$ sono detti *coefficienti di amplificazione* degli errori relativi. Se sono dello stesso ordine dei vari $\epsilon_{x_{i}}$, il calcolo della funzione si dice *ben condizionato*. Altrimenti è *mal condizionato*. Intuitivamente significa che ad un piccolo errore relativo dei dati corrisponde un grande errore relativo totale.

##### 1.4.3 Gli errori nelle quattro operazioni

Applicando le formule descritte sopra è possibile specificare i valori di $\delta_{d}$ e $\epsilon_{d}$
per tutte le quattro operazioni, che sono i seguenti.

![[Screenshot from 2026-04-18 13-47-43.png|697]]            

Osservazioni importanti sono che gli errori relativi sono molto alti per l'addizione e la sottrazione quando i due numeri hanno simile modulo ma segno opposto / uguale, mentre per la moltiplicazione e la divisione possono esplodere gli errori assoluti.
Quando si sommano due numeri vicini in modulo ma con segno opposto, avviene il fenomeno della *cancellazione*. Lo si può vedere così: se le prime $k$ cifre significative sono uguali, diverranno tutte $0$, e il calcolatore rimarrà con solo $m - k$ cifre decimali corrette. A questo punto cambierà l'esponente per evitare gli zeri in testa e della rappresentazione su $m$ cifre ce ne saranno $k$ completamente errate, che non rappresentano vera informazione. 


# 2. Richiami di algebra lineare

Questa sezione ha l'obiettivo di complementare il capitolo 2 delle dispense del prof, spiegando e dando intuizioni per alcuni risultati citati.

##### 2.1 Secondo teorema di Laplace

Il secondo teorema di Laplace ha il seguente enunciato:

![[Screenshot from 2026-04-19 15-21-06.png|697]]

Dove $A$ è una matrice di ordine $n$. Il significato è che se si tenta di calcolare il determinante di $A$ utilizzando il primo Teorema di Laplace ma con una riga $r$ sbagliata si otterrà determinante pari a 0. Questa operazione equivale infatti a calcolare il determinante di un'altra matrice $A'$ che ha la sua riga $i$ uguale alle sua riga $r$. Avendo due righe identiche, ha determinante nullo. Stesso ragionamento vale con le colonne.

##### 2.2 Minori e complementi algebrici generalizzati

Data una matrice $A \in \mathbb{C}^{n\times n}$, un suo *minore di ordine $k$* è il determinante di una sottomatrice di ordine $k$ ottenuta scegliendo $k$ righe e $k$ colonne da $A$, indicabile con $\det(M)$.
Si chiama invece *complemento algebrico generalizzato* di un certo minore $M$ il determinante della sottomatrice di ordine $n - k$ ottenuta prendendo le righe e colonne non presenti in $M$ moltiplicato per il giusto segno. In simboli, è la quantità
$$\large (-1)^{s} \det(M^c)$$
dove $s$ è la somma degli indici delle righe e colonne scelte.
Si chiamano "generalizzati" perché tipicamente nei teoremi di Laplace sui determinanti compaiono solo complementi algebrici di una riga e una colonna, mentre questi lo sono genericamente di $k$ righe e colonne.
##### 2.3 Teorema di Laplace Generalizzato

Se $A \in \mathbb{C}^{n\times n}$,
$$\large \det(A) = \sum_{S} (-1)^{\sigma(s)} \det(M_{S})\det(M_S^c)$$
ossia il suo determinante è uguale alla somma dei prodotti di tutti i minori di ordine $k$ ($\det(M_{S})$) per i loro complementi algebrici generalizzati (il resto dei termini). La funzione $\sigma(S)$ associa a $S$ la somma dei suoi elementi.

##### 2.4 Teorema di Binet-Cauchy

Il Teorema di BC lega il determinante di due matrici $A \in \mathbb{C}^{m \times n}$ e $B \in \mathbb{C}^{n \times n}$ al determinante del loro prodotto $C = AB$, che sarà quadrato di ordine $m$.
Ci sono due casi:
1. $m > n$ 
	In questo caso, il rango di $A$ è al più $n$. Dunque anche il rango di $C$ è al più $n$. Ma dato che $m > n$, $C$ non è di rango massimo e quindi si ha	$$\large \det(C) = 0$$
2. $m \leq n$ 
	Qui vale la seguente relazione, con S che varia tra tutti i possibili insiemi di $m$ indici da 1 a $n$:
$$\large \det (C) = \sum_{S}\det(A_{S})\det(B_{S})$$
	Dunque il determinante di $C$ è la somma dei prodotti di tutti i minori di ordine massimo di $A$ e $B$.  
	Questo risultato segue dall'applicazione del [[2. Richiami di Algebra Lineare#2.3 Teorema di Laplace Generalizzato | Teorema di Laplace Generalizzato]] alla matrice a blocchi
	$$M =\left( \begin{matrix}
	I_{n} & B \\
	A & 0
	\end{matrix} \right)$$
	 e svolgendo magia nera avanzata.
	
##### 2.5 Blocchi di Jordan

Un *blocco di Jordan* $J_{k}(\lambda)$ è una matrice quadrata di ordine $k$ che ha:
- l'autovalore $\lambda$ sulla diagonale principale;
- $1$ sulla sovradiagonale (ogni entrata sopra la diagonale principale);
- $0$ in ogni altra posizione.

##### 2.6 Teorema di Jordan

Questo importante teorema garantisce per ogni matrice quadrata $A$ l'esistenza di una *Forma Canonica di Jordan*, ossia una forma paradiagonale.
Formalmente, data la matrice $A$ di ordine $n$ avente $k \leq n$ autovalori distinti, questa è sempre simile a una matrice $J$ così definita:
$$\large J = diag(B_{1}, B_{2}, \dots, B_{k})$$
dove ogni blocco $B_{i}$ è di ordine $\alpha(\lambda_{i})$ ed è della forma
$$\large B_{i} = diag(J_{1}, J_{2}, \dots , J_{\gamma(\lambda_{i})})$$
dove i vari $J_{j}$ sono blocchi di Jordan con autovalore $\lambda_{i}$.
Osserviamo un po' di fatti per dare senso a questo orrore:
- Ogni blocco $B_{i}$ è di ordine $\alpha(\lambda_{i})$ affinché ogni autovalore compaia nella forma paradiagonale un numero di volte pari alla sua molteplicità algebrica. Per di più, $\sum_{j=1}^k\alpha(\lambda_{j}) = n$ per cui torna anche a livello di dimensioni della matrice.
- Ogni blocco $B_{i}$ è composto da un numero di blocchi di Jordan pari alla molteplicità geometrica del corrispondente autovalore. Questo perché per ogni autovettore corrispondente a $\lambda_{i}$ ha il suo blocco di Jordan e la sua catena di autovettori generalizzati (qui si va nel magico.)

##### 2.7 Primo Teorema di Gerschgorin

I teoremi di Gerschgorin ci danno informazioni sulla localizzazione degli autovalori di una matrice $A \in \mathbb{C}^{n\times n}$ nel piano complesso.
Segue l'enunciato del primo:
$$\large F_{i} = \{z \in \mathbb{C} \mid |z-a_{ii}| < \rho_{i}\}, \quad \text{con } \rho_{i} = \sum_{i\neq j} |a_{ij}|$$
$$\text{Allora, se }\lambda \text{ è un autovalore di A vale}$$
$$\large \lambda \in F = \bigcup F_{i}$$
Dunque gli autovalori di una matrice non possono essere troppo lontani dai valori sulla diagonale principale. Questa distanza è infatti limitata dalla somma degli altri elementi della riga, che "obbligano" gli autovalori a trovarsi all'interno dell'unione di questi cerchi. Consiglio di visionare la dimostrazione sulle dispense in quanto è semplice e utile.

##### 2.8 Secondo teorema di Gerschgorin

Secondo questo teorema, se $k$ cerchi di Gerschgorin uniti sono disgiunti dai rimanenti $n - k$, i primi $k$ contengono $k$ autovalori e gli altri $n -k$ i rimanenti.
Per capire perché questo fatto è vero, partiamo da una matrice diagonale $D$ con autovalori pari agli elementi sulla diagonale di $A$. Gli autovalori sono tutti fermi nei centri dei cerchi di Gerschgorin di $A$. Se iniziamo a deformare la matrice $D$ con continuità per trasformarla in $A$, gli autovalori iniziano a spostarsi all'interno dei cerchi di Gerschgorin in modo continuo: pertanto non possono "saltare" da una regione del piano ad un'altra disgiunta. Ogni autovalore rimane quindi nell'unione di cerchi in cui è partito.

##### 2.9 Terzo teorema di Gerschgorin

Questo teorema afferma che se $A$ è una matrice irriducibile e un autovalore appartiene alla frontiera di $F$, deve appartenere alla frontiera di *tutti* i cerchi di Gerschgorin che compongono F. Intuitivamente, ci dice che gli autovalori sono più tipicamente "all'interno" dei cerchi di Gerschgorin piuttosto che vicini al bordo.
Ho cercato di capire bene cosa causasse questo fenomeno, ma a causa della mia limitata comprensione della riducibilità non ci sono riuscito.

##### 2.10 Valori singolari

I valori singolari sono una generalizzazione del concetto di autovalore per matrici non quadrate. 
Data una matrice $A \in \mathbb{C}^{m\times n}$  indichiamo con $\sigma_{i}$ i suoi valori singolari. Se indichiamo con $a_{i}$ gli $n$ autovalori di $A^HA$, vale la relazione
$$\large \sigma_{i} = \sqrt{ a_{i} }$$
Tipicamente, i valori singolari si riordinano affinché siano in ordine decrescente per valori crescenti dell'indice.
Proprio come una matrice quadrata può essere diagonalizzata, esiste una *decomposizione ai valori singolari* in cui ogni matrice $A$ può essere scritta come 
$$\large A = U \Sigma V^H$$  dove U e V sono matrici unitarie e $\Sigma= \left( \begin{matrix}D \\ 0\end{matrix} \right)$, con $D = diag(\sigma_{i})$.

##### 2.11 Norme vettoriali

Una *norma vettoriale* è una funzione $\lVert x \rVert: \mathbb{C}^n \to \mathbb{R^+}$ con le seguenti proprietà:

- $\lVert x \rVert = 0 \iff x = 0$
- $\lVert \alpha x \rVert = \lvert \alpha \rvert \lVert x \rVert, \quad \forall x \in \mathbb{C}^n, \forall \alpha \in \mathbb{C}$
- $\lVert x + y \rVert \leq \lVert x \rVert + \lVert y \rVert, \quad \forall x, y \in \mathbb{C}^n$

Le più usate sono le seguenti:

- *norma 1*:                     $\lVert x \rVert_1 = \sum_{i=1}^n \lvert x_{i} \rvert$
- *norma euclidea*:       $\lVert x \rVert_{2} = \sqrt{ \sum_{i=1}^n \lvert x \rvert^2 }$
- *norma $\infty$*:                   $\lVert x \rVert_\infty = \max \lvert x_{i} \rvert$

##### 2.12 Teorema di Equivalenza tra Norme

Questo importante teorema afferma che date due norme vettoriali $\lVert x \rVert_{q}$ e $\lVert x \rVert_{p}$, esistono sempre $\alpha, \beta \in R^+$ tali che

$$\large \alpha \lVert x \rVert_{p} \leq \lVert x \rVert _{q} \leq \beta\lVert x \rVert _{p} \quad \forall x \in \mathbb{C}^n$$

Il significato di questo teorema è che proprietà molto importanti come la continuità o la convergenza di una successione / funzione non dipendono dalla norma scelta ma sono proprietà intrinseche dello *spazio*. Le norme sono quindi tutte *topologicamente* equivalenti. Questo ha conseguenza pratiche molto utili: la convergenza o stabilità di un algoritmo non dipende dalla norma utilizzata, ma è assoluta.
Non sono però equivalenti da altri punti di vista, quali l'ottimizzazione: la strada più breve tra due punti cambia radicalmente da norma a norma.

##### 2.13 Norme matriciali

Le norme matriciali sono l'estensione del concetto di norma alle matrici. Devono rispettare delle proprietà simili a quelle delle norme vettoriali, ma sicuramente il concetto più interessante è quello di *norma matriciale indotta*. Data una matrice $A$ e una norma vettoriale, questa si definisce come
$$\large \lVert A \rVert = \sup_{x\neq_{0}} \frac{{\lVert Ax \rVert}}{\lVert x \rVert }$$
Intuitivamente, $\lVert A \rVert$ è il massimo fattore di allungamento che la "trasformazione" associata ad $A$ può causare ad un vettore $x$.  Si utilizza questa definizione perché garantisce la proprietà $\lVert Ax \rVert \leq \lVert A \rVert \lVert x \rVert$, detta *compatibilità* con la norma vettoriale.
Le norme indotte hanno tante proprietà interessanti: per esempio, se una matrice ha norma indotta minore di 1 allora (condizione sufficiente!) sarà convergente. 
Vale anche sempre la relazione per norme indotte $\rho(A) \leq \lVert A \rVert$, dove $\rho$ è il raggio spettrale.

##### 2.14 Norma di Frobenius

La *norma matriciale di Frobenius* di una matrice $A \in \mathbb{C}^{m\times n}$si definisce come
$$\large \lVert A \rVert ^2_{F} = \sum_{i=1}^m\sum_{j=1}^n a_{ij}^2$$

##### 2.15 Teorema di Gelfand

Questo teorema magico afferma che
$$\large \lim_{ n \to \infty } \lVert H^n \rVert ^{1/n} = \rho(H)$$
dunque il comportamento asintotico della norma di $H$ viene eventualmente dominato dal suo raggio spettrale.

# 3. Sistemi di equazioni lineari

I metodi di risoluzione dei sistemi lineari si dividono in *diretti* ed *iterativi*. 
I metodi diretti forniscono una soluzione esatta (a meno di errori di arrotondamento) mentre i metodi iterativi la approssimano mediante una successione.

##### 3.1 Algoritmo base di Gauss

Dato un sistema di equazioni lineare descritto da $Ax = b$, dove $A \in \mathbb{R}^{n\times n}$ (l'estensione del ragionamento a $\mathbb{C}$ non è complicata) cerchiamo di ridurlo ad un sistema della forma $Rx = c$, dove $R$ è una matrice triangolare superiore con gli elementi sulla colonna diversi da 0. Una volta giunti a questa espressione, il sistema si risolve con semplicità.
Il metodo consiste nell'applicare iterativamente il seguente procedimento:
- si sceglie la prima colonna $j$ che non ha tutti zeri sotto la diagonale
- per ogni riga $i > j$ , si definisce $\displaystyle l_{ij} = \frac{a_{ij}}{a_{jj}}$ e si effettua l'operazione di riga $r_{i} = r_{i} - l_{ij}\:r_{j}$, dove $r$ è da intendersi come l'intera riga trattata come vettore.
- Si ripete
Questo procedimento azzera tutte le entrate sotto la diagonale e ci porta alla forma desiderata.
L'esistenza della soluzione del sistema è garantita quando si ha $\det(A)\neq 0$.
L'algoritmo qui descritto però fallisce se in qualche passo si ha $a_{jj} = 0$. Affinché questo non accada, la matrice $A$ deve avere tutti i minori principali di testa diversi da 0, condizione molto più stringente rispetto a quella sul determinante.
Questa condizione emerge a causa del legame che sussiste tra minori principali ed elementi diagonali della matrice $R$. Vale la relazione $r_{ii} = M_{i}/M_{i-1}$, che spiega come mai questo implichi che i minori debbano essere non nulli.
Per risolvere questo problema, ci serve il pivoting.

##### 3.2 Tecniche di pivoting

Il pivoting consiste nel permutare righe e colonne di una matrice per ottenere vantaggi nell'esecuzione dell'algoritmo di Gauss ed evitare che i minori principali di testa siano nulli. Queste operazioni sono equivalenti a riordinare le equazioni del sistema o cambiare nome alle variabili, quindi chiaramente non ne alterano la soluzione.
Un grande nemico del metodo di Gauss è l'errore numerico. Ad ogni passo dobbiamo calcolare dei moltiplicatori, che sono del tipo $\displaystyle l_{ij} = \frac{a_{ij}}{a_{jj}}$ .  $a_{jj}$ è detto *elemento pivotale*, e se è in modulo molto piccolo [[1. Rappresentazione dei numeri e Teoria degli errori#1.4.3 Gli errori nelle quattro operazioni| l'errore relativo della divisione]] esplode, rendendo l'algoritmo instabile. Una soluzione intuitiva è utilizzare il *pivoting parziale*, in cui supponendo di dover operare sulla colonna $j$ si procede nel seguente modo. Supponiamo che
$$\large \max_{1\leq i\leq n} \lvert a_{ij} \rvert = \lvert a_{rj} \rvert $$
allora scambiamo di posto le righe di indice $j$ e $r$, per far si che l'errore relativo locale della divisione sia il minimo possibile e che $\lvert l_{ij} \rvert \leq 1$, che evita il propagarsi di errori tra un passaggio e l'altro in quanto le singole righe vengono moltiplicate per numeri più piccoli.
Esiste anche il *pivoting totale*, in cui si cerca il massimo $a_{ij}$ in tutta la matrice, permutando eventualmente anche le colonne, per avere stabilità ancora maggiore.
Quando $\det(A) \neq 0$, esiste sempre un riordinamento delle righe di $A$ che permette di eseguire l'algoritmo di Gauss senza divisioni per zero. Il pivoting è quindi il "ponte" che ci permette di eseguire questo algoritmo su ogni matrice $A$ non singolare.

##### 3.3 Fattorizzazione LR (o LU per le persone normali)

L'algoritmo di Gauss trasforma una matrice $A$ in un'altra matrice $R$ triangolare superiore. Se ipotizziamo che la matrice $A$ non necessiti di permutazioni di righe / colonne affinché l'algoritmo termini, possiamo descrivere la relazione che sussiste tra $A$ ed $R$ come
$$\large A = LR$$
dove $L$ è una matrice triangolare inferiore con $L_{ii} = 1$ e $L_{ij} = l_{ij}$, dove gli $l$ sono proprio i moltiplicatori dell'algoritmo di Gauss.
Una osservazione interessante è che $\det (A) = \det(R)$, dunque questa fattorizzazione permette di calcolare il determinante con una complessità di $n^3$, migliore della classica $n!$.

##### 3.4 Metodi di Fattorizzazione

La fattorizzazione LR è infinitamente più swag dell'algoritmo di Gauss. Ragion per cui sono stati inventati diversi *metodi di fattorizzazione diretta*, che mirano a costruire direttamente le due matrici $L$ ed $R$.
Il fondamento di questi metodi è trattare l'uguaglianza $A = LR$ come un sistema di $n^2$ equazioni del tipo
$$\large a_{ij} = \sum_{h=1}^{\min(i, j)} l_{ih} \; r_{hj}$$
che risultano semplicemente dalla definizione di prodotto tra matrici, ricordando però che $L$ ed $R$ hanno molti elementi a $0$.

##### 3.5 Metodo di Doolittle

Si inizia ponendo $l_{ii} = 1$ come condizione iniziale.
Si procede osservando che è possibile utilizzare la sommatoria di sopra in questo modo:
- $i \leq j$ : $$\large \begin{aligned}
             a_{ij} &= \sum_{h=1}^i l_{ih}r_{hj} \\
             &= \sum_{h=1}^{i-1} l_{ih}r_{hj} \; + l_{ii}\:r_{ij} \\
             &= \sum_{h=1}^{i-1} l_{ih}r_{hj} \; + r_{ij} \\
             
             \implies r_{ij} &= a_{ij} - \sum_{h=1}^{i-1} l_{ih}r_{hj}
          \end{aligned}$$
-  $j < i$ : $$\large \begin{align}
a_{ij} &= \sum_{h=1}^j l_{ih}r_{hj} \\
&= \sum_{h=1}^{j-1} l_{ih}r_{hj} \; + l_{ij}\:r_{jj} \\
\implies l_{ij} &= \frac{1}{r_{jj}} \left( a_{ij} - \sum_{h=1}^{j-1} l_{ih}r_{hj}\right) 
\end{align}$$
Queste formule ci fanno notare che per calcolare la riga $i$ di $R$ ci serve:
- $L_{i}$ fino all'entrata $i-1$;
- le $i-1$ righe precedenti di $R$.
Per calcolare la colonna $j$ di $L$ servono:
- le $j-1$ colonne precedenti di $L$;
- $R^j$ fino all'entrata $j-1$.  
Questa sorta di "dipendenza incrociata" tra $R$ e $L$ ci permette di creare un algoritmo iterativo per calcolarle.

Dato che all'inizio dell'algoritmo $L_{1}$ è nota ($l_{11} = 1, l_{1i} = 0$) l'algoritmo può partire calcolando la prima riga di $R$.
A questo punto non possiamo calcolare la seconda, dato che ci servirebbe $L_{2}$.
Qui entra in gioco un'osservazione: dato che $L$ è triangolare inferiore, calcolare le prime $i$ colonne significa anche calcolare le prime $i$ righe.
Quindi possiamo calcolare $L_{2}$ calcolando $L^1$, dato che $L_{2}$ ci serve solo fino all'entrata $1$. 
Calcolata $L_{1}$, calcoliamo $R_{2}$, poi $L_{2}$, ..., in questo modo ad ogni passo tutti i termini che compaiono nella sommatoria sono già stati calcolati.

Si noti che la divisione per $r_{jj}$ implica che il metodo qui descritto fallisca quando almeno un $r_{jj}$ è nullo. Non è difficile notare che questa condizione  equivale all'avere un minore principale di testa di $A$ nullo, in quanto il minore di testa di ordine $k$ si ottiene come $\prod_{i}^k r_{ii}$. Questa è la stessa condizione che porta alla fallibilità dell'algoritmo di Gauss, che può essere risolta tramite il pivoting.
##### 3.6 Fattorizzazione di Cholesky

Se la matrice $A$ è simmetrica e definita positiva, è possibile semplificare di molto la semplificazione per ottenere
$$\large A = LL^T$$
con $L$ diagonale inferiore con elementi diagonali positivi (ma non necessariamente unitari).
Applicando l'identità $l_{ij} = r_{ji}$ alle formule ottenute sopra, otteniamo la seguente espressione per $L$:
$$\large l_{ij} = \frac{1}{l_{jj}}\left(a_{ij} - \sum_{h=1}^{j-1} l_{ih}l_{jh} \right), \quad i\neq j$$
$$\large l_{jj} = \sqrt{ a_{jj} -\sum_{h=1}^{j-1} l_{jh}^2 }, \quad i = j$$

Abbiamo inoltre la garanzia che i minori principali siano tutti non nulli, quindi il problema del pivoting non si pone grazie al chad Cholesky.

##### 3.7 Fattorizzazione QR e metodo di Householder

Si può fattorizzare ogni matrice $A$ quadrata in un prodotto che coinvolga una matrice ortogonale $Q$ e una matrice triangolare superiore $R$. Per far questo, tipicamente, si procede nel seguente modo, detto *metodo di Householder*.
Il metodo è basato sull'applicazione ripetuta alla matrice $A$ di una serie di isometrie (quindi rappresentate da matrici ortogonali) che in particolare sono delle riflessioni. La matrice che rappresenta la riflessione rispetto ad un piano ortogonale al vettore $u$ unitario è
$$\large H =I - 2 {uu^T}$$
faccio notare che $uu^T$, in quanto prodotto di un vettore $n\times1$ e un vettore $1 \times n$, risulta in una matrice $n \times n$. 
Se si vuole utilizzare un vettore $v$ non unitario, basta sostituire a $u$ il vettore $\displaystyle \frac{v}{\lVert v \rVert}$, per ottenere
$$\large H = I -2 \frac{{vv^T}}{v^Tv}$$
Vogliamo applicare alla matrice $A$ una riflessione di questo genere per far si che la sua prima colonna $a_{1}$ diventi un vettore parallelo ad $e_{1}$, dunque della forma $(c, 0, 0, \dots, 0)^T$. Possiamo fare un paio di osservazioni. Innanzitutto, deve essere $v = k(a_{1}-ce_{1})$, in quanto altrimenti il vettore $a_{1}$ non potrebbe finire riflesso in $ce_{1}$. Verificare la condizione sul piano può aiutare. Possiamo anche notare che la costante $k$ non è davvero rilevante, in quanto il vettore sarà "normalizzato" per costruire $H$, dunque si può rimuovere.
In seguito, dato che $H$ è una isometria, deve valere $\lVert a_{1} \rVert = \lVert Ha_{1} \rVert = \lvert c \rvert$. Dunque abbiamo come equazione $c = \pm \lVert a_{1} \rVert$. 
Da queste due osservazioni possiamo concludere
$$\large v = a_{1} \mp \lVert a_{1} \rVert e_{1}$$
Quale segno scegliamo? La scelta saggia è una sola. Se fosse $a_{1} < 0$, scegliere il $+$ potrebbe portare a cancellazioni numeriche molto dannose qualora fosse $a_{1} \approx \lVert a \rVert$. Dunque ci conviene scegliere segno uguale a quello di $a_{1}$, ottenendo
$$\large v = a_{1} + sign(a_{11})\lVert a_{1} \rVert e_{1}$$
Possiamo costruire così la prima matrice $H_{1}$ e proseguire considerando lo stesso ragionamento sulla sottomatrice di $A$ senza la prima riga e la prima colonna. In questo modo otteniamo una serie di matrici $H_{1}, \dots, H_{n-1}$ tali che 
$$\large \left( \prod_{i=1}^{n-1}H_{i} \right) A = R$$
da cui si ottiene 
$$\large A = QR$$
dove $Q = \prod_{i=1}^{n-1}H^T_{i}$  (ponendo attenzione a scriverle nell'ordine giusto). Anche $Q$ è ortogonale dato che prodotti di matrici ortogonali sono matrici ortogonali.
Il metodo di Householder ha una complessità pari circa al doppio di quella di Gauss, ma è molto utilizzato perché garantisce grande stabilità numerica. Il perché verrà spiegato nel prossimo paragrafo.
##### 3.8 Errori, stabilità e condizionamento dei metodi diretti

Possiamo fare due tipi di valutazione degli errori.
Il primo, detto di *analisi dell'errore all'indietro*, consiste nel considerare l'errore $\delta x$ che commettiamo sulla soluzione $x$ del sistema come causato da imprecisioni sui dati iniziali, ossia $\delta A$ e $\delta b$. Dunque consideriamo il nostro algoritmo come risolvente un sistema della forma
$$\large (A+\delta a)(x+\delta x) = b + \delta b$$
L'entità dell'errore relativo sulla soluzione dipende dal [[Glossario#Condizionamento|condizionamento]] del problema.
Il teorema malefico che permette di maggiorare l'errore relativo $\displaystyle \epsilon_{x} = \frac{\lVert \delta x \rVert}{\lVert x \rVert}$ è:

$$\large \epsilon_{x} \leq \frac{\mu(A)}{1-\mu(A)\epsilon_{A}}(\epsilon_{A} + \epsilon_{b})$$

dove $\mu(A) = \lVert (A) \rVert\lVert A^{-1} \rVert$ e sotto le importanti condizioni che $\lVert \delta A \rVert < 1/\lVert A^{-1} \rVert$ e che $A + \delta A$ sia non singolare.
Si può osservare che il lato destro è proporzionale a $\mu (A)$, in quanto dalla condizione sopra si può ricavare $\mu(A)\epsilon_{A} < 1$. Dunque il valore $\mu(A)$ si chiama spesso *numero di condizionamento* ed è un buon indice del condizionamento del problema. Se è troppo grande, il problema diventa mal condizionato.
Si noti anche che l'errore è solo linearmente proporzionale a $\delta b$, mentre la proporzionalità rispetto a $\delta A$ è più marcata e pericolosa.

Si può altrimenti portare avanti l'analisi dell'errore *a posteriori*, che consiste nello stimare l'errore partendo dalla soluzione calcolata $\tilde{x}$.
Definiamo *residuo* la quantità $r = b - A\tilde{x}$. Da qui si ha, se $\lVert  \rVert$ è una norma naturale
$$\large \begin{aligned}
A(x - \tilde{x}) &= r \\
x - \tilde{x} &= A^{-1}r \\
\lVert x - \tilde{x} \rVert &\leq \lVert A^{-1} \rVert \lVert r \rVert  \\
\\
Ax = b & \implies \lVert x \rVert \geq \frac{{\lVert b \rVert}}{\lVert A \rVert } \\
\\
\epsilon_{x} &\leq \mu(A) \frac{{\lVert r \rVert}}{\lVert b \rVert }
\end{aligned}
$$

Anche questo modo di analisi quindi conferma l'importanza di $\mu(A)$.
Si può dimostrare che se la matrice $A$ è normale vale anche l'identità
$$\large \mu(A) = \frac{|\lambda_{max}|}{|\lambda_{min}|}$$
ossia il numero di condizionamento è uguale al rapporto tra le norme degli autovalori massimo e minimo.
Questa identità ci mostra la potenza del metodo di Householder per garantire stabilità numerica. Infatti essendo le matrici $H$ ortogonali, i loro autovalori in modulo valgono tutti $1$ ed il loro numero di condizionamento è proprio $1$, che è il minimo valore possibile. Le matrici ortogonali, infatti, non propagano gli errori, il che le rende effettivamente perfette per i fini del calcolo numerico.
##### 3.9 Metodi iterativi

I metodi iterativi consistono nel trasformare il nostro problema di calcolo di un'incognita, spesso definita da un'equazione come può essere $Ax = b$ o da simili vincoli, in un problema di punto fisso di una certa funzione $\phi(x)$.
Per *punto fisso* si intende un certo $\tilde{x} \in R^n$ tale che valga 
$$\large \tilde{x} = \phi(\tilde{x})$$Si costruisce quindi una successione per ricorrenza del tipo

$$\large x_{k} = \phi(x_{k-1})$$

scegliendo $\phi$ in modo che il suo punto fisso sia la soluzione del problema originale e sperando che $\lim_{ k \to \infty } x_k$ sia proprio il punto fisso cercato.
In realtà possiamo fare di meglio che affidarci alla speranza. Se la nostra funzione $\phi$ è *continua*, allora vale 
$$\large \lim_{ n \to \infty } \phi(x_{n}) = \phi(\lim_{ n \to \infty } x_{n}) $$
dunque se ammettiamo che la nostra successione abbia un limite $\tilde{x}$, deve valere $\tilde{x} = \phi(\tilde{x})$ prendendo il limite di entrambe le parti della definizione della ricorrenza. Quindi se $\phi$ è continua, il limite è proprio il punto fisso cercato.
Ma come sappiamo se esiste o meno un limite? A tal proposito ci viene in soccorso il teorema di Banach, o [[A. Teorema delle Contrazioni (o di Banach) | Teorema delle Contrazioni]], che garantisce esistenza e unicità della soluzione se $\phi$ è una contrazione. A questo teorema ho dedicato una paginetta a sé stante perché mi è piaciuto troppo, quindi leggete quella se siete confusi.
Ricapitolando, il nostro metodo iterativo può funzionare se scegliamo accuratamente $\phi$, in modo che:
- sia una contrazione;
- abbia come punto fisso la soluzione al problema originale.

##### 3.10 Stima dell'errore reale del metodo iterativo

Purtroppo tutti i ragionamento non tengono conto degli errori di arrotondamento, che trasformano la ricorsione ideale in una del tipo
$$\large x_{k+1} = \phi(x_{k})+ \delta_{k}$$
che, detto $a$ il punto fisso di $\phi$, porta ad esprimere l'errore come
$$\large e_{k} = \phi(x_{k-1}) - \phi(a) + \delta_{k}$$
Questa successione non ha le stesse proprietà teoriche di quella ideale, tuttavia se riusciamo a trovare maggiorazioni del tipo $\lvert \delta_{k} \rvert \leq \lvert \delta \rvert$ possiamo dire qualcosa in più.
Utilizzando l'espansione di Taylor in $a$ otteniamo
$$\large e_{k} \approx \nabla\phi(a)e_{k-1} + \delta_{k}$$
 (imprecisione, ci andrebbe il jacobiano) che vale se l'errore è abbastanza piccolo in modulo. Se lavoriamo su un intervallo chiuso e limitato in cui $\phi$ è derivabile,  si ha $\lVert \nabla \phi(a) \rVert \leq 1$ dato che $\phi$ è una contrazione. Questo implica che la ricorsione qui sopra abbia un limite preciso, cioè
$$\large \lim_{ k \to \infty } \lVert e_{k} \rVert  \approx \frac{\delta}{ 1 - \lVert \nabla\phi(a) \rVert } $$
L'errore dovuto alle approssimazioni numeriche quindi è amplificato se $\lVert \nabla \phi(a) \rVert \approx 1$, mentre è schiacciato e riassorbito se quel valore tende a 0.
La domanda sorge spontanea: e se è 0? In questo caso si verificano situazioni ancora più favorevoli per la convergenza che tratteremo più avanti, in particolare nel capitolo 4.

##### 3.11 Metodi iterativi per la risoluzione di sistemi lineari

Se la matrice $A$ è sparsa, ossia ha molti elementi nulli, fattorizzarla la rende spesso *densa*, il contrario, e questo è computazionalmente inefficiente.
I metodi iterativi hanno dunque gran peso nella teoria dei sistemi lineari in quanto riescono a mantenere la sparsità del problema.
Come possiamo mappare $Ax = b$ in un problema di punto fisso? Un metodo è il seguente:
$$\large Ax - b = 0 $$
$$\large x = x - G(Ax-b)$$
$$\large x = (I-GA)x+Gb$$
Dunque la nostra funzione $\phi$ sarebbe $\phi(x) = Hx + c$, con $H$ e $c$ definiti come qui sopra. Dobbiamo quindi trovarne i punti fissi, possibilmente imponendone la convergenza per qualsiasi vettore iniziale. Usando la teoria delle contrazioni, possiamo scrivere
$$\large \begin{align}
\lVert \phi(x_{1}) -\phi(x_{2})\rVert & = \lVert Hx_{1} - Hx_{2}\rVert  \\
 & = \lVert H(x_{1}-x2) \rVert \\
  & \leq \lVert H \rVert \lVert x_{1}-x_{2} \rVert 
\end{align} $$
Dunque il metodo è una contrazione se e soltanto se $\lVert H \rVert < 1$  con $\lVert  \rVert$ norma naturale. Da qui possiamo dedurre che **se*** vale questa condizione, il metodo converge. 
La condizione qui sopra non è necessaria ma solo sufficiente. Noi però siamo interessati a trovarne una che sia anche necessaria, così da poter dare all'errore la maggiorazione più stringente possibile.
Per farlo, possiamo definire un vettore $e_{k} = x_{k} - a$, dove $a = Ha + c$ è il punto fisso cercato. Questo $e_{k}$ rappresenta quanto siamo lontani dalla soluzione, ed è facile controllare che verifica l'equazione
$$\large e_{k} = He_{k-1}$$
che diventa
$$\large e_{k} = H^k e_{0}$$
perciò comunque scelto un arbitrario $e_{0}$, il metodo converge se e soltanto se la matrice $H$ è convergente.
Ricordando un po' di algebra lineare, sappiamo che la condizione $H$ convergente è equivalente a $\rho(H) < 1$.
Esiste una formula magica chiamata [[2. Richiami di Algebra Lineare#2.14 Teorema di Gelfand | Teorema di Gelfand]] che può aiutarci a stimare l'errore al passo $k$.
$$\large \lVert e_{k}\rVert \leq \lVert H^k \rVert \lVert e_{0} \rVert   $$
$$\large \implies \frac{{\lVert e_{k} \rVert }}{\lVert e_{0} \rVert } \leq \lVert H^k \rVert \approx \rho(H)^k$$
Se desideriamo un errore assoluto rispetto alla soluzione di $\lVert e_{0} \rVert \times 10^{-m}$, dalla disuguaglianza qui sopra possiamo ricavare
$$\large k \geq \frac{m}{-\log_{10}\rho(H)}$$
Tipicamente la quantità al denominatore è detta *velocità asintotica di convergenza*, perché esprime il rapporto tra la precisione desiderata e il numero di passi necessari ad ottenerla (il tempo).
Potremmo voler arrestare il nostro metodo anche quando la differenza tra due termini consecutivi è troppo piccola, dato che questo implica che le nostre operazioni stanno avendo risultati poco significativi. Vogliamo quindi ottenere una stima dell'errore che stiamo commettendo sulla soluzione in funzione della quantità $\lVert x_{k+1} -x_{k}\rVert$, che ipotizziamo essere $\leq \epsilon$ come criterio di arresto.
Per farlo partiamo dalla definizione della ricorsione
$$\large x_{k+1} = Hx_{k} + c$$
sottraendo $x_{k}$ da ambo i lati 
$$\large x_{k+1} - x_{k} =  (H-I)x_{k} + c$$
e ricordando che $c = - (H - I)a$
$$\large \large x_{k+1} - x_{k} =  (H-I)e_{k}$$
$$\large \implies \lVert e_{k} \rVert \leq \lVert (H-I)^{-1} \rVert \epsilon  $$
dove si fa presente che $H-I$ è invertibile perché $H$ è convergente.
Chiaramente se la norma matriciale è molto grande il metodo è inefficiente, pertanto un altro criterio potrebbe essere basato sul residuo e portare, applicando la maggiorazione dell'errore relativo ottenuta alla fine del paragrafo 3.7, a
$$\large \frac{{\lVert e_{k} \rVert}}{\lVert a \rVert } \leq \mu(A) \frac{{\lVert r_{k} \rVert }}{\lVert b \rVert }$$
se quindi scegliamo come criterio d'arresto
$$\large \frac{{\lVert r_{k} \rVert }}{\lVert b \rVert } \leq \epsilon$$
sappiamo maggiorare con precisione l'errore relativo. Anche qui, però, se $A$ è mal condizionata il criterio è poco affidabile. Pertanto tipicamente si affiancano criteri di arresto del tipo $k \geq N$ prefissato.

##### 3.12 Metodi di Jacobi e Gauss-Seidel

In questo paragrafo mostriamo due metodi iterativi celebri con qualità differenti. Si parte dalla scomposizione di $A$ nella forma
$$\large A = D - E - F$$
dove $D$ ha solo gli elementi diagonali di $A$ ed $E, F$ sono rispettivamente triangolare inferiore e superiore con diagonale nulla.
Per il *metodo di Jacobi*, si riscrive il sistema come
$$\large Dx = (E+F)x +b$$
da cui 
$$\large x_{k+1} = D^{-1}(E+F)x_{k} + D^{-1}b$$ che tipicamente si scrive, indicando con $x_{i}^{(k)}$ la componente di indice $i$ di $x_{k}$,
$$\large x_{i}^{k+1} = \frac{1}{a_{ii}} \left( b_{i} - \sum_{j=1, j\neq i}^n a_{ij}x_{j}^{(k)}\right)$$
Notiamo che il calcolo di ogni $x_{i}^{k+1}$ dipende solo da $x_{k}$, quindi questo algoritmo ha il grande vantaggio di essere parallelizzabile su hardware che lo permette.

Se scriviamo il sistema nella forma
$$\large (D-E)x = Fx + b$$
abbiamo il *metodo di Gauss-Seidel* la cui formula iterativa è
$$\large x_{k+1} = (D-E)^{-1}Fx + (D-E)^{-1}b$$
più tipicamente, invece di questa se ne usa un'altra, ottenuta dall'equazione del sistema con
$$\large Dx_{k+1} = Ex_{k+1} + Fx_{k} + b$$
$$\large x_{k+1} = D^{-1} \left[ Ex_{k+1} +Fx_{k} + b\right]$$
perché si scrive in questo modo? Lo si fa per ottenere la seguente espressione delle singole componenti
$$\large x_{i}^{k+1} = \frac{1}{a_{ii}} \left( b_{i} - \sum_{j=1}^{i-1}a_{ij}x_{j}^{k+1} -\sum_{j=i+1}^na_{ij}x_{j}^k\right)$$
che permette di usare nel calcolo di ogni indice $i$ del nuovo vettore le $i-1$ entrate di $x_{k+1}$ già calcolate. L'utilizzo di questi termini "freschi" permette all'algoritmo di usare meno memoria (si possono calcolare in-place) e inoltre gli conferisce una convergenza più rapida, come vedremo in seguito, dato che per calcolare i vari $x_{i}^{k+1}$ si usano i termini nuovi che sono "più corretti" dei vecchi. Al contempo, essendo sequenziale, questo metodo non è parallelizzabile in modo semplice.
Chiaramente per entrambi i metodi è necessario che $a_{ii} \neq 0$, il che è sempre ottenibile permutano righe / colonne.

Che condizioni sufficienti abbiamo per la convergenza dei due metodi?
Per Jacobi, la matrice di iterazione è 
$$\large H_{j} = D^{-1}(E+F) = D^{-1}(D-A) = I - D^{-1}A$$
e dunque vogliamo che sia vera la condizione $\rho(D^{-1}A) \in [0, 2]$ affinché il metodo converga. Notiamo che la matrice $D^{-1}A$ ha tutti $1$ sulla diagonale, in quanto ha ogni riga scalata del fattore  $1/{a_{ii}}$. Se prendiamo $A$ a predominanza diagonale forte, abbiamo allora per il [[2. Richiami di Algebra Lineare#2.7 Primo Teorema di Gerschgorin| Primo teorema di Gerschgorin]] 
$$\large \lvert \lambda-1 \ \rvert \leq \frac{1}{a_{ii}}\sum_{i}a_{ij} \leq 1$$
quindi tutti i dischi sono centrati in $1$ e hanno raggio minore o uguale a $1$, il che garantisce proprio la proprietà sul raggio spettrale che ci serve.
Ragionamenti simili (ma non troppo) si possono fare anche per il metodo di Gauss-Seidel, quindi per entrambi vale come condizione sufficiente per la convergenza avere $A$ a predominanza diagonale forte.
In aggiunta, Gauss-Seidel converge anche se la matrice $A$ è simmetrica e definita positiva.

##### 3.13 Metodi di rilassamento

Il metodo di Gauss-Seidel spesso è comunque un po' troppo pigro. Altre volte, invece, non ne vuole sapere di convergere. Pertanto sono stati inventati i *metodi di rilassamento*, basati sull'aggiunta di un fattore $\omega$ che va ad *esagerare* o *frenare* la spinta che verrebbe dal metodo iterativo. Formalmente, possiamo scrivere il metodo di Gauss-Seidel come
$$\large x_{k+1} = x_{k} + c_{k}$$
con $c_{k} = D^{-1} \left[ Ex_{k+1} +Fx_{k} + b\right] - x_{k}$. In questo senso, è come se il metodo suggerisse una direzione in cui spostarsi ad ogni passo per andare verso la soluzione del problema. Possiamo quindi introdurre un fattore $\omega$ per ottenere
$$\large x_{k+1} = x_{k} + \omega c_{k}$$
Tipicamente, affinché il metodo converga, serve scegliere $\omega \in [0, 2]$. Se $\omega < 1$, stiamo rallentando la progressione del metodo, che è utile se questo tende a divergere troppo. Al contrario, se $\omega > 1$, stiamo accelerando la sua convergenza, che è utile quando è troppo lento.

##### 3.14 Risoluzione di sistemi lineari come problema di minimo

Se la matrice $A$ è simmetrica e definita positiva, possiamo provare a trasformare il nostro problema in un problema di minimo di una forma quadratica basata su $A$ (le forme quadrate ammettono sempre minimo), quindi della forma
$$\large \phi(x) = \frac{1}{2}x^TAx + c^Tx$$
Dove $c$ è un generico vettore. Vorremmo che il minimo di una tale funzione fosse in $x=a$, dove $Aa = b$, pertanto poniamo il gradiente di $\phi$ uguale a zero
$$\large Ax +c =0$$
che ci suggerisce di porre $c = b$.
Pertanto la forma quadratica che dobbiamo minimizzare è
$$\large \phi(x) = \frac{1}{2}x^TAx + b^Tx$$
si presti attenzione alla relazione $\nabla \phi = Ax - b = -r(x)$, dove $r$ è il residuo del sistema.
Per la risoluzione di uno generico problema di minimo abbiamo già visto nel corso di ricerca operativa il *metodo del gradiente* (steepest descent). L'idea è di creare una successione $\{ x_{k} \}$ tale che la successione $\{ F(x_{k})\}$ sia decrescente e idealmente converga al minimo cercato.
La successione assume, in questo metodo, la forma
$$\large x_{k+1} = x_{k} + \lambda_{k}d_{k}$$
dove $d_{k} = -\nabla \phi(x_{k})$ e $\lambda_{k}$ viene scelto in modo da minimizzare la restrizione $\phi(x_{k} + \lambda_{k}d_{k})$. 
Nel caso del nostro problema vale $d_{k} = r_{k}$ e la condizione di minimizzazione della restrizione è equivalente (con un po' di conti) alla condizione $r_{k+1} \cdot r_{k} = 0$ e quindi all'ortogonalità dei residui consecutivi.
La convergenza di questo metodo è lenta se $A$ è malcondizionata.

##### 3.15 Metodo del gradiente coniugato chad

Il metodo del gradiente come descritto qui sopra non si comporta a dovere la maggior parte delle volte. Tende a fare troppo a zig-zag e ad ogni passo cancella un po' del progresso che aveva fatto al passo precedente. 
Sai qual'è uno dei pochi casi in cui ha una performance clamorosa? Se la matrice $A$ è l'identità. In quel caso, è facile verificare che il paraboloide della forma quadratica ha curve di livello circolari con centro nel punto di minimo, quindi il gradiente punta direttamente verso il minimo e in $1$ iterazione si è già lì. 
Questo caso è così favorevole che anche muovendosi in direzioni casuali è possibile giungere al minimo. Infatti, se si costruisce la successione facendo sì che valga $d_{k+1} \cdot d_{k} = 0$, ossia muovendosi in direzioni sempre perpendicolari, è possibile giungere al minimo in *al più* $n$ iterazioni. L'intuizione del perché succede è abbastanza semplice, infatti ad ogni passo la successione azzera l'errore rispetto al minimo su una data direzione. Essendo quelle successive perpendicolari, il progresso compiuto sulle direzioni precedenti non viene annullato e quindi si termina in massimo $n$ passi.

Però questo è solo un caso particolare fortuito, di certo non c'è modo di utilizzarlo per ottenere un god algoritmo che termini in $n$ passi in ogni caso...


![[mgc.png|697]]

Ok, hear me out bro. Ti ricordi che $A$ è simmetrica e definita positiva, giusto? Allora per quanto detto [[3. Sistemi di Equazioni lineari#3.6 Fattorizzazione di Cholesky | qui sopra]] ammette una fattorizzazione di Cholesky del tipo $A = LL^T$, con $L$ triangolare inferiore. Se proviamo a vedere come la matrice $L^T$ trasforma lo spazio ed in particolare la nostra forma quadratica, otteniamo
$$\large y = L^Tx \implies x = (L^T)^{-1}y$$
$$\large \implies \phi(y) = \frac{1}{2}y^Ty - \tilde{b}^Ty$$
(Fai tu i conti laido, sono facili)
Dunque nello spazio trasformato da $L^T$ la nostra forma quadratica diventa una forma quadratica derivata dalla matrice identità, come quelle di cui parlavamo sopra, con minimo in $\tilde{b}$.
Possiamo quindi scegliere come procedere nell'algoritmo del gradiente in base all'effetto che una certa azione avrebbe nello spazio trasformato da $L^T$. 
La successione 
$$\large x_{k+1} = x_{k} + \lambda_{k}d_{k}$$
$$\large d_{k} = r_{k} + \beta_{k}d_{k-1}$$
diventa, nello spazio trasformato,
$$\large y_{k+1} = y_{k} + \lambda_{k}L^Td_{k}$$
che equivale a muoversi in una certa direzione dettata da $L^Td_{k}$. Affinché questa successione converga al minimo, è necessario che due direzioni successive siano perpendicolari nello spazio trasformato
$$\large (L^Td_{k})^T(L^Td_{k-1}) = 0$$
Qui entra in gioco il trick mistico: l'espressione qui sopra è equivalente a
$$\large d_{k}^TLL^Td_{k-1} = 0 $$
$$\large \implies d_{k}^TAd_{k-1}=0$$
Quindi affinché il metodo segua direzioni perpendicolari alle precedenti nello spazio trasformato, e quindi converga in $n$ iterazioni, deve essere rispettata questa condizione sulle direzioni, ossia devono essere *coniugate* rispetto ad $A$ (da qui il nome del metodo).
Spero che l'intuizione sia chiara, detto questo non ho assolutamente voglia di mettermi a scrivere bene l'algoritmo. Guardatelo sulle dispense, ho fatto abbastanza.

##### 3.16 Metodi a blocchi

Non mi va davvero di descrivere i metodi a blocchi in particolare per la loro verbosità di notazione. Pertanto mi limiterò ad esporne l'idea e i vantaggi.
L'idea alla base del metodo a blocchi è di utilizzare uno qualsiasi dei metodi esposti sopra con matrici partizionate a blocchi, trattando ogni blocco come un singolo elemento. Per esempio, nel metodo di Gauss a blocchi il moltiplicatore $l_{ij}$ diventa $L_{ij} = A_{ij}A_{jj}^{-1}$.
Ci sono diverse ragioni che hanno spinto verso lo sviluppo dei metodi a blocchi:
- le CPU / GPU moderne adorano prelevare dalla memoria *blocchi* di dati e operare contemporaneamente sull'intero blocco per poi rispedirlo indietro. Strutturando il metodo a blocchi si sfruttano meglio le ottimizzazioni hardware.
- Su blocchi più piccoli si possono usare metodi che generano meno errori ma che sarebbero eccessivamente costosi da usare sull'intera matrice. Si tratta di una sorta di *compromiso* tra la realtà dei metodi esatti e quelli iterativi.
- Spesso da problemi reali provengono matrici già partizionate a blocchi, in cui ogni blocco ha un significato fisico / ingegneristico preciso. In questo caso risolvere per blocchi significa anche valutare le interazioni locali prima di passare a quelle globali.


# 4. Equazioni e sistemi non lineari

Sia $f(x) : R \to R$ una funzione continua su un certo intervallo $I$ e si supponga che non sia della forma $f(x) = ax+b$ con $a,b \in R$. Allora si dice *equazione non lineare* l'equazione
$$\large f(x) = 0$$
Il nostro obbiettivo è risolverla, dunque trovare gli zeri della funzione $f$. 

##### 4.1 Metodi iterativi per l'approssimazione degli zeri

Tipicamente questo viene fatto tramite metodi iterativi, quindi formule del tipo
$$\large x_{n+1}=\phi_{n}(x_{n}, \dots, x_{n-k+1}), \quad \quad k\geq 1$$
Come spiegato nel capitolo 3, un'opportuna scelta dei valori iniziali permette alla successione costruita di convergere alla radice $\alpha$. Un metodo della forma sopra indicata si dice *metodo iterativo a k punti*, dato che il calcolo del nuovo punto dipende dai $k$ punti precedenti. Inoltre notate che la funzione $\phi$ usata per il calcolo di $x_{n+1}$ può dipendere da $n$. Se questo non succede, il metodo si dice *stazionario*.

Se la successione $\{x_{n}\}$ converge ad un limite $\alpha$, la nostra radice, possiamo associare al metodo iterativo due costanti, dette *ordine di convergenza* $p$ e *fattore di convergenza* $C$, che soddisfano la seguente relazione
$$\large \lim_{ n \to \infty } \frac{{\lvert e_{n+1} \rvert }}{\lvert e_{n} \rvert^p } = C \neq 0$$
in cui $e_{n} = x_{n} - \alpha$ è l'errore commesso rispetto alla radice ad ogni passo.
Ragionando sulla formula, è chiaro che metodi con convergenza *lineare* ($p =1$) devono necessariamente avere $C < 1$, altrimenti non convergerebbero. Ciò non è necessariamente vero se $p > 1$, dato che la potenza nell'espressione $\lvert e_{n+1} \rvert \approx C\lvert e_{n} \rvert^p$ è in grado comunque di portare la serie alla convergenza con una opportuna scelta del punto iniziale.

##### 4.2 Metodo di bisezione

Che dire, è un sempreverde. Si costruisce un intervallo $(x_{n}, \hat{x}_{n})$ a partire da uno iniziale $(a, b)$ nel quale la soluzione è compresa e lo si dimezza ad ogni passo. Non ho voglia di farne una descrizione formale, ma per chi fosse confuso dalla presenza di $\hat{x}_{n}$, semplicemente è un artificio formale per esprimere l'operazione di scegliere ad ogni passo l'estremo precedente che permette di mantenere vera la condizione $f(x_{n})f(\hat{x}_{n}) < 0$.
Dato che l'intervallo si dimezza, vale la relazione
$$\large |x_{n+1}-\alpha | \leq \frac{1}{2^n}(b-a)$$
che implica la convergenza del metodo. Un pro di questo metodo è che converge sempre a patto che l'intervallo iniziale contenga la soluzione (facilissimo da verificare con la condizione $f(a)f(b) < 0$) e che è possibile stabilire a priori quante iterazioni servono per ottenere un'errore assoluto desiderato $\delta$ grazie alla formula
$$\large n \geq \log_{2}\left( \frac{{b-a}}{\delta} \right)$$
ricavabile dall'espressione di sopra. Un suo contro è la sua lentezza, infatti è possibile dimostrare che è di ordine lineare e il suo fattore di convergenza è circa $C \approx \frac{1}{2}$ (facile da credere).

##### 4.3 Metodo di falsa posizione

Questo metodo è concettualmente molto simile a quello di bisezione, quindi procede costruendo un intervallo $(x_{n}, \hat{x}_{n})$ in cui la soluzione è sempre contenuta. La differenza sta nel modo in cui viene costruito $x_{n+1}$, che viene approssimato con lo zero della retta che passa per i punti $(x_{n}, f(x_{n}))$ e $(\hat{x}_{n}), f(\hat{x}_{n})$. L'idea è che se la funzione in uno dei due estremi ha valore assoluto minore, ha senso che lo zero sia più vicino a quell'estremo. Con un po' di calcoli, si giunge alla formula chiusa
$$\large x_{n+1} = x_{n} - f(x_{n})\frac{{x_{n}-\hat{x}_{n}}}{f(x_{n})-f(\hat{x}_{n})}$$
e poi si aggiorna $\hat{x}_{n+1}$ affinché la radice rimanga nell'intervallo. 
Tipicamente questo metodo converge un po' più in fretta di quello di bisezione, nonostante abbia anch'esso ordine 1. Ha però qualche criticità:
- si può dimostrare che quando $f'(\alpha) \approx 0$, $C \approx 1$. Questo rende la convergenza del metodo lentissima, in quanto le secanti fanno fatica ad approssimare bene una retta orizzontale;
- Se nell'intervallo la derivata seconda della funzione ha segno costante uno degli estremi dell'intervallo rimane fisso, garantendo convergenza teorica ma riducendo l'efficacia del metodo in pratica.

##### 4.4 Metodo delle secanti

I metodi visti finora continuano a imporre la condizione $f(x_{n})f(\hat{x}_{n}) < 0$. E se la abbandonassimo?
Nasce così il metodo delle secanti, che parte da due punti e procede esattamente come il metodo della falsa posizione ma senza imporre la presenza della radice. Pertanto costruisce una successione della forma $(x_{n}, x_{n-1})$ dove vale la relazione
$$\large x_{n+1} = x_{n} - f(x_{n})\frac{{x_{n}-x_{n-1}}}{f(x_{n})-f(x_{n-1})}$$
Questo metodo rappresenta una semplificazione teorica del metodo della falsa posizione e in effetti è molto più veloce: si può [[4.4 Ordine del metodo delle secanti |dimostrare]] che l'ordine di convergenza del metodo è $C = \phi$, dove $\phi$ indica la sezione aurea $1.618\dots$ 
Sebbene sia di ordine maggiore, anche questo metodo ha delle criticità. 
- il metodo è locale. Questo implica che converge solo se si scelgono i due punti iniziali in un intorno sufficientemente stretto della radice $\alpha$;
- vale la stessa condizione presente precedentemente, ossia $f'(\alpha) \neq 0$;
- Al denominatore è presente il termine $f(x_{n}) - f(x_{n-1})$, quindi se la secante è orizzontale o ha coefficiente angolare molto piccolo il metodo esce dal bacino di convergenza.

##### 4.5 Metodi iterativi di punto fisso

Anche detti *metodi iterativi a un punto*, i metodi di punto fisso possono tornarci utili anche nella risoluzione di equazioni non lineari.
Data una equazione $f(x)=0$, è sempre possibile ricondurla ad una espressione di punto fisso $x = \phi(x)$, per esempio ponendo
$$\large \phi(x) = x - g(x)f(x)$$
con $g$ una qualsiasi funzione continua.
Tenendo a mente il [[A. Teorema delle Contrazioni (o di Banach)|teorema delle contrazioni]], sappiamo che se operiamo su un intervallo $I$ in cui vale la condizione
$$\large \lvert \phi'(x) \rvert < 1 \quad \forall x\in I$$
allora la successione $x_{n} = \phi(x_{n-1})$ convergerà sicuramente all'unico punto fisso di $\phi$. 
Possiamo dire qualcosa in più anche sull'ordine di un tale metodo. Usando l'espansione di Taylor in $\alpha$, abbiamo
$$\large e_{n} = \phi(x_{n-1}) - \phi(\alpha) = \sum_{i=1}^{p-1} \frac{\phi^{(i)}(\alpha)}{i!}e_{n-1}^i + \frac{\phi^{(p)}(c)}{p!}e_{n-1}^p$$
per qualche $p$ positivo e qualche $c \in [x_{n-1}, \alpha]$. Da questa formula è chiaro che l'ordine del metodo è $p$ se e soltanto se vale $\phi^{(i)}(\alpha)=0 \quad \forall i<p$, infatti in quel caso 
$$\large \lim_{ n \to \infty } \frac{|e_{n}|}{|e_{n-1}|^p} =\frac{|\phi^{(p)}(\alpha)|}{p!} \neq 0$$

che ci conferma $p$ come ordine di convergenza e quel termine come fattore.
Possiamo dire qualcosa in più anche sui criteri d'arresto, infatti vale
$$\large x_{n}-x_{n-1} = e_{n}-e_{n-1}$$
$$\large x_{n}-x_{n-1} \approx e_{n}\left( 1-\frac{1}{\phi'(\alpha)} \right) $$
$$\large \lvert e_{n} \rvert \approx \lvert x_{n}-x_{n-1} \rvert \left\lvert  \frac{\phi'(\alpha)}{\phi'(\alpha)-1}  \right\rvert $$
Il moltiplicatore è un numero finito che però schizza se il problema è mal condizionato e $\phi'(\alpha) \approx 1$. Questo calcolo ci permette però di concludere che l'errore è dello stesso ordine della differenza di due termini successivi, che è estremamente semplice da verificare, e ci suggerisce quindi un ottimo criterio di stop.
Chiaramente la presenza di arrotondamenti nella macchina porta ad una successione perturbata, la cui analisi si trova [[3. Sistemi di Equazioni lineari#3.9 Stima dell'errore reale del metodo iterativo|nel capitolo 3]]. (so che il modo in cui ho trattato queste parti è un po' convoluto e salta da un capitolo all'altro, fixerò )

##### 4.6 Metodi di Aitken e Steffensen

Se consideriamo un metodo di ordine lineare, questo si comporta un po' come una progressione geometrica, nel senso che ad ogni passo l'errore viene moltiplicato per una costante $K < 1$ ed eventualmente converge a 0. Dati 3 termini consecutivi della successione, possiamo provare ad utilizzarli per costruire una stima del punto fisso basandoci proprio su questo fatto. Infatti, per n sufficientemente grande vale
$$\large x_{n+1} -\alpha \approx C(x_{n}-\alpha)$$
$$\large x_{n+2} -\alpha \approx C(x_{n+1} -\alpha)$$
da cui con un po' di trick si arriva a
$$\large \alpha \approx \frac{{x_{n}x_{n+2}-x_{n+1}^2}}{x_{n+2}-2x_{n+1}+x_{n}}$$
Questa è la nostra stima, che possiamo usare per costruire un'altra successione. Definendo $\Delta_{n}=x_{n+1}-x_{n}$, abbiamo
$$\large z_{n}=x_{n}- \frac{\Delta_{n}^2}{\Delta_{n+1}-\Delta_{n}}$$
che si ottiene modificando leggermente l'espressione di sopra per $\alpha$ al fine di ridurre gli errori di cancellazione numerica.
Questa successione va sotto il nome di *metodo di Aitken* ed è ottima perché converge con ordine maggiore rispetto alla successione di partenza. Si può dimostrare questo fatto scrivendo l'errore come $e_{n} = Ke_{n-1} + O(e_{n-1}^2)$ e sostituendo dentro l'espressione per $z_{n}$. I termini lineari si cancelleranno, lasciando solo quelli di ordine superiore.
Un'idea sorge spontanea. Se $z_{n}$ è una approssimazione della radice migliore di $x_{n+2}$, perché non utilizzare quello per proseguire la successione? Questa è l'idea alla base del *metodo di Steffensen*, che ha la seguente espressione, posti $y_{n} = \phi(x_{n})$ e $z_{n} = \phi(y_{n})$ i due punti successivi
$$\large x_{n+1}  = x_{n} - \frac{(y_{n}-x_{n})^2}{z_{n}-2y_{n}+x_{n}}$$
Dato che questo metodo "comprime" due passaggi del metodo standard in un colpo e poi usa l'approssimazione di Aitken per cancellare l'errore predominante, è possibile dimostrare che se l'ordine del metodo iniziale è $p$ allora l'ordine del metodo di Steffensen è $2p-1$. Per i più precisi, tranquilli, l'approssimazione di Aitken nonostante sia stata qui ricavata partendo da un metodo lineare vale anche per metodi superlineari (magia).
Purtroppo il metodo di Steffensen viene raramente usato per metodi di ordine superiore al primo, in quanto:
- raddoppia l'ordine, sì, ma aumenta anche il costo computazionale;
- la superlinearità rende il denominatore della ricorsione molto piccolo molto in fretta, il che porta ad imprecisioni significative nei calcoli.

##### 4.7 Metodo di Newton

Il più squalo dei metodi ad un punto per risolvere equazioni non lineari è il metodo di Newton. L'idea alla base è sostituire la funzione con la sua retta tangente (espansione di Taylor al primo ordine) e cercarne lo zero, che è elementare. La sua formula chiusa, facilmente ricavabile, è
$$\large x_{n+1} = x_{n}-\frac{f(x_{n})}{f'(x_{n+1})}$$
per avere qualche informazione sulla sua convergenza, consideriamo un intervallo chiuso $I$ che contiene la radice $\alpha$ e studiamo la derivata di $\phi(x)$.
$$\large \phi'(x) = \frac{f(x)f''(x)}{f'^2(x)}$$
$$\large \implies \phi'(\alpha) = 0 \quad \text{ se }f'(\alpha)\neq 0$$
Questa informazione ci permette di concludere, in base alla definizione di continuità, che scelto un certo $K < 1$ esiste sempre un intorno $I_{\alpha}$ tale $\lvert \phi'(x) \rvert < K \quad \forall x\in I_{\alpha}$. Per il [[A. Teorema delle Contrazioni (o di Banach)|teorema delle contrazioni]], questo implica la convergenza del metodo al suo unico punto fisso.
Inoltre, dato che $\phi'(\alpha) = 0$, possiamo concludere che il metodo è di ordine maggiore o uguale al secondo. Dato che tipicamente non vale $\phi''(\alpha)=0$, l'ordine di convergenza è proprio 2 e il fattore di convergenza è $C = 1/2\left\lvert  \frac{f''(\alpha)}{f'(\alpha)}  \right\rvert$.
Da notare la *località* del metodo di Newton, che converge solo se si parte da un intorno di $\alpha$ sufficientemente piccolo. *Quanto* piccolo dipende dalla funzione ma è stimabile, per raggiungere un tale intorno si può poi per esempio procedere per bisezione.
Da notare anche che tutte le osservazioni fatte qui sopra dipendono dalla condizione $f'(\alpha) \neq 0$.
Ci sono poi delle regolette di merda che assicurano convergenza globale ma non ho voglia di scriverle. Sostanzialmente riguardano la monotonia della funzione nell'intervallo scelto, l'assenza di flessi e la scelta di un intervallo sufficientemente grande.
Un esempio carino è il metodo di Newton applicato a $x^m-c =0$, che ha come soluzione la radice $m$-esima di $c$. Questa equazione appartiene al caso appena discusso, quindi è possibile ottenere convergenza globale.
Come possiamo procedere se lo zero della funzione è uno zero non semplice, ossia se $f'(\alpha) = 0$ ? Innanzitutto possiamo scrivere
$$\large f(x) = g(x)(x-\alpha)^s$$
che sarà sicuramente vero per qualche $g$ e qualche $s$, che è la molteplicità di $\alpha$.
A questo punto è possibile ottenere una versione leggermente diversa del metodo di Newton facendo i calcoli e sostituendo $f$ con la formula qui sopra. Si ottiene
$$\large \phi'(\alpha) = 1-\frac{1}{s}$$
Dunque se $s > 1$ il metodo è di ordine lineare.
Si può però sostituire la funzione $f$ con $\displaystyle F(x) = \frac{f(x)}{f'(x)}$ che ha gli stessi zeri ma tutti semplici. Questa sostituzione permette di recuperare l'ordine quadratico al costo di un maggior impiego di risorse computazionali.
Se si conosce a priori la molteplicità della radice si possono fare altri trick per avere performance migliori.

##### 4.8 Metodi iterativi in $R^n$

In questa sezione il bro semplicemente estende i ragionamenti fatti finora al caso $n$-dimensionale. Non ho voglia di riscriverlo in quanto a livello concettuale vale tutto quello che c'è sopra.

# 5. Calcolo di autovalori

In questo capitolo discutiamo di strategie per calcolare autovalori e autovettori di matrici quadrate.

##### 5.1 Metodo delle potenze

Questo metodo ci permette di calcolare iterativamente l'autovalore di modulo massimo di una certa matrice $A$ diagonalizzabile insieme 
all'autovettore associato.
L'idea alla base del metodo delle potenze è di moltiplicare ripetutamente il vettore $x$ per la matrice $A$. In questo modo l'autovalore di modulo maggiore inizierà ad esercitare un'influenza sempre maggiore sui vettori risultanti, allineandoli sempre di più all'autovettore a lui associato. Questo processo porterà quindi il nostro vettore a convergere verso l'autovettore. Vediamolo più formalmente.
Supponiamo di partire con un certo vettore $x$. Supponiamo inoltre che valga
$$\large \lvert \lambda_{1} \rvert \geq \lvert \lambda_{2} \rvert \geq \dots \lvert \lambda_{n} \rvert  $$la quale condizione si può sempre realizzare semplicemente riordinando gli autovalori.
Se $A$ è diagonalizzabile, ammette una base di autovettori $u_{1}, \dots, u_{n}$. Possiamo quindi scrivere
$$\large x = \sum_{i=1}^nx_{i}u_{i}$$
se moltiplichiamo entrambi i membri per $A^k$, otteniamo
$$\large A^kx = \sum_{i=1}^n \lambda_{i}^kx_{i}u_{i}$$
possiamo ora raccogliere a destra per $\lambda_{1}^k$, ottenendo
$$\large A^kx = \lambda_{1}^k \left(x_{1}u_{1} + \sum_{i=2}^n x_{i} \left( \frac{\lambda_{i}}{\lambda_{1}} \right)^k u_{i}\right)$$
questa espressione ci convince a costruire una successione $\{ y_{k}\}$ tale che 
$$\large y_{0} = x, \quad y_{k}=A y_{k-1}$$
per la quale varrà quindi la proprietà
$$\large \lim_{ n \to \infty } y_{n} = \lambda_{1}^nx_{1}u_{1}$$
e che quindi convergerà all'autovettore $u_{1}$.
La successione così definita ha il grande problema di fare overflow / underflow, in quanto il modulo di $y_{k}$ cresce / decresce in maniera illimitata. Pertanto si mette in pratica qualche forma di normalizzazione. Un esempio può essere costruire la successione
$$\large y_{k} = Az_{k-1}, \quad z_{k} = \frac{y_{k}}{\alpha_{k}}$$
dove $\alpha_{k}$ è una costante di normalizzazione che può ad esempio coincidere con la norma euclidea di $y_{k}$. 
Dall'autovettore possiamo estrarre anche l'autovalore associato. Ci sono diversi modi di farlo, ad esempio si può calcolare il rapporto $y_{k}/y_{k-1}$, che per $k \to \infty$ tende proprio all'autovalore $\lambda_{1}$. Un modo molto più diffuso, però, è utilizzare il [[B. Il quoziente di Rayleigh | quoziente di Rayleigh]]. Consiglio caldamente di leggere l'appendice.

Discutiamo alcuni "casi limite" del metodo qui descritto.
Se $A$ non è diagonalizzabile, clamorosamente, il metodo converge lo stesso.
Se l'autovalore di modulo massimo ha molteplicità algebrica maggiore di 1, il metodo converge ma non all'autovettore associato (anche perché ce ne sarebbe più di uno). Converge invece ad un vettore generico appartenente all'autospazio di $\lambda_{1}$. :)

Esiste un procedimento chiamato *deflazione* che permette di calcolare tutti gli autovalori di $A$ utilizzando questo metodo. Una volta trovati $\lambda_{1}$ e $u_{1}$, si consideri la matrice
$$\large A_{1} = A - \lambda_{1}x_{1}x_{1}^H$$
è facile verificare che ha come autovalori gli stessi di $A$ ma con $0$ al posto di $\lambda_{1}$. L'autovalore di modulo massimo è ora $\lambda_{2}$ e si può ripetere il procedimento.

##### 5.2 Metodo di Jacobi

Il *metodo del chad Jacobi* permette di trovare tutti gli autovalori e autovettori di una matrice hermitiana. Ci limitiamo qui al caso reale e quindi la consideriamo solo simmetrica.
L'idea alla base del metodo si basa sul seguente principio: se $G$ è una matrice ortogonale, allora
$$\large \lVert G^TAG \rVert_{F} = \lVert A \rVert _{F} $$
dove $\lVert  \rVert_{F}$ indica la [[2. Richiami di Algebra Lineare#2.14 Norma di Frobenius |norma di Frobenius]]. Questo è intuitivamente vero perché la norma di Frobenius è basata sulla somma degli elementi al quadrato, quindi è uguale alla somma delle norme euclidee delle colonne (o delle righe) che sono conservate dalle isometrie.
Consideriamo una matrice ortogonale $G$ tale che $(G^TAG)_{ij} = 0$, dove $i \neq j$, quindi che azzera un elemento fuori dalla diagonale. Dato che la norma di Frobenius si conserva, la quantità che abbiamo rimosso dall'elemento $ij$ deve spostarsi da qualche parte. Se riuscissimo a trovare una matrice $G$ che sposti quella quantità sulla diagonale, diminuendo la somma degli elementi fuori diagonale, avremmo costruito un metodo convergente ad una matrice diagonale. La matrice $G^TAG$ è simile a quella iniziale e pertanto ha gli stessi autovalori: se è diagonale, gli elementi sulla diagonale sono proprio gli autovalori di $A$. Questo è il cuore del metodo di Jacobi, la cui definizione iterativa è proprio
$$\large A_{k+1}=G_{rs}^{(k)^T}A_{k}G_{rs}^{(k)}, \quad A_{1} = A$$
dove $G_{rs}^{(k)}$ è una matrice di rotazione fatta così

![[Screenshot from 2026-05-10 12-43-44.png]]

l'angolo $\phi$ si sceglie in modo da azzerare l'elemento $a_{rs}$. La dimostrazione che la somma dei quadrati degli elementi non diagonali tende a zero è più complicata e non mi va di riportarla, dovete trustrare Jacobi.
Se definiamo
$$\large H_{k}=\prod_{i=1}^k G_{i}$$
allora vale la relazione
$$\large A_{k+1}=H_{k}^TAH_{k} \implies AH_{k}=H_{k}A_{k+1}$$
dato che $A_{k+1}$ tende ad una matrice diagonale, l'equazione sopra vista considerando una colonna di $H_{k}$ ha questa forma
$$\large Ah_{k} = \lambda h_{k}$$
dunque le colonne di $H_{k}$ approssimano gli autovettori di $A$. crazy.

Per scegliere i due indici $rs$ tipicamente si adotta uno di due approcci:
- si sceglie l'elemento $a_{rs}$ tale che sia maggiore possibile in modulo, affinché la parte non diagonale si azzeri più velocemente possibile. Questo metodo però necessita di $n$ operazioni di comparazione al fine di scegliere l'elemento maggiore;
- si annullano ciclicamente gli elementi $11, 12, \dots , 1n, 21, \dots, (n-1)n$, ottenendo il *metodo di Jacobi ciclico*. Ha il vantaggio di non dover effettuare comparazioni aggiuntive.


# 6. Il problema dei minimi quadrati

Siano $A \in \mathbb{C}^{m\times n}$, $x \in \mathbb{C}^n$ e $b \in \mathbb{C}^m$. Allora se $m > n$ il sistema lineare $Ax = b$ si dice *sovradeterminato*. Se siamo fortunati e $b \in \mathrm{Im}(A)$, il sistema ha una soluzione. Altrimenti, possiamo chiederci per quale valore di $x$ si abbia
$$\large \lVert r \rVert = \min_{x\in\mathbb{C}^n}\lVert Ax-b \rVert =\gamma$$
dove $r$ è il residuo del sistema e $\lVert  \rVert$ indica la norma euclidea. Questo si chiama *problema dei minimi quadrati*.

##### 6.1 Sistema normale

Si può, quasi per magia, caratterizzare molto precisamente l'insieme $X$ dei vettori che soddisfano l'equazione espressa qui sopra.
Partiamo innanzitutto dal considerare $C^m$ come partizionato in due sottospazi ortogonali, $\mathrm{Im}(A)$ e $\mathrm{Im}(A)^\bot$. Per un ottimo teorema che al momento non ho voglia di precisare, ogni vettore è esprimibile come somma di due vettori appartenenti a questi spazi (in quanto sono ortogonali). Pertanto possiamo scrivere
$$\large b = b_{1}+b^\bot$$
Immaginiamo $\mathrm{Im}(A)$ come un piano. Il vettore $b$ è per forza di cose fuori dal piano. Come possiamo minimizzare la distanza tra la nostra soluzione $Ax$, che sta sul piano, ed il vettore $b$? Chiaramente scegliendo $x$ come proiezione ortogonale di $b$ su $\mathrm{Im}(A)$. Questa è l'idea chiave alla base della caratterizzazione delle soluzioni del problema.
Ponendo $Ax = b_{1}$, possiamo asserire che
$$\large r = b^\bot$$
e dunque $r \in \mathrm{Im}(A)^\bot$. Questo equivale, pensandoci un po', alla condizione che $r$ sia ortogonale a tutte le colonne di $A$, in quanto queste formano sicuramente una base (al più ne basta un loro sottoinsieme, se $A$ non ha rango massimo) di $\mathrm{Im}(A)$. Questa condizione si può esprimere nel seguente modo
$$\large A^Hr = 0$$
da cui
$$\large A^HAx =A^Hb$$
che è una caratterizzazione esplicita dell'insieme $X$, detta *sistema normale*.
Sono utili alcune osservazioni sul rango di $A$. Si nota intanto ragionandoci un attimo che $rk(A) = rk(A^HA)$, il che lega due quantità importanti del sistema normale e di quello originario.
A seconda del rango di $A^HA$ (che è quadrata) possono verificarsi due scenari:
- rango massimo. In questo caso esiste esattamente un vettore $x^*$ che soddisfa il problema. 
- rango non massimo. Questo implica la presenza di uno spazio nullo per $A$, dunque la soluzione non è più unica. Trovato un $x_{0}$ che risolva il sistema, l'insieme $X$ sarà esprimibile come $$ \large X= \{x_{0}+v, \; v\in \ker(A^HA) \}$$
Entrambi questi casi mostrano che $X$ è un insieme chiuso e convesso. Trustate.
Possiamo essere interessati, tra le molteplici soluzioni, a cercarne una particolare, come quella di minima norma. Ne esiste una? Proviamo a costruirla.
Ponendo $K = \ker(A^HA)$ per brevità, possiamo considerare gli insiemi $K$ e $K^\bot$ e scrivere la soluzione cercata come 
$$\large x^* = x_{p} + x^\bot$$
per cui vale, dato che $x_{p}^Hx^\bot = 0$
$$\large \lVert x^* \rVert =\lVert x_{p} \rVert +\lVert x^\bot \rVert $$
Volendo minimizzare la somma, dato che $x_{p}$ è nel kernel, possiamo porre $x_{p} = 0$, in quanto questo non altera la validità di $x^*$ come soluzione. Questo equivale a non "sprecare" energia muovendosi in direzioni che non contano per arrivare alla soluzione. Quindi $x^* \in \ker(A^HA)^\bot$.
Per dimostrare esistenza e unicità della soluzione, consideriamo l'insieme
$$\large B = \{x \in \mathbb{C}^n : \; \lVert x \rVert \leq \lVert x_{0} \rVert   \}$$
possiamo sicuramente asserire che se esiste un minimo è in $B$. Essendo $B$ un compatto (chiuso e limitato) e la norma una funzione continua ha sicuramente un minimo per Weierstrass.
Un modo per risolvere il sistema, se $A$ ha rango massimo, è utilizzare la [[3. Sistemi di Equazioni lineari#3.6 Fattorizzazione di Cholesky|fattorizzazione di Cholesky]] in quanto $A^HA$ è definita positiva. Altrimenti si può procedere con altri metodi classici.

##### 6.2 Metodo QR

Vediamo un altro metodo per risolvere il problema dei minimi quadrati che si basa sulla [[3. Sistemi di Equazioni lineari#3.7 Fattorizzazione QR e metodo di Householder|fattorizzazione QR]]. Nel paragrafo linkato abbiamo visto come usare il metodo di Householder per fattorizzare una matrice quadrata $A$. Il procedimento è estendibile in maniera triviale a matrici di dimensioni $m \times n$, con $m \geq n$. Le differenze sono:
- la matrice $Q$ avrà dimensione $m \times m$, come tutte le matrici di simmetria;
- la matrice $R$ avrà le ultime $n$ righe tutte nulle, per mantenere la forma triangolare superiore.
Ora che sappiamo come procedere, ipotizziamo che $A$ abbia rango massimo. possiamo scrivere sicuramente
$$\large R = \left[ \;\begin{matrix}
R_{1}  \\
O
\end{matrix} \; \right]$$
dove $R_{1}$  è quadrata e non singolare in quanto $A$ ha rango massimo. Possiamo scrivere
$$\large \lVert Ax-b \rVert = \lVert QRx-b \rVert =\lVert Q(Rx-Q^Hb) \rVert =\lVert Rx-Q^Hb \rVert  $$
$$\large = \lVert Rx-c \rVert $$
Dato che $\lVert Qv \rVert = \lVert v \rVert$ ($Q$ è una isometria). Possiamo ugualmente partizionare $c$ in
$$\large c = \left[ \;\begin{matrix}
c_{1} \\
c_{2}
\end{matrix} \; \right]$$
dove $c_{1} \in \mathbb{C}^n$ e $c_{2} \in \mathbb{C}^{m-n}$. Da qui vale $$\large \lVert Rx-c \rVert^2 = \lVert R_{1}x-c_{1} \rVert^2 + \lVert c_{2} \rVert^2 $$ da cui il minimo della norma si ha azzerando il primo termine a sinistra, che è sicuramente possibile in quanto $R_{1}$ è non singolare. In questo caso, sappiamo che $\gamma = \lVert c_{2} \rVert$.

##### 6.3 Confronto costo computazionale

Il primo metodo enunciato nel capitolo ha costo computazionale:
- $n^2m/2$ per la costruzione di $A^HA$;
- $n^3/6$ per la risoluzione del sistema con Cholesky;
che risulta in una complessità totale di $\frac{n^2}{2}\left( m + \frac{n}{3} \right)$. 

Il metodo QR invece ha costo:
- $n^2(m-n/3)$ per la fattorizzazione;
- $n^2/2$ per la risoluzione del sistema triangolare.
che risulta in una complessità totale di $n^2\left( m-\frac{n}{3} \right)$. 

se facciamo l'ipotesi che $m \gg n$, che ti giuro essere sensata, il primo metodo è circa 2 volte più veloce. Tuttavia, come sappiamo, i metodi basati sulla fattorizzazione $QR$ sono molto più generosi per quanto riguarda la propagazione degli errori.

# 7. Interpolazione ed approssimazione

Il problema dell'*interpolazione* consiste nella stima di una certa funzione $f(x)$, di cui si conoscono un insieme finito di valori, in un punto diverso da quelli dati. Connesso a questo ma più generale è il problema dell'*approssimazione*, che consiste nel sostituire a $f(x)$ una funzione che sia più facile da calcolare cercando di minimizzare il conseguente errore.

#### 7.1 Interpolazione polinomiale

Dato un insieme di $n+1$ punti reali $x_{0}, \dots, x_{n}$ tutti distinti in corrispondenza dei quali conosciamo i valori di $f$, l'*interpolazione polinomiale* consiste nel determinare un polinomio di grado al più $n$ tale che
$$\large P(x_{i}) =f(x_{i}) \quad \forall i \in [0, n]$$
Questa condizione costituisce un sistema lineare di $n+1$ equazioni in altrettante incognite (i coefficienti del polinomio) la cui matrice è detta di *Vandermonde* ed ha determinante diverso da 0 se i punti $x_{i}$ sono a due e due distinti, come ipotizzato. Pertanto esiste un solo polinomio interpolante di grado al più $n$.
Oltre alla risoluzione del suddetto sistema lineare, esistono metodi più semplici e veloci per la costruzione del polinomio interpolante.

#### 7.2 Interpolazione di Lagrange

L'idea alla base di questa tecnica di interpolazione è la seguente: riuscire a trovare un polinomio $q_{i}$ tale che 
$$\large q_{i}(x_{j}) = 0 \quad \forall j \neq i$$
$$\large q_{i}(x_{i}) = 1$$
Se riusciamo a costruire un tale polinomio, il polinomio interpolante diventa semplicemente
$$\large P(x) = \sum_{i=0}^{k}q_{i}(x)f(x_{i})$$
Per trovare la forma di $q_{i}$, notiamo che se deve essere 0 in corrispondenza di $x_{j}$ deve valere
$$\large (x-x_{j}) \quad | \quad q_{i}(x)$$
(dove con $|$ si indica che il polinomio a sinistra divide, o è un fattore, di quello a destra)
Dato che un polinomio di grado $n$ ha al più $n$ zeri, il polinomio $q_{i}$ avrà la forma
$$\large q_{i}(x) = c_{i}\prod_{j=0,\; j \neq i}^{n}(x-x_{j})$$
dove $c_{i}$ è una costante. L'ultima condizione che rimane è farlo valere 1 in corrispondenza di $x_{i}$, da cui otteniamo
$$\large c_{i} = \frac{1}{\prod_{j=0,\; j \neq i}^{n}(x_{i}-x_{j})}$$
Abbiamo così costruito il polinomio interpolante di Lagrange, la cui forma completa è
$$\large P(x) = \sum_{i=0}^{k} \left[ \frac{\prod_{j=0,\; j \neq i}^{n}(x-x_{j})}{\prod_{j=0,\; j \neq i}^{n}(x_{i}-x_{j})} \right]f(x_{i})$$
bruttina, lo so. Ma ha un suo fascino.

#### 7.3 Formula di Aitken-Neville

Dati i soliti punti di indici $0, \dots, n$ esiste un modo ricorsivo per costruire il polinomio interpolante. Sensatamente, questo metodo assocerà ad una serie di indici di punti $i, \dots, k$ un polinomio $P_{i, k}$.
Questo si può fare, e per comprendere come dobbiamo vedere la magica formula di Aitken-Neville. Questa formula "incolla" due polinomi per costruire il successivo:
$$\large P_{0, k}(x) = \frac{{(x -x_{0})P_{1, k}(x) -(x-x_{k})P_{0, k-1}(x)}}{x_{k}-x_{0}}$$
Provando a sostituire i vari $x_{i}$ nel polinomio così costruito vi renderete conto della veridicità di questa formula.

#### 7.4 Interpolazione di Newton e differenze divise

Dato un polinomio interpolante che passa per $k$ punti, come faccio a costruirne uno di grado superiore che passa anche per un punto aggiuntivo? Posso provare ad aggiungere una sorta di "polinomio correttivo" $q_{k}(x)$, che sia ininfluente nei punti già trattati ma sistemi il valore per il nuovo punto.
In simboli, voglio che
$$\large P_{k+1}(x) = P_{k}(x) + q_{k}(x)$$
Sappiamo che per tutti gli $x_{i}$ con $i \in [0, k]$ si ha $P_{k}(x_{i}) = y_{i}$. Vogliamo che questa proprietà valga anche per $P_{k+1}(x)$. Ma allora abbiamo $q_{k}(x_{i}) = 0$, il che implica
$$\large (x-x_{i}) \quad | \quad q_{k}(x) \quad \forall i\in[0, k]$$
Come prima, dato che $q_{k}(x)$ ha grado $k+1$, è della forma
$$\large q_{k}(x) = c_{0,k}\prod_{i=0}^{k}(x-x_{i})$$
et voilà. Il coefficiente si chiama $c_{0, k}$ perché ragionevolmente la sua forma dipende dai punti $x_{0}, \dots , x_{k}$. Questa è la formula dell'interpolazione di Newton:
$$\large P_{0,k}(x) = \sum_{i=0}^{k}\left[ \prod_{j=0}^{i-1}(x-x_{j})\right] c_{0, i}$$
Bene, abbiamo finito. Passiamo al prossimo argomento. Aspetta, come dici? I coefficienti $c_{0, k}$ quanto valgono? Ahahahahahaahahahahahahah

![[soldato.png]]

Dato che abbiamo una forma chiusa di $P_{0, k}(x)$ possiamo usare la formula di Aitken-Neville per ottenere una definizione ricorsiva dei coefficienti $c_{0, k}$.
Sostituendo dentro A-N, otteniamo
$$\large \sum_{i=0}^{k}\left[ \prod_{j=0}^{i-1}(x-x_{j})\right] c_{0, i} = \frac{
(x-x_{0})\sum_{i=1}^{k}\left[ \prod_{j=1}^{i-1}(x-x_{j})\right] c_{1, i} - (x-x_{k})\sum_{i=0}^{k-1}\left[ \prod_{j=0}^{i-1}(x-x_{j})\right] c_{0, i}
}{x_{k}-x_{0}}$$
Lo so. Lo so, fa male leggerla. Pensa quanto ha fatto male scriverla.
Per ottenere la tanto agognata relazione, dobbiamo uguagliare i coefficienti dei termini di grado massimo dei due polinomi (lato destro e sinistro dell'uguale). Così facendo otteniamo
$$\large c_{0, k} = \frac{{c_{1,k} - c_{0, k-1}}}{x_{k}-x_{0}}$$
che è quello che cercavamo.
La funzione malefica $c_{0, i}$ ha un nome e si chiama *differenza divisa* dei punti $0, \dots, i$. Un'altra notazione per indicarla è
$$\large f[x_{0}, \dots, x_{k}]$$
che in particolare se il primo indice coinvolto è 0 e l'ultimo è $k$ prende il nome di *differenza divisa di ordine k+1*.

#### 7.7 Teorema del valor medio generalizzato

Questo teorema swag afferma che esiste $\xi \in [\min\{x_{0}, \dots, x_{n}\}, \max\{x_{0}, \dots, x_{n}\}]$ tale che
$$\large f[x_{0}, \dots, x_{n}] = \frac{f^{(n)}(\xi)}{n!}$$
Si chiama così perché per $n=1$ è esattamente il Teorema del Valor Medio che si vede in Analisi 1, per cui dato un intervallo di due punti esiste un punto in cui la tangente alla funzione è parallela alla retta che li congiunge.
Una curiosa conseguenza di questo risultato è il legame tra il polinomio di Newton e quello di Taylor. Infatti, facendo tendere tutti gli $x_{i}$ ad $x_{0}$ si ottiene
$$\large \lim_{ x_{k}, \dots, x_{1} \to x_{0} } f[x_{0}, \dots, x_{k}] = \frac{f^{(n)}(x_{0})}{n!} $$
e dunque questa operazione di limite trasforma il polinomio interpolante di Newton in quello di Taylor.
#### 7.6 Errore nell'interpolazione polinomiale

Sostituendo una generica funzione $f(x)$ di cui conosciamo $n+1$ punti con il rispettivo polinomio di Newton, che errore commettiamo? Per rispondere, possiamo immaginare di aggiungere ai nostri punti un altro punto, identificato dalle coordinate $(x, f(x))$. Il polinomio interpolante, per ogni valore di $x$, dovrà in questo modo coincidere con la funzione. Otteniamo
$$\large f(x) = P_{0,n}(x) + \prod_{i=0}^n(x-x_{i}) \; f[x_{0}, \dots, x_{n}, x]$$
A partire da questa espressione, applicando il teorema del valor medio generalizzato, otteniamo (indicando con $E(x)$ l'errore)
$$\large E(x) = \prod_{i=0}^n(x-x_{i}) \; \frac{f^{(n+1)}(\xi)}{(n+1)!}$$
che ci permette di maggiorare l'errore qualora conoscessimo una maggiorazione della derivata $n+1-$esima della funzione.

#### 7.7 Interpolazione osculatoria di Hermite - definizione

Immaginiamo di avere, come prima,  $n+1$ punti reali nei quali conosciamo i valori della funzione $f(x_{i})$. In più conosciamo anche i valori della derivate negli stessi punti $f'(x_{i})$. Come facciamo a costruire il polinomio interpolante?
In simboli, stiamo cercando il polinomio $H(x)$ tale che
$$\large H(x_{i}) = f(x_{i}), \quad H'(x_{i}) = f'(x_{i}), \quad \forall i\in[0, n]$$
Intuitivamente il polinomio sarà di grado $2n+1$, ed è possibile costruirlo seguendo due approcci distinti.

#### 7.8 Interpolazione osculatoria - Newton

Si può riciclare il polinomio di Newton anche per l'interpolazione osculatoria. L'idea geniale alla base di questo metodo consiste nell'inserire ogni punto dato *due volte*, costruendo un insieme di punti $z_{0}, z_{1}, \dots , z_{2n+1}$ tale che 
$$\large z_{2i} = z_{2i+1} = x_{i} \quad \forall i \in [0, n]$$
Applicando l'interpolazione di Newton a questo insieme di punti, ci troviamo di fronte ad un problema quando dobbiamo calcolare le differenze divise del tipo $f[z_{i}, z_{i+1}]$. Ma ricordando il risultato espresso in 7.7, sappiamo che
$$\large \lim_{ z_{i} \to z_{i+1}} f[z_{i}, z_{i+1}] = f'(z_{i})$$
e dunque possiamo sostituire forzatamente alla differenza divisa il valore $f'(x_{i})$, che abbiamo come dato. Così procedendo, il polinomio osculatore sarà
$$\large H(x) = \sum_{i=0}^{2n+1}\left[ \prod_{j=0}^{i-1}(x-z_{j})\right] f[z_{0}, \dots, z_{i}]$$
#### 7.9 Interpolazione osculatoria - Lagrange

Si può riciclare anche il metodo di Lagrange. L'idea è di costruire dei polinomi $l_{r}(x)$ tali che
$$\large l_{r}(x_{i}) = 0, \quad l'_{r}(x_{i})= 0, \quad \forall i \neq r$$
$$\large l_{r}(x_{r}) = 1, \quad l'_{r}(x_{r}) = 1$$
così da usarli per assemblare il polinomio finale. In realtà, per la nostra sanità mentale, ci conviene spezzare le proprietà in due e costruire due "specie" di polinomi $v_{r}(x)$ e $d_{r}(x)$, tali che
$$\large v_{r}(x_{i}) = l_{r}(x_{i}), \quad v_{r}'(x_{i}) = 0$$
$$\large d_{r}(x_{i}) = 0, \quad d_{r}'(x_{i}) = l'_{r}(x_{i})$$
in modo che i polinomi $v$ agiscano solo sul valore del polinomio nei punti di interesse ed i polinomi $d$ solo sulla derivata, senza interferire tra loro. I polinomi $v$ e $d$ si chiamano rispettivamente *funzioni fondamentali di prima e seconda specie dell'interpolazione di Hermite*.

Non è interessante dilungarsi sulla dimostrazione di tali espressioni, ma vale
$$\large v_{r}(x) = [1-2q_{r}'(x_{r})(x-x_{r})]q_{r}^2(x)$$
$$\large d_{r}(x) = (x-x_{r})q_{r}^2(x)$$
dove $q_{r}(x)$ è il blocco di Lagrange visto in 7.2.
Date queste espressioni, il polinomio interpolante risulta essere
$$\large H(x) = \sum_{i=0}^{n}\left[v_{i}(x)f(x_{i}) +d_{i}(x)f'(x_{i})\right]$$
Con questo approccio è abbastanza facile dimostrare l'unicità del polinomio osculatore, ma la ometto per culopesite.

#### 7.10 Errore nell'interpolazione osculatoria

Dato che abbiamo ricavato $H(x)$ tramite Newton, è possibile stimare l'errore esattamente come fatto in 7.6, tramite la formula
$$\large E(x) =\prod_{i=0}^{n}(x-x_{i})^2 \; \frac{f^{(2n+2)}(\xi)}{(2n+2)!}$$

dove per $\xi$ valgono le stesse considerazioni precedenti.

#### 7.11 Interpolazione con funzioni spline

Le interpolazioni polinomiali precedentemente presentate hanno il difetto di far crescere il grado del polinomio interpolante *linearmente* con il numero di punti. Se si iniziano ad aggiungere troppi punti, il polinomio diventa poco maneggevole e può anche essere sensibilmente impreciso rispetto alla funzione (vedasi le Runge spikes).
Per risolvere questi inconvenienti si può utilizzare l'interpolazione mediante splines, o *interpolazione polinomiale a tratti*. L'idea è di sostituire alla funzione $f$ un polinomio definito a tratti, in cui per ogni intervallo $[x_{i}, x_{i+1}]$ c'è un corrispondente polinomio di grado $m$, tipicamente molto minore di $n$. 
Formalmente, si dice *funzione spline di grado $m$* relativa ai punti $x_{0}, \dots, x_{n}$ una funzione $S(x):[x_{0}, x_{k}] \to R$ della forma
$$\large S(x) = \sum_{j=0}^{m}a_{0j}x^j \quad \forall x \in [x_{0}, x_{1}]$$
$$\large S(x) = \sum_{j=0}^{m}a_{1j}x^j \quad \forall x \in [x_{1}, x_{2}]$$
$$ \dots$$
$$\large S(x) = \sum_{j=0}^{m}a_{n-1j}x^j \quad \forall x \in [x_{n-1}, x_{n}]$$
chiaramente vogliamo che questo polinomio rispetti alcune proprietà, per esempio vogliamo che passi per i punti desiderati
$$\large S(x_{i}) = y_{i} \quad \forall i\in[0, n]$$
e che si comporti come un polinomio non definito a tratti, dunque sia continuo, derivabile, ecc.
$$\large S(x) \in C^{m-1}([x_{0}, x_{n}])$$
Tipicamente si opera con spline cubiche, dove $m=3$, e in casi di partizione uniforme, cioè in cui $x_{i} - x_{i-1} = h$. In questo caso (non so se anche negli altri) ci ritroviamo con $4n$ coefficienti degli $n$ polinomi $p_{i}$ da determinare e $4n-2$ equazioni, il che ci lascia liberi di individuare altre 2 equazioni a nostro piacimento. Le scelte più famose sono:
$$\large \text{Spline naturale} \quad p_{1}''(x_{0}) = p_{k}''(x_{k}) = 0$$
$$\large \text{Spline periodica} \quad p_{1}'(x_{0}) = p_{k}'(x_{k}), \;p_{1}''(x_{0})=p_{k}''(x_{k})$$
$$\large \text{Spline vincolata} \quad p_{1}'(x_{0}) = f'(x_{0}), \; p_{k}'(x_{k}) = f'(x_{k})$$
(se sono note le derivate sui bordi).
Imponendo queste condizioni, si arriva ad un sistema tridiagonale a predominanza diagonale forte, che dunque ammette una unica soluzione calcolabile in $O(n)$. 
In questo caso, inoltre, si può dimostrare un teorema aborto di maggiorazione degli errori che è fatto così ![[Screenshot from 2026-06-07 17-41-36.png]]

#### 7.12 Minimi quadrati nel discreto

Date $m+1$ funzioni continue nell'intervallo di interesse $\phi_{i}(x)$, con $m\leq n$, ed i soliti $n+1$ punti $x_{i}$ con i rispettivi valori $f(x_{i})$. Vogliamo approssimare $f$ tramite la funzione
$$\large \Phi(x) = \sum_{i=0}^mc_{i}\phi_{i}(x)$$
Ci restano da scegliere i coefficienti $c_{i}$. Farlo nel senso dei minimi quadrati significa sceglierli al fine di minimizzare la funzione
$$\large \Psi(c_{0}, \dots, c_{m})= \sum_{j=0}^n \left[ \Phi(x_{j})-f(x_{j}) \right]^2$$
ossia la somma degli scarti quadratici tra la funzione $\Phi$ e la nostra $f$.
Se poniamo $c = (c_{0}, \dots, c_{m})^T$, $b = (f(x_{0}), \dots, f(x_{k}))^T$ e $A_{ij} = \phi_{j}(x_{i})$, vale l'identità
$$\large \Psi(c) = (Ac-b)^T(Ac-b) = \lVert Ac-b \rVert_{2}^2 $$
da quanto detto nel capitolo sul [[6. Il problema dei minimi quadrati |problema dei minimi quadrati]] sappiamo che le $c$ che minimizzano questa espressione risolvono le *equazioni normali*
$$\large A^TAc = A^Tb$$
da qui valgono le considerazioni fatte nel capitolo 6.

# 8. Integrazione numerica

L'obiettivo di questa sezione è sviluppare metodi per calcolare integrali definiti di una generica funzione $f$.

#### 8.1 Formula di quadratura e sua precisione

Data una funzione $f$ sufficientemente regolare (?) su un intervallo reale $[a, b]$, vogliamo calcolare 
$$\large I(f) = \int_{a}^b f(x)dx$$
utilizzando una *formula di quadratura* che ha forma
$$\large J_{n}(f) = \sum_{i=0}^na_{i}f(x_{i})$$
in cui i vari $a_{i}$ sono i *pesi* e gli $x_{i}$ i *nodi*. Perché si chiama quadratura? Perché una semplice intuizione geometrica della somma qui sopra (nel caso in cui $\sum_{i=0}^na_{i} = b - a$) la associa al calcolare l'area della curva tramite la costruzione di rettangoli sottesi, come si fa nell'integrazione di Riemann. In questo caso, i vari $a_{i}$ sono le lunghezze delle basi dei rettangoli.
L'*errore di quadratura* è un operatore lineare (capirete dopo il perché di questa precisazione) che associa ad una funzione $f$ l'errore derivante dalla sua approssimazione tramite quadratura su un dato intervallo:
$$\large E_{n}(f) = I(f) - J_{n}(f)$$
Si dice che la formula di quadratura ha *grado di precisione* $m$ se
$$\large E_{n}(x^i) = 0 \quad \forall i\in[0, m], \quad E_{n}(x^{m+1}) \neq 0$$
che equivale a garantire il suo perfetto funzionamento sui polinomi di grado al più $m$.

#### 8.2 Teorema di Peano

Il teorema di Peano ci permette di stimare l'errore di quadratura di una funzione, ma non solo: ci permette anche di distinguere l'errore proveniente dalla scelta del metodo e l'errore proveniente dalla singola funzione (che può essere più o meno adatta ad essere integrata).
Tutto parte dal [[C. Resto integrale del polinomio di Taylor|resto integrale di Taylor]]. Ipotizziamo che il grado di precisione del metodo sia $m$. Dato che l'errore di quadratura è un operatore lineare, possiamo scrivere
$$\large E(f) = E(P_{m}) + E(R_{m}(x))$$
dato che il polinomio di Taylor $P_{m}$ ha grado $m$, vale $E(P_{m}) = 0$. Dunque possiamo scrivere
$$\large E(f) = E \left( \int_{a}^b \frac{f^{(m+1)}(t)}{m!}(x-t)_{+}^mdt \right)$$
da cui, per la linearità di $E$,
$$\large E(f) = \frac{1}{m!}\int_{a}^b f^{(m+1)}(t) \;E((x-t)^m_{+}) dt$$
la derivata di $f$ è rimasta fuori da $E$ in quanto è una funzione di $t$ mentre $E$ si occupa solo di funzioni della variabile $x$. La funzione
$$\large K(t) = E((x-t)^m_{+})$$
è detta *nucleo di Peano* e come si può notare dipende *solo* dal metodo scelto, non dalla particolare funzione $f$. La formula finale del Teorema di Peano diventa quindi
$$\large E(f) = \frac{1}{m!}\int_{a}^b f^{(m+1)}(t) \; K(t) \;dt$$
nei casi particolari in cui il nucleo di Peano non cambia segno, è possibile applicare il Teorema della Media Integrale per scrivere, per qualche $\xi \in (a, b)$
$$\large E(f) = \frac{f^{(m+1)}(\xi)}{m!}\int_{a}^b K(t)dt$$
in questo caso si possono raccogliere tutti i termini che non dipendono da $f$ in una costante e scrivere
$$\large E(f) = K \; f^{(m+1)}(\xi)$$
Tipicamente, per calcolare l'integrale del nucleo di Peano si procede con un po' di furbizia: si prende una funzione di cui sia nota la derivata di ordine $m+1$, come ad esempio $x^{m+1}$, e si ricava il valore dell'integrale (che è una costante) secondo la formula
$$\large K = \frac{E(x^{m+1})}{(m+1)!}$$
dove l'errore di quadratura di $x^{m+1}$ è di facile calcolo.

#### 8.3 Formule di Newton-Cotes

Nelle applicazioni pratiche si ha spesso a che fare con campionamenti di dati ad intervalli di tempo regolari. Per questo motivo una famiglia di formule di quadratura famose, dette di *Newton-Cotes*, lavorano considerando i nodi disposti in progressione aritmetica
$$\large h = \frac{{b-a}}{n}, \quad x_{i} = x_{0} + hi, \quad x_{0} = a$$
da notare che il primo e l'ultimo nodo coincidono con gli estremi dell'intervallo, quindi queste formule sono dette *chiuse*, per differenziarle da quelle in cui i nodi sono tutti interni e che sono dette *aperte*.
Determinati i nodi dobbiamo scegliere i pesi in modo da ottenere la precisione massima possibile. Avendo $n+1$ pesi possiamo imporre $n+1$ condizioni, che sono sufficienti per ottenere una formula con grado di precisione *almeno* pari* a $n$, ponendo
$$\large E_{n}(x^i) = 0 \quad \forall i\in[0, n]$$
queste condizioni possono essere espresse mediante un sistema lineare la cui matrice è di Vandermonde (non singolare), pertanto esiste sempre esattamente un insieme di pesi ideale. 
Per determinare i pesi in modo più intuitivo si può utilizzare l'interpolazione di Lagrange. Se utilizziamo i nodi per costruire il polinomio interpolante e poi approssimiamo l'integrale di $f$ con l'integrale del polinomio, la formula avrà sicuramente grado di precisione $n$, in quanto utilizzata su un polinomio di grado $n$ o inferiore ne calcolerà l'area esatta. Allora possiamo scrivere
$$\large f(x) = \sum_{i=0}^n l_{i}(x)f(x_{i}) + R(x)$$
dove i vari $l_{i}$ sono i polinomi di Lagrange e $R$ è il polinomio che esprime l'errore dovuto all'interpolazione, che ricordiamo essere
$$\large \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^n(x-x_{i})$$
Da qui possiamo scrivere
$$\large I(f) = \sum_{i=0}^n I(l_{i})f(x_{i}) \; + I(R)$$
Da cui poniamo 
$$\large J_{n}(f) = \sum_{i=0}^n I(l_{i})f(x_{i})$$
e dunque
$$\large a_{i} = I(l_{i})$$
e come errore di quadratura otteniamo
$$\large E_{n}(f) = \frac{1}{(n+1)!}I \left( 
f^{(n+1)}(\xi)\prod_{i=0}^n(x-x_{i}) \right)$$
Per chi si stesse chiedendo perché non estraiamo la derivata $n+1$ - esima valutata in $\xi$ dall'integrale, ricordate che $\xi$ [[7. Interpolazione ed approssimazione#7.6 Errore nell'interpolazione polinomiale|dipende dal valore di x]] e dunque non è una costante.
A livello di precisione le formule di Newton-Cotes hanno un limite forte, in quanto per $n > 7$ iniziano a verificarsi fenomeni di Runge che causano importanti errori di arrotondamento. Per questo spesso si adottano le formule *generalizzate* o *composite*, che consistono nel "tagliare" l'intervallo $[a, b]$ in $m$ fette ed applicare Newton-Cotes con 2 o 3 punti ad ogni intervallino, massimizzando così la precisione al crescere di $m$.

#### 8.4 Polinomi ortogonali

Spendiamo due parole sul concetto di ortogonalità tra polinomi, in quanto questa ci sarà utile nel prossimo paragrafo. Consideriamo lo spazio vettoriale $\Pi$ dei polinomi, sul quale definiamo un prodotto scalare
$$\large <p, q> = \int_{a}^bw(x)p(x)q(x) \;dx$$
dove $w(x)$ è una funzione non negativa su $[a, b]$.
Partendo dalla base canonica $\{1, x, x^2, \dots\}$ ed applicando l'ortogonalizzazione di Gram-Schmidt, è possibile costruire una base ortogonale di polinomi $\{p_{0}, p_{1}, \dots, p_{n}, \dots\}$  con l'importante proprietà che $p_{k}$ ha esattamente grado $k$. Questo ci permette di dimostrare il seguente importante risultato.

*Scelto un naturale $k$, ogni polinomio $Q$ di grado minore di $k$ è ortogonale a $p_{k}.$*

Questo è banale e segue dall'osservazione che un polinomio di grado inferiore a $k$ sicuramente non può avere componenti nella direzione di $p_{k}$ (altrimenti sarebbe di grado $k$) e dunque deve essergli ortogonale perché ha solo altre componenti della base. 
Proprietà ancora più interessante è l'unicità di questa base, fissati $a, b$ e $w$, a meno di una costante moltiplicativa.

#### 8.5 Quadratura Gaussiana

In questo capitolo trattiamo una versione leggermente più complicata del problema della quadratura, in cui ci poniamo come obiettivo il calcolo di 
$$\large \int_{a}^b w(x)f(x)$$
dove $w$ è una funzione peso non negativa. Può essere molto comodo introdurre questa modifica per tutta una serie di motivi che non ho voglia di discutere.
Non scegliendo a priori come disporre i nodi nell'intervallo il numero di condizioni che possiamo imporre raddoppia e diventa $2n +2$. Con queste, possiamo ottenere un grado di precisione molto maggiore e pari a $2n+1$ tramite le condizioni
$$\large E_{n}(x^i) = 0 \quad \forall i\in[0, 2n+1]$$
queste, come quelle sopra, formano un sistema lineare che però è più complicato da risolvere, specialmente a mano. Pertanto quel chad di Gauss doveva squalarla e trovare un modo leggendario per trovare i valori corretti dei nodi.
In particolare, Gauss si accorse che per avere precisione massima i nodi devono essere esattamente le $n+1$ radici del polinomio $p_{n+1}$ discusso nel capitolo di sopra. Queste sono tutte reali, distinte ed appartenenti ad $[a, b]$. 
La dimostrazione non mi va di scriverla, ma il passaggio main è di scrivere un generico polinomio di grado $2n+1$ come quoziente e resto rispetto a $p_{n+1}$.

# A. Teorema delle contrazioni (o di Banach)

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

# B. Il quoziente di Rayleigh

Il *quoziente di Rayleigh* è una funzione che associa ad un certo vettore $x \in \mathbb{C}^n$ un numero reale $R(x)$, che rappresenta la migliore approssimazione di un autovalore associato al vettore $x$. In che senso?
Immaginiamo che il vettore $x$ sia la stima di un certo autovalore $u$ di una matrice $A$. Possiamo allora chiederci: qual'è il reale $\alpha$ che minimizza la differenza tra le espressioni $Ax$ e $\alpha x$? Per trovarne l'espressione, poniamo
$$\large \frac{d}{d\alpha}\lVert Ax-\alpha x \rVert =0$$
questo equivale a risolvere il problema dei minimi quadrati. Considerando la norma hermitiana, abbiamo
$$\large \frac{d}{d\alpha}(Ax-\alpha x)^H(Ax-\alpha x) = 0$$
$$\large x^H(Ax-\alpha x) + (Ax-\alpha x)^Hx = 0$$
$$\large x^H (A+A^H)x -2\alpha x^Hx =0$$
$$\large \implies \alpha= \frac{x^H\left( \frac{{A+A^H}}{2}\right)x}{x^Hx}$$
Questa espressione è una sorta di "quoziente di Rayleigh generalizzato", in un senso che capiremo dopo.
Vediamo di rispondere ad una ulteriore domanda: se conosco l'errore che sto commettendo su $x$ come stima dell'autovettore $u$, posso stimare anche l'errore che sto commettendo su $\alpha$ come stima dell'autovalore $\lambda$?
Per farlo, consideriamo il vettore $x$ e l'autovettore $u$, entrambi normalizzati, ed esprimiamo l'errore compiuto come
$$\large x = u + \epsilon w$$
dove $w$ è un vettore unitario perpendicolare a $u$ ($u^Hw = 0$). Io lo so che ti stai fidando però pensaci un secondo: sta scrittura non c'ha un cazzo di senso. Il membro a sinistra dovrebbe avere modulo $1$ e quello a destra ha modulo $1 + \epsilon^2$. Ma vaffanculo. Eppure, in realtà, ha tutto senso. Questo perché potremmo sistemare la cosa *normalizzando di nuovo* l'espressione a destra. In questo modo otteniamo
$$\large x = \frac{{u+\epsilon w}}{\sqrt{ 1+\epsilon^2 }}$$
che invece è un'espressione corretta. Potremmo portare avanti i calcoli in questo modo, ma ci accorgiamo di una god proprietà del quoziente: è omogeneo di grado zero, ossia
$$\large R(x) = R(kx), \quad k \in \mathbb{C}$$
quindi calcolare l'errore usando la prima o la seconda espressione per $x$ è uguale. Otterremo lo stesso identico errore. 
Qualcuno potrebbe obbiettare che non c'era davvero ragione di normalizzare $x$, e questo avrebbe semplificato tutto, ma nella pratica molte volte si ha a che fare con vettori normalizzati quindi fidati che conveniva.
Dicevamo. Per stimare l'errore, calcoliamo $R(x)$. Ti risparmio un bordello di calcoli, in cui sostanzialmente devi semplificare roba utilizzando le due identità $Au=\lambda u$ e $w^Hu=0$. Alla fine risulta
$$\large R(x) = \frac{{{\lambda + \frac{1}{2}\epsilon}u^H(Aw) + \epsilon^2w^H\left( \frac{{A+A^H}}{2} \right)w}}{1+\epsilon^2}$$
dove volendo si può usare Taylor per scrivere $\frac{1}{1+x}\approx 1-x$ ma si vede abbastanza bene anche senza che l'errore è lineare in $\epsilon$.
L'espressione di sopra ci porta a voler considerare il caso in cui $A$ sia hermitiana ($A=A^H$). In questo caso il termine in $\epsilon$ si cancella e l'errore diventa proporzionale ad $\epsilon^2$, che è molto molto meglio.
Tipicamente, il quoziente di Rayleigh è in realtà espresso nel seguente modo
$$\large R(x) = \frac{x^HAx}{x^Hx}$$
come mai? Chiaramente se $A$ è hermitiana l'espressione è equivalente, ma negli altri casi sembra essere errata. Ci sono diverse ragioni.
Innanzitutto, notiamo che se $x$ è esattamente un autovettore l'espressione restituisce comunque l'autovalore esatto. Questo è utile perché se ad esempio $x$ è parte di una successione che converge all'autovettore, anche questa espressione convergerà all'autovalore.
Notiamo anche un'altra proprietà: ricordando che ogni matrice si può scrivere come una somma di una matrice simmetrica $S$ e una antisimmetrica $W$, si ha
$$\large x^HAx = x^HSx + x^HWx$$
se stiamo lavorando nel campo dei reali, allora vale sempre $x^TWx = 0$. Questo implica che lavorare con la matrice $A$ è esattamente uguale a lavorare con una matrice $S$ simmetrica, per cui vale quanto detto sopra.
Infine, tante volte è computazionalmente comodo usare questa espressione perché si è già calcolato il valore $Ax$ che si può qui riutilizzare subito.

Si può interpretare il quoziente di Rayleigh di un vettore $x$ come una media degli autovalori di $A$ pesati con le coordinate di $x$. Per capire cosa intendo, si può scrivere $x$ rispetto alla base formata dagli autovettori di $A$ (qualora sia diagonalizzabile) e calcolare il quoziente rispetto a questa espressione. Risulterà
$$\large R(x) = \frac{\sum_{i=1}^n \lambda_{i}x_{i}^2}{\sum_{i=1}^nx_{i}^2}$$
da cui possiamo ottenere, utilizzando le proprietà delle medie
$$\large \lambda_{min} \leq R(x) \leq \lambda_{max}$$

# C. Resto integrale del polinomio di Taylor

Data una funzione continua $f$ Taylorizzabile, è possibile Taylorizzarla con la seguente formula
$$\large f(x) = P_{m}(x) + R_{m}(x)$$
in cui $P_{m}$ è il *polinomio di Taylor* di grado $m$ ed ha l'espressione
$$\large P_{m}(x) = \sum_{i=0}^m \frac{f^{(i)}(a)}{i!}(x-a)^i$$
mentre $R_{m}$ è il *resto di Taylor* ed è esprimibile in diversi modi. Uno di questi è il *resto integrale*, che si ottiene in un modo magico e che rappresenta l'attuazione di una correzione continua basata sulla derivata $m+1$ - esima per far coincidere il polinomio con la funzione. La sua formula è
$$\large R_m(x) = \int_{a}^x \frac{f^{(m+1)}(t)}{m!}(x-t)^mdt$$
un problema di questa formula è la presenza di un intervallo ad estremi variabili. Per risolverlo, si utilizza una funzione definita a tratti detta **potenza tronca**, che si indica con $(x-t)^m_{+}$ e si comporta normalmente se $t < x$ ma vale 0 per valori di $t$ superiori. In questo modo è possibile scrivere l'integrale come
$$\large \int_{a}^b \frac{f^{(m+1)}(t)}{m!}(x-t)^m_{+} dt$$