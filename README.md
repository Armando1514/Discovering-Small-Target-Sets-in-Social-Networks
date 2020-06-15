# # CyberSecurity

## 1. Monitoraggio e Network Analysis

### Definizioni utili

- Domini di sicurezza

  Insieme di risorse che sono gestite da policy comuni dal punto di vista della sicurezza. Ogni dominio di sicurezza ha un grado di affidabilità (trust degree) o livello di sicurezza che ne definisce le regole di visibilità rispetto ad altri domini, ad esempio un dominio di sicurezza con grado massimo ha piena visibilità dei domini con grado inferiore. Il viceversa non si può dire a meno di specifiche eccezioni esplicitamente dichiarate.

	- Dominio di sicurezza Outside

	  Dominio outside è tutto il mondo internet esterno, avrà solitamente il grado di trust a 0.

	- Dominio di sicurezza DMZ

	  Alcune macchine per forza di cose devono essere visibili all'esterno (come i web server o un server di posta elettronica). Queste macchine sono all'interno della nostra organizzazione e sono visibili all'esterno. Di conseguenza saranno in un dominio intermedio chiamato zona demilitarizzata (DMZ), di solito hanno un grado di trust 0 < x <100.

	- Dominio di sicurezza Inside

	  Inside è l'organizzazione interna da proteggere, la zona più delicata, bisogna nasconderla bene dall'esterno, tipicamente abbiamo i database, il grado di trust è 100 (massimo).

- Perimetro di sicurezza

  Il perimetro è il confine tra una rete e l'altra. La creazione di un perimetro di sicurezza, quindi, può essere definita come la creazione di protezioni necessarie all'ingresso in una rete privata per proteggerla da intrusioni.

- Superficie di attacco

  La superficie di attacco di un sistema è quella parte del sistema stesso che può essere esposta ad accesso o a modifiche di utenti non autorizzati. Un esempio possono essere gli input degli utenti, i protocolli utilizzati e altro. Un approccio alla sicurezza informatica è di ridurre la superficie di attacco rendendo il software o il sistema più difficile da attaccare (come chiudere tutte le porte del sistema non utilizzate).

- Flusso

  Insieme di pacchetti caratterizzati da una stessa porta di origine, una stessa porta di destinazione e uno stesso protcollo, che vanno da una entità all'altra appartenenti a due domini di sicurezza differenti. Bisogna saper interpretare i vari flussi e la loro identità per capire se sono regolari o frutto di attacchi.

### Sniffing

Uno sniffer è una applicazione software che è in grado di acquisire pacchetti a livello datalink.  Quindi ci permette di analizzare il traffico di rete. 
Varie applicazioni:
Analisi automatica alla ricerca di possibili pattern.
Analisi delle anomalie per scoprire eventuali problemi all'interno della rete.
Analisi delle prestazioni per scoprire problemi o bottleneck.
Rilevamento delle intrusioni in rete così da rilevare attacchi o minacce in corso. 
Registrazione del traffico di rete per creare dei logs riguardanti le comunicazioni in rete per analisi post-mortem.

- Come catturare il traffico

	- Traffic Access Port (TAP)

	  Soluzione hardware dedicata che fornisce una copia del traffico su una tratta fra 2 dispositivi (molti di questi dispositivi non richiedono alimentazione elettrica). Il TAP opera a livello 1 e non richiede configurazioni specifiche su switch o server. Lo sniffer è posto subito dopo il TAP, cioè riceve i dati dal TAP. 
	  Risulta invisibile poiché a livello 1, inoltre, rispetto alle tradizionali interfacce di rete che scartano frame malformati, il TAP poiché agisce a livello fisico, ha visione di tutto, anche degli errori.

	- Attacco ARP Poisoning

		- Definizione Address Resolution Protocolo 
 (ARP)

		  Lo scopo del protocollo ARP è fornire la "mappatura" tra indirizzo IP (32 bit IPV4) e l'indirizzo ETH(MAC) corrispondente all'end-point in una rete locale ethernet.
		  Nel protocollo viaggiano due tipi di messaggi:
		  ARP request: richiesta di risoluzione di un indirizzo IP.
		  ARP reply: risposta contente l'indirizzo MAC.
		  Le risposte sono memorizzate nell'ARP CACHE per limitare il traffico sulla rete perché altrimenti si dovrebbero inviare continuamente ARP request prima di inviare ciascun pacchetto al destinatario.
		  Il problema principale è che il protocollo risulta stateless, ovvero, non ricorda le richieste fatte in precedenza, ogni richiesta è indipendente da tutte le altre e l'ultima arrivata è quella utilizzata.

		- Attacco ARP Poisoning

		  L'attacco funziona sia in ambienti LAN che Wi-Fi, perché per poter comunicare nelle reti locali, bisogna risolvere tutti gli indirizzi MAC (quindi l'attaccante deve trovarsi nella stessa subnet locale per vedere i messaggi ARP). 
		  Funzionamento:
		  L'host A invia un'ARP request per conoscere il MAC address di C.
		  Il router C risponde con il suo MAC ed aggiorna la sua ARP Cache con il MAC del richiedente e il suo IP.
		  L'host A associa il MAC address di C al suo IP address nell'ARP Cache.
		  L'host B (man-in-the-middle) invia un ARP reply ad A che associa l'indirizzo IP di C al suo MAC address.
		  L'host B (man-in-the-middle) invia un ARP reply a C che associa il MAC address di B all'IP di A.
		  Sia C che A aggiornano l'ARP CACHE con il MAC address di B associato che opererà in perfetta logica man in the middle.

	- Port Mirroring

	  Possiamo configurare lo switch in modo da portare il traffico destinato ad una porta in copia su un'altra dove è presente l'host con lo sniffer, lo stesso ragionamento lo possiamo fare per portare un range di porte o una intera VLAN in copia su una sola porta. Non tutti gli switch permettono di fare port mirroring.

- Come analizzare il traffico

	- TCPDump e Wireshark

	  Sono due sniffer che permettono di analizzare e filtrare il traffico (solo per scegliere cosa visualizzare e cosa catturare, non agiscono da firewall). Possono interpretare il traffico in due modi: live e post-mortem, l'intercettazione è sempre live, mentre l'analisi di essa è sempre post mortem. Le funzionalità di wireshark sono simili a quelle di TCPDump ma con una interfaccia grafica e maggiori funzionalità di filtraggio.

	- Promiscous mode

	  Modalità di controllo in cui l'interfaccia di rete o wireless fà passare all'unità centrale (CPU) tutto il traffico osservato sulla rete. Nella modalità non promiscua, invece, l'interfaccia di rete lascia passare alla CPU solo i messaggi che contengono nel campo del destinatario l'indirizzo dell'interfaccia, scartando, quindi, tutti gli altri che non le sono destinati.

## 2. Politiche di Sicurezza e Controllo Accessi

### Dove fare filtraggio

- Border Router

  Primo punto di sbarramento della propria rete, permette di centralizzare buona parte dei controlli di sicurezza. Tipicamente essendo un router o uno switch, sono di livello 3, rendendo disponibili i meccanismi di controllo accessi sulla base di IP e delle porte TCP/ UDP, che però risultano stateless.
  Bisogna tener presente di non eccedere nei controlli, nel senso che un eccesso di politiche applicate su un dispositivo che non ha le prestazioni per poterlo fare, potrebbe tradursi in bottleneck.

- Firewall

  Termine inglese che significa "muro tagliafuoco", è la principale componente passiva di difesa perimetrale. Per passivo si intende che non ha un ruolo attivo nella difesa, ovvero non ha una reazione proattiva nei confronti di un attacco, ma si comporta passivamente bloccando il traffico relativo all'attacco.
  Ha compiti di security enforcing con lo scopo di controllare il traffico tra due o più reti:
  Permette solo quello autorizzato da politiche di sicurezza.
  Rileva e segnala eventuali tentativi di violazione della politica di sicurezza.
  Svolge eventualmente funzioni aggiuntive di auditing e accounting.
  Eventualmente svolge funzioni di collegamento tra due o più segmenti di rete differenti (ovvero agisce da proxy e content filter per mediare l'accesso a specifiche applicazioni, anche grazie al NAT, Network Address Translator)
  Non solo ci proteggiamo dal traffico interno, ma proteggiamo anche il traffico esterno dal traffico interno, quindi controllo ciò che esce dal mio dominio di sicurezza.
  PRO:
  Statefull (un router è stateless).
  Policy centralizzate.
  Possibilità di ispezionare il traffico fino al livello aplicazione.
  CONTRO: Aggravio nelle prestazioni generale della rete.

	- Modalità Routed

	  Opera a livello 3, segmenta le reti diverse sulla base degli indirizzi IP. Si presenta come un dispositivo di livello 3 ed ha quindi bisogno di un indirizzo IP su ogni interfaccia, il traffico viene instradato su base IP sulle varie interfacce di rete.

	- Modalità Trasparente

	  Opera a livello 2, segmenta la rete sulla base del MAC address. Quindi non fà routing su base IP address.Risulta completamente trasparente nella rete, nonostante ogni interfaccia individui comunque un segmento VLAN differente anche se associate alla stessa rete IP. I segmenti connessi alle interfacce devono essere sulla stessa subnet di livello 3 e i dispositivi devono puntare al router davanti al firewall( che verrà attraversato in maniera trasparente). 
	  Scegliere un firewall trasparente assicura vantaggi di avere un firewall totalmente invisibile all'esterno ma non ha le funzionalità di NAT e protocollo di routing associati, IP, DHCP, QoS, VPN, Multicast etc.

- REGOLA D'ORO DEL FILTRAGGIO

  I controlli vanno messi il più vicino possibile all'origine del traffico che bisogna controllare/filtrare, così non ho un aggravio delle prestazioni su tutta la rete e riesco a definire policy ad hoc per quel dominio di sicurezza.

### Tipi di filtraggio

- Filtraggio Stateless/ Packet Inspection

  Avviene solo sulla base di IP(sorgente e destinazione), porta e protocollo (TCP/ UDP). Non si ha nessuna percezione del flusso di pacchetti che fanno parte di una connessione end-to-end.

- Filtraggio Stateful/ Session Filtering

  Quando viene stabilita una connessione (three-way-handshake), allora queste informazioni diventano entry di una tabella di stato (stateful table).
  In tale modo si può fare session filtering, ovvero man mano che arrivano i pacchetti, non sono visti come pacchetti indipendenti ma come appartenenti ad una sessione.
  Ad esempio si può verificare se un messaggio destinato a un dispositivo interno delicato, sia frutto o meno di una connessione partita dall'interno e quindi controllo nella stateful table se esiste una entry con ip sorgente interno, ip destinazione del messaggio arrivato e con clausola ESTABLISHED.

- Content Filtering

  Filtraggio di contenuti indesiderati attraverso l'ispezione delle URL (livello applicazione) o addirittura del contenuto, quindi il firewall esegue l'ispezione del payload.
  Difficile da applicare se vi è implementata crittografia nelle comunicazione.

	- Deep Packet Inspection (DPI)

	  Forma di filtraggio dei pacchetti dati che esami il payload dei pacchetti alla ricerca di contenuti che non risultano idonei a determinati criteri prestabiliti.
	  La ricerca può avvenire per identificare ed eventualmente agire su anomalie dei protocolli, intrusioni, worms, per ottimizzare il traffico sulla rete o raccogliere dati statistici.
	  La DPI può operare spaziando dal layer 2, fino al layer 7.

### Politiche di filtraggio

- Tipi di Policy

	- Deny All

	  Tutto ciò che non è specificatamente permesso è negato, permette una elevata sicurezza.

	- Allow All

	  Tutto ciò che non è specificatamente negato è permesso, facilita la gestione. Policy che viene usata poco negli ambiti di sicurezza, tuttavia è ultile per troubleshooting e traffic shaping.

- Controllo Accessi livello Utente/ Architettura AAA

  Autentication, Authorization, Accounting (AAA), sono architetture che si basano sulla separazione delle fasi di controllo ad accessi in:
  Authentication, per identificare l'utente.
  Authorization, per definire a quali risorse può accedere l'utente.
  Accounting, ovvero tener traccia delle operazioni effettuate dall'utente.

- Modello Controllo Accessi

  Fare controllo accessi significa proteggere il sistema sulla base di determinate politiche rappresentabili tramite la tripla M=(S, O, A), dove:
  S è l'insieme di entità o soggetti (entità attive).
  O è l'insieme di oggetti (entità passive).
  A  è l'insieme di regole che specificano le azioni che possono compiere i soggetti.
  Ogni soggetto può essere anche oggetto. 
  Il tutto può essere rappresentato tramite una matrice del controllo degli accessi (Lampson) dove sulle righe abbiamo i soggetti e sulle colonne gli oggetti e per ogni casella è inserita la modalità di accesso.

	- Access Contorl List (ACL)

	  Si prende ogni colonna della matrice di Lampson, cioè ad ogni oggetto si associano i soggetti che possono accedervi e in che modo, e.g.
	  F1 = { ( s1, rw); (s2, r) }.
	  Si basano sull'autenticazione, quindi bisogna autenticare l'utente, ogni oggetto avrà la lista dei possibili fruitori (è il modello più utilizzato).

		- ACL per Packet Filtering

		  Possiamo fare filtraggio dei pacchetti sui dispositivi di demarcazione attraverso le ACL. Gli elementi che possono essere oggetto di controllo sono:
		  Indirizzi sorgente e destinazione (IP o MAC).
		  Numero di porta (TCP o UDP ad esempio).
		  Protocollo (IP, TCP, etc.).
		  Tipo di messaggio.
		  Data e ora (ad esempio di notte è chiuso il traffico in uscita).

			- Sintassi delle ACL

			  Lista di istruzioni da applicare ad un'interfaccia in ciascuna delle direzioni (ingresso/ uscita) con lo scopo di gestire il traffico filtrando i pacchetti che entrano ed escono.
			   Le azioni ammissibili sono permit o deny.
			  Le ACL operano secondo ricerca lunga, ovvero le ACL vengono elaborate finché non c'è un matching. L'ordinamento è in base all'ordine in cui vengono inserite le clausole (quando si scrivono le ACL è importante l'ordine). Appena un pacchetto soddisfa una delle condizioni, la valutazione si interrompe e il resto delle ACL non viene preso in considerazione.Se il pacchetto non soddisfa nessuna delle condizioni viene scartato ("deny any any"). Per il modo in cui vengono eseguite le ACL, è buona prassi inserire all'inizio le istruzioni più restrittive.

				- ACL Standard

				  Effettuano controllo esclusivamente sull'indirizzo sorgente. Nel caso si tratti di un singolo indirizzo basta scrivere l'IP, se sono un range di IP, si può inserire una wildcard mask che definisca la dimensione (intesa come intervallo di indirizzi della subnet) a cui appartiene l'IP.

				- ACL Estese

				  Controllo accessi su base indirizzo sorgente, indirizzo destinazione, porta sorgente, porta destinazione e protocollo utilizzato.
				  Una caratteristica importante delle ACL estese è quella della stateful inspection, cioè possiamo capire se un pacchetto TCP fa parte di una sessione di comunicazione preesistente. In questo modo si può capire se i dati in entrata fanno parte di una sessione iniziata dall'interno (three-way-handshake), per fare questo basta definire nella clausola la keywork ESTABLISHED. 
				  Meccanismo utile quando si vuole verificare che i pacchetti in arrivo siano frutto di una richiesta partita dall'interno e non di risposte non richieste dall'interno.

			- Problemi Spoofing IP sorgente

			  L'indirizzo IP è attualmente il meccanismo cardine per identificare la provenienza del traffico, la falsificazione di tale dato è alla base di una buona parte degli attacchi e delle azioni ostili. Lo spoofing consiste nella falsificazione dell'indirizzo sorgente.
			  Gli ISP per impedire ciò dovrebbero applicare ACL che non fanno uscire dei pacchetti dal proprio dominio se l'indirizzo sorgente non appartiene ai loro indirizzi assegnati. 
			  Basta che uno ISP non fà ciò ed è tutto vanificato.

	- Capability List

	  Una capability è un "ticket" o diritto di accesso per ogni risorsa, queste vengono rappresentate mediante righe della matrice e ogni riga rappresenta la capacità di un utente di fare una certa operazione su un oggetto. E.g.
	  S1 = { (f2, rw); (f4, w); (f3, rw)}

- Network Access Control (NAC)

  Approccio moderno al controllo accessi nel contesto di una rete, tende a unificare su un'unica piattaforma di controllo accessi le tecnologie di sicurezza operanti a livello di end-point (anti-virus, intrusion detection), i meccanismi a livello di autenticazione di sistema (password, biometria etc.) e i meccanismi tradizionali per il controllo della sicurezza in rete.
  L'obiettivo è controllare la sicurezza degli end-point (macchine terminali) facendo in modo che sulla rete ci siano solamente le macchine che sono compatibili con la politica di sicurezza prestabilita. 
  Tipicamente i dispositivi non compatibili con le policy del NAC vengono messi in quarantena( possono solo aggiornarsi).
  Sistema utile per la protezione delle minacce interne, poiché limita gli host vulnerabili che non rispettano le policy di sicurezza prestabilite.

### Firewall di Nuova Generazione

- Limiti di un firewall tradizionale

  Non protegge da virus e trojan.
  Non protegge da attacchi sconosciuti(0-day).
  Non protegge da connessioni che non lo attraversano (backdoor).
  Non lo protegge da attacchi interni ( ovvero il 75 % degli attacchi).
  Non lo protegge da attacchi fisici.
  Non può essere utilizzato come unico punto di difesa.

- Caratteristiche dei Firewall di Nuova Generazione

  Compatibilità con firewall di prima generazione.
  Funzionalità di Intrusion Prevention.
  Full stack visibility & management.
  Extra firewall Intelligence (integrazione con sistemi di monitoraggio esterni).
  Integrazioni con user directories.

	- Classificazione del traffico

	  Bisogna comprendere il traffico, cioè associare il traffico ad una specifica applicazione (non più sulla base delle porte perché si può fare protocol obfuscation). 
	  Per classificare il traffico bisogna riconoscere a livello protocollare specifiche applicazioni, come ad esempio riconoscere comunicazione Tor, un colloquio Skype, etc.

		- Cisco NBAR

		  Network Based Application Recognition (NBAR) è un motore di classificazione disponibile solo su firewall e router Cisco per la classificazione del traffico in tempo reale tramite deep packet inspection e payload analyis. Può verificare quindi il traffico per capire il tipo di applicazione a cui appartiene.
		  Si può anche limitare in banda un determinato tipo di traffico, oltre che rilevare ad esempio in uno specifico traffico HTTP un determinato pattern (payload inspection).

### Intrusion

Intrusion = insieme di azioni mirate a compromettere la sicurezza di uno specifico target o risorsa in rete ed in particolare a danneggiare:
L'integrita, danneggiamento o modifica della risorsa.
Confidenzialità, violazione privacy ed estrazione dei dati.
Disponibilità, Denial of Service.

- Intrusion Detection System

  Sistemi basati sul concetto di poter andare a rilevare tempestivamente un'attività anomala riconoscendola come intrusione. Identificato l'evento senza però intervenire, l'IDS monitore il traffico offline e genera un allarme (log) quando rileva traffico dannoso.
  Dispositivo passivo perché si limita ad analizzare il flusso di traffico attraverso vari punti di intercettazione nella rete ( non è quindi attraversato dal traffico e consente comunque il transito e l'attività di traffico dannoso).

- Intrusion Prevention System

  Sistema attivo, quindi il traffico deve attraversarlo, tipicamente ha una componente IDS interna che rileva l'attività sospetta, però anziché segnalarla solo, reagisce ad essa resettando la connessione o riprogrammando il firewall in modo da bloccare il traffico di rete fonte potenzialmente dannosa.
  Quindi abbiamo la capacità di bloccare dinamicamente gli attacchi. Possiamo ritrovare i seguenti meccanismi di difesa attiva:
  Rilevamento: identifica in tempo reale gli attacchi dannosi alla rete e alle risorse host.
  Prevenzione: interrompe l'esecuzione dell'attacco rilevato.
  Reazione: immunizza il sistema da attacchi futuri da una fonte malevola.

- IDS/ IPS vs Firewall

  Entrambi preposti a controllare la sicurezza di una rete.
  Un firewall di nuova generazione può rilevare gli attacchi o intrusioni proveniente dall'esterno ed intervenire per impediare che si verifichino.
  Tipicamente i firewall limitano l'accesso tra segmenti di rete associate a domini di sicurezza differenti per prevenire intrusioni e non segnalano un attacco proveniente all'interno. Un IDS/ IPS può invece rilevare attacchi che hanno origine dall'interno.

- IPS vs IDS

  IDS PRO: nessun impatto sulla rete in termini di prestazioni e nessun impatto in caso di guasto della componente.
  IPS PRO: blocca i pacchetti durante l'attacco.
  IDS CONTRO: Non blocca i pacchetti ostili, li segnala solo
  IPS CONTRO: impatta sulle prestazioni di rete e un guasto o sovraccarico influiscono su tutta la rete.

## 3. Attacchi in Rete

### Attacchi Attivi

Gli attacchi attivi sono gli attacchi che sono percepibili e che possono essere rilevati facilmente da un sistema di IDS.

- Network Scanning

  Prima di effettuare l'attacco abbiamo diverse fasi:
  Discovery: scoprire la struttura della rete.
  Vulnerability e service assesment: scoprire eventuali vulnerabilità.
  Firewalking: ovvero non solo capire cosa c'è dall'altro lato, ma anche come funziona e come è protetto al fine di ricostruire le policy ACL della vittima. Ad esempio quando un messaggio viene scartato dal firewall, esso va a ritroso con un messaggio ICMP Prohibited, che può essere utilzzato per ricavare le policy.
  Vale il concetto di security obscurity: quando più è invisibile la struttura, quando più sono nascoste le misure di protezione, tanto più si guadagna un vantaggio di posizione.

	- Passive Scanning

	  Si basa sull'analisi del traffico di rete, eseguita ad esempio attraverso strumenti di sniffing come wireshark. Dall'analisi dei pacchetti catturati sarà possibile conoscere gli indirizzi IP/ MAC di host attivi e le porte realmente utilizzate rispetto quelle attive.

	- Active Scanning

	  Basato sull'uso di uno strumento attivo per scoprire host e servizi attivi su una rete third party, creando così una "mappa" della stessa. 
	  Per raggiungere tale obiettivo, abbiamo vari strumenti di scansione:
	  Inviare pacchetti appositamente predisposti all'host di destinazione.
	  Analizzare le risposte ottenute che gli consentono di individuare le caratteristiche di interesse ed effettuare il mapping.
	  NMAP è un tool che realizza buona parte delle buone tecniche di scansione. Ci permette anche di capire se una porta è chiusa perché non è attiva o è filtrata.

		- Network Scan

		  Tecniche per ottenere informazioni sulla struttura della rete. Il primo passo prima di individuazione dei sistemi vulnerabili presenti su di una rete, è capire quali sono gli host attivi.

			- UDP Network Mapping

			  Servizio deprecato, basato sull'invio ad una macchina qualsiasi sulla porta 6 di una ECHO Request UDP e la macchina deve rispondere a ritroso con un ECHO Reply UDP. 
			  Se mi arriva tale messaggio so che la macchina esiste, mi basta mandare la request ad un indirizzo casuale di quel dominio di IP per vedere se esiste un host attivo.

			- ICMP Network Mapping

			  Si invia un ECHO-Request (ping) ad una macchina casuale, se è attiva risponderà con ECHO-Reply. Si può bloccare con un ACL non consentendo il ping dall'esterno.

			- TCP Stealth Network Mapping

			  Sfrutto il protocollo three-way-handshake TCP, ogni volta che un host riceve un SYN-ACK su una qualsiasi porta, esso deve rispondere con un RST per restaurare un nuovo three-way-handshake. Quindi se ricevo RST l'host esiste. Posso bloccare il traffico SYN-ACK fuori sequenza con la clausola ESTABLISHED nella ACL, così il firewall si accorge che non è conseguenza di un nessun SYN partito dall'interno e blocca il pacchetto.

			- ICMP Traceroute Network Mapping

			  Traceroute: ricavare il percorso seguito dai pacchetti sulle reti, ovvero gli indirizzi IP di ogni router attraversato per raggiungere il destinatario. Si imposta anche il numero di hop massimi tramite TTL.
			  Funzionamento protocollo TraceRoute:
			  Quando si invia un pacchetto al target di cui si vuole ricavare il percorso di traceroute con il campo TTL impostato ad 1.  Il primo router costatando che il campo TTL ha raggiunto 0, invierà un errore al mittente (ICMP Time Exceeded). L'applicazione memorizzerà l'IP del primo router, quindi invierà un nuovo pacchetto con TTL impostato a 2. L'operazione verrà ripetuta finché non sarà arrivata al destinatario, che invierà un ICMP Echo Reply.
			  Nel caso ci sia un firewall a bloccare l'avanzata, riceveremo secondo protocollo un messaggio "destinazione non raggiungibile", quindi oltre a cpaire gli host attivi, possiamo capire anche i router intermedi, capendo i router anteposti prima del firewall che protegge la rete.

			- Firewalking Traceroute Network Mapping

			  Una volta rilevato il firewall tramite la tecnica ICMP Traceroute Network Mapping, si può andare a fare firewalking, ovvero, andare a capire le policy di sicurezza implementate dal firewall.
			  Funzionamento:
			  Si inviano pacchetti ICMP alla rete interna, quando tali pacchetti non sono accettati, si riceve un messaggio a ritroso ICMP Administratively prohibited, che può essere utilizzato dall'attaccante per ricavare le politiche di packet filtering del firewall.

		- Port Scan

			- UDP Portscan

			  Si invia un messaggio ICMP (ping) su un host scoperto in precedenza su una porta qualsiasi, se risponde con "port unreachable" la porta è chiusa, se invece non risponde, la porta è aperta.

			- TCP Portscan

			  Si sfrutta il fatto che inviando un SYN le porte aperte accettano connessioni mentre le chiuse no. Il three-way-handshake viene completato e dopo sarà possibile chiuderlo regolarmente. Se una porta è chiusa, la vittima risponderà con un RST. In generale tentativi di questo genere vengono loggati.

			- SYN TCP Portscan

			  Per evitare di essere loggati dal sistema, il three-way-handshake non viene completato, quindi si invia il SYN, attendendo il SYN-ACK corrispondente che mi indica che la porta è aperta e dopo ciò, chiudo subito la connessione.

			- NON-SYN-ACK-RST TCP Scan

			  Sfrutta il fatto che secondo lo standard RFC 793, un host che riceve un pacchetto con flag FIN attivo, nel caso in cui la porta sia chiusa debba rispondere con flag RST attivo, mentre nel caso sia chiusa, ignori semplicemente il pacchetto.

			- TCP Decoy Scan

			  La reale provenienza della scansione è mascherata attraverso l'invio di un enorme numero di altri pacchetti di scansione da indirizzi spoofati, nascondendo così l'autore.

- Interruzione Servizi (DoS)

  Attacco che compromettere la disponibilità di apparati o di connessioni di rete tenendoli impegnati in operazioni inutili ed onerose o saturando la capacità disponibile.

	- Tipi di attacchi DoS

		- Volumetrici/ Bandwidth Saturation

		  Caratterizzati da un elevato numero di pacchetti inviati al fine di saturare la banda.

			- Flood Attack

			  Vengono inviati pacchetti UDP, TCP, ICMP spoofando gli indirizzi sorgenti. 
			  Un esempio è l'ICMP Flooding, dove vengono inviati un numero elevato di messaggi ICMP generando il sovraccarico elaborativo di router e hosts.
			  Si blocca con un filtraggio in banda a specifici flussi di traffico individuati da ACLs.
			  Durante ICMP flooding posso limitare la banda dei flussi a traffico relativo al protocollo ICMP

			- Reflection Attack

			  Non si genera direttamente il flusso di pacchetti verso la vittima, ma si sfrutta un terzo host che genera il flusso di pacchetti verso la vittima, questo effetto è chiamato "riflessione".

			- Amplification Attack

			  Realizzato sfruttando elementi di rete non configurati correttamente, ad esempio inviando messaggi di broadcast ad una intera rete con ip source quello della vittima.

				- Broadcast Amplification/ Smurfing Attack

				  Un agente spoofa l'indirizzo sorgente con quello della vittima e invia in broadcast messaggi ICMP echo-request ad una subnet di grandi dimensioni.  L'intera subnet target risponderà per intero alla vittima target.
				  Per difendermi da questo attacco, la subnet deve bloccare il traffico esplicitamente destinato a indirzzi broadcast.

				- DNS Amplification

				  Sfrutta le query ricorsive DNS.
				  L'attaccante si attribuisce l'indirizzo IP della vittima chiedendo informazioni riguardanti una intera zona, verrà risposto con i nameserver dell'intera zona, permettendo un fattore teoricamente maggior di 30. 
				  Per difendere basta non autorizzare query ricorsive per host non affidabili.

				- NTP Amplification

				  Network Time Protocol (NTP) è un protocollo per sincronizzare gli orologi dei computer all'interno di una subnet. Il servizio NTP supporta una query per richiedere i dati sul traffico dei client connessi attraverso il comando "monlist".
				  Quindi si può inviare una richiesta get monolist al server NTP, utilizzando come sorgente l'indirizzo IP della vittima.
				  Per bloccare questo attacco basta autorizzare tale comando solo ai server NTP Trusted.

				- Memcache Amplification

				  Sistema di caching distribuito che consente il caching in memoria di oggetti in rete. Quindi basta inviare una query per richiedere gli oggetti con l'IP della vittima per causarle un danno.

		- Non volumetrici/ Resource Starvation

		  Si tende a saturare altre risorse del sistema piuttosto che i link della rete. 
		  Tali componenti possono essere tempo di CPU, memoria di sistema, spazio su disco, handles di file, etc.
		  In generale un sistema sotto questo attacco diventa inusabile oppure collassa. In questo caso l'aggressore ha accesso lecito in parte o totale ad una risorsa di sistema e abusando di questa risorsa riesce a consumare ulteriori risorse, provocando così il rifiuto di servizio da parte degli altri utenti. Sono attacchi difficili da rilevare.

			- Attacchi Dos Low-Rate

			  Invio di richieste HTTP parziali o malformate nel contesto di una sessione in grado di creare problemi al server target (cash, congestione o carico CPU).
			  Un esempio è Deeply-Nested XML, ovvero, si fà l'exploiting di messaggi SOAP inserendo un gran numero di tag annidati all'interno del message body. 
			  Il parser XML andrà in difficoltà perché impiegherà più CPU per elaborare tali richieste.
			  Inviamo flussi costanti a basso rate o burst periodici di durata limitata.
			  Col tempo questi attacchi hanno effetti notevoli, poiché aumentano il consumo energetico essendo la CPU utilizzata al massimo della sua capacità e portano quindi all'usura della macchina.

			- Slowloris

			  Prova a mantenere le connessioni aperte ad un server web e a trattenerle aperte il più lungo possibile.
			  Per fare ciò, apre una connessione e invia richieste parziali. Periodicamente invierà intestazioni HTTP aggiungendo pezzi alla richiesta ma mai completando la richiesta, in questo modo appesantirà il server.

			- Landing

			  Basato sull'invio di TCP SYN con l'indirizzo e la porta impostati identici con l'indirizzo della vittima. Può causare il loop di invio e ricezione dei pacchetti dallo stesso server portandolo al down.

			- Ping Of Death

			  Si basa sulla logica di ricostruzione di pacchetti IP dai frammenti. 
			  Consiste di invio di un pacchetto IP con una taglia maggiore di quella consentita dalla grandezza massima di un pacchetto  consentito dall'host vittima, in questo modo causo un buffer overflow con conseguente blocco del servizio o in casi più gravi di crash del sistema.

			- TearDrop

			  Consiste nell'inserire in alcuni pacchetti frammenti di spaziatura errate.
			  In questo modo al momento dell'assemblaggio vi saranon dei vuoti o degli intervalli in overlapping che possono rendere instabile il sistema.

			- TCP SYN Flooding

			  Tecnica caratterizzata dall'apertura di un numero elevato di connessioni da indirizzi diversi spoofati verso la vittima cercando di evitare l'ACK di chiusura del TCP three-way-handshake al fine di saturare la coda di connessione.
			  Ogni server ha una queue di connessioni simultanee che possono essere mantenute aperte così da riempirla, in modo che il server neghi ulteriori tentativi di connessione leciti.

			- SSL/ TLS Handshake Attack

			  Sfrutta la differenza di peso computazionale per le operazioni di cifratura e decifratura RSA. In genere l'effort per decifrare è 10 volte superiore a quello per cifrare.

			- SYN Flood con BackScattering

			  Combina la logica del SYN flood con la riflessione. 
			  Consiste nell'invio di SYN con indirizzi sorgente spoofati con quello della vittima e causando l'invio di SYN di risposta alla stessa vittima.
			  Si può reagire a questo tipo di attacco limitando in banda il flusso di traffico offensivo evitando di influenzare le sessioni TCP già completamente stabilite.

			- TCP con Flood

			  Consiste nel completare la connessione TCP e poi inviare piccole richieste HTTP Head e ripetere ciò.

			- Diagnostic Port Dos

			  Consiste nell'invio di elevate quantità di traffico TCP o UDP sulle porte di diagnostica dei router.
			  Può avere notevole impatto sia sulla rete che sul carico elaborativo del router stesso fino a causarne il blocco o il degradare delle prestazioni.
			  Si può evitare disabilitando i servizi di "diagnostic port".

	- Botnets

	  A seguito di un attacco (eventualmente tramite worm) sull'host compromesso viene installato un programma definito bot.
	  Il bot fornisce all'attaccante un meccanismo di controllo remoto sull'host compromesso, questa tecnica viene utilizzata per creare reti di host compromessi (botnet) comandate da una infrasttruttura Command and Control (C&C).

		- Agent-Handler

		  In questo modello gli agenti sono i bot, ovvero le entità che realizzano fisicamente/ direttamente l'attacco generando flussi di traffico verso i target. 
		  Poi ci sono gli host intermedi, chiamati handler, che schermano il bot master che controlla tutto e ricevono comandi da esso per poi propagarli ai bots.

		- Web-Based

		  Anzichè usare gli handler classici è possibile usare dei web server intermedi. 
		  Gli agent in attesa di comandi si connettono periodicamente a uno o più server legittimi e solo quando trovano una keywork specifica, effettuano l'attacco.

		- IRC-Based

		  Si utilizza un canale IRC (canale chat, canale pubblico in cui tutti possono scrivere), i bot sono in ascolto su questo canale e quando l'attacker scrive una determinata keyword nel canale, i bot la leggono e generano l'azione associata a tale keyword.

		- P2P-Based

		  Si utilizza una rete P2P dove l'attaccante e tutti i bot fanno parte della stessa rete P2P con ruoli diversi. L'attaccante è l'unico che può pubblicare un determinato contenuto che viene utilizzato dai singoli bot per individuare una logica di azione .

	- Difesa Attachi DoS

		- Mitigazione Statica

		  Permette di contrastare l'attacco tramite policy statiche (ACLs), quindi si stabiliscono regole di filtraggio.
		  L'IDS non offre alcuna mitigazione, si limita a segnalare l'evento.
		  Per eseguire la mitigazione statica è utile anche un firewall tradizionale, che però, risulta efficace con attacchi di capacità limitata, quando si arriva a capacità superiore, il router è lo strumento ideale.
		  Con l'aumentare del traffico degli attacchi diventano sempre più utili i sistemi IPS o i firewall di nuova generazione (anche per limitare in banda determinate applicazioni).
		  Ad esempio durante ICMP flooding posso limitare la banda dei flussi relativi a ICMP ECHO e UNREACHABLE (anche a seguito di un rilevamento da parte di un IPS).

			- ACL Smurfing

			  Lato vittima: La vittima ha ricevuto un elevatissimo numero di echo-reply rispetto le echo-request. Gli indirizzi sorgenti degli echo reply sono raggruppati in un insieme limitato di origini che individuano gli amplificatori dovuti a un broadcast.
			  Lato attaccante inconsapevole: L'amplificatore, invece, avrà ricevuto un numero di echo-request elevato rispetto alle echo-reply.  Gli indirizzi di destinazione degli echo-request sono diretti alla vittima. Si riscontra un elevato numero di broadcast sulla rete LAN interna.

			- ACL SYN Flood

			  Il numero di pacchetti relativi alla fase di 3-way-handshake supera abbondatemente quello di pacchetti su connessioni già stabilite.

			- ACL Ping Flood

			  Il numero di echo-request e reply ricevute è elevato con i request che in genere superano i reply. Inoltre gli indirizzi sorgente non sono oggetto di spoofing.

		- Mitigazione Dinamica

		  In questi casi si paga di mitigazione "network centrica" (o reazione coordinata in rete), cioè, non solo i firewall, gli IPS o i router si oppongono all'attacco, ma anche l'intera rete in maniera cooperativa reagisce in accordo a policy comuni.
		  La reazione coordinata in rete prevede una serie di fasi:
		  Fase di detection: si parte da una fase di detection in cui vanno rilevati gli attacchi DDoS mediante tecniche di anomaly detection viste in precedenza.
		  Fase di diversione del traffico: in questa fase, a partire dalla piattaforma di detection, bisogna avviare una procedura di instradamento/ diversione del traffico verso i centri di analisi e filtraggio (centri di cleaning) chiamati sinkhole per ripulire il traffico.
		  Fase di cleaning/ filtraggio: quando il traffico arriva nei centri di cleaning, vengono applicati dei filtri al traffico interessato per poter eliminare la parte ostile e far passare il traffico legittimo.
		  Fase di reinjection/ reinstradamento: infine, la piattaforma garantisce il corretto re-instradamento del traffico ripulito verso il target.

			- Mitigazione via BGP Blackholing

			  Border Gateway Protocol, o BGP, durante un attacco DoS, può aiutare ad applicare politiche di ridirezione.
			  Gli annunci BGP governano l'instradamento del traffico anche durante un DDoS.  Viene annunciato l'IP della vittima e propagato un messaggio di BLACKHOLE community. Tutti i router che ricevono questo annuncio bloccano il traffico in maniera totale per questa route.
			  Il BGP Blackholing non è in grado di lavorare in maniera selettiva, quindi bloccherà tutto il traffico per quella route.

			- Mitigazione via BGP Flowspec

			  Ci permette di decidere su quali flussi di traffico agire in modo selettivo, richiede  il supporto di nuove address-family che permettono un filtraggio più granulare (type) e di specifiche azioni da compiere.

### Man In The Middle (MITM)

- Hijacking

  Consiste nel dirottare (hijacking) il traffico generato durante una comunicazione tra due host verso un terzo host (attaccante) il quale finge di essere l'end-point legittiomo della comunicazione allo scopo di:
  Modificare il contenuto della comunicazione.
  Generare messaggi in maniera fraudolenta (injection).

	- DHCP Spoofing

	  Dynamic Host Configuration Protocol (DHCP), è un protocollo applicativo che permette ai dispositivi o terminali di una certe rete locale di ricevere automaticamente ad ogni richiesta di accesso  da una rete IP (quale una LAN), la configurazione IP necessaria per stabilire una connessione e operare su una rete più ampia basata su Internet Protocol.
	  Questo protocollo è stateless, per cui quando si intercetta facendo sniffing sulla rete una macchina che ha inviato una richiesta DHCP (che avvengono in broadcast), prima che risponda il vero server può inviare una informazione fraudolenta con un grado massimo di affidabilità in modo da modificare alcune informazioni come Default Gateway e DNS (se risponderà il server vero, il grado di affidabilità sarà per forza minore e non verrà preso in considerazione). Facendo così tutto il traffico della rete LAN passerà attraverso l'attaccante che si comporterà da Man In The Middle.

	- IRDP Spoofing

	  Il protocollo IRDP (ICMP Router Discovery Protocol) viene usato nel momento in cui un host non ha configurato un proprio default gateway o ne ha uno errato, in questo caso la rete se ne rende conto e gli manda un corretto default gateway tramite messaggio "router advertisement" che avrà al suo interno il livello di preferenza e un lifetime. L'attaccante può settare i campi di "lifetime" e "livello di preferenza" al massimo e diventare il nuovo default gateway della vittima operando sempre in logica man in the middle.

	- ICMP Redirect

	  Il protocollo ICMP tra i vari tipi di messaggi di notifica degli errori che esso prevede ha anche il messaggio "redirect". Se in una rete esistono più router in grado di instradare il traffico verso l'esterno, la rete può individuare il percorso ottimale su cui passare e inviare a ritroso un messaggio "redirect" per segnalare un "default gateway" più efficiente. Un attaccante può mandare un messaggio ICMP redirect per farsi ridirigere il traffico sulla propria macchina e operare in logica man in the middle.

	- Injection: TCP Session Hijacking

	  Parliamo della possibilità di aggiungere pacchetto o messaggi ad una connessione full-duplex (bidirezionale).
	  Per un attacco del genere abbiamo bisogno di determinare i numeri di sequenza (sequence number prediction)  dei messaggi TCP per mantenere sincronizzata la connessione.
	  Quindi spiano una connessione TCP già attiva (già è avvenuta il three-way-handshake fra i due host comunicanti) ed è possibile sostituirsi ad uno dei due host.
	  Esempio:
	  C spia la connessione fra A e B e registra i numeri di sequenza dei pacchetti.
	  C blocca B (ad esempio tramite SYN Flood), l'utente B quindi interrompe la sessione con A, mentre A è inconsapevole.
	  C invia pacchetti con il corretto numero di sequenza (che ha spiato in precedenza) con mittente B, in modo che A non si accorga di nulla.
	  In questo modo C può iniettare pacchetti in una sessione pre-esistente.

	- DNS Hijacking

	  I server DNS sono coinvolti essenzialmente nella traduzione di domini negli indirizzi IP corrispondenti.
	  Mantengono una cache locale (con un TTL per l'aging) per risolvere in maniera efficiente i domini.
	  Quando in cache non ci sono informazioni per risolvere la query, il server interroga un altro server e il progetto può procedere in modo iterativo.
	  Sono strutturate in gerarchia rispetto alle proprie zone di autorità a partire dai root server.
	  Il DNS ha una debolezza costruttiva: per rendere il processo di risoluzione più efficiente vengono utilizzate delle cache locali a ciascun sistema DNS (che sia client o server) con TTL assegnato ad ogni entry. Se un attaccasse riuscisse ad iniettare all'interno della cache di un DNS (client o server) delle entry fraudolente, quello che succede è che il DNS risponderà a tutte le query successive con i risultati di queste query.

- Hijacking BGP

  Le tecniche di hijacking possono colpire i meccanismi  di routing, ovvero i protocolli utilizzati dai vari router per scambiarsi informazioni di raggiungibilità.
  Rischi maggiori nei punti di peering dove posso dirottare i flussi di una intera nazione.

	- Route-Flapping

	  Infiltrazione che si può propagare fino all'ultimo router connesso ad Internet.
	  Consiste nell'annunciare route prima tramite un percorso e poi tramite un altro.
	  Causa il reset delle connesisoni BGP, ovvero un resend a tantissimi routers della nuova router che devono aggiornare la route.

	- AS-Path Padding

	  Il percorso BGP AS-Path è un attributo obbligatorio, il che signifca che è presente per tutti i prefissi scambiati tra i BGP. Quando un router BGP invia un aggiornamento a un vicino in un diverso autonomous system (ISP) di rete, aggiunge il proprio numero AS alla parte sinistra del percorso AS. In modo da indicare gli AS che devono essere attraversati prima di giungere a lui. Ci possono essere più percorsi che conducono allo stesso AS.
	  Un attaccante può ridurre la lunghezza dell’AS path per forzare il passaggio del traffico attraverso un'altra route (magari propria) o, annunciare delle route inesistenti.

	- BGP Injection

	  Iniezione di una route fake a livello dell’ISP (livello3) per ottenere una divisione del traffico verso un mio centro di calcolo che poi solo successivamente sarà reinstradato verso la destinazione originaria. Opero in perfetta logica man in the middle su scala mondiale. Posso ricevere traffico da una intera nazione per poi una volta raccolto mandare verso la destinazione originaria.

## 4. Worms

### Definizioni

- Definizione Worms

  Un worm è un agente SW auto-replicante opportunamente studiato per diffondersi attraverso la rete.
  Tipicamente sfrutta vulnerabilità note in servizi molto diffusi, può causare danni significativi come: 
  lancio di attacchi DDoS.
  Installazione di Bot per craere BotNets.
  Accesso o compromissione di dati sensibili.
  I worms sono auto-contenuti e si diffondono in maniera autonoma replicandosi attraverso i link di comunicazione.

- Definizione Trojan

  Fondamentalmente i Trojan non sono virus e non sono destinati a danneggiare o eliminare i file di sistema. Il più delle volte sono programmi considerati sicuri dall'utente che hanno delle backdoor.
  Il loro unico compito è quello di fornire una porta di accesso per programma maligni o utenti malevoli che si possono inserire nel sistema rubando i dati importanti della vittima senza la sua conoscenza e consenso.

- Definizione Virus

  I virus hanno la capacità di replicarsi, ma lo fanno danneggiando i file presenti sul computer vittima. Il loro principale punto debole consiste nel fatto che possono entrare in azione solo se hanno il supporto di un pogramma ospite a cui attaccarsi, ad esempio file eseguibili, canzoni e video e viaggiano su Internet attraverso questi "ospiti".

### Classificazione Worms

- Host compute worms

  Interamente contenuti sull'host in cui girano, usano la rete solo per propagarsi.

- Network worms

  Sono su host differenti ed usano la rete per scopi diversi attinenti alla cooperazione al fine di propagarsi e controllare al meglio le macchine su cui risiedono.

### Meccanismi di Difesa

- Signature Inference

  Visto che il worm si diffonde massivamente, è necessario cercare una signature, ovvero un pattern ricorrente del worm.
  Per trovare il pattern è necessario osservare il traffico e cercare meccanismi automatici e stringhe comuni tra i vari flussi di traffico.
  Questi pattern possono essere utilizzati a scopo di content filtering oppure di content sifting.

- Content Sifting

  Assumiamo l'esistenza di una bitstring univoca W in ogni istanza di un particolare worm. Allora definiamo come:
  Content prevalence: W sarà più comune nel traffico rispetto ad altre bitstring della stessa lunghezza.
  Address Dispersion: pacchetti contenenti quella sottostringa W saranno indirizzati ad un numero sproporzionato di source e destination distinte, quindi posso portare il conto di quanti pacchetti contenti W e con source e destination distinte, transitano nella mia rete.
  Il content sifting consiste nel trovare le stringhe W con alta content prevalence e alto address dispersion e poi bloccarne il traffico.

### Strategie di Infezione

- Localized Scanning

  Scansione orientata preferenzialmente ad elementi che risiedono nella stessa subnet della vittima. Tipicamente ci si muove da un datalink all'altro ed appena si riesce a prendere il controllo di una macchina opened, si passa ad un altor datalink.

- Topological Scanning

  Usa informazioni acquisite dagli host già compromessi per individuare nuove vittime. I sistemi P2P sono poco vulnerabili perché hanno tanti nodi poco collegati.

- Hit List Scanning

  Viene raccolta una lista di 10,000- 50,000
  hosts potenzialmente vulnerabili che idealmente godono di buona connettività di rete, prima di poi lanciare la diffusione del worms verso essi.

- Random Permutation Scanning

  Tutti i worm condividono una permutazione pseudocasuale dello spazio di indirizzamento. Ogni macchina infettata attraverso una specifica hit list avvia la scansione partendo da un punto della permutazione.
  Assicura che gli stessi indirizzi non siano oggetto di probing ripetuto.

## 5. Anonimato in Rete

### Onion Routing

L'onion routing è una tecnica di anonimizzazione delle comunicazioni in una rete di telecomunicazioni.
In una rete Onion, i messaggi sono incapsulati in "strati" di crittografia che vengono paragonati a strati di una cipolla, dato l'incapsulamento. 
Il dato criptato viene trasmesso attraverso una serie di nodi, chiamati onion router, ognuno dei quali "sbuccia" via via un singolo strato di crittografia, scoprendo così il contenuto da inviare al prossimo nodo di destinazione del dato.
Il mittente resta anonimo perché ciascun intermediario conosce solo la posizione del nodo immediatamente precedente e del nodo immediatamente successivo.

- Tor (The Onion Router)

  Dal principio di Onion Routing nasce Tor. 
  Abbiamo una rete di overlay basata sull'onion routing che consente di effettuare connessioni anonime in uscita e di fornire servizi nascosti.
  I nodi sono connessi fra loro tramite collegamenti logici (rete virtuale).
  Il nodo di ingresso (entry guard), garantisce l'accesso all'infrastruttura di overlay (di solito sono i più sensibili, quindi saranno selezionati in base alla loro affidabilità nel tempo).
  Mentre il nodo di uscita (exit node) garantisce l'accesso alla global Internet.
  La rete Tor prevede 4 tipologie di nodi:
  Client: In questa configurazione normale di base, Tor gestisce unicamente le connessioni dell'utente permettendogli di collegarsi alla rete Tor.
  Middleman router (o middle relay): è un nodo che getisce il traffico di terzi da e per la rete Tor.
  Exit router (exit relay): è un nodo Tor che gestisce il traffico di terzi verso l'esterno. Si possono definire delle exit policy sulla connessione in uscita all'esterno della rete Tor.
  Bridge router: sono nodi semi-pubblici di tipo sperimentali, sono studiati per permettere ai client di collegarsi anche in presenza di un filtraggio efficace contro Tor (come in Cina). Non compaiono nella lista pubblica ma devono essere richiesti esplicitamente.

	- Configurazione Default

	  Si possono scegliere il numero di relay, per default sono 3. Un numero di relay maggiore diminuisce le prestazioni e aumenta la latenza, inoltre, non migliore di molto la sicurezza e aumenta di utilizzare nodi compromessi.
	  Tutti i dati sono inviati in celle di taglia fissa (se i dati sono di dimensioni minori, viene aggiunto del padding per raggiungere la dimensione fissa), così diventa difficile fare assunzioni sul contenuto in base alla grandezza del pacchetto.

	- Perfect Forward Secrecy

	  Nello scenario in cui venisse usata una coppia di chiave pubblica/ privata negoziata con ogni relay per cifrare il traffico .
	  Se venisse rubata la chiave privata dei 3 nodi relay e venisse anche catturato tutto il traffico futuro e passato, potrebbe essere decifrato.
	  Tor supporta il perfect forward secrecy, ovvero, una proprietà dei protocolli di negozazione delle chiavi che assicura che venga generata una chiave per ogni sessione dell'utente. Questo rende la vita molto difficile a chi un domani voglia attaccare con forza bruta una grossa mole di comunicazioni cifrate, perché l'attaccante dovrebbe calcolare la chiave di cifratura per ogni sessione generata dall'utente durante lo scambio di dati. Quindi se anche riuscisse a catturare la chiave compromettendo le 3 macchine, non sarebbe in grado di decriptare il traffico generato in precedenza, ma solo quello futuro.
	  Negoziazione:
	  Il client node negozia una chiave di sessione con l'entry node, poi invia all'entry node una richiesta di negozziazione della chiave di sessione con un nodo relay, tale negoziazione avverrà comunicando con l'entry node e mai con il nodo relay, la stesso procedimento anche con l'exit node.
	  Finita la negozziazione delle chiavi di sessione il client sarà in grado di fare l'encrypt del dato con tutte e 3 le chiavi.

	- Hidden Services

	  Sono servizi di rete di cui non si conosce la collocazione fisica. 
	  Sono resistenti alla censure e alla violanzione fisica ( non si sà dove è localizzato il server).
	  Diventa difficile risalire a chi pubblica e a chi usufruisce del servizio.
	  La scelta dei relay casuali è sempre composta da 3 nodi, non vengono citati di seguito per semplicità nella trattazione, ma si consideri sempre ogni circuito come composto da 3 nodi.
	  Funzionamento lato server:
	  Affinché i client possano conttatare l'hidden server, esso deve rendere nota la sua esistenza nella rete Tor.  L'hidden service effettua le seguenti operazioni:
	  Sceglie alcuni relay a caso.
	  Stabilisce delle onion routes verso di essi.
	  Chiede loro di fungere da introduction point comunicandogli la propria chiave pubblica.
	  L'hidden server crea un hidden service descriptor contenente:
	  La sua chiave pubblica.
	  Un sommario degli introduction point.
	  Firma questo descriptor con la propria chiave privata.
	  Invia il descriptor ad una directory.
	  Il descriptor verrà successivamente trovato dai client che richiederanno "XYZ.onion", dove XYZ è un nome di 16 caratteri derivato in modo univoco dalla chiave pubblica dell'hidden service.
	  Dopo ciò l'hidden service è attivo.
	  Funzionamento lato client:
	  Il client può iniziare a stabilire la connessione scaricando il descrittore dal directory server. Se esiste un descrittore per "XYZ.onion", il client conoscerà il gruppo di introduction point e la corretta chiave pubblica.
	  Nello stesso momento il client crea un circuito verso un altor relay scelto a caso e gli chiede di fungere da rendezvous point comunicandogli una one-time secret password.
	  Una volta ottenuto il descriptor e pronto il rendezvous point, il client crea un introduction message (cifrato con la chiave pubblica dell'hidden service) contenente l'indirizzo del rendezvous point ed la one-time-secret password.
	  Il client invia questo messaggio ad uno degli introduction point chiedendogli che venga consegnato all'hidden service.
	  L'hidden server decifra l'introduction message del client con la sua chiave privata ed ottiene:
	  L'indirizzo del rendezvous point.
	  La one-time secret password.
	  Il server crea un circuito verso il rendezvous point e gli invia laone-time secret in un rendezvous message per autenticarsi.
	  Nell'ultimo passaggio il rendezvous point notifica al client che la connessione è stabilita con successo; dopodiché il client e l'hidden service possono usare i loro circuiti verso il rendezvous point per comunicare tra di loro. Il rendezvous point inoltre e riceve semplicemente i messaggi da client e server.

	- Attacchi a Tor

	  Tor assicura anonimizzazione a livello 3, ma non a livello applicazione.
	  Inoltre a livello 3 si possono associare sorgente e destinazione attraverso l'analisi del traffico nel punto di entrata da client a entry guard e di uscita da exit node a Internet.
	  Gli attacchi che possiamo avere sono di due tipi:
	  Correlazione temporale: un attaccante è in grado di osservare il traffico sull'entry guard e sull'exit node può prelevare informazioni sui pacchetti e sui loro tempi di invio /ricezione e correlare il traffico osservato rompendo l'anonimato. Alcuni node relay, però, ritardano casualmente alcuni pacchetti.
	  Correlazione sulla dimensione dei pacchetti: difficile in Tor perché sono di dimensione fissa.
	  Il traffico che attraversa la rete Tor è cifrato ma non è detto che lo sia all'uscita dell'Exit node, quando l'exit node toglie l'ultimo strato di cifratura avremo traffico HTTP (se non è stato utilizzato HTTPS) e l'attaccante può catturare le richieste e prelevare informazioni importanti come: user agent, cookie e parametri get e post.

### FreeNet

Rete adattativa di nodi peer-to-peer che si interrogano reciprocamente per immagazzinare e recuperare file di dati identificati da nomi (chiavi) indipendenti dalla locazione. Sistema per scrivere e leggere file da Internet senza che si possa risalire a chi li ha scritti, chi li conserva sul disco e chi li recupera. Formata da server (nodi) paritetici; i nodi normalmente includono un proxy che permette di accedere al server con un form, utilizzando il protocollo HTTP. Freenet, spezzetta, crittografa, duplica, disperde i contenuti del file, e riesce ad eseguire l’operazione inversa per recuperarli. Più un'informazione è richiesta più si moltiplica sui nodi,informazioni non richieste a lungo si cancellano. Il sistema non è completamente deterministico, e non consente di provare che un certo file proviene da un nodo locale e non da un altro nodo della rete.Convergenza veloce (successo nella ricerca) con traffico limitato nel caso medio. Si ferma solo quando il contenuto richiesto viene trovato, scalabilità elevata. Ma Convergenza lenta nel caso peggiore.
Architettura:
struttura peer-to-peer. Ogni utente agisce in maniera indipendente. Non esiste un directory server centrale. I nodi si scambiano direttamente informazioni in una logica query/response. L’informazione non può essere rimossa da Freenet ma solo lasciata “morire” di morte naturale. l’informazione che viene richiesta si moltiplica su più nodi e si “avvicina” ai nodi che la richiedono.
Comunicazione e routing: la comunicazione autenticata e cifrata (DSA E SHA1) fra nodi tramite il protocollo FNP (Freenet Network Protocol). I client applicativi che vogliono utilizzare i servizi Freenet di un nodo locale utilizzano un altro protocollo chiamato FCP (Freenet Client Protocol). Instradamento key-based: ogni nodo richiede una chiave, nell’ordine, ai nodi limitrofi. Ogni nodo costruisce dinamicamente una routing table che contiene gli indirizzi degli altri nodi e le chiavi che si supponga posseggano.

### Virtual Private Network (VPN)

Le VPN sono nate per garantire un servizio di LAN extension realizzando un canale di comunicazione end-to-end sfruttando la rete pubblica (Internet) per sostituire un collegamento dedicato.
Abbiamo collegamenti User-to-Site, quando un utente vuole collegarsi tramite la propria rete aziendale ad Internet.
Oppure, Site-to-Site, quando voglio collegare l'intranet di una organizzazione ad un'altra senza spendere i soldi necessari ad affittare dei collegamenti fisici.
Quindi i collegamenti instaurati da una VPN ci fanno credere che siamo su un collegamento dedicato, quando invece non è così. 
Con la Lan Extension una volta che siamo entrati, accediamo alla rete interna come se fossimo presenti fisicamente sulla rete locale. Un esempio è quando accediamo come utenti remoti alla nostra rete azienda, ci viene attribuito un indirizzo IP della rete interna e diventiamo a tutti gli effetti un nodo della rete stessa con tutte le attribuzioni del caso.
Tutto ciò è possibile anche grazie al tunneling.
Le VPN non sono un servizio di anonimizzazione completo, perché se manomesse, è possibile vedere tutte le connessioni verso di esse.

- Usi della VPN

  Perché usare una VPN?
  Una delle maggiori  ragioni per l'adozione delle VPN è che sono economiche, perché realizzare la connettività remota tramite rete dedicata costa.
  Scalabili, perché creare tante linee fisiche dedicate quando il numero di utenti cresce diventa difficile da gestire.
  Sicurezza, maggior controllo, poiché abbiamo confidenzialità e integrità nonché mutua autenticazione e non ripudio grazie alla crittografia end-to-end.
  Casi d'uso:
  Accesso remoto ad una LAN privata attraverso Internet: ad esempio per effettuare lo smartworking ed accedere da casa alla nostra rete aziendale.
  Connessioni fra reti privati attraverso Internet. Ad esempio una azienda che ha varie reti private sparse sul territorio e vuole connetterle, potrà utilizzare la VPN.
  Connessione tra computers attraverso una Internet, simile al primo caso, ma con la differenza che piuttosto che effettuare una proiezione di una macchina all'interno di una rete, è possibile avere una connessione fra PC.

- Tunneling

  Il concetto chiave di una VPN è il concetto di Tunneling: La VPN è costituita da una serie di connessioni punto-punto trasportate dai canali di Internet. La tecnica di tunneling prevede di incapsulare un protocollo all'interno di un altro protocollo, cioè trasportare i pacchetti associati ad un protocollo all'interno del payload di pacchetti con un altro protocollo (in questo caso pacchetti TCP/IP).
  I due estremi del tunnel effettueranno l'incapsulamento ed il decapsulamento (ad esempio i due router di bordo).

- Semi-anonimato delle VPN

  Quando utilizziamo un servizio VPN(come NordVPN), non usiamo il nostro indirizzo IP reale, ma usiamo l'indirizzo IP della rete VPN a cui siamo collegati che ci fonisce il servizio. Quindoi dal punto di vista dell'identificazione siamo anonimi. In realtà, non completamente anonimi, perché anonimi vuol dire che nonostante possa verificarsi la compromissione di un componente dedicato alla sicurezza/ anonimato, noi dobbiamo sempre restare anonimi. Quindi le VPN sono la stessa cosa di quando ci connettiamo ad un proxy, se il proxy viene compromesso, l'anonimato è annullato.

## 6. E-Mail Security

### Mail Spoofing

Il protocollo Simple Mail Transfer Protocol (SMTP), noto per essere insicuro. Tutte le funzioni di relay SMTP sono svolte da un daemon che aspetta connessioni sulla porta 25 per inviare la posta in uscita o ricevere quella in ingresso (tipiche funzioni di un Mail Transfer Agent, MTA). Quindi collegandosi sulla porta 25 e seguendo il protocollo necessario all'invio di una email, possiamo inviare un messaggio con falso mittente al destinatario.
Su questa Fragilità di basa il concetto di mail spoofing, ovvero falsificare l'email inserendo un falso mittente con lo scopo di raggirare il destinatario (magari ai fini di phishing).
Ho un ulteriore problema di riconoscimento del mittente, ovvero gli open relay. Oltre a cercare di camuffare l’header, gli spammer molto spesso usano una tecnica indicata come 3rd party relay, cioè utilizzano il server di un terzo soggetto (che solitamente non ha alcun legame tra mittente e destinatario) come relayer, ossia come propagatore di un messaggio SMTP. Quindi il mittente reale del messaggio siavvale di un relay che risulta aperto per far partire email di spam. Questo è possibile perché il protocollo SMTP, utilizzato per l'invio dei messaggi di posta, non prevede una autenticazione per poter inviare dei messaggi. Per impedire l’invio tramite il proprio sistema è necessario far autenticare gli utenti prima di permettere l’invio.

### Come capire il mittente di una email?

Uno strumento che ci viene in aiuto per la rilevazione del mittente è l'header del messaggio email:
Partendo dal basso dell'header i tag "to, subject, from" sono totalmente inaffidabili e non hanno alcun peso nella nostra analisi, perché possono essere modificati dall'utente.
Ogni header ha i relay su cui è transitato il messaggio prima di arrivare all'host destinatario. Tale messaggio transitando su più relay crea una catena e man mano che si incontrano dei relay, vengono aggiunti uno sopra l'altro. Anche questa parte può essere modificata.
Quindi, cosa si fà?
L'unico modo per capire qualcosa del mittente è analizzare i relay su cui è transitato il messaggio, ci saranno alcuni affidabili che sono noti provider, mentre altri sconosciuti che non devo prendere in considerazione. Se il relay è affidabile, supponiamo google, salverà nella propria entry table il message-id che è transitato su di lui, quindi in maniera collaborativa, potrei chiedere a google se effettivamente quel messaggio con tale id è transitato sul loro server. Di conseguenza tramite questa rilevazione, avrei conferma di non alterazione, almeno del campo relativo al transito sul relay di google e di conseguenza potrei fidarmi del campo "from" per capire da chi ha ricevuto tale messaggio. Posso fare questo ragionamento a ritroso cercando di costruire i pezzi, se non riesco a risalire al mittente, posso fare dei controlli incrociati su date e nazioni di provenienza basandomi su relay affidabili. Non ho garanzie di successo.

### Tecniche AntiSpam

Black&White-listing e RBL: Controlli effettuati sull'header dei messaggi. Ogni volta che riceve una mail, il server consulta una lista di indirizzi, ha una lista mittenti validi (white) ed una lista di mittenti non sicura (black) e sulla base di questo possiamo decidere se accettare il mittente o meno.
Realtime blocking list (RBL): Possiamo anche affidarci a società terze che gestiscono un database aggiornato con tutti i cattivi mittenti, tipicamente questo servizio è chiamato . Gli RBLs si possono consultare utilizzando protocolli DNS (query e response).
Spam URI realtime Blacklist (SURBL): RBL avanzata che non controlla solo gli header ma anche il body del messaggio alla ricerca di url che riconducano a domini spammer. Ad esempio se è partita una campagna spam per vendita di viagra, venduta da un determinato sito, allora se nella email riconosco tale sito, vuol dire che è spam.
Filtri di contenuti: Il sistema di posta prima di consegnare le mail applica vari algoritmi di analisi dei messaggi e assegna con varie metriche un fattore di confidenza per classificare o meno l'email come spam. Ovviamente è richiesto un training del sistema.
Sender Policy Framework(SPF): consiste nel pubblicare record DNS corrispondenti ai server che possono inviare posta in un particolare dominio, il ricevente può così controllare se il server mittente risulta pubblicato sul DNS secondo le regole di SPF .
Filtri bayesiani: sono basati su principi statisticiad esempio se un pezzo di testo si trova spesso nello spam si assegna una probabilità alta di spam.
GreyListing: Quando cerco di collegarmi al server email per destinare una email e ottengo che il server è indisponibile, il relay mette l'email in una queue per spedirla in un secondo memento. Gli spammer non implementano questo meccanismo perché devono andare veloce, quindi non viene ritentato l'invio. Un server potrebbe gestire una grey list, per ogni messaggio entrante il server crea la tripla < sending IP, sender, recipient>, se il messaggio non è nella grey list,mando un messaggio che il server è non disponibile (405), quando il mittente riceve tale messaggio, prova il rinvio se noon è spam, quindi controllo che tale email sia nella grey-list e la poasso alla whitelist per recapitarla al destinatario.
Razor: rete distribuita collaborativa per identificare lo spam, grazie al contributo degli utenti. Razor mantiene un DB di spam in propagazione che i client possono consultare per filtrare lo spam. L'input degli utenti viene pesato sulla reputazione degli stessi.
Tarpits: Gli spammer vogliono velocità, però l’utilizzatore normale non è sensibile a tale velocità. Si sfrutta questa caratteristica per rallentare in maniera anomala la funzionalità di un delay. In pratica quando un server riceve posta intervallata con tempi umani si comporta normalmente, ma quando riceve posta con una velocità elevata, che caratterizza un inviante non umano, può applicare una politica di tarpits, ovvero intenzionalmente introduce un delay nel tempo di servizio. 
Spam Assasin: Piattaforma Apache Open source per classificare lo spam, implementa un meccanismo di base bayesiano basato sul punteggio. Spam assassin ha introdotto una leadboard chiamato X-Spam-Score per segnalare con un punteggio quanto è probabile che sia spam un determinato messaggio.

## 7. Web Security

### Web Browser e Web Application

Web browser (front-end): può essere attaccato da qualsiasi sito visitato, gli attacchi implicano l'installazione di malware (keylogger, botnes), il furto di documenti e la perdita di dati privati.
Web application (back end): realizzato usando Javascript, PHP, ASP, JSP. Molti bugs potenziali: XSS, SQL Injection, XSRF. Gli attacchi implicano la clonazione di credit card  e il defacing di siti.

### SSL/ TLS

Transport Layer Security (TLS), successore di Secure Sockets Layer (SSL), è un protocollo crittografico di presentazione usato nel campo delle telecomunicazioni e dell'informatica che permette una comunicazione sicura dalla sorgente alla destinazione (end-to-end) su reti TCP/ IP fornendo autenticazione. integrità dei dati e confidenzialità operando al di sopra del layer di trasporto. 
Un esempio di applicazione di SSL/ TLS è il protocollo HTTPS.
Il protocollo TLS consente alle applicazioni client/ server di comunicare attraverso la rete in maniera da prevenire il "tampering" (manomissione) dei dati, la falsificazione e l'intercettazione. In un browser l'autenticazione TLS è unilaterale, ovvero, solo il server si autentica presso il client. Il funzionamento del protocollo TLS può essere suddiviso in tre fasi principali:
Negoziazione fra le parti a riguardo dell'algoritmo da utilizzare.
Scambio delle chiavi (RS Diffie-Hellman) e autenticazione (RSA).
Cifratura simmetrica (DES, AES), autenticazione dei messaggi e interità dei messaggi (SHA1).

- 1. Scambio Certificati

  Server e client vogliono comunicare:	
  Il client chiede la public key al server.
  Il server invia la public key ad una certificate authority dimostrando anche la sua identità.
  La certificate authority emette un certificato digitale (contenente la chiave pubblica del server) firmato con la sua chiave privata (del CA).
  Il server invia il certificato digitale al client che conoscerà la chiave pubblica del CA e quindi riuscirà a ricavare la chiave pubblica del server e a verificarne l'integrità.
  Dopo questa autenticazione il browser indica una connessione sicura mostrando l'icona del lucchetto.
  Nota: Questa autenticazione non è sufficiente a garantire che il sito con cui si è collegati sia quello richiesto. Per esserne sicuri è necessario analizzare il contenuto del certificato rilasciato e controllare la catena di CA che lo firmano. I siti che intendono ingannare l'utente non possono utilizzare il certificato del sito che vogliono impersonare perché non hanno la possibilità di cifrare in modo valido il certificato che utilizza la chiave privata del CA per farlo, quindi solo loro possono.

- 2. Autenticazione Server-Side (TLS 1.3)

  Il server deve farsi verificare dal client e non viceversa ( di solito è così). 
  Funzionamento:
  Il client invia un "Client Hello" message e l'elenco delle chiavi di cifratura supportate, ma fa anche un'ipotesi su quale algoritmo di crittografia utilizzerà il server e invia  anche i dati necessari per accordarsi nella generazione della chiave pubblica basandosi sull'algoritmo che suppone sia scelto.
  Dopo che ha ricevuto il "ClientHello" il server seleziona la suite di crittografia e l'algoritmo di accordo per la chiave. Quindi sarà pronto a generare la chiave dato che ha già la chaive condivisa dal client.
  Quindi il server invia ServerHello confermando che la chiave è stata scelta e il certificato (ora crittografato perché ha una chiave). Ed il messaggio finished.
  Da questo punto in poi possono avviare una comunicazione HTTP.

- Attacchi Man In The Middle

  L’attaccante mettendosi in mezzo alla comunicazione tra cliente e server può vedere tutto il traffico in chiaro e modificarlo a piacimento. Nello specifico l’attaccante intercetta l’invio del hello da parte del Cliente e lo gira al server, il quale risponde con il suo certificato. Allora, l’attaccante invece di inviare il certificato del server al cliente, invia un suo certificato valido, successivamente avviene lo scambio di chiavi e a questo punto l’attaccante può leggere o modificare le richieste fatte dal cliente prima di rigirarle al server. Per ovviare a questo problema anche il client dovrebbe possedere un certificato cosi da essere autenticato dal server.

### Vulnerabilità Lato Server

- Buffer Overflow

  Un buffer overflow si verifica ogni qualvolta l'insieme dei dati è più grande del buffer dove devono essere memorizzati. Ne consegue una sovrascrittura della porzione di memoria successiva al buffer, contenente istruzioni macchina necessarie ad una normale esecuzione del programma. L'obiettivo è quello di sforare la capacità del buffer andando a modificare l'indirizzo della istruzione che segue.
  Per un attacco del genere l'attaccante deve conoscre l'architettura del sistema target (non funziona con linguaggi ad alto livello come java).
  Possono causare segmentation fault nel caso migliore, ma l'attaccante potrebbe anche fare un code injection attack, ovverlo inserire un indirizzo che potrebbe puntare a del codice maligno inserito da un attaccante e la CPU eseguirà l'istruzione che si trova a tale indirizzo.
  Soluzione: Istruction-set Randomization, ovvero, attraverso una chiave di codifica vengono creati un insieme unico di istruzioni randomizzate e tali nuove istruzioni vanno a sostituire il codice sorgente del programma originale, così l'attaccante non riconoscerà il "linguaggio" utilizzato.

- SQL Injection Attack

  Tecnica di code injection usata per attaccare applicazioni di gestione dati. Con tale tecnica vengono inserite delle stringhe SQL malevole all'interno di campi di input in modo che queste ultime vengano poi eseguite. Esso sfrutta le vulnerabilità di sicurezza del codice mal scritto di una applicazione, ad esempio quando l'input utente non è correttamente filtrato da "caratteri di escape" contenuti nelle stringhe SQL oppure non è fortemente tipizzato, può ricevere degli input insapettati.
  Soluzioni:
  Si possono impedire l'inserimento di caratteri speciali e limitare la lunghezza dell'input.
  Si può usare SQL parametrizzato, cioè si può costruire una query SQL con escaping di argomenti fatto a priori.
  SQL randomization: Si inserisce un proxy fra client e server che traduce la query trasformandola in una query pulita prima di mandarla al client.

### Vulnerabilità lato Client/ Server - Cross-Site-Scripting (XSS)

Vulnerabilità che affligge i siti web dinamici con un insufficiente controllo dell'input nei form. Permette di inserire o eseguire codice lato client. Qualsiasi pagina web che esegue il rendering HTML e contenente l'input dell'utente è vulnerabile.
Trovando il modo di iniettare script malevoli su un sito attendibile, l'utente malintenzionato può:
Eseguire script dannosi nel browser web di un client.
Inserire tag come <script>, <object>, <applet>, <form> e <embed>.
Rubare informazioni sulla sessione Web e cookie di autenticazione.
Accedere al computer client.
Due tipi di attacco:
Reflected XSS (non persistente), ovvero i dati forniti dall'utente ( di solito tramite form HTML) sono usati immediatamente dallo script lato server per costruire le pagine risultanti senza controllare la correttezza della richiesta. Quindi senza controllo, i dati forniti dall'utente non validi sono inclusi nella pagina risultante. Un esempio è il motore di ricerca nei siti, se questi motori di ricerca non filtrano o vietano i caratteri HTML, e in più inseriscono nella pagina risultante della ricerca il messaggio di cosa si stà cercando, posso includere dei tag <script> con il mio script malevolo, quindi la vittima vedrà che l'url è affidabile ma quando cliccherà sul link associato alla ricerca, verrà eseguito lo script.
XSS persistente: Si verifica quando i dati forniti dall'attaccante vengono salvati sul server e quindi visualizzati in modo permanente sulle pagine normalmente fornite agli utenti durante la normale navigazione.

## Implementazione

### Network Based

Approccio orientato all'analisi del traffico di rete. Quindi si analizza il traffico per rilevare intrusioni, permettendo di monitorare non un singolo host ma la rete completa. Questa implementazione è basata su punti di osservazione multipli (sniffer) posti in punti strategici della rete. Questi sistemi sono in grado di fare deep packet inspection sul traffico di rete e sono in grado di riconoscere tracce di attacchi come la violazione di protocolli e l'occorrenza di pattern non normali.

### Host Based

Approccio orientato all'analisi dell'attività dei singoli processi sulle singole macchina coinvolte. Quindi monitoraggio, auditing e analisi a livello di sistema operativo per riconoscere attività ostili.

## Approcci

### Misuse Detection

Si lavora su base di conoscenza al fine di costruire una serie di regole che descrivono l'attività di intrusione sulla base di pattern di traffico specifico, questi pattern vengono chiamati signature.
Per descrivere questi pattern si usano linguaggi descrittivi che definiscono le espressioni di matching sia a livello di protocolli di rete che di payload. 
Sono molto accurati ma non sono in grado di riconoscere attacchi non strutturati come i zero-day.

### Anomaly Detection

Non necessitano di base di conoscenza ma si comportano in maniera totalmente adattiva e sono in grado di riconoscere attacchi non strutturati. Il sistema è in grado di imparare attraverso il machine learning. In un sistema anomaly detection si definisce un profilo che descrive un comportamento "normale" del fenomeno in osservazione e si vanno a generare le possibili variazioni rispetto ad esso. Quindi abbiamo una classificazione binaria, da un lato comportamento normale, dall'altor anomalia.

*XMind - Trial Version*
