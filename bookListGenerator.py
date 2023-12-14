import random


class bookListGenerator:
    def __init__(self, mood) -> None:
        self.selected_mood = mood

    def generate_list(self):
        if self.selected_mood == "WittySatire":
            complete_list = [
                "Gulliver's Travels by Jonathan Swift",
                "Catch-22 by Joseph Heller",
                "Animal Farm by George Orwell",
                "The Hitchhiker's Guide to the Galaxy by Douglas Adams",
                "Candide by Voltaire",
                "Don Quixote by Miguel de Cervantes",
                "Slaughterhouse-Five by Kurt Vonnegut",
                "A Confederacy of Dunces by John Kennedy Toole",
                "The Importance of Being Earnest by Oscar Wilde",
                "The Picture of Dorian Gray by Oscar Wilde",
                "1984 by George Orwell",
                "Brave New World by Aldous Huxley",
                "Thank You for Smoking by Christopher Buckley",
                "Lolita by Vladimir Nabokov",
                "The Man Who Knew Too Much by G.K. Chesterton",
                "The Sellout by Paul Beatty",
                "Pale Fire by Vladimir Nabokov",
                "The Loved One by Evelyn Waugh",
                "American Psycho by Bret Easton Ellis",
                "The White Tiger by Aravind Adiga",
                "Money by Martin Amis",
                "Good Omens by Neil Gaiman and Terry Pratchett",
                "The Secret Agent by Joseph Conrad",
                "The Metamorphosis by Franz Kafka",
                "A Modest Proposal by Jonathan Swift",
                "Babbitt by Sinclair Lewis",
                "White Noise by Don DeLillo",
                "The Princess Bride by William Goldman",
                "The Road to Wigan Pier by George Orwell",
                "The Handmaid's Tale by Margaret Atwood",
                "Breakfast of Champions by Kurt Vonnegut",
                "The Master and Margarita by Mikhail Bulgakov",
                "The Phantom Tollbooth by Norton Juster",
                "Vile Bodies by Evelyn Waugh",
                "The Broom of the System by David Foster Wallace",
                "A Clockwork Orange by Anthony Burgess",
                "The Dice Man by Luke Rhinehart",
                "Slapstick by Kurt Vonnegut",
                "The Fat Years by Chan Koonchung",
                "The Elephant Vanishes by Haruki Murakami",
                "The Elementary Particles by Michel Houellebecq",
                "The Yiddish Policemen's Union by Michael Chabon",
                "The Electric Kool-Aid Acid Test by Tom Wolfe",
                "The Bus Driver Who Wanted to Be God & Other Stories by Etgar Keret",
                "Confederates in the Attic by Tony Horwitz",
                "The Sellout by Paul Beatty",
                "The Nix by Nathan Hill",
                "Less by Andrew Sean Greer",
                "The Circle by Dave Eggers",
                "The Sympathizer by Viet Thanh Nguyen"
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "RomanticFantasy":
            complete_list = {}

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "GothicHorror":
            complete_list = {}

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "UpbeatMystery":
            complete_list = [
                "The Adventures of Sherlock Holmes by Arthur Conan Doyle",
                "Gone Girl by Gillian Flynn",
                "The Girl with the Dragon Tattoo by Stieg Larsson",
                "In the Woods by Tana French",
                "The No. 1 Ladies' Detective Agency by Alexander McCall Smith",
                "The Cuckoo's Calling by Robert Galbraith (pseudonym for J.K. Rowling)",
                "Still Life by Louise Penny",
                "Big Little Lies by Liane Moriarty",
                "And Then There Were None by Agatha Christie",
                "The Silent Patient by Alex Michaelides",
                "The Hound of the Baskervilles by Arthur Conan Doyle",
                "Sharp Objects by Gillian Flynn",
                "The Da Vinci Code by Dan Brown",
                "Dark Places by Gillian Flynn",
                "The Secret History by Donna Tartt",
                "The Shadow of the Wind by Carlos Ruiz Zafón",
                "Tinker, Tailor, Soldier, Spy by John le Carré",
                "The Maltese Falcon by Dashiell Hammett",
                "The Snowman by Jo Nesbø",
                "The Alienist by Caleb Carr",
                "The Secret Place by Tana French",
                "In Cold Blood by Truman Capote",
                "The Likeness by Tana French",
                "The Lincoln Lawyer by Michael Connelly",
                "Rebecca by Daphne du Maurier",
                "Before I Go to Sleep by S.J. Watson",
                "The Woman in White by Wilkie Collins",
                "Shutter Island by Dennis Lehane",
                "The Secret Keeper by Kate Morton",
                "The Silent Wife by A.S.A. Harrison",
                "The Wife Between Us by Greer Hendricks and Sarah Pekkanen",
                "Sharp Objects by Gillian Flynn",
                "The Truth About the Harry Quebert Affair by Joël Dicker",
                "Stillhouse Lake by Rachel Caine",
                "The Death of Mrs. Westaway by Ruth Ware",
                "The Breakdown by B.A. Paris",
                "The Wife by Alafair Burke",
                "The Girl on the Train by Paula Hawkins",
                "Magpie Murders by Anthony Horowitz",
                "Before I Let You In by Jenny Blackhurst",
                "The Butterfly Garden by Dot Hutchison",
                "Bluebird, Bluebird by Attica Locke",
                "The Silent Corner by Dean Koontz",
                "I Am Watching You by Teresa Driscoll",
                "The Good Girl by Mary Kubica",
                "The Girl Before by J.P. Delaney",
                "The Night Olivia Fell by Christina McDonald",
                "The Lost Man by Jane Harper",
                "The Hunting Party by Lucy Foley",
                "The River by Peter Heller"
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "ReflectivePoetry":
            complete_list = [
                "Rashmirathi",
                "Madhushala",
                "Raat Pashmine Ki",
                "Urvashi",
                "Kamayani",
                "Angan ke par Dwar",
                "Tarkash",
                "Apne Samne",
                "Shekhar: Ek Jeevani",
                "Meri sreshtha kavitayen: sabhi kavya-kritiyon mein se kavi dvara chuni hui sreshtha kavitaon ka",
                "Phir Meri Yaad",
                "Taar Saptak",
                "Talkhiyan",
                "Sab kuchh Hona Bacha Rahega",
                "Sansad se Sadak Tak",
                "Parshuram Ki Pratiksha",
                "Rangbhoomi",
                "Chuni Hui Kavitayen",
                "Yama",
                "Chidambara",
                "Saaye Mein Dhoop",
                "Mahabhoj",
                "Padmavat",
                "Magadh",
                "Yaha andara ki bata hai: hasya vyangya kavya sangraha",
                "Mera Kuchh Samaan: My Poetry Collection",
                "Rashmirathi",
                "Madhushala",
                "Raat Pashmine Ki",
                "Nindiya Chor",
                "Bandini",
                "¿¿¿¿ ¿¿ ¿¿¿: Koyal Kee Kook",
                "The Essential Rumi",
                "And Still I Rise",
                "Lyrical Ballads",
                "I Remember",
                "Pillow Thoughts",
                "The Sun and Her Flowers",
                "Paradise Lost",
                "Devotions",
                "Divine Comedy",
                "Call Us What We Carry",
                "Howl and Other Poems",
                "The Wild Iris",
                "The Dream Songs",
                "The Poetry of Rilke",
                "The Poetry of Derek Walcott 1948-2013",
                "Postcolonial Love Poem",
                "The Wild Fox of Yemen",
                "Urban Tumbleweed: Notes from a Tanka Diary",
                "Selected Poems",
                "Collected Poems",
                "How we became human",
                "The poems of Marianne Moore",
                "Goblin Market",
                "The Waste Land by T.S. Eliot",
                "Leaves of Grass by Walt Whitman",
                "The Collected Poems of W.B. Yeats by W.B. Yeats",
                "The Complete Poems of Emily Dickinson by Emily Dickinson",
                "Ariel by Sylvia Plath",
                "The Sun and Her Flowers by Rupi Kaur",
                "Milk and Honey by Rupi Kaur",
                "The Essential Rumi translated by Coleman Barks",
                "The Prophet by Kahlil Gibran",
                "The Odyssey by Homer (translated by Robert Fagles)",
                "The Iliad by Homer (translated by Robert Fagles)",
                "Selected Poems by E.E. Cummings",
                "The Complete Poems by Anne Sexton",
                "Selected Poems by Langston Hughes",
                "The Essential Neruda: Selected Poems by Pablo Neruda",
                "Maud Martha by Gwendolyn Brooks",
                "Don't Call Us Dead by Danez Smith",
                "Bluets by Maggie Nelson",
                "Teaching My Mother How to Give Birth by Warsan Shire",
                "The Essential Ginsberg by Allen Ginsberg",
                "The Essential Rilke translated by Galway Kinnell and Hannah Liebmann",
                "Native Guard by Natasha Trethewey",
                "The Essential Haiku: Versions of Basho, Buson, & Issa translated by Robert Hass",
                "The Penguin Anthology of Twentieth-Century American Poetry edited by Rita Dove",
                "Aimless Love: New and Selected Poems by Billy Collins",
                "The Essential Emily Dickinson by Emily Dickinson",
                "The Sun Is Also a Star by Nicola Yoon",
                "Night Sky with Exit Wounds by Ocean Vuong",
                "The Essential Whitman by Walt Whitman",
                "Calling a Wolf a Wolf by Kaveh Akbar",
                "Citizen: An American Lyric by Claudia Rankine",
                "The Carrying: Poems by Ada Limón",
                "Bullets into Bells: Poets & Citizens Respond to Gun Violence edited by Brian Clements, Alexandra Teague, and Dean Rader",
                "The Essential Haiku: Versions of Basho, Buson, & Issa translated by Robert Hass",
                "Selected Poems by Langston Hughes",
                "The Essential Neruda: Selected Poems by Pablo Neruda",
                "Selected Poems by Langston Hughes",
                "The Essential Neruda: Selected Poems by Pablo Neruda"
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "AdventurousSciFi":
            complete_list = [
                "Neuromancer by William Gibson",
                "Dune by Frank Herbert",
                "Foundation by Isaac Asimov",
                "Stranger in a Strange Land by Robert A. Heinlein",
                "Snow Crash by Neal Stephenson",
                "The Left Hand of Darkness by Ursula K. Le Guin",
                "Brave New World by Aldous Huxley",
                "1984 by George Orwell",
                "The Hitchhiker's Guide to the Galaxy by Douglas Adams",
                "Ender's Game by Orson Scott Card",
                "Hyperion by Dan Simmons",
                "The Martian by Andy Weir",
                "Altered Carbon by Richard K. Morgan",
                "The Expanse series by James S.A. Corey",
                "Starship Troopers by Robert A. Heinlein",
                "Red Mars by Kim Stanley Robinson",
                "2001: A Space Odyssey by Arthur C. Clarke",
                "The Three-Body Problem by Liu Cixin",
                "Solaris by Stanislaw Lem",
                "I, Robot by Isaac Asimov",
                "A Canticle for Leibowitz by Walter M. Miller Jr.",
                "The Moon is a Harsh Mistress by Robert A. Heinlein",
                "Fahrenheit 451 by Ray Bradbury",
                "The War of the Worlds by H.G. Wells",
                "The Time Machine by H.G. Wells",
                "Do Androids Dream of Electric Sheep? by Philip K. Dick",
                "The Invisible Man by H.G. Wells",
                "Gateway by Frederik Pohl",
                "The Windup Girl by Paolo Bacigalupi",
                "Snow Queen by Joan D. Vinge",
                "Redshirts by John Scalzi",
                "Binti by Nnedi Okorafor",
                "The City and the Stars by Arthur C. Clarke",
                "The Forever War by Joe Haldeman",
                "The Fifth Sacred Thing by Starhawk",
                "The Hunger Games by Suzanne Collins",
                "The Dispossessed by Ursula K. Le Guin",
                "The Stars My Destination by Alfred Bester",
                "Dark Matter by Blake Crouch",
                "The Player of Games by Iain M. Banks",
                "The Quantum Thief by Hannu Rajaniemi",
                "Ancillary Justice by Ann Leckie",
                "Accelerando by Charles Stross",
                "The Book of the New Sun by Gene Wolfe",
                "The Diamond Age by Neal Stephenson",
                "A Fire Upon the Deep by Vernor Vinge",
                "Flowers for Algernon by Daniel Keyes"
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "MelancholicHistory":
            complete_list = [
                "War and Peace",
                "Gone with the Wind",
                "Wolf Hall",
                "The Book Thief",
                "Memoirs of a Geisha",
                "Outlander",
                "The Nightingale",
                "The Name of the Rose",
                "A Tale of Two Cities",
                "The Underground Railroad",
                "I, Claudius",
                "Beloved",
                "The Other Boleyn Girl",
                "The Pillars of the Earth",
                "One Hundred Years of Solitude",
                "The Guns of August",
                "The Three Musketeers",
                "The Historian",
                "The Red Badge of Courage",
                "The Tattooist of Auschwitz",
                "The Four Winds",
                "Things Fall Apart",
                "The Book of Longings: A Novel",
                "The Immortals of Meluha",
                "Train to Pakistan",
                "The Great Indian Novel",
                "India After Gandhi",
                "Discovery of India",
                "India's Struggle for Independence",
                "History of Modern India",
                "Bhagavad Gita",
                "A Suitable Boy",
                "India's Ancient Past",
                "Arthashastra",
                "Panchatantra",
                "Mahabharata",
                "Charaka Samhita",
                "India: A History",
                "An Era of Darkness: The British Empire in India",
                "Kama Sutra",
                "The Little Clay Cart (Mrcchakatika)",
                "Khaak Aur Khoon",
                "Ancient India",
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list

        elif self.selected_mood == "ChildrensFantasy":
            complete_list = [
                "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
                "Alice's Adventures in Wonderland by Lewis Carroll",
                "The Hobbit by J.R.R. Tolkien",
                "Matilda by Roald Dahl",
                "The Lion, the Witch and the Wardrobe by C.S. Lewis",
                "Where the Wild Things Are by Maurice Sendak",
                "A Wrinkle in Time by Madeleine L'Engle",
                "Peter Pan by J.M. Barrie",
                "Howl's Moving Castle by Diana Wynne Jones",
                "The Tale of Despereaux by Kate DiCamillo",
                "The Secret Garden by Frances Hodgson Burnett",
                "The Princess Bride by William Goldman",
                "Bridge to Terabithia by Katherine Paterson",
                "Coraline by Neil Gaiman",
                "Percy Jackson and the Olympians: The Lightning Thief by Rick Riordan",
                "His Dark Materials: Northern Lights by Philip Pullman",
                "Winnie-the-Pooh by A.A. Milne",
                "The Graveyard Book by Neil Gaiman",
                "The Wizard of Oz by L. Frank Baum",
                "Artemis Fowl by Eoin Colfer",
                "Inkheart by Cornelia Funke",
                "Charlotte's Web by E.B. White",
                "The Neverending Story by Michael Ende",
                "The Golden Compass by Philip Pullman",
                "The BFG by Roald Dahl",
                "The Wind in the Willows by Kenneth Grahame",
                "The Magic Faraway Tree by Enid Blyton",
                "The Phantom Tollbooth by Norton Juster",
                "The Boxcar Children by Gertrude Chandler Warner",
                "The Last Unicorn by Peter S. Beagle",
                "Tuck Everlasting by Natalie Babbitt",
                "Ella Enchanted by Gail Carson Levine",
                "The Tale of Peter Rabbit by Beatrix Potter",
                "The Giver by Lois Lowry",
                "The Spiderwick Chronicles: The Field Guide by Tony DiTerlizzi and Holly Black",
                "The Chronicles of Narnia: Prince Caspian by C.S. Lewis",
                "The Enchanted Wood by Enid Blyton",
                "Charlie and the Chocolate Factory by Roald Dahl",
                "The House with Chicken Legs by Sophie Anderson",
                "The Magician's Nephew by C.S. Lewis",
                "The Phantom of the Opera by Gaston Leroux",
                "Dragon Rider by Cornelia Funke",
                "The Adventures of Tintin: The Secret of the Unicorn by Hergé",
                "James and the Giant Peach by Roald Dahl",
                "Pippi Longstocking by Astrid Lindgren",
                "Fablehaven by Brandon Mull",
                "A Series of Unfortunate Events: The Bad Beginning by Lemony Snicket",
                "The Miraculous Journey of Edward Tulane by Kate DiCamillo",
                "The Little Prince by Antoine de Saint-Exupéry",
                "The Invention of Hugo Cabret by Brian Selznick"
            ]

            if len(complete_list) > 30:
                no_of_items = 30
            else:
                no_of_items = len(complete_list)

            list = random.sample(complete_list, no_of_items)
            return list
