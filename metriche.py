# Genera tutte le metriche n,m
totale=0 # contatore delle metriche calcolate

def metriche(lettere,n,m,metrica):
# lettere: contatore delle rime usate 
# n: lunghezza sequenza
# m: numero delle rime sa utilizzare (n<=m)
# metrica: metrica corrente in costruzione
  global totale
  global fileOut
   
  l=len(metrica)
  completo=True
  # Verifico se tutte le rime sono stae usate almeno una volta
  for i in range(m):
    completo=lettere[i]>0 and completo

  if l==n and completo:
    # la metrica calcolata ha la lunghezza richiesta e utilizza tutte le rime
    totale+=1
    stringa="metrica["+str(totale)+"]="+ metrica
    if outputFile=="s":
      fileOut.write(stringa)
      fileOut.write("\n")
    else:
      print(stringa)
  else:
    #  appendo alla metrica corrente tutte le possibili prosecuzioni e richiamo metriche per ognuna di esse se:
    #  * la lunghezza della metrica non raggiunge n
    #  * l'iesima rima non ha superato il numero massimo di utilizzi (n-m+1)
    #  * la lunghezza della metrica è >= della i-esima rima (la rima b si puà usare solo dalla seconda posizione, la c dalla terza e così via
    #  * la rima precedente è stata già usata almeno una volta nella metrica (non posso usare c se non ho mai usato b)
    for i in range(m):
      if l<n and lettere[i]<=n-m+1 and l>=i and (i==0 or lettere[i-1]>0):
        lettere2=lettere[:]
        lettere2[i]+=1
        # richiamo metriche aggiungendo alla metrica attuale la rima corrispondente a i
        metriche(lettere2,n,m,metrica+chr(ord("a")+i))

#Main
n=int(input("Inserisci la lunghezza della sequenza: "))
m=n+1
while (m>n or m<0):
  m=int(input("Inserisci il numero di rime [0 per generarle tutte su file]: "))


  
if m>0:
  #Richiede la scrittura opzionale su file
  outputFile="-"
  while outputFile!="s" and outputFile!="n":
    outputFile=input("Vuoi scrivere l'output su file? [s/n]")
    if outputFile=="s":
      nomeFile=input("Inserisci il nome del file: ")
      fileOut=open(nomeFile,"w")
  lettere=[]
  #Inizializza lettere con i contatori delle rime usate: inizialmente tutto a zero
  for i in range(m):
    lettere.append(0)
  metriche(lettere,n,m,"")
  print (totale)
  if outputFile=="s":
    fileOut.close()
else:
  outputFile="s"
  for j in range(1,n+1):
    print(j)
    nomeFile="./Output/out"+str(n)+"_"+str(j)+".txt"
    fileOut=open(nomeFile,"w")
    lettere=[]
    totale=0
    for i in range(j):
      lettere.append(0)
    metriche(lettere,n,j,"")
    fileOut.close()
  print(totale)
