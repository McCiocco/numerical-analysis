
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
