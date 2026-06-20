Data una funzione continua $f$ Taylorizzabile, è possibile Taylorizzarla con la seguente formula
$$\large f(x) = P_{m}(x) + R_{m}(x)$$
in cui $P_{m}$ è il *polinomio di Taylor* di grado $m$ ed ha l'espressione
$$\large P_{m}(x) = \sum_{i=0}^m \frac{f^{(i)}(a)}{i!}(x-a)^i$$
mentre $R_{m}$ è il *resto di Taylor* ed è esprimibile in diversi modi. Uno di questi è il *resto integrale*, che si ottiene in un modo magico e che rappresenta l'attuazione di una correzione continua basata sulla derivata $m+1$ - esima per far coincidere il polinomio con la funzione. La sua formula è
$$\large R_m(x) = \int_{a}^x \frac{f^{(m+1)}(t)}{m!}(x-t)^mdt$$
un problema di questa formula è la presenza di un intervallo ad estremi variabili. Per risolverlo, si utilizza una funzione definita a tratti detta **potenza tronca**, che si indica con $(x-t)^m_{+}$ e si comporta normalmente se $t < x$ ma vale 0 per valori di $t$ superiori. In questo modo è possibile scrivere l'integrale come
$$\large \int_{a}^b \frac{f^{(m+1)}(t)}{m!}(x-t)^m_{+} dt$$
