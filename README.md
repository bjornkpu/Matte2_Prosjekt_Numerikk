# Matte2_Prosjekt_Numerikk
#### Dette er koden for prosjektoppgaven i Matematikk 2 Numerikk. Vår 2018
-----

## Oppgavetekst
### Oppgave 1
Løs oppgave 5.1.21 og 5.1.22a på side 253 i læreboka). Les kapittel 0.5 før dere
gjør denne oppgaven. Dere vil trenge Taylors formel med restledd R5(x) = (f^6 (c)/6!)(x-x0)^6 .

Likningene (2.32) og (2.33) trenger dere ikke å bevise. Et tips for teoridelen er å vise sammenhengen
mellom uttrykkene på side 102 og 103. For eksempel kombineres (2.27) og (2.28)
til å gi (2.29). Gi detaljene for dette. Vis også sammenhengen mellom formlene (2.29) til (2.31)
og matrise-uttrykket i (2.34). Hvilke rader i matrisen hører sammen med formlene?

### Oppgave 2
Skriv et Python-program som definerer strukturmatrisen i (2.34). Viktig: Bruk
`A=spdiags(...)` for å initialisere A da dette vil være nødvendig i senere oppgaver. Dere kan
bruke dette utgangspunktet
```Python
import scipy as sp
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix

def lagA(n):
	e = sp.ones(n)
	A = spdiags([e, 4*e, 6*e, -4*e, e],[-2, -1, 0, 1, 2], n, n)
	A = lil_matrix(A)
	B = csr_matrix([[*, *, *, *],	# Sett inn din kode istedet for *
					[*, *, *, *],	# i matrisen B
					[*, *, *, *]])	
	A[0, 0:4]		= B[0, :]
	A[n-2, n-4:n]	= B[1, :]
	A[n-1, n-4:n]	= B[2, :]
	return A
```

### Oppgave 3
Finn løsning `yc` på problemet med en bjelke uten ekstra masse enn egenmassen ved å bruke
`n = 10` intervaller. (Lag kode der dere bruker programmet fra oppgave 2)
PS! Dere kan løse `Ay = b` ved hjelp av Python-koden `y = spsolve(A,b)`. Den importeres ved
hjelp av
```Python
from scipy.sparse.linalg import spsolve
```

### Oppgave 4
a)  Den korrekte løsningen av likningen med konstant `f(x) = f` er

      `y(x)=(f/24EI)x^2 (x^2 -4Lx+6L^2 )` .
      
  Vis dette ved å derivere 4 ganger og sett inn i likningen.
    
b)  Utledningen av formlene for de deriverte brukte Taylors formel med feil-ledd `(y^(6) (c)/6!)h^6` for å
    estimere feilen. Vis at for den korrekte løsningen er `y^(6) (c) = 0`. (Den numeriske metoden
    for den 4-deriverte `Ay` er derfor eksakt).
    
c)  Regn ut vektoren `ye = [y(0.2) y(0.4) y(0.6) y(0.8) · · · y(2.0)]^T` for den eksakte
    løsningen og regn ut numerisk den fjerdederiverte av `y(x)` ved hjelp av den nummeriske
    fjerdederiverte `Aye`.
    
d)  Sammenlign svaret i c) med vektoren b fra oppgave 3 og finn foroverfeil og relativ foroverfeil
    til den nummeriske fjerdederiverte `y → Ay`. Anta at relativ bakoverfeil er `εmach = 2−52`
    Regn ut feilforstørringen og sammenlign med kondisjonstallet til A. Hva ser du?
    
e)  Sammenlikn også svaret i oppgave 3 med den eksakte løsningen. Finn foroverfeilen `||yc − ye||1`
    Den er i størrelsesorden `εmach`. Forklar hvorfor.

### Oppgave 5
Kjør utregningene i oppgave 3 om igjen for `n = 20, 40, . . . , 10 · 2^11`. Lag en tabell
over feilen i punktet `x = L` for hver n. For hvilken n er feilen størst? Hvorfor endrer feilen seg
med n slik som den gjør? Du kan f˚a bruk for ˚a sammenlikne med kondisjonstallet til A for de
forskjellige verdiene av n.

### Oppgave 6
Vi legger en sinusformet haug p˚a bjelken. Det betyr at vi legger til en funksjon
`s(x) = −pg sin (π/L)x` til funksjonen `f(x)`.

a)  Bevis at
  
          `y(x) = (f/24EI)x^2 (x^2 − 4Lx + 6L^2) −(gpL/EIπ) ((L^3/π^3) sin(π/L)x − (x^3/6)+(Lx^2/2)−(L^2x/π^2)`
          
tilfredstiller Euler-Bernoulli-likningen og randbetingelsene for en bjelke som er festet i
den ene enden og fri i den andre:

          `y(0) = y'(0) = y''= y'''(L) = 0` .

b)  Kjør om igjen utregningene i oppgave 5 om igjen men med den sinusformede belastningen.
La `p = 100kg/m` og plot den korrekte løsningen mot den nummerisk beregnede løsningen.

c)  Plot feilen for `yn` oppgave 6b i et koordinatsystem der begge akser er logaritmiske.
PS! Du kan bruke `plot(log(X),log(Y))` plot finner dere i pakken pyplot som dere importerer
med
```Python
import matplotlib.pyplot as pl
```
d)  Plot ogs˚a kondisjonstallet til A multiplisert med `εmach` og den teoretiske feilen `h^2 = L^2/n^2`
i den fjerdederiverte i samme koordinatsystem som i c). Her skal dere se 2 rette linjer og
en kurve som “følger” disse linjene.

e)  Den teoretiske feilen `h^2` i de numeriske formlene vil avta for økende n. Etter en hvis n av
øker allikevel feilen. Forklar ved hjelp av kondisjonstallet til A

f) Hva er den optimale verdien av n?

### Oppgave 7
Nå skal du erstatte haugen med en person som står tærne ytterst på stupebrettet.
Du kan anta at all vekt er jevnt fordelt langs hele foten som du kan regne er 30 cm. Personen
veier 50kg. Finn hvor mye stupebrettet bøyes ned ved enden. Hvilken verdi av n er best å
bruke? Du vil trenge å legge til kraft per enhetslengde definert ved:

      `s2(x)={ -g · 50/0.3 kg/m   ,L-0.3m<=x<=L
               0N/m               ,0m<=x<L-0.3m`
