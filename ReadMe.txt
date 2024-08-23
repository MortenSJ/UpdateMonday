ReadMe

For at kunne køre python scriptene kræver det at python er installert. Og at monday-pakken er installeret. 
https://www.python.org/downloads/windows/ sørg for at den installeres "globalt" på pcen
Herefter kø denne komando i en admin CMD: Pip install monday==2.0.0.rc3

Hent hele dette projekt ned og gem det. Logikken i scriptet bruger filerne som vil ligge i mappen. 

Inden første kørsel:
--------------------
Åben Monday og find Board ID for det board, som der skal laves opdateringer på. 

En vejledning til at finde forskellige IDer findes her: https://support.monday.com/hc/en-us/articles/360000225709-Board-item-column-and-automation-or-integration-ID-s

Kør 'RunGetGroupIDs' for at få txt filen med Gruppe ID'er. Her skal du bruge BoardID'et på det board du gerne vil have grupper fra

Med Board ID og gruppe id, kør nu 'RunGetItems'.
Dette giver CSV filen Items, som skal bruges til at mappe data sammen i MondayDataMapping. 

Mapningsarket (MondayDataMapping): 
----------------------------------
I mapping arket er der tre faner
Fanen Monday er der, hvor data samles/mappes
	Kolonne A er navnet på processen - Dette kan hentes fra Items filen
	Kolonne B er kø navnet, indsættes fra Elastic fanen. 
	Kolonne C Hentes ud fra data i kolonne B
	Kolonne D er nummeret på det board, hvor itemet skal opdateres. 
	Kolonne E er columneID fra monday, hvor data skal opdateres. 
Fanen mondayID er her hvor du indsætter data fra Item filen, som blev udtrukket ovenfor. 
Fanen Elastic er et udtræk fra Kibana, med kø navn, status og transaktion - husk ingen tusindtalsseperator i antal, for et CSV udtræk fra Kibana er med US setting hvor komma og punktum er bytte om. RHG Kibana udtræk kan ses her: https://kibana.rpa.rm.dk/s/analytics/app/dashboards#/view/b36f7107-e513-5883-bcfb-8d3eac2264b5?_g=(filters:!())

Når mapningen er færdig, klik på Opret CSV knapen i mapningsarket, herved genereres en CSV fil. Hvis data til opdatering skal opdateres skal en nuværende fil overskrives. 
Denne fil bruges når du køre 'RunUpdateMonday'. 

Proces ved løbende opdateringer: 
--------------------------------
Mapningsarket holdes løbende opdateret og nye processer og køer tilføjes på fanen Monday. 
Inden opdatering downloades en opdateret csv fra Kibana. (Åben Kibana, klik på de tre prikker ud for tabellen, More, Download as CSV)
Data fra CSV filen kopieres og indsættes i celle A1 på Elastic fanen. Herefter klikkes der på "Tekst til kolonner" knappen i Excel under "Data ribben", og der laves en afgrænsning på , (komma). Dette gør at data splittes ud i de tre kolonner. Transaktionerne står i kolonne C og Kønavnet i A. 
På fanen Mapning, klikkes på knappe Opret CSV, denne aktivere en makro, som danner en ny CSV som gemmes oven i monday_data_v4.csv. Hvis Excel spørger om filen må overskrives så klik Ja. 
Her efter kan du køre RunUpdateMonday.bat - denne starter i CMD'en - følg vejledning der.
Data er herefter opdateret i Monday. 
