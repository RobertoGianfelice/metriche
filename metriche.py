# Genera tutte le metriche n,m
totale=0 # contatore delle metriche calcolate

def metriche(lettere,n,m,metrica):
# lettere: contatore delle rime usate 
# n: lunghezza sequenza
# m: numero delle rime sa utilizzare (n<=m)
# metrica: metrica corrente in costruzione
  global totale
  l=len(metrica)
  completo=True
  # Verifico se tutte le rime sono stae usate almeno una volta
  for i in range(m):
    completo=lettere[i]>0 and completo

  if l==n and completo:
    # la metrica calcolata ha la lunghezza richiesta e utilizza tutte le rime
    totale+=1
    print("metrica[",totale,"]=",metrica)
  else:
    #  appendo alla metrica corrente tutte le possibili prosecuzioni e richiamo metriche per ognuna di esse se:
    #  * la lunghezza della metrica non raggiunge n
    #  * l'iesima rima non ha superato il numero massimo di utilizzi (n-m+1)
    #  * la lunghezza della metrica è >= della i-esima rima (la rima b si puà usare solo dalla seconda posizione, la c dalla terza e così via
    #  * la rima precedente è stata già usata almeno una volta nella metrica (non posso usare c se non ho mai usato b)
    for i in range(m):
      if l<=n and lettere[i]<=n-m+1 and l>=i and (i==0 or lettere[i-1]>0):
        lettere2=lettere[:]
        lettere2[i]+=1
        # richiamo metriche aggiungendo alla metrica attuale la rima corrispondente a i
        metriche(lettere2,n,m,metrica+chr(ord("a")+i))

#Main
n=int(input("Inserisci la lunghezza della sequenza: "))
m=n+1
while (m>n or m<1):
  m=int(input("Inserisci il numero di rime: "))

lettere=[]
#Inizializza lettere con i contatori delle rime usate: inizialmente tutto a zero
for i in range(m):
  lettere.append(0)
metriche(lettere,n,m,"")
