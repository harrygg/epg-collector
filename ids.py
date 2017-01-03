# -*- coding: utf8 -*-

ids = [
##my-epg
"HBO",
"HBO 2",
"HBO 3",
"Cinemax",
"Cinemax 2",
"Filmbox Extra HD",
#Sport EPG
"Sport1 US",
"Sport1+",
"Viasat Sport HD",
"Sport Klub 1",
"Sport Klub 2",
"Sport Klub 3",
"Sport Klub 4",
"Sport Klub 5",
"Sport Klub 6",
"Sport Klub 1 HR",
"Sport Klub 2 HR",
"Sport Klub 3 HR",
"Arena Sport 1 (SRB)",
"Arena Sport 2 (SRB)",
"Arena Sport 3 (SRB)",
"Arena Sport 4 (SRB)",
"Arena Sport 5 (SRB)",
"Arena Sport 1 HR",
"Arena Sport 2 HR",
"Arena Sport 3 HR",
"Arena Sport 4 HR",
"Arena Sport 5 HR",
"Sky Sports 1",
"Sky Sports 2",
"Sky Sports 3",
"Sky Sports 4",
"Sky Sports 5",
"Sky Sports F1",
"FOX Sports 1 NL",
"FOX Sports 2 NL",
"FOX Sports 3 NL",
"FOX Sports 4 NL",
"FOX Sports 5 NL",
"FOX Sports 6 NL",
"BT Sport 1",
"BT Sport 2",
"Sky Bundesliga 1",
"Sky Sport 1",
"Sky Sport 2",
"Sky Sport Austria",
"beIN Sports 1 HD (fr)",
"beIN Sports 2 HD (fr)",
"beIN Sports 3 HD (fr)",
"Матч ТВ",
"Матч! Футбол 1",
"Матч! Футбол 2",
"Матч! Футбол 3",
"Наш футбол",
"Конный мир",
"Box Nation",
"Movistar F1",
"Movistar GP",
"RAI Sport 1",
"RAI Sport 2",
"Supper Tennis HD",
"Nova Sport 2 HD (CZ)",
"FightBox HD",
"TRT Spor",
"NTV Spor",
"A Spor",
"LIG TV",
"LIG TV 2",
"LIG TV 3",
"Racing UK",
"Motors UK",
"Русский Экстрим",
"Eurosport 1 DE",
"Eurosport",
"Eurosport 2",
#Bulgarian
"БНТ 1",
"БНТ 2",
"BNT World",
"БНТ HD",
"Btv",
"Btv Comedy",
"Btv Cinema",
"Btv Action",
"Btv Lady",
"Ring",
"Nova",
"Diema",
"Diema Family",
"KinoNova",
"Nova Sport",
"Diema Sport",
"Diema Sport 2",
"Fox",
"Fox Crime",
"Fox Life",
"National Geographic",
"NatGeo Wild",
"Viasat Nature/History HD",
"Viasat Explore",
"Viasat History",
"Viasat Nature",
"TV 1000",
"Discovery HD",
"Discovery",
"Discovery World",
"Discovery Science",
"ActionPlus",
"CinemaPlus",
"ComedyPlus",
"FPlus",
"FilmPlus",
"SportPlusHD",
"TVPlus",
"Шумен",
"AXN",
"AXN Black",
"AXN White",
"Планета HD",
"Планета Фолк",
"Планета",
"Bloomberg BG",
"Bulgaria On Air",
"CNN International",
"Food Network",
"Skat",
"Alfa",
"Boomerang",
"Cartoon Network",
"BiT",
"ТВ Европа",
"24 kitchen",
"Eurocom",
"JimJam",
"Kanal3",
"Skat",
"Food Network",
"Kanal3",
"Travel TV",
"TLC",
"Ekids",
"Animal Planet",
"CBS Reality",
"CBS Drama",
"Comedy Central",
"FightBox HD",
"DocuBox HD",
"FilmBox Plus HD",
"History Channel",
"AMC",
"Черно море",
"PO TV",
"Rimex TV",
"ВТК",
"VTV",
"Agro TV",
"Hobby TV",
"HobbyLovHD",
"Дестинация BG",
"V Arena",
"Trace Sport Stars HD",
"CI Networks",
"HMTV",
##BG EPG
"359TV",
"AutoMotorSport",
"BoxTV",
"BGMusicChannel",
"BabyTV",
"Balkanika",
"BulHistory",
"BrazzersTVEurope",
"City",
"DuckTV",
"Disney",
"DisneyJunior",
"DaVinciLearning",
"DSTV",
"DMSat",
"DeluxeLoungeHD",
"DestinationBG",
"EnglishClubTV",
"FolklorTV",
"FENTV",
"FenFolk",
"FineLiving",
"FashionTV",
"FoodNetworkHD",
"Fiesta",
"FixFoxy",
"HustlerTV",
"HitMix",
"Jukebox",
"MagicTV",
"mezzo",
"MTVRocks",
"MTVHits",
"MyZen",
"music",
"MotoSportHD",
"MedicalChannel",
"MovieSTAR",
"MTVLiveHD",
"MAD",
"NickJr",
"Nickelodeon",
"news",
"Outdoor",
"OtBlizoHD",
"PerviyKanal",
"PVTV",
"Ribalka",
"Rodina",
"Skat",
"TheVoice",
"TV1",
"TiankovFolk",
"TraceSportStars",
"TravelChannel",
"Telekabel",
"TheWorld",
"VH1",
"VH1Classic",
"WorldFashionChannel",
#Russian
"Первый канал. (Европа)",
"Первый канал",
"ТВН - ТВ Центр",
"ТНТ",
"RTVi",
"Живи",
"Охота и рыбалка",
"Россия HD",
"НТВ",
"Россия 24",
"НТВ-Мир",
"РТВ - Наше кино",
"РТР Планета СНГ",
"Дом кино",
"Время",
"Телекафе",
"ТБН",
"Наука 2.0",
"Россия 1",
"Russian Travel Guide (RTG TV)",
"Армения ТВ",
"Еврокино",
"Моя Планета",
"Ю",
"РЕН ТВ",
"Русский Иллюзион",
"TV1000 Megahit HD",
"TV1000 Premium HD",
"TV1000 Comedy HD",
"СТС",
"ICTV (Украина)",
"СТБ",
"НТН (Украина)",
"ТЕТ",
"Новый Канал",
"112 Украина",
"5 канал (Украина)",
"Тонис",
"Наука",
"Шансон-TB",
"Музыка Первого",
"MusicBox TV",
###Serbian
"Pink Kids",
"Pink Western",
"Pink Classic",
"Pink Movies",
"Pink Romance",
"Pink Thriller",
"Pink Action",
"Pink Crime & Mystery",
"Pink Sci Fi & Fantasy",
"Pink Comedy",
"Pink Horror",
"Pink Family",
"Pink Premium",
"Pink Film",
"Pink Soap",
"Pink Serije",
"Pink World Cinema",
"Pink Show",
"Pink Style",
"Pink Extra",
"Pink World",
"Pink Reality",
"Pink Zabava",
"Pink Plus",
"Pink Fashion",
"Pink Live",
"Pink Folk 1",
"Pink Folk 2",
"Pink Hits 1",
"Pink Hits 2",
"Pink Koncert",
"Pink Parada",
"Pink&Roll",
"Pink Music 1",
"Pink Music 2",
"Pink Music 3",
"Pink Music 4",
"Pink Music 5",
"Pink Nostalgie",
"CCTV9 Documentary",
"Dorcel",
"Brazzers",
"Hustler",
"Hustler HD",
"France 24",
"3sat DE",
"CMusicTV",
"mezzolivehd",
"RussiaToday",
"CCTVNews",
"mad",
"DEVIVA",
"DEJukeBox",
"DEDeluxeMusic",
"DEZDFInfo",
"DEZDFKultur",
"DEZDFNeo",
"ArirangTV",
"Sci-FiTelly",
"AlienInvasion",
"FilmboxArthouseHD",
"360TuneBoxHD"NTV-Public",
"NTV-Education",
"NTV-Media",
"Russia Today Documentary",
"PIK",
"MusicBoxTV",
"MusicBoxRU",
"MusicBoxUA",
"1HD",
"NHKWorld",
"E4",
"France 2 (Fr)",
"France 3 (Fr)",
"RTL9 (Fr)",
#German
"13th Street HD",
"ARD",
"Discovery DE HD",
"Kabel1",
"Nat Geo HD DE",
"Natgeo Wild EU HD",
"MGM",
"PRO7",
"RTL",
"RTL 2",
"SAT1",
"Super RTL",
"TNT Film",
"TNT Serie HD",
"VOX",
#uk
"Al Jazeera Eng",
"and TV",
"BBC Worldnews",
"BBC 4",
"CNBC",
"Comedy Central UK",
"Discovery Turbo HD",
"Euronews",
"ITV 1",
"ITV 2",
"ITV 3",
"Movies 24 UK",
"SyFy UK",
"SONY SAB",
"SONY MAX",
"Star Life OK",
"B4U Movies",
"B4U Music",
"ARY News",
"ARY Digital",
"ARY QTV",
"COLORS",
"Rishtey",
"Sikh Channel",
"Sangat",
"Sky Atlantic",
"Channel 4",
"Sky 1",
"Sky 2",
"Sky Action",
"Sky Comedy",
"Sky SciFi/Horror",
"Sky Premiere",
"Sky Family",
"Sky Select",
"Sky Thriller",
"Sky Drama",
"Sky Living",
"Sky News",
]
