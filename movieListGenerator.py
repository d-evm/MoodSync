import random


class movieListGenerator:
    def __init__(self, mood) -> None:
        self.selected_mood = mood

    def generate_list(self):
        if self.selected_mood == "Animation":
            complete_list = {}

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "Action":
            complete_list = [
                "Sholay",
                "Agneepath",
                "Wanted",
                "Dabangg",
                "Singham",
                "Ek Tha Tiger",
                "Bang Bang",
                "Dhoom",
                "Dhoom 2",
                "Dhoom 3",
                "Race",
                "Race 2",
                "Tiger Zinda Hai",
                "Dabangg 2",
                "Singham Returns",
                "War",
                "Sooryavanshi",
                "Pushpa: The Rise - Part 1",
                "RRR",
                "K.G.F: Chapter 1",
                "K.G.F: Chapter 2",
                "Badlapur",
                "Vikram Vedha",
                "Gangs of Wasseypur",
                "Baahubali: The Beginning",
                "Baahubali 2: The Conclusion",
                "Uri: The Surgical Strike",
                "Ghajini",
                "Don",
                "Rowdy Rathore",
                "Jung",
                "Mohra",
                "Vijaypath",
                "Ghatak",
                "Indian",
                "Loha",
                "Karan Arjun",
                "Border",
                "Anth",
                "A Wednesday",
                "Shootout at Wadala",
                "Gadar: Ek Prem Katha",
                "Liger",
                "Commando",
                "Commando 2",
                "Commando 3",
                "Deewar",
                "Shershaah",
                "Mard",
                "Maa Tujhe Salaam",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "Comedy":
            complete_list = [
                "Andaz Apna Apna",
                "Hera Pheri",
                "Phir Hera Pheri",
                "Delhi Belly",
                "Hungama",
                "Dhamaal",
                "Total Dhamaal",
                "Double Dhamaal",
                "Masti",
                "Great Grand Masti",
                "Grand Masti",
                "Housefull",
                "Housefull 2",
                "Housefull 3",
                "Housefull 4",
                "Kis Kisko Pyaar Karu",
                "Golmaal",
                "Golmaal Returns",
                "Golmaal 3",
                "Golmaal Again",
                "Munna Bhai M.B.B.S",
                "No Entry",
                "De Dana Dan",
                "Bhagam Bhag",
                "Dhol",
                "Ajab Prem Ki Ghazab Kahani",
                "No Problem",
                "Khichdi",
                "Heyy Babyy",
                "3 Idiots",
                "PK",
                "Khosla Ka Ghosla",
                "Golmaal",
                "Padosan",
                "Welcome",
                "Welcome Back",
                "Chupke Chupke",
                "Shaukeen Entertainment",
                "Hero No. 1",
                "Chalti Ka Naam Gaadi",
                "Kya Supercool Hai Hum",
                "Raja Babu",
                "Chhoti Si Baat",
                "Hadh Kar Di Aapne",
                "Biwi No. 1",
                "Partner",
                "Hulchul",
                "Khiladi 786",
                "Ready",
                "Haseena Maan Jaayegi",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "Thriller":
            complete_list = [
                "Drishyam",
                "Black Friday",
                "NH 10",
                "Gangs of Wasseypur",
                "Paan Singh Tomar",
                "Gulaal",
                "Talvar",
                "A Wednesday",
                "Shahid",
                "Shaurya",
                "Kahaani",
                "Baby",
                "Company",
                "Special 26",
                "Shool",
                "Badlapur",
                "Kaminey",
                "Shanghai",
                "City Lights",
                "Sangharsh",
                "Dushman",
                "Sarkar",
                "Shagird",
                "Sarkar Raj",
                "Maqbool",
                "The Burning Train",
                "Sarfarosh",
                "Jawan",
                "IB71",
                "Khufiya",
                "Madras Cafe",
                "Runway 34",
                "Freddy",
                "Chor Nikal Ke Bhaga",
                "Gumraah",
                "Neeyat",
                "Monica, Oh My Darling",
                "Ugly",
                "Raazi",
                "Haseen Dillruba",
                "A Thursday",
                "Bell Bottom",
                "Darlings",
                "Ek Villain",
                "Ek Villain Returns",
                "Drishyam",
                "Drishyam 2",
                "Bazaar",
                "Malang",
                "Pink",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "Romantic":
            complete_list = [
                "Jab We Met",
                "Veer Zaara",
                "Barfi",
                "Hum Tum",
                "Dilwale Dulhania Le Jayenge",
                "Kuch Kuch Hota Hai",
                "Dil To Pagal Hai",
                "Hum Dil De Chuke Sanam",
                "Hum Aapke Hain Koun",
                "Love Aaj Kal",
                "Devdas",
                "Mohabbatein",
                "Rab Ne Bana Di Jodi",
                "Mughal-E-Azam",
                "Jab Tak Hai Jaan",
                "Chalte Chalte",
                "Qayamat Se Qayamat Tak",
                "Om Shanti Om",
                "Silsila",
                "Lamhe",
                "Taal",
                "Dil",
                "Raja Hindustani",
                "Kabhi Kabhie",
                "Tere Naam",
                "Aashiqui 2",
                "Chandni",
                "Bobby",
                "Sita Ramam",
                "Rocky Aur Rani Ki Prem Kahani",
                "Ae Dil Hai Mushkil",
                "Ok Jaanu",
                "Vivaah",
                "Goliyon Ki Rasleela Ram-Leela",
                "Satyam Shivam Sundaram",
                "Rocky Aur Rani Ki Prem Kahani",
                "Atrangi Re",
                "Laila Majnu",
                "Prem Rog",
                "Heena",
                "Nadiya Ke Paar",
                "Satyam Shivam Sundaram",
                "Dilwale",
                "Dil Se",
                "Zero",
                "Saathiya",
                "Saagar",
                "Fanaa",
                "Love Aaj Kal",
                "Band Baaja Baaraat",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "Fantasy":
            complete_list = [
                "Koi Mil Gaya",
                "Ra.One",
                "PK",
                "Brahmastra: Part One - Shiva",
                "Makkhi",
                "Paheli",
                "Drona",
                "Taarza: The Wonder Car",
                "Puli",
                "Aladin",
                "Baahubali",
                "Baahubali 2",
                "OMG",
                "Bhediya",
                "Jajantaram Mamantaram",
                "Chota Jadugar",
                "Aabra Ka Daabra",
                "Bhoot Uncle",
                "Adipurush",
                "Tumbbad",
                "A Flying Jatt",
                "Vaah! Life Ho Toh Aisi",
                "Sheshaag",
                "Hatim Tai",
                "Magadheera",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "Horror":
            complete_list = [
                "Raaz",
                "Raaz 3",
                "Raaz: The Mystery Continues",
                "Krishna Cottage",
                "Bhoot",
                "Raaz Reboot",
                "Darna Zaroori Hai",
                "Haunted 3D",
                "Ragini MMS",
                "Ragini MMS 2",
                "Ek Thi Daayan",
                "Stree",
                "Tumbbad",
                "Bulbbul",
                "Roohi",
                "Pari",
                "Bhoot Police",
                "Durgamati",
                "Bhool Bhulaiyaa",
                "Bhool Bhulaiyaa 2",
                "Dybbuk",
                "1920",
                "1920: Evil Returns",
                "1920 London",
                "1920: Horrors of the Heart",
                "1921",
                "Aatma",
                "Bhoot Returns",
                "Shaapit",
                "Purani Haveli",
                "Purana Mandir",
                "Veerana",
                "Raat",
                "Bhediya",
                "Creature 3D",
                "Adhura",
                "Ghost Stories",
                "Ghoul",
                "Blurr",
                "Betaal",
                "Laxmii",
                "Kaal",
                "Naina",
                "Chhorii",
                "Red Rose",
                "Phoonk",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "Drama":
            complete_list = [
                "Omg2",
                "Gadar 2",
                "Satyaprem ki katha",
                "Haddi",
                "Sirf ek bndaa kafi h",
                "Bawaal",
                "Selfiee",
                "Bhuj: The Pride of India",
                "Laal Singh Chaddha",
                "Chor Nikal Ke Bhaga",
                "Raksha Bandhan",
                "Gangubai Kathiawadi",
                "Rocky Aur Rani Ki Prem Kahani",
                "Major",
                "Bharat",
                "October",
                "Chhichhore",
                "Kalank",
                "Malaal",
                "The Power",
                "Jai Bhim",
                "Love Aaj Kal",
                "83",
                "Dear Zindagi",
                "Adipurush",
                "Atrangi Re",
                "Uri: The Surgical Strike",
                "Padmavat",
                "RRR",
                "Soorarai Pottru",
                "Pushpa: The Rise",
                "Sultan",
                "Drishyam 2",
                "Lust Stories",
                "Tamasha",
                "Jab Harry Met Sejal",
                "Sanju",
                "Bajrangi Bhaijan",
                "Aashiqui 2",
                "Goliyon Ki Raasleela Ram-Leela",
                "PK",
                "Bajirao Mastani",
                "Cocktail",
                "ABCD2",
                "Dilwale",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list
