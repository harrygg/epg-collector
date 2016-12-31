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
"24kitchen",
"Alfa",
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
"V Arena",
"Trace Sport Stars HD",
"CI Networks",
"HMTV",
##BG EPG
"359TV",
"AutoMotorSport",
"BoxTV",
"Vratza",
"BGMusicChannel",
"BabyTV",
"Balkanika",
"BulHistory",
"BrazzersTVEurope",
"City",
"Euronews",
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

"HobbyLovHD",
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
"Trakiq",
"porn",
"RING",
"Rimeks",
"Ribalka",
"Rodina",
"Skat",
"TheVoice",
"TV1",
"TVT",
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
"Sky Hits DE",
"Sky Action DE",
"Sky Atlantic DE",
"Sky Cinema DE",
"Syfy DE",
"13th Street DE",
"TNT Film DE",
"TNT Serie DE",
"MGM DE",
"Rai 1 IT",
"Rai 2 IT",
"Sky Sport Austria DE",
"Sky Fußball Bundesliga DE",
"National Geographic DE",
"Nat Geo Wild DE",
"Discovery Channel DE",
"History Channel DE",
"France 24",
"Al Jazeera",
"BBC World",
"3sat DE",
"Arte DE",
"ZDF DE",
"Lig TV 1 (Tr)",
"Lig TV 2 (Tr)",
"Lig TV 3 (Tr)",
"Digi Sport 1",
"Digi Sport 2",
"Digi Sport 3",
"Canal+ Deportes (Spa) ",
"ORF 1",
"ORF 2",
"BBC World News",
"CI",
"Comedy Central UK",
"CNBC UK",
"Food Network",
"H2 UK",
"Sky 1 UK",
"Sky 2 UK",
"Sky Movies Action &amp; Adventure UK",
"Sky Movies Comedy UK",
"Sky Movies Sci-Fi &amp; Horror UK",
"Sky Movies Select UK",
"Sky Movies Family UK",
"Sky Movies Premiere UK",
"Sky Movies Drama &amp; Romance UK",
"Setanta Sports Ireland 1 UK",
"Premier Sports UK",
"NHK World UK",
"Sky News UK",
"Travel Channel",
"DeutscheWelle",
"KBSWorld",
"GINXTV",
"iConcerts",
"Discovery Turbo UK",
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
"360TuneBoxHD",
"FastnFunBoxHD",
"FashionBox",
"NTV-Public",
"NTV-Education",
"NTV-Media",
"PK-test",
"FP-test",
"Russia Today Documentary",
"PIK",
"MusicBoxTV",
"MusicBoxRU",
"MusicBoxUA",
"RUMTV",
"RusongTV",
"1HD",
"FashionOneHD",
"NHKWorld",
"E4",
"BBC1",
"CBBC",
"CBSRealityUK",
"CBSDramaUK",
"Bein Sports HD (es)",
"Bein Sports 1",
"Bein Sports 2",
"Bein Sports 3",
"Bein Sports 4",
"beIN Sport 1 (Fr)",
"beIN Sport 2 (Fr)",
"beIN Sport 3 (Fr)",
"France 2 (Fr)",
"France 3 (Fr)",
"RTL9 (Fr)",
#German
"Kabel Eins DE",
"Super RTL DE",
"ARD",
"RTL DE",
"RTL 2 DE",
"ProSieben DE",
"SAT1",
"VOX DE",
"Sixx DE",
"KiKA",
"Das Erste",
]
