"""
Management command to load all questions from PSAT 8/9 Practice Test 1.
English (Reading & Writing): 81 questions across 3 modules
Math: 66 questions across 3 modules
Difficulty: Module 1 = medium, Module 2 Easier = easy, Module 2 Harder = hard
"""
from django.core.management.base import BaseCommand
from practice.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Load PSAT Practice Test 1 questions into the database'

    def handle(self, *args, **options):
        math = Subject.objects.get(slug='math')
        english = Subject.objects.get(slug='english')

        # ── English Topics ──────────────────────────────────────────────
        ev, _ = Topic.objects.get_or_create(subject=english, name='Vocabulary in Context')
        rc, _ = Topic.objects.get_or_create(subject=english, name='Reading Comprehension')
        de, _ = Topic.objects.get_or_create(subject=english, name='Data and Evidence')
        gv, _ = Topic.objects.get_or_create(subject=english, name='Grammar: Verb Usage')
        gp, _ = Topic.objects.get_or_create(subject=english, name='Grammar: Punctuation')
        tr, _ = Topic.objects.get_or_create(subject=english, name='Transitions')
        rn, _ = Topic.objects.get_or_create(subject=english, name='Research Notes')

        # ── Math Topics ──────────────────────────────────────────────────
        alg, _ = Topic.objects.get_or_create(subject=math, name='Algebra and Equations')
        fun, _ = Topic.objects.get_or_create(subject=math, name='Functions and Graphs')
        geo, _ = Topic.objects.get_or_create(subject=math, name='Geometry')
        dsp, _ = Topic.objects.get_or_create(subject=math, name='Data, Statistics, and Probability')
        wp, _  = Topic.objects.get_or_create(subject=math, name='Word Problems')

        # ── helper ───────────────────────────────────────────────────────
        def q(topic, diff, text, a, b, c, d, ans, expl=''):
            Question.objects.create(
                subject=topic.subject, topic=topic, difficulty=diff,
                text=text, option_a=a, option_b=b, option_c=c, option_d=d,
                correct_answer=ans, explanation=expl,
            )

        M = 'medium'; E = 'easy'; H = 'hard'

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Section 1, Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(ev, M,
          "In 1913, approximately 91% of the roads in the United States were rural dirt roads. "
          "Experts recognized the need for improved surfaces and, as part of an ambitious "
          "________, worked toward the completion of the Lincoln Highway in 1916: extending "
          "from New York City to San Francisco, the Lincoln Highway became the first "
          "coast-to-coast highway in the United States.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "treaty", "undertaking", "invention", "failure", "B",
          "'Undertaking' best describes the ambitious project to build the Lincoln Highway.")

        q(ev, M,
          "Bill Morrison has dedicated his career to presenting archival film footage set to "
          "modern music. As part of his process, Morrison ________ several different composers, "
          "whom he asks to write a score that will allow him to present old, decaying footage "
          "as part of a new, integrated narrative. Among other accolades, his 2002 film "
          "Decasia was selected for preservation by United States National Film Registry.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "works with", "praises", "argues with", "cautions", "A",
          "Morrison collaborates with composers, so 'works with' is the most logical choice.")

        q(ev, M,
          "Archaeologists have long believed that the first meaningful contact between East "
          "and West occurred with the opening of the Silk Road in the second century BCE, but "
          "new findings suggest otherwise. Archaeologists have recently excavated statues from "
          "China, and senior archaeologist Xiuzhen Li of the Emperor Qin Shi Huang's Mausoleum "
          "Site Museum believes the findings ________ previous conclusions: terracotta acrobats "
          "and bronze birds such as swans and cranes indicate a strong Greek influence and the "
          "involvement of Greek sculptors from as far back as the fifth century BCE.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "contradict", "confirm", "investigate", "demonstrate", "A",
          "The new findings suggest the opposite of previous conclusions, so 'contradict' is correct.")

        q(ev, M,
          "The following text is adapted from Katherine Mansfield's 1922 short story "
          "'The Garden Party.' The narrator is describing one part of a neighborhood that "
          "he has just arrived in.\n\n"
          "That really was extravagant, for the little cottages were in a lane to themselves "
          "at the very bottom of a steep rise that led up to the house. A broad road ran "
          "between. True, they were far too near. They were the greatest possible eyesore, "
          "and they had no right to be in that neighbourhood at all. They were little mean "
          "dwellings painted a chocolate brown.\n\n"
          "As used in the text, what does the word 'mean' most nearly mean?",
          "Displeasing", "Welcoming", "Captivating", "Abusing", "A",
          "In this context, 'mean' describes the unattractive, unpleasant appearance of the cottages.")

        q(rc, M,
          "Missoula, Montana, is known for a children's theater that casts children in plays "
          "as the company travels from city to city. The Missoula Children's Theater (MCT) "
          "was founded in 1970 as a company of adults performing for children, but in 1972 "
          "the two founders realized there was a high demand for the kids themselves to "
          "perform the shows. Now touring nationally, the MCT goes to different cities and "
          "casts local children in each show, building a community experience in each "
          "location while keeping the spirit of the theater intact.\n\n"
          "Which choice best states the main purpose of the text?",
          "To detail the surge in theater popularity in Missoula from 1970 onwards",
          "To contrast the Missoula Children's Theater with other theater companies in Missoula",
          "To describe the history and current contributions of the Missoula Children's Theater",
          "To advocate for people to raise funds for children's theater in Missoula", "C",
          "The passage describes MCT's founding, evolution, and current national touring model.")

        q(rc, M,
          "The following text is from Jane Austen's 1814 novel Mansfield Park. Fanny, a "
          "10-year-old girl, has recently moved in with her aunt and uncle.\n\n"
          "From this day Fanny grew more comfortable. She felt that she had a friend, and "
          "the kindness of her cousin Edmund gave her better spirits with everybody else. "
          "The place became less strange, and the people less formidable; and if there were "
          "some amongst them whom she could not cease to fear, she began at least to know "
          "their ways, and to catch the best manner of conforming to them.\n\n"
          "Which choice best states the main purpose of the text?",
          "To explain how Edmund and his family feel about Fanny",
          "To detail Fanny's adjustment to her situation",
          "To describe the fears that Fanny shares with Edmund",
          "To discuss how Fanny came to live at Mansfield Park", "B",
          "The passage shows Fanny gradually adapting and growing more comfortable in her new home.")

        q(rc, M,
          "Alloparental care occurs when an animal cares for offspring that are not its own. "
          "Most research on this behavior in other animals has focused on genetic relatedness "
          "of the adopted animal to its adoptive parent. However, biologist Marianne Riedman "
          "and Burney Le Boeuf showed that it can occur in unrelated pairs as well (i.e., "
          "not from the same family). In their study, which focused on a colony of northern "
          "elephant seals (Mirounga angustirostris) in California, the researchers further "
          "reported that some females adopted pups alongside their own or adopted multiple "
          "pups at the same time.\n\n"
          "Which choice best describes the function of the first sentence in the text as a whole?",
          "It provides a theory that is confirmed by the text.",
          "It introduces an occurrence that is examined by the text.",
          "It states a challenge that is described by the text.",
          "It makes an argument that is contradicted by the text.", "B",
          "The first sentence defines alloparental care, which the rest of the passage examines.")

        q(rc, M,
          "The following text is from Sir Arthur Conan Doyle's 1892 novel The Adventures "
          "of Sherlock Holmes. Dr. John Watson has joined a disguised Holmes as they await "
          "a person of interest in an investigation.\n\n"
          "It was already dusk, and the lamps were just being lighted as we paced up and "
          "down in front of Briony Lodge, waiting for the coming of its occupant. The house "
          "was just such as I had pictured it from Sherlock Holmes' succinct description, "
          "but the locality appeared to be less private than I expected. On the contrary, "
          "for a small street in a quiet neighbourhood, it was remarkably animated.\n\n"
          "Which choice best states the main purpose of the text?",
          "It shows a character expressing a lack of surprise regarding a location.",
          "It demonstrates a character's response to a surprising situation.",
          "It details why a character has visited a certain neighborhood.",
          "It contrasts two different characters' assumptions about a location and its activity level.", "B",
          "Watson expected a quiet area but found it surprisingly animated — a response to an unexpected situation.")

        q(rc, M,
          "Between 1883 and 1914, architect Antoni Gaudí designed seven different residential "
          "properties inside and around Barcelona. These buildings represent his personal "
          "style, which combined elements of Gothic and Baroque architecture with his own "
          "signature interest in flowing structures reminiscent of natural landscapes and "
          "features. The buildings have the architectural hallmarks of the time but are also "
          "notable for pushing the boundaries of design into a new era, making Gaudí one of "
          "the first modernist architects.\n\n"
          "Which choice best describes the function of the underlined sentence "
          "('These buildings represent his personal style...') in the text as a whole?",
          "It explains how Gaudí's buildings were often featured in architectural magazines.",
          "It highlights Gaudí's desire to become one of the first modernist architects.",
          "It describes how Gaudí became involved in architecture.",
          "It details certain notable aspects of Gaudí's buildings.", "D",
          "The underlined sentence describes specific notable features of Gaudí's architectural style.")

        q(de, M,
          "The discovery of human teeth and bones from a 700-year-old Pueblo in present-day "
          "Arizona has yielded new information about the people who once lived there. Using "
          "strontium isotope analysis, T. Douglas Price and his team were able to determine "
          "where the pueblo inhabitants originated. By comparing strontium in Pueblo rocks, "
          "human bones and teeth, and rock and bone samples from several different sites, "
          "Price and his team discovered that different groups of Native Americans from "
          "different parts of the Southwest all migrated to the Pueblo following a massive "
          "drought.\n\nWhich choice best states the main idea of the text?",
          "Prior to the development of strontium isotope analysis, scientists needed to dissect rock specimens in order to determine their origin.",
          "Due to an innovation, scientists can uncover and analyze more human bone and tooth remains than they could previously.",
          "Scientists have been successful in locating a Native American migration trail that was utilized 700 years ago.",
          "With the assistance of specialized technology, scientists have determined the origins of some members of the Pueblo tribe.", "D",
          "The text is mainly about how strontium isotope analysis revealed the origins of Pueblo inhabitants.")

        q(rc, M,
          "The following text is adapted from E. M. Forster's 1908 novel A Room with a View. "
          "Lucy, a young British woman, is visiting the city of Florence, Italy.\n\n"
          "Her first morning was ruined, and she might never be in Florence again. A few "
          "minutes ago she had been all high spirits, talking as a woman of culture, and "
          "half persuading herself that she was full of originality. Now she entered the "
          "church depressed and humiliated, not even able to remember whether it was built "
          "by the Franciscans or the Dominicans. Of course, it must be a wonderful building. "
          "But how like a barn! And how very cold!\n\nWhich choice best states the main idea of the text?",
          "Lucy is visiting a church in Florence because she has never been inside of a church before.",
          "Lucy is depressed until the warmth of the church raises her spirits.",
          "Lucy is upset and flustered by an experience she has had in Florence.",
          "Lucy is initially disappointed by the appearance of a church in Florence but is soon enamored with it.", "C",
          "Lucy's morning has been ruined and she is depressed — she is upset by an experience in Florence.")

        q(rc, M,
          "The American designer, screenwriter, and producer Polly Platt was a hugely "
          "influential force in film during the late twentieth century, but her contributions "
          "are often overlooked by those outside of the film industry. The lack of visible "
          "career opportunities for women in male-dominated Hollywood contributed to her "
          "being overshadowed by the men whose careers she supported. Notably, she launched "
          "the careers of famous directors such as Cameron Crowe, Wes Anderson, and her "
          "ex-husband Peter Bogdanovich through her creative roles behind the scenes that "
          "relegated her to the background despite her artistic genius.\n\n"
          "Which choice best states the main idea of the text?",
          "Few of Platt's films are available for purchase today because she only worked on a small number of pictures.",
          "People may not be as aware of Platt's work as they should be because Crowe, Anderson, and Bogdanovich have received more attention.",
          "During Platt's career, her contributions to the film industry have been more frequently acknowledged than those of Crowe, Anderson, or Bogdanovich's.",
          "Platt worked on some of the same films as Crowe, Anderson, and Bogdanovich but used different filmmaking techniques than they did.", "B",
          "The text emphasizes that Platt's contributions are overlooked, overshadowed by the men whose careers she helped.")

        q(de, M,
          "The table below shows Buddhists in Three Asian Countries and North America:\n\n"
          "India: ~9 million Buddhists, 2% of world Buddhist population\n"
          "China: ~244 million Buddhists, 50% of world Buddhist population\n"
          "Thailand: ~64 million Buddhists, 13% of world Buddhist population\n"
          "North America: ~4 million Buddhists, 1% of world Buddhist population\n\n"
          "Buddhism is a major world religion with an estimated 488 million adherents "
          "worldwide. It is the primary religion of Thailand. Interestingly, even though "
          "Buddhism originated in India, there are other countries that contain a much "
          "larger number of Buddhists among their populations.\n\n"
          "Which choice most effectively uses data from the table to support the underlined claim?",
          "Approximately 50 percent of the world Buddhist population lives in China, while only about one percent of the world Buddhist population lives in North America.",
          "Thailand has approximately 64 million practicing Buddhists, which is much more than the approximate number of Buddhists who live in India.",
          "Thailand is estimated to have at most 16 million practicing Buddhists, while the country contains an estimated 13 percent of the world Buddhist population.",
          "Buddhists make up 50 percent of the population of China, which has 244 million people.", "B",
          "Thailand (64 million) has far more Buddhists than India (9 million), where Buddhism originated — directly supporting the claim.")

        q(de, M,
          "Octavia Butler's 1993 science fiction novel The Parable of the Sower has "
          "influenced literature in several different ways. Its Black female main character "
          "inspired other Black authors to write their own science fiction tales. Lauren "
          "Olamina, the main character, was also influential in starting a wider artistic "
          "movement. The depiction of a Black girl who eventually travels through space "
          "inspired other Black writers to explore the theme of future technology in their "
          "works, contributing to the development of Afrofuturism.\n\n"
          "Which statement, if true, would most strongly support the claim in the underlined sentence?",
          "Novels about Black characters by Black authors written since 1993 have often been compared to The Parable of the Sower.",
          "In social media posts, a number of Black authors cite The Parable of the Sower as a primary influence in writing their own science fiction works.",
          "In interview transcripts, several famous authors who are not Black claim that reading The Parable of the Sower helped them develop their approach to science fiction.",
          "The Parable of the Sower won multiple awards upon publication and is considered by many readers to be the best science fiction book of the last 100 years.", "B",
          "Black authors citing the novel as their primary influence directly supports its role in developing Afrofuturism.")

        q(de, M,
          "The graph below shows Monthly Inches of Rainfall from January to June in "
          "Roanoke and Virginia Beach, Virginia. Both cities show a pattern of decreasing "
          "rainfall from January to February, followed by an increase from April to May.\n\n"
          "A student is conducting research about inches of rainfall per month in cities "
          "across Virginia. While studying trends in Roanoke and Virginia Beach, the student "
          "concludes that rainfall in inches from the months of January to June in these "
          "cities follows a similar pattern.\n\n"
          "Which choice best describes data from the graph that support the student's conclusion?",
          "Roanoke and Virginia Beach both have more than three monthly inches of rainfall from January to February but less than four monthly inches of rainfall from May to June.",
          "The monthly inches of rainfall in both Roanoke and Virginia Beach remain constant from March to April before beginning to increase in May.",
          "The monthly inches of rainfall in both Roanoke and Virginia Beach decrease from January to February and then increase from April to May.",
          "Roanoke and Virginia Beach both have less than three inches of rainfall from January to June.", "C",
          "Both cities show a similar pattern: decrease Jan–Feb, then increase Apr–May.")

        q(rc, M,
          "In writing her 2013 drama The Flick, playwright Annie Baker used a theater "
          "convention of inserting long, awkward silences into her plays. Baker takes this "
          "convention to an extreme; The Flick is three-and-a-half hours long with much of "
          "it taking place in silence. In the play, Baker pays homage to the 'quiet' actors "
          "in Chekhov plays and silent film stars like Charlie Chaplin, who fill silence "
          "with emotion through body language and facial expressions. It might seem like "
          "including awkward silence would be too disquieting for the audience, and in fact, "
          "some people left The Flick in the middle. However, theater critics lauded The "
          "Flick for its acknowledgment of the history of theater and cinema and awarded "
          "Baker the Pulitzer Prize for the work. This reaction suggests that ________\n\n"
          "Which choice most logically completes the text?",
          "Baker influenced many other playwrights to create works with long, awkward silences.",
          "many theater critics may have overlooked Baker's central message in The Flick.",
          "Baker's use of silence helped her complete a goal she had when making The Flick.",
          "silent film star Charlie Chaplin was one of Baker's favorite actors.", "C",
          "Critics praised the silence as an acknowledgment of theater/cinema history — the goal Baker aimed for.")

        q(gv, M,
          "Created in 1978, the Cape Grim Air Archive is a collection of air samples obtained "
          "at the Cape Grim Baseline Air Pollution Station in Tasmania. The location was "
          "chosen because the air coming from the Southern Ocean is unaffected by local "
          "pollution from landmasses. Approximately every three months, researchers fill "
          "stainless steel flasks with air and ________ the samples to the archive.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "were adding", "added", "had added", "add", "D",
          "'Add' is parallel to 'fill' — both are present tense verbs describing the researchers' routine.")

        q(gv, M,
          "How do scientists classify fossils from millions of years ago as those of mammals "
          "or reptiles? Researchers ________ the teeth to help distinguish mammals from "
          "reptiles: mammals have only two sets of teeth, the baby set and the permanent "
          "set, while reptiles replace their teeth throughout their lives.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "to use", "using", "having used", "use", "D",
          "'Use' is the correct simple present form as the main verb of the sentence.")

        q(gv, M,
          "In the 2009 book A Mighty Long Way, Carlotta Walls LaNier describes how her "
          "attendance at Little Rock Central High School in Arkansas as one of the first to "
          "integrate the school ________ her life and the lives of her family and community "
          "members.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
          "to affect", "affected", "having affected", "affecting", "B",
          "'Affected' is the correct past tense verb to complete the noun clause.")

        q(gp, M,
          "Katherine Siva Saubel was a scholar, activist, and tribal leader dedicated to "
          "the preservation of Cahuilla language, history, and culture. She conducted "
          "research with linguists at UCLA as well as the University of Cologne in "
          "________ with anthropologist Lowell John Bean, she wrote Temalpakh (From the "
          "Earth): Cahuilla Indian Knowledge and Usage of Plants.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "Germany, and", "Germany,", "Germany and", "Germany", "A",
          "'Germany, and' correctly connects the two independent clauses with a comma and coordinating conjunction.")

        q(gp, M,
          "In 2011, British choreographer and dancer Sarah Michelson considered the space "
          "and context of the venue when designing the work she called ________ in the "
          "performers' space, the audience is confronted with a new perspective and urged "
          "to identify with the dancers.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "Devotion. Sitting", "Devotion sitting", "Devotion, sitting", "Devotion sitting,", "A",
          "'Devotion.' ends the clause about the work title; 'Sitting in the performers' space' begins the next clause as a participial phrase.")

        q(tr, M,
          "While her husband worked as a mechanic with the Tuskegee Airmen, Azellia White "
          "learned to fly. She earned her pilot's license in 1946, making her one of the "
          "first African American women to earn a license in the United States. ________ "
          "she and her husband, along with two other Tuskegee Airmen, founded the Sky Ranch "
          "Flying Service, a flight school and airport for African American aviators.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Moreover,", "In other words,", "Nevertheless,", "Still,", "A",
          "'Moreover' adds additional information — she didn't just earn her license, she also co-founded a flight school.")

        q(tr, M,
          "Author Aleksis Kivi was one of the first prominent writers in the Finnish "
          "language. In 1864, he wrote the play Heath Cobblers. ________ in 1870, he wrote "
          "the novel Seitsemän veljestä (Seven Brothers), the first significant novel in "
          "Finnish. He is still regarded as the national writer of Finland.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "On the other hand,", "For example,", "Later,", "D",
          "'Later' indicates a chronological progression from 1864 to 1870.")

        q(tr, M,
          "American choreographer and conceptualist Ralph Lemon took ten years to create "
          "a trilogy of performances to present social issues. ________ Lemon expressed "
          "himself through painting, but he found that movement through dance allowed him "
          "to communicate more thoroughly and accurately.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Initially,", "In effect,", "Hence,", "At any rate,", "A",
          "'Initially' introduces the first stage — he started with painting before discovering dance.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "• Miguel Algarín was a Puerto Rican poet and writer.\n"
          "• With other poets, he founded the Nuyorican Poets Café.\n"
          "• The café was noteworthy for popularizing slam poetry, or spoken word poetry, "
          "by hosting poetry slams.\n"
          "• Poetry slams are events at which poetry is performed and judged.\n\n"
          "The student wants to describe what was noteworthy about Algarín's café. Which "
          "choice most effectively uses relevant information from the notes to accomplish this goal?",
          "Algarín helped to found the Nuyorican Poets Café.",
          "Slam poetry, or spoken word poetry, was popularized through events at which poetry is performed and judged.",
          "Algarín's café popularized slam poetry by hosting poetry slams, events at which poetry is performed and judged.",
          "A Puerto Rican poet and writer, Miguel Algarín helped found Nuyorican Poets Café.", "C",
          "Option C combines the key noteworthy fact (popularized slam poetry) with the definition of poetry slams.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "• Alodia was one of the three medieval Nubian kingdoms.\n"
          "• It was located in what is now known as Sudan.\n"
          "• Alodia was formed sometime after 350 CE when the Kingdom of Kush fell.\n"
          "• In historical records, it was first mentioned in 569 CE.\n"
          "• The capital of Alodia was Soba, which was a large trading hub.\n\n"
          "The student wants to specify the year Alodia was first mentioned in the "
          "historical records. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "Alodia, a medieval Nubian kingdom, was first mentioned in historical records in 569 CE.",
          "One of the three medieval Nubian kingdoms, Alodia formed after the Kingdom of Kush fell.",
          "Soba, a large trading hub, was the capital of Alodia.",
          "The Nubian kingdom Alodia formed sometime after 350 CE.", "A",
          "Only option A specifically mentions when Alodia was first mentioned in historical records: 569 CE.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "• Conventionally, opera is a dramatic type of theater consisting of music and singers.\n"
          "• The music is classical, and the singers learn the words from a libretto, or script.\n"
          "• In the 1960s, the idea of a rock opera became appealing to various rock artists and groups.\n"
          "• Rock operas use rock music and are typically released as concept albums.\n"
          "• Rock operas do not have scripts, unless these operas are adapted for the stage.\n\n"
          "The student wants to emphasize a difference between rock operas and conventional "
          "operas. Which choice most effectively uses relevant information from the notes to "
          "accomplish this goal?",
          "Operas have featured classical music but also rock music.",
          "Conventionally, an opera uses a libretto and consists of classical music, not rock music.",
          "Unlike conventional operas, rock operas use rock music and do not have scripts.",
          "Rock operas were developed in the 1960s and are generally released as concept albums.", "C",
          "Option C directly contrasts the two: conventional operas have scripts and classical music; rock operas do not have scripts and use rock music.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Section 1, Module 2—Easier
        # ════════════════════════════════════════════════════════════════

        q(ev, E,
          "Dame Zaha Hadid, an architect active during the second half of the twentieth "
          "century, was known for her organic and ________ building designs. Rather than "
          "adhering to the symmetry of traditional structural elements, she favored "
          "deconstructivism, which is defined by fragmented shapes and flowing movements.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "logical", "unusual", "straightforward", "typical", "B",
          "'Unusual' fits — Hadid's deconstructivist designs were far from conventional.")

        q(ev, E,
          "Each dolphin has its own whistle sequence, similar to a human name, that its "
          "mother teaches it when it is young. These individualized ________ help dolphins "
          "locate one another in murky water and other situations where visibility is poor.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "contracts", "sizes", "ornaments", "arrangements", "D",
          "'Arrangements' best describes the individualized whistle sequences (sonic patterns) dolphins use to identify each other.")

        q(ev, E,
          "Family Legacies: The Art of Betye, Lezley, and Alison Saar was an exhibit of "
          "mixed-media assemblages exploring the Saar family's history, traditions, and "
          "spirituality. The exhibit ________ two generations, tracing how daughters Alison "
          "and Lezley expanded their mother Betye's work.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "disregarded", "adopted", "bridged", "criticized", "C",
          "'Bridged' two generations — the exhibit connected across two generations of artists.")

        q(ev, E,
          "Alfred Hitchcock's successful movie career was aided by the ________ of "
          "accomplished composer Bernard Herrmann, whose musical works provided the perfect "
          "backdrop for Hitchcock's films such as the comedic The Trouble With Harry and "
          "the terrifying, award-winning film Psycho.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "criticisms", "arguments", "talent", "retirement", "C",
          "Hitchcock's career was aided by Herrmann's 'talent' as a composer.")

        q(rc, E,
          "Canals, rivers, and storm drains carry garbage and debris out into the ocean. "
          "But the debris carried out by these waterways could not make it farther out to "
          "sea without the help of a strong ocean current. Researchers label these currents "
          "'gyres.' These gyres carry debris along a consistent pathway, leading to "
          "significant accumulation of garbage at specific points in the ocean. Though "
          "oceanographers had long suspected the existence of one such garbage patch in "
          "the Pacific Ocean, it was Charles Moore, a racing boat captain, who discovered "
          "the Great Pacific Garbage Patch, which covers 1.6 million square kilometers.\n\n"
          "Which choice best describes the function of the underlined portion "
          "('Researchers label these currents \"gyres\"') in the text as a whole?",
          "It details the difference among three types of waterways.",
          "It highlights Charles Moore's opinion about the challenges he has overcome.",
          "It presents a scientific term that is relevant to the rest of the discussion.",
          "It highlights the intriguing nature of the discovery that is mentioned.", "C",
          "The underlined sentence introduces the scientific term 'gyres,' which is central to explaining how debris accumulates.")

        q(de, E,
          "Text 1: Joshua Plotnik and Frans B. M. de Waal observed 26 Asian elephants "
          "(Elephas maximus) to determine how they reacted to distressing stimuli. The "
          "researchers observed that when one animal was distressed, other elephants "
          "approached the distressed animal and touched it with their trunks. The "
          "researchers claimed that this behavior suggests that elephants can be altruistic, "
          "trying to console other elephants without any direct benefit to themselves.\n\n"
          "Text 2: The idea of animals trying to console one another through touch in times "
          "of distress seems logical, particularly for a species such as elephants, which "
          "have been known to exhibit various forms of tactile behavior. However, it is "
          "quite likely that the animals are simply congregating following an event that "
          "distressed several individuals, with some perhaps showing a delayed reaction to "
          "the distressing stimuli and seeking social cohesion as a means of safety.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond to the "
          "researcher's claim in Text 1 regarding the behavior of the Asian elephants?",
          "The behavior observed may be sufficiently explained without concluding that the elephants were exhibiting altruistic tendencies.",
          "The behavior observed may have been due to the confined nature of the elephant enclosure rather than to the distress of an individual.",
          "The behavior observed likely implies that the elephants were actively working to benefit themselves by seeking comfort in others.",
          "The behavior observed may not be evidence of altruistic behavior in Elephas maximus because only some of the elephants exhibited it.", "A",
          "Text 2 suggests an alternative, non-altruistic explanation — congregating for social cohesion rather than altruism.")

        q(rc, E,
          "Los Angeles's Contra-Tiempo Activist Dance Theater, founded by Ana Maria "
          "Alvarez, creates dance works featuring multimedia in collaborations with artists "
          "such as choreographer Marjani Forté. For the company's joyUS justUS performance, "
          "Alvarez invites members of the audience to participate in dance and movement "
          "exercises and then create their own collaborative dance.\n\n"
          "Which choice best states the main idea of the text?",
          "Alvarez invites members of the audience to create their own dance to illustrate the complexity of the task.",
          "The Contra-Tiempo Activist Dance Theater company performs dances from all over the United States but mostly performs dances choreographed by Los Angeles natives.",
          "Alvarez began the Contra-Tiempo Activist Dance Theater company to perform dances choreographed by Marjani Forté.",
          "The Contra-Tiempo Activist Dance company gives audience members the opportunity to both observe and participate in collaborative dance performances.", "D",
          "The text describes how audience members participate in dance exercises and create their own collaborative dance.")

        q(de, E,
          "The table below shows data from anthropologist Florent Détroit's 2019 discovery "
          "of Homo luzonensis fossils:\n\n"
          "Homo sapien: molar diameter 10mm, average height 5'4\"\n"
          "Homo floresiensis: molar diameter 9.8mm, average height 3'6\"\n"
          "Homo luzonensis: molar diameter 8mm, average height 3'5\"\n\n"
          "The fossils suggest that, compared to several other hominin species, "
          "Homo luzonensis had ________\n\n"
          "Which choice most effectively uses data from the table to complete the claim?",
          "a smaller molar diameter, and a taller average height.",
          "a larger molar diameter, and a shorter average height.",
          "a larger molar diameter, and a taller average height.",
          "a smaller molar diameter, and a shorter average height.", "D",
          "Homo luzonensis had the smallest molar diameter (8mm) and the shortest average height (3'5\") of the three species.")

        q(de, E,
          "The table below shows data about celestial objects:\n\n"
          "Mercury: primary gas = Oxygen, 42%\n"
          "Venus: primary gas = Carbon dioxide, 96%\n"
          "Pluto: primary gas = Nitrogen, 90%\n"
          "Earth's Moon: primary gas = Argon, 70%\n"
          "Titan (Moon of Saturn): primary gas = Nitrogen, 97%\n\n"
          "Like Earth, some objects in the solar system have atmospheres composed of more "
          "than 80% nitrogen. Two examples of such objects are ________\n\n"
          "Which choice most effectively uses data from the table to complete the statement?",
          "Pluto and Earth's Moon.", "Titan and Pluto.", "Mercury and Titan.", "Pluto and Mercury.", "B",
          "Titan (97% nitrogen) and Pluto (90% nitrogen) both have atmospheres more than 80% nitrogen.")

        q(de, E,
          "Captain Dimitrios Kontos and his team of Greek sponge divers discovered the "
          "wreckage of a first-century cargo ship. One of the items recovered from the "
          "wreck was the Antikythera mechanism. This mechanism is a complex geared device "
          "from ancient times, and many scholars believe it is the world's first computer.\n\n"
          "Which finding, if true, would most directly support the scholars' claim?",
          "Debris from other mechanisms has been found at the Greek site that were probably the work of inventors.",
          "Other versions of the same first-century mechanism have been found in the ruins of many residences in the area, including in one residence that may have belonged to an inventor.",
          "Similar mechanisms have been discovered at other sites dating to the same century whose people often shared ideas with those who lived near the Greek site.",
          "Descriptions of the mechanism from the same time period have been noted to claim that its primary purpose was to calculate complex mathematical approximations.", "D",
          "Ancient descriptions calling the device a computing mechanism would directly support the claim it is the world's first computer.")

        q(de, E,
          "Water without any dissolved particles appears blue because that is the color of "
          "light that is reflected from the water particles. Water containing sediment from "
          "broken-down rock looks brown or yellow because those are the hues most commonly "
          "reflected off of sediment. Water containing algae usually looks green because "
          "green is the primary color reflected off the algae. However, approximately "
          "one-third of rivers in the United States have changed color in the last 35 years, "
          "with normally algae-rich waters becoming more yellow. One team of researchers "
          "hypothesized that this phenomenon is the result of human activity, with dams and "
          "water runoff altering the composition of the dissolved particles in the water.\n\n"
          "Which finding, if true, would most directly weaken the team's hypothesis?",
          "Algae-rich waterways can appear yellow if the algae are exposed to certain naturally occurring compounds.",
          "Yellow or brown water remains the same color when mixed with blue water due to existing sediment in the water.",
          "Dams and water runoff produce a deeper yellow water color in the United States than they do in other regions of the world.",
          "Yellow or brown water and green water are rarely mixed together in nature.", "A",
          "If algae turn yellow due to natural compounds (not human activity), this weakens the hypothesis that human activity is the cause.")

        q(rc, E,
          "Appalachian fiddle musicians, many of whom immigrated from Scotland and Ireland "
          "in the 1700s, gave rise to modern-day American bluegrass music. The genre is "
          "still popular today, with annual fiddle contests drawing up to 10,000 people at "
          "a time. However, historical recordings of the traditional fiddle music are few "
          "and far between, and those that do exist are largely stored on media that is "
          "susceptible to decay. This has led some historians to dedicate their time to "
          "implement safer storage practices for the recordings. By ensuring the security "
          "of these valuable sound and video records, they are also ________\n\n"
          "Which choice most logically completes the text?",
          "ensuring that listeners of fiddle music can attend concerts by their favorite performers.",
          "protecting at least some of the history of Appalachian musical culture.",
          "expanding awareness of Appalachian fiddle music beyond the lands of its origin.",
          "assisting future Appalachian fiddle musicians who are interested in recording their own music.", "B",
          "Preserving the recordings preserves the history of Appalachian musical culture.")

        q(rc, E,
          "Based on computer models of the collision that formed our moon, Keiichi Wada, "
          "Eiichiro Kokubo, and Junichiro Makino determined that the disk that eventually "
          "coalesced into the Moon must have been primarily solid or liquid particles. The "
          "team calculated that a disk made primarily of gas would have been vaporized in "
          "the collision and a satellite the size of our Moon would not have formed. In "
          "their models, the team set the impact velocity at approximately 15 km/s, leading "
          "to the development of a primarily gaseous disk and a very small satellite. "
          "Because collision velocity depends on the masses of the colliding bodies, the "
          "researchers concluded that ________\n\nWhich choice most logically completes the text?",
          "the disk that eventually formed the Moon was of significant enough mass to also form the Earth.",
          "the impact velocity at which the collision that formed the Moon occurred must be slower than the initial calculations suggested.",
          "the mass of the bodies that collided to form the Moon must have been within a specific range.",
          "if the impact velocity of the collision that formed the Moon had been faster, the moon would have been much larger than it is today.", "C",
          "Since velocity depends on mass, and the right conditions had to produce the Moon, the masses must have been within a specific range.")

        q(gv, E,
          "Ramola Vaidya is a wastewater engineer. She studies ways to make treated "
          "wastewater flow into underground water sources called aquifers rather than into "
          "rivers. This allows aquifers that have run dry ________ and prevents local "
          "waterways from becoming polluted.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "to refill", "refilled", "refills", "have refilled", "A",
          "'To refill' is the correct infinitive form after 'allows... to'.")

        q(gp, E,
          "Critics of young adult literature have ________ The Outsiders by S. E. Hinton, "
          "a novel based on the author's own high school experiences in 1960s Tulsa, "
          "Oklahoma, as one of the pioneering works in the genre.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "recognized.", "recognized:", "recognized", "recognized,", "C",
          "No punctuation is needed between the verb 'recognized' and its object.")

        q(gv, E,
          "Complete metamorphosis, or holometabolism, is a complex process used by some "
          "insects, such as butterflies and bees. You ________ the less complex partial "
          "metamorphosis, when insects change the shape of their bodies, in the previous "
          "chapter.\n\nWhich choice completes the text so that it conforms to the conventions of Standard English?",
          "saw", "will see", "see", "will be seeing", "A",
          "'Saw' is the correct past tense — 'in the previous chapter' indicates this information was already presented.")

        q(gp, E,
          "Foscadh, a movie in which the actors speak the Irish language, is based on "
          "Donal Ryan's novel The Thing About December. It was nominated for the 2022 "
          "Academy Awards in the category of Best International Foreign Film. In the movie, "
          "the character of John Cunliffe, played by Dónall Ó Héalaí, suddenly ________ "
          "the responsibilities of adulthood after becoming an orphan and inheriting his "
          "parents' farm.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "learns. About", "learns about", "learns, about", "learns; about", "B",
          "No punctuation is needed between the verb 'learns' and the preposition 'about'.")

        q(gp, E,
          "The marble lions on each side of the entrance to the Beaux-Arts Main Branch "
          "building of the New York Public Library are two of New York City's most famous "
          "and beloved works of public art. The library's website says that ________ named "
          "'Patience' and 'Fortitude' by Mayor Fiorello LaGuardia in the 1930s after the "
          "virtues the city's residents would need during the ongoing Great Depression.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "some were", "it was", "one was", "they were", "D",
          "'They were' correctly refers to the plural subject 'the marble lions'.")

        q(gp, E,
          "GMO (Genetically Modified Organisms) foods can contain higher amounts of certain "
          "nutrients than non-GMO ________ critics of GMO foods claim that the long-term "
          "health risks are still unknown.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "foods", "foods, but", "foods,", "foods but", "B",
          "'Foods, but' correctly joins two independent clauses with a comma and coordinating conjunction.")

        q(gp, E,
          "When you first see the traditional Croatian pastry known as a licitar, you might "
          "not recognize it as something edible. It is often bright red and highly decorated, "
          "sometimes even used as a Christmas tree ornament. Licitars date back to the "
          "Middle Ages, and in the 18th and 19th centuries, ________ made by highly "
          "respected craftspeople.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "these were", "this was", "they were", "those were", "C",
          "'They were' correctly uses a pronoun agreeing with the plural 'licitars'.")

        q(gv, E,
          "By utilizing single nuclei RNA-sequencing (sNuc-Seq), scientists can explore "
          "the previously unknown mechanism by which axolotl salamanders are able to "
          "regenerate brain matter. sNuc-Seq could be utilized as a method of single-cell "
          "sequencing that ________ the cells' nuclei instead of the entire cells.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "has targeted", "targets", "targeted", "is targeting", "B",
          "'Targets' is the correct simple present tense for a factual statement about what the method does.")

        q(gv, E,
          "Hippocamp, the smallest moon known to orbit the planet Neptune, ________ named "
          "after the same mythological sea-horse monster that inspired the name for the "
          "part of the human brain responsible for managing memory.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "is", "were", "are", "have been", "A",
          "'Is' is correct — Hippocamp is singular.")

        q(tr, E,
          "English materials scientist Nicola Spaldin studies multiferroics, materials that "
          "display multiple ferroic properties, such as ferromagnetism, ferroelasticity, "
          "and ferroelectricity. Spaldin was one of the first researchers to explain why "
          "there are so few multiferroics; ________ Spaldin was asked to join a team "
          "studying bismuth ferrite and its multiferroic characteristics.\n\n"
          "Which choice completes the text with the most logical transition?",
          "in other words,", "in spite of this,", "as a result,", "likewise,", "C",
          "'As a result' — her expertise in explaining why multiferroics are rare led (as a result) to her being asked to study one.")

        q(tr, E,
          "Wildfires in the western United States affect the weather in the central United "
          "States. ________ wildfires produce increased levels of aerosol and heat, creating "
          "an environment more conducive to storms and causing heavy precipitation and large "
          "hail in the central United States.\n\n"
          "Which choice completes the text with the most logical transition?",
          "In addition,", "Likewise,", "Therefore,", "Specifically,", "D",
          "'Specifically' introduces the specific mechanism by which wildfires affect weather.")

        q(tr, E,
          "The Atlantic menhaden is an example of a keystone species, sometimes referred "
          "to as 'the most important fish in the sea' despite its small size. Menhaden "
          "perform an important function within their environment by consuming large amounts "
          "of algae that can grow out of control and produce toxic 'blooms' in the absence "
          "of menhaden. ________ they are a key food source for shorebirds and larger "
          "oceanic fish.\n\nWhich choice completes the text with the most logical transition?",
          "Furthermore,", "Indeed,", "For instance,", "Specifically,", "A",
          "'Furthermore' adds an additional reason why menhaden are important — they're also a food source.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "• Saturn's rings are about 45,000 miles wide and 1,000 yards thick.\n"
          "• They are primarily composed of pure water ice.\n"
          "• Multiple theories have been proposed to explain the origin of Saturn's rings.\n"
          "• Some astronomers believe Saturn's rings were formed from the remnants of a moon.\n"
          "• This moon may have drifted too close to Saturn and then been destroyed by tidal "
          "forces, resulting in the rings' formation.\n\n"
          "The student wants to specify how Saturn's rings may have been formed. Which choice "
          "most effectively uses relevant information from the notes to accomplish this goal?",
          "Saturn's rings were formed primarily out of pure water ice.",
          "According to some astronomers, it's possible that when one of Saturn's moons got too close to the planet, tidal forces destroyed the moon, forming Saturn's rings.",
          "Astronomers have proposed various theories to explain the formation of Saturn's rings.",
          "Saturn's rings are 1,000 yards thick, 45,000 miles wide, and composed primarily of pure water ice.", "B",
          "Option B directly specifies one mechanism for how the rings formed: a moon destroyed by tidal forces.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "• The inland taipan (Oxyuranus microlepidotus) is a species of Australian snake "
          "that produces an extremely harmful venom.\n"
          "• The inland taipan is a member of the Elapidae family of snakes, the majority "
          "of which are venomous.\n"
          "• One bite from the inland taipan contains enough venom to kill more than 100 "
          "average-sized humans.\n"
          "• It typically feeds on marsupials and rodents, as its venom is specifically "
          "adapted to kill mammals.\n"
          "• After biting its prey, the inland taipan instantly releases its hold, unlike "
          "other snakes of the Elapidae family.\n\n"
          "The student wants to emphasize how harmful the venom of the inland taipan can "
          "be. Which choice most effectively uses relevant information from the notes to "
          "accomplish this goal?",
          "The inland taipan instantly releases its hold after biting its prey, unlike other members of the mostly venomous Elapidae family of snakes.",
          "The inland taipan's venom is specifically harmful to mammals, such as marsupials and rodents.",
          "The Elapidae family of snakes, the majority of which are venomous, includes Australia's inland taipan.",
          "The venom from one bite of an inland taipan is extremely harmful, capable of killing more than 100 average-sized humans.", "D",
          "Option D best emphasizes the harm by quantifying it: one bite can kill more than 100 humans.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Section 1, Module 2—Harder
        # ════════════════════════════════════════════════════════════════

        q(ev, H,
          "A sculptor and designer, Isamu Noguchi was deeply affected by his international "
          "travels and ________ incorporating a range of cultural perspectives into his art "
          "pieces. He accomplished this by experimenting with different art mediums, studying "
          "traditional Japanese pottery and Chinese calligraphy, and utilizing a broad "
          "spectrum of materials such as bronze, aluminum, steel, and cast iron.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "skeptical about", "unfamiliar with", "focused on", "resistant to", "C",
          "Noguchi was deeply affected by travels and 'focused on' incorporating diverse cultural perspectives.")

        q(ev, H,
          "A single paragraph summary of Alan Paton's novel Cry, the Beloved Country can't "
          "possibly capture the ________ undertaken by James Jarvis, who goes from expressing "
          "ignorance towards the plight of those around him to providing aid and hope to "
          "those downtrodden by societal injustices.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "burden", "precaution", "dormancy", "transformation", "D",
          "James Jarvis undergoes a 'transformation' — a fundamental change from ignorance to compassion.")

        q(ev, H,
          "The theremin, an unconventional and non-traditional instrument, is named for its "
          "inventor, Russian scientist Lev Theremin. This electronic instrument, a predecessor "
          "to the synthesizer, is made of a box that emits sound waves. The warbling musical "
          "tones produced are highly ________; the pitch and volume can be altered "
          "substantially by minute changes to the position of the musician's hands between "
          "two antennae on either end of the box.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "neglected", "diverse", "commanding", "predictable", "C",
          "'Commanding' best describes theremin tones — powerful and attention-grabbing, with pitch and volume varied dramatically by hand position.")

        q(ev, H,
          "In the 1990s, the rise in personal computers allowed artists greater access to "
          "MIDI devices that create electronic music, giving musicians such as Imogen Heap "
          "the ability to produce full albums on their own. Heap utilized this ________ "
          "access to creative technology to craft influential works that blend electronica "
          "and emotion, like her album Speak for Yourself (2005).\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "routine", "expanded", "unstable", "expected", "B",
          "Personal computers 'expanded' access to creative technology for musicians like Heap.")

        q(de, H,
          "Text 1: Over the past four decades, citizens of Saipan, one of the Northern "
          "Mariana Islands, have reported several sightings of invasive brown tree snakes "
          "(Boiga irregularis), although none have been confirmed. Amy Adams and colleagues "
          "conducted multiple active surveys for the snakes over a 19-year period. "
          "Surprisingly, they observed no brown tree snakes on the island. While this "
          "result does not prove that brown tree snakes do not occur on Saipan, it strongly "
          "suggests that there is not an established population of them.\n\n"
          "Text 2: Not only have there been many reported sightings of brown tree snakes "
          "(Boiga irregularis) on Saipan since 1980, but multiple snakes also have been "
          "confirmed intercepted at ports of entry. The snakes are well camouflaged, and "
          "there were probably individuals hidden during the Adams team's surveys. Since it "
          "only takes a small number of this invasive species to devastate an ecosystem, "
          "the island of Saipan must continue to be surveyed so that appropriate "
          "countermeasures can be taken.\n\n"
          "Based on the texts, Adams's team and the author of Text 2 would most likely "
          "agree with which statement about brown tree snakes?",
          "It may be difficult to locate brown tree snakes on the island of Saipan.",
          "Many brown tree snakes are better able to camouflage themselves on Saipan than they are on other islands.",
          "More brown tree snakes would probably be located on the island of Saipan if different types of surveys were conducted.",
          "Brown tree snakes are likely to be difficult to locate on Saipan because there is a much smaller population of them than of other snake species on the island.", "A",
          "Text 1: surveys found none (hard to find). Text 2: snakes are well camouflaged (hard to find). Both agree they're difficult to locate.")

        q(rc, H,
          "Los Angeles's Contra-Tiempo Activist Dance Theater, founded by Ana Maria "
          "Alvarez, creates dance works featuring multimedia in collaborations with artists "
          "such as choreographer Marjani Forté. For the company's joyUS justUS performance, "
          "Alvarez invites members of the audience to participate in dance and movement "
          "exercises and then create their own collaborative dance.\n\n"
          "Which choice best states the main idea of the text?",
          "Alvarez invites members of the audience to create their own dance to illustrate the complexity of the task.",
          "The Contra-Tiempo Activist Dance Theater company performs dances from all over the United States but mostly performs dances choreographed by Los Angeles natives.",
          "Alvarez began the Contra-Tiempo Activist Dance Theater company to perform dances choreographed by Marjani Forté.",
          "The Contra-Tiempo Activist Dance company gives audience members the opportunity to both observe and participate in collaborative dance performances.", "D",
          "The text describes how audience members both observe and actively participate in creating collaborative dance.")

        q(rc, H,
          "Medical studies can be interventional, in which people are placed into treatment "
          "and control groups, or observational, in which people who may fall into such "
          "groups are observed without interference. Each type of study is valuable in "
          "different ways. Interventional studies allow researchers to directly investigate "
          "the efficacy of a new medicine, for example, with less potential for inaccurate "
          "data due to outside factors. Observation studies can help researchers determine "
          "the validity of diagnostic tests or the effects of an environmental change. "
          "However, if the results of an interventional and an observational study on "
          "patients who have undergone heart surgery are in opposition, there may have been "
          "bias in participant selection in one or both of the studies that affected the "
          "results produced.\n\nWhich choice best states the main idea of the text?",
          "Conflicting results between interventional and observational studies of patients such as those who have undergone heart surgery are strong indicators of an error made by both studies that impacted the credibility of those studies.",
          "When the results of an interventional study and those from an observational study of patients such as those who have undergone heart surgery conflict, the interventional study is more likely than the observational study to produce credible data.",
          "Studying patients such as those who have undergone heart surgery in both interventional and observational modalities often leads to contradictory results that scientists struggle to reconcile.",
          "Patients such as those who have undergone heart surgery can be studied in both interventional and observational modalities, but each has different advantages and must still account for the possibility of bias.", "D",
          "The text explains both types of studies, their advantages, and notes that both can be subject to bias.")

        q(de, H,
          "The graph shows Nesting Success Rates of Loggerhead Sea Turtles Based on "
          "Presence of Nourishment (2001–2003). Key data: Nourished beach nesting ratios: "
          "2001 ≈ 0.58, 2002 ≈ 0.30, 2003 ≈ 0.52. Non-nourished beach ratios: "
          "2001 ≈ 0.62, 2002 ≈ 0.63, 2003 ≈ 0.57.\n\n"
          "A section of beach in the Archie Carr National Wildlife Refuge in Florida was "
          "artificially nourished in 2002. Biologists Kelly A. Brock and colleagues "
          "investigated the nesting success of loggerhead sea turtles on the nourished beach "
          "and an adjacent non-nourished beach. They reasoned that the unfamiliarity of the "
          "loggerhead turtles to the artificial nourishment initially deterred them from "
          "nesting at the nourished beach, but that this effect was reduced as the turtles "
          "became more acclimated to the nourishment.\n\n"
          "Which choice best describes data from the graph that support Brock and "
          "colleagues' reasoning?",
          "The nesting success ratio at the nourished beach dropped from 2001 to 2002, but in 2003 it increased and became closer to the nesting success ratio at the non-nourished beach.",
          "The lowest nesting success ratio at the nourished beach was approximately 0.3, and the highest nesting success ratio at the non-nourished beach was approximately 0.63.",
          "The nourished beach had a greater nesting success ratio in 2001 than did the non-nourished beach, and this difference fluctuated significantly in 2002 and again in 2003.",
          "The highest nesting success ratio for the non-nourished beach was in 2001, but the non-nourished beach achieved a nesting success ratio of 0.5 or higher for all three years studied.", "A",
          "The nourished beach dropped in 2002 (when nourishment was new) and recovered in 2003 (as turtles acclimated) — supporting the reasoning.")

        q(de, H,
          "In 1965, Congress established the National Endowment for the Arts (NEA), which "
          "operates as an independent federal agency, to provide grant funds to schools, "
          "nonprofits, and individuals in an effort to democratize participation in the "
          "arts. A spokesperson for the NEA claims that its funds have resulted in a "
          "significant increase in the number of non-profit theater companies and symphony "
          "orchestras in the United States.\n\n"
          "Which quotation from a work by an economist would be the most effective evidence "
          "for the spokesperson to include in support of this claim?",
          '"The priority of the NEA was to promote the growth of the arts, and public records indicate that its funding has contributed to a six-fold increase in the number of non-profit theater companies over the last 50 years."',
          '"Although the NEA started as a government initiative, activists successfully called for its establishment as an independent agency because they believed it could better accomplish its goal of promoting the arts that way."',
          '"For decades, the subsidy of arts programs in foreign countries was supported by the citizens of those countries, but in the United States, the proposal to create the National Endowment for the Arts was initially met with skepticism by the general population."',
          '"Congress\'s creation of an independent federal agency for the arts echoed a prevalent belief among US citizens that the role of a governing body is not only to legislate but also to enrich the lives of its populace."', "A",
          "Option A directly supports the claim by citing a six-fold increase in non-profit theater companies due to NEA funding.")

        q(de, H,
          "A primary pathway in the water cycle involves the evaporation of water from "
          "Earth's surface followed by its condensation in the atmosphere and return to the "
          "surface as precipitation. Hans Knoche and Harald Kunstmann used meteorological "
          "models with moisture-tagging capabilities to track the movement of moisture from "
          "a surface source to its eventual destination as precipitation. The researchers "
          "tagged the water in Lake Volta in Ghana, West Africa, and used the model to "
          "determine how much of the water evaporated from the lake returned locally. "
          "Average recycling ratios for other regions fall between 10 and 50%. They "
          "concluded that very little local precipitation comes from Lake Volta and most of "
          "the water that evaporates from the lake is transported elsewhere.\n\n"
          "Which finding, if true, would most directly support the researchers' conclusion?",
          "Water evaporated from Lake Volta accounts for just 6% of the precipitation in the area surrounding the lake, and only 2% of the water evaporated from Lake Volta returns to the lake itself as precipitation.",
          "The water evaporated from Lake Volta contains higher quantities of saline, which causes water to evaporate more slowly, and has an average recycling ratio between 10% and 50%.",
          "In the valley surrounding Lake Volta, the average recycling ratio was above 10% near the lake's shoreline and below 10% farther from the lake.",
          "The majority of the area surrounding Lake Volta was found to have an average recycling ratio greater than 50%.", "A",
          "A recycling ratio of only 6% / 2% directly supports the conclusion that most water is transported elsewhere.")

        q(de, H,
          "The table shows a survey by researcher Simon Shackley on public perception of "
          "offshore carbon dioxide capture and storage (CCS):\n\n"
          "Response | Initial % | Final %\n"
          "Don't know | 25 | 8\n"
          "Approve | 11 | 32\n"
          "Strongly approve | 2 | 6\n"
          "Disapprove | 24 | 16\n"
          "Strongly disapprove | 14 | 10\n\n"
          "The team found that educating people about the process increased public approval. "
          "For example, 25% of respondents did not know what they thought about CCS at the "
          "start of the survey, while at the end, that number decreased to 8% and ________\n\n"
          "Which choice most effectively uses data from the table to complete the text?",
          "16% of respondents stated that they strongly approved of carbon dioxide capture and storage.",
          "24% of respondents stated that they disapproved of carbon dioxide capture and storage.",
          "32% of respondents stated that they approved of carbon dioxide capture and storage.",
          "10% of respondents stated that they strongly disapproved of carbon dioxide capture and storage.", "C",
          "After education, approval rose to 32% — showing the increase in approval, consistent with the text's claim about education.")

        q(rc, H,
          "The Rapa Nui people settled on the island of Rapa Nui, also known as Easter "
          "Island, sometime before 1200 CE and lived in isolation for hundreds of years. "
          "They are the only Polynesian civilization known to have developed writing, a "
          "pictorial script called Rongorongo, which researchers and linguists have been "
          "unable to decipher. Nevertheless, knowledge of the Rapa Nui people has been "
          "carried forward over time through archaeological artifacts, customs, and oral "
          "traditions. This suggests that ________\n\nWhich choice most logically completes the text?",
          "investigating the culture's archaeological artifacts has enabled researchers to decode the culture's writing system.",
          "researching a culture is more straightforward without an understanding of the culture's writing system.",
          "deciphering a culture's writing system isn't a requirement in order to gain insight into that culture.",
          "linguistics research should focus on uncovering archaeological artifacts rather than understanding pictorial scripts.", "C",
          "Despite not deciphering Rongorongo, knowledge of Rapa Nui persists — so deciphering the writing isn't required to understand the culture.")

        q(de, H,
          "In Brazil, capuchin monkeys have been found to use stones to open seeds and "
          "nuts. They choose stones based on their specific properties. For example, the "
          "stones the monkeys used as a hammer were four times heavier than average stones, "
          "while the stones used as anvils were over eight times heavier. When studying "
          "excavated stone tools that were used by monkeys about 600 to 700 years ago, "
          "archaeologist Michael Haslam found that the tools are similar to the ones used "
          "by monkeys today in terms of rock materials and weights, and both tool types had "
          "been arranged in small piles to be used again and again. This suggests to Haslam "
          "that ________\n\nWhich choice most logically completes the text?",
          "monkeys have learned that both types of stone tools are more effective than their own teeth for opening seeds and nuts.",
          "stone tools of both types are valuable enough for monkeys to keep and reuse as needed.",
          "stones used as hammers are easier for the monkeys to use than stones used as anvils.",
          "monkeys prefer to trade stones used as hammers but won't trade the stones they use as anvils.", "B",
          "The fact that tools were piled for reuse — 600-700 years ago and today — suggests they are valuable enough to keep.")

        q(gv, H,
          "Neil Gaiman's novel Coraline follows the adventures of a young girl who discovers "
          "a world that mirrors her own but holds a sinister secret. The book's depiction of "
          "children ________ the themes of developing courage and overcoming adversity even "
          "at a young age.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "are exploring", "explores", "explore", "have explored", "B",
          "'Explores' is correct — the singular subject 'depiction' requires a singular verb.")

        q(gp, H,
          "Wound care is a growing concern in the healthcare system due to costs and "
          "complications in the healing process. A team of scientists and engineers in the "
          "UK is working to create wound dressings that contain biosensors: these sensors "
          "monitor wound healing in real ________ prevent risk of infection, and save on "
          "healthcare costs.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "time,", "time;", "time", "time. And", "A",
          "'Time,' creates a list: 'monitor wound healing in real time, prevent risk of infection, and save on healthcare costs.'")

        q(gp, H,
          "Gravity, an attraction that occurs between all objects that have ________ is "
          "significantly weaker than the other three fundamental forces but has the most "
          "obvious effect on humans' lives.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "mass—", "mass", "mass and", "mass,", "D",
          "'Mass,' closes the relative clause 'that occurs between all objects that have mass,' with a comma before the main verb 'is'.")

        q(gp, H,
          "The technology of search engines has transformed the internet by allowing "
          "keywords or questions to be inputted and then generating a list of relevant "
          "sources within ________ the process of researching each source can be "
          "time-consuming in comparison to the more direct answers that an AI chatbot "
          "can provide.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "seconds still,", "seconds, still;", "seconds, still,", "seconds; still,", "D",
          "'Seconds; still,' — the semicolon separates two independent clauses; 'still' is a transition meaning 'nevertheless'.")

        q(gp, H,
          "A research initiative from Daniel Hermens and other Australian scientists, "
          "________ can be predicted by analyzing young people's 'brain fingerprints' over time.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "the Longitudinal Adolescent Brain Study has used MRI scans to show that mental health outcomes",
          "MRI scans—used by the Longitudinal Adolescent Brain Study—show that mental health outcomes",
          "mental health outcomes, the Longitudinal Adolescent Brain Study has used MRI scans to show,",
          "it was shown in the Longitudinal Adolescent Brain Study that mental health outcomes", "A",
          "'The Longitudinal Adolescent Brain Study' correctly identifies the research initiative as the subject of the main clause.")

        q(gp, H,
          "In the 1990s, Lebanese contemporary media artist Walid ________ instituted The "
          "Atlas Group, a fictional foundation that serves as an archive used to add context "
          "to pieces related to the Lebanese Civil Wars.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "Raad,", "Raad;", "Raad:", "Raad", "D",
          "No punctuation is needed between the subject 'Walid Raad' and the verb 'instituted'.")

        q(gv, H,
          "Ojibwe poet Heid Erdrich, ________ to illustrate themes related to modern "
          "Indigenous issues, has produced a number of award-winning video-poems with "
          "multi-disciplinary Ojibwe artist Jonathan Thunder.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "hoping", "hoped", "hopes", "is hoping", "A",
          "'Hoping' is the correct participial phrase modifying the subject 'Heid Erdrich'.")

        q(gv, H,
          "Zoonotic diseases, including those caused by viruses and parasites, ________ "
          "infectious illnesses with a wide range of symptoms and effects and can be "
          "transferred between animals and humans.\n\n"
          "Which choice completes the text so that it conforms to the conventions of Standard English?",
          "is", "has been", "are", "was", "C",
          "'Are' correctly agrees with the plural subject 'Zoonotic diseases'.")

        q(tr, H,
          "The Atlantic hurricane season officially runs from June 1 to November 30, and "
          "citizens living in affected areas know there is a higher risk of dangerous "
          "weather during this time. ________ a recent study found that hurricanes in the "
          "Atlantic basin have been trending about five days earlier per decade since 1979, "
          "suggesting the possibility of a need for a shift in what's considered the "
          "hurricane season.\n\nWhich choice completes the text with the most logical transition?",
          "Therefore,", "However,", "Overall,", "Otherwise,", "B",
          "'However' introduces a contrasting finding — the conventional season dates may need to shift.")

        q(tr, H,
          "CAVES is a training course for astronauts that mimics some of the conditions of "
          "outer space. The goal of the course is to prepare astronauts for the challenging "
          "conditions that exist in long spaceflights. Jeanette Epps was the first African "
          "American woman to complete the CAVES course; ________ she became a role model "
          "for future female and African American candidates.\n\n"
          "Which choice completes the text with the most logical transition?",
          "specifically,", "instead,", "therefore,", "rather,", "C",
          "'Therefore' — completing the CAVES course led to her becoming a role model.")

        q(tr, H,
          "Bulgarian and Macedonian folkloric tradition includes Martenitsi, small "
          "adornments made of yarn in the shape of dolls, worn to celebrate the start of "
          "the spring season. An observer of the tradition puts on the Martenitsa on the "
          "springtime holiday Baba Mara Day and removes it after seeing a stork, a swallow, "
          "or a blossoming tree. After removing the Martenitsa, some tie it to a fruit "
          "tree's branch, a gesture meant to give the tree good fortune and health. "
          "________ some place the Martenitsa on the ground under a rock, and the type of "
          "insect closest to the rock the following day is said to indicate what kind of "
          "fortune the wearer can expect for the rest of the year.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "For example,", "Alternatively,", "In fact,", "C",
          "'Alternatively' describes a different option for what to do with the Martenitsa.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "• Deciduous forests are found in two distinct biomes.\n"
          "• Tropical deciduous forests experience seasonal rainfall variations.\n"
          "• Temperate deciduous forests experience seasonal temperature variations.\n"
          "• Temperate deciduous forests have been harvested for wood, timber, and charcoal.\n"
          "• As a result of this harvesting, less than one-fourth of the original temperate "
          "deciduous forests remain today.\n\n"
          "The student wants to emphasize a difference between tropical and temperate "
          "deciduous forests. Which choice most effectively uses relevant information from "
          "the notes to accomplish this goal?",
          "Deciduous forests are found in two distinct biomes: tropical deciduous forests and temperate deciduous forests.",
          "Tropical deciduous forests have variations in rainfall, whereas temperate deciduous forests have variations in temperature.",
          "Although tropical and temperate deciduous forests are both deciduous forests, these forests do have some differences.",
          "Less than one-fourth of the original temperate deciduous forests remain after being harvested for wood, timber, and charcoal.", "B",
          "Option B directly contrasts the two types: tropical forests have rainfall variations while temperate forests have temperature variations.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "• The Eocene-Oligocene extinction event occurred a little over 33 million years ago.\n"
          "• 63% of African mammals died out during this event.\n"
          "• These extinct mammals included rodents and early primates.\n"
          "• One possible cause for the event was a global cooling that decreased "
          "temperatures in a relatively short time frame.\n"
          "• One reason for the declining temperatures was a decrease in carbon dioxide in "
          "the atmosphere.\n\n"
          "The student wants to explain a possible cause of the Eocene-Oligocene extinction "
          "event. Which choice most effectively uses relevant information from the notes to "
          "accomplish this goal?",
          "The Eocene-Oligocene extinction event occurred a little over 33 million years ago at a time of a global cooling.",
          "63% of African mammals, including rodents and early primates, died out during the Eocene-Oligocene extinction event.",
          "The Eocene-Oligocene extinction event may have been the result of decreased levels of carbon dioxide in the atmosphere, which caused a global cooling.",
          "An extinction event can occur when global temperatures decline.", "C",
          "Option C traces the cause chain: decreased CO2 → global cooling → extinction event.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "• Monoculture farming is the practice of growing one crop at a time.\n"
          "• Polyculture farming grows a variety of crops.\n"
          "• When a field has only one crop, the crop is at greater risk of damage by pests.\n"
          "• When a variety of crops is grown, the threat of pests is lower.\n\n"
          "The student wants to contrast monoculture farming with polyculture farming. "
          "Which choice most effectively uses relevant information from the notes to "
          "accomplish this goal?",
          "Polyculture farming—growing a variety of crops—yields a farm that is less susceptible to pests compared with monoculture farming—growing one crop at a time.",
          "Monoculture farming, which grows only one type of crop at a time, increases a crop's risk of damage by pests.",
          "Some styles of farming grow one kind of crop while others grow a variety.",
          "Monoculture farming and polyculture farming are two different practices that can be threatened by pests.", "A",
          "Option A contrasts both types in one sentence and includes the key difference in pest risk.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Section 2, Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(alg, M, "What is the value of 2a if 8a = 40?",
          "5", "10", "44", "46", "B",
          "8a = 40 → a = 5 → 2a = 10")

        q(alg, M, "Which of the following expressions is equivalent to 9 − x³ − 4?",
          "−x³ − 36", "−x³ − 5", "−x³ + 5", "−x³ + 13", "C",
          "9 − x³ − 4 = 5 − x³ = −x³ + 5")

        q(wp, M,
          "The temperature, t, of a bowl of soup is 145 degrees Fahrenheit when the soup "
          "is first served. The soup cools at an average rate of 0.63 degrees Fahrenheit "
          "per minute for the first 10 minutes. If m is the number of minutes after the "
          "soup is served and t is the temperature of the soup, in degrees Fahrenheit, "
          "which equation best models this situation?",
          "t = −0.63m + 0.63", "t = −0.63m + 145", "t = 145m", "t = 145m + 145", "B",
          "Starts at 145°F, decreases at 0.63 per minute: t = 145 − 0.63m = −0.63m + 145")

        q(alg, M,
          "The combined weight of Daniel and his father, Frank, is 240 pounds. Daniel "
          "weighs d pounds, Frank weighs f pounds, and Frank weighs three times as much "
          "as Daniel. Which system of equations represents this situation?",
          "d = 3f\nd + f = 240",
          "d = 240f\nd + f = 3",
          "f = 240d\nd + f = 3",
          "f = 3d\nd + f = 240", "D",
          "Frank = 3 × Daniel: f = 3d. Total weight: d + f = 240.")

        q(fun, M,
          "The graph models the amount of money, in dollars, that a child adds to her "
          "piggy bank in x weeks, without removing any of the money. The line passes "
          "through approximately (0, 10) and (5, 60), showing a linear increase. "
          "According to the graph, how much money on average, in dollars, does the child "
          "add to the piggy bank each week?",
          "2.50", "10", "25", "35", "B",
          "Slope = (60 − 10) / (5 − 0) = 50/5 = $10 per week")

        q(wp, M,
          "A rectangle with a length of 6 centimeters has an area of 42 square centimeters. "
          "What is the width, in centimeters, of the rectangle?",
          "6", "7", "13", "36", "B",
          "Area = length × width → 42 = 6w → w = 7")

        q(geo, M,
          "The relationship between the base and the height of a certain triangle can be "
          "expressed by the equation (1/2)bh = 30. If b = 12, what is the value of h?",
          "3", "4", "5", "6", "C",
          "(1/2)(12)h = 30 → 6h = 30 → h = 5")

        q(wp, M,
          "The equation w = 72m represents the number of words, w, typed by a court "
          "stenographer during a trial, where m represents the number of minutes spent "
          "typing. What is the best interpretation of the number 72 in this context?",
          "The stenographer typed a total of 72 words.",
          "The stenographer typed a total of 72m words.",
          "The stenographer typed an average of 1/72 words per minute.",
          "The stenographer typed an average of 72 words per minute.", "D",
          "72 is the rate (coefficient of m) — 72 words per minute.")

        q(alg, M,
          "Given the system of equations:\n3x + y = 17\ny = 5\n"
          "Which ordered pair is the solution to the given system of equations when the "
          "system is graphed in the xy-plane?",
          "(2, 3)", "(3, 5)", "(4, 5)", "(5, 4)", "C",
          "y = 5 → 3x + 5 = 17 → 3x = 12 → x = 4. Solution: (4, 5)")

        q(alg, M,
          "Which of the following expressions is equivalent to 144x² − 192x + 64?",
          "(6x − 4)(6x − 4)",
          "(6x + 4)(6x − 4)",
          "(12x − 8)(12x − 8)",
          "(12x + 8)(12x − 8)", "C",
          "(12x − 8)² = 144x² − 192x + 64 ✓")

        q(dsp, M,
          "All of the values in data set A are shown: 3, 12, 15, 21, 26, 37\n"
          "What is the median of data set A?",
          "18", "19", "21", "34", "A",
          "6 numbers → median = average of 3rd and 4th = (15 + 21)/2 = 18")

        q(fun, M,
          "The function g is defined by the equation g(x) = √x − 9. "
          "What is the value of g(25)?",
          "−4", "−3", "−2", "4", "A",
          "g(25) = √25 − 9 = 5 − 9 = −4")

        q(fun, M,
          "An online used bookstore records revenue based on the price per book sold. "
          "The data is modeled by a graph showing a parabola that opens downward, with "
          "the revenue (in hundreds of dollars) on the y-axis and price per book (dollars) "
          "on the x-axis. The parabola appears to peak near x = 8, y = 64, passes through "
          "approximately (6, 60) and (10, 60), and has y = 0 at x = 0 and near x = 16. "
          "Based on the model, which table gives three values of x and their corresponding "
          "values of y?",
          "x: 0, 0, 10  |  y: 16, 64, 60",
          "x: 0, 6, 8  |  y: 0, 60, −64",
          "x: 0, 6, 64  |  y: 16, 60, 8",
          "x: 6, 8, 10  |  y: 60, 64, 60", "D",
          "From the parabola: at x = 6, y ≈ 60; at x = 8 (peak), y ≈ 64; at x = 10, y ≈ 60 (symmetric).")

        q(fun, M,
          "The estimated value, in dollars, of a photocopier x years after the date of "
          "purchase is given by the function p(x) = 7,466(0.80)ˣ, where 0 < x ≤ 10. "
          "In this context, what is the best interpretation of the statement 'p(2) is "
          "approximately equal to 4,778'?",
          "When the estimated value of the photocopier is 4,778 dollars, it is 1/2 of the estimated value of the photocopier in the previous year.",
          "When the estimated value of the photocopier is 4,778 dollars, it is 2% greater than the estimated value of the photocopier in the previous year.",
          "2 years after the date of purchase, the value of the photocopier will be approximately 4,778 dollars.",
          "2 years after the date of purchase, the value of the photocopier will have decreased by a total of approximately 4,778 dollars.", "C",
          "p(2) means x = 2 years after purchase; the value equals approximately 4,778 dollars.")

        q(wp, M,
          "How many minutes are there in 4 days?\n(1 day = 24 hours and 1 hour = 60 minutes)",
          "4800", "5040", "5760", "6000", "C",
          "4 × 24 × 60 = 5,760 minutes")

        q(fun, M,
          "The scatterplot shows the relationship between two variables, x and y, with a "
          "line of best fit. The line passes through approximately (1, 6) and (7, 15). "
          "Which of the following is closest to the slope of the line of best fit?",
          "−1.5", "1.5", "−15", "15", "B",
          "Slope ≈ (15 − 6)/(7 − 1) = 9/6 = 1.5")

        q(geo, M,
          "The hypotenuse of a certain right triangle has a length of 8 inches. If the "
          "length of one of the triangle's legs is 6 inches, what is the length, in inches, "
          "of the triangle's other leg?",
          "2√7", "10", "14", "28", "A",
          "a² + 6² = 8² → a² = 64 − 36 = 28 → a = √28 = 2√7")

        q(alg, M,
          "The equation 37a + b = c relates the positive numbers a, b, and c. "
          "Which equation correctly expresses b in terms of a and c?",
          "b = c − 37a", "b = c + 37a", "b = 37ac", "b = c/(37a)", "A",
          "37a + b = c → b = c − 37a")

        q(alg, M,
          "What is the product of the solutions to the equation 2x² + 30x − 12 = 0?",
          "−15", "−6", "6", "15", "B",
          "By Vieta's formulas, product of roots = c/a = −12/2 = −6")

        q(fun, M,
          "Linear function f is defined by the equation f(x) = kx − 79. If f(7) = 40 "
          "and k is a constant, what is the value of f(11)?",
          "40", "79", "108", "187", "C",
          "f(7) = 7k − 79 = 40 → 7k = 119 → k = 17. f(11) = 17(11) − 79 = 187 − 79 = 108")

        q(dsp, M,
          "Enrollment in a certain park district program decreased by 70% from September "
          "1997 to September 1998. Enrollment then increased by 110% from September 1998 "
          "to September 1999. What was the net percentage decrease in enrollment from "
          "September 1997 to September 1999?",
          "33%", "37%", "40%", "63%", "B",
          "Start: 100. After −70%: 30. After +110%: 30 × 2.1 = 63. Net decrease = (100 − 63)/100 = 37%")

        q(alg, M,
          "What is the value of 4x² + 8x if x² + 2x − 20 = 0?",
          "20", "40", "80", "160", "C",
          "x² + 2x − 20 = 0 → x² + 2x = 20. Therefore 4x² + 8x = 4(x² + 2x) = 4(20) = 80")

        # ════════════════════════════════════════════════════════════════
        # MATH — Section 2, Module 2—Easier
        # ════════════════════════════════════════════════════════════════

        q(dsp, E,
          "There are 45 gumballs of various flavors in a gumball machine: 12 grape, "
          "14 strawberry, 10 lemon, and 9 watermelon. If one gumball is removed from "
          "the machine at random, what is the probability that it is a watermelon gumball?",
          "9/45", "12/45", "14/45", "36/45", "A",
          "P(watermelon) = 9/45 = 1/5")

        q(dsp, E,
          "The table summarizes the approximate time of the most recent visit to the "
          "dentist's office by 300 patients:\n\n"
          "One week ago: 3 patients\n"
          "One month ago: 17 patients\n"
          "Three months ago: 54 patients\n"
          "Six months ago: 91 patients\n"
          "One year ago: 135 patients\n"
          "Total: 300 patients\n\n"
          "According to the table, how many patients had their most recent visit to the "
          "dentist's office one month ago or three months ago?",
          "17", "37", "54", "71", "D",
          "17 + 54 = 71 patients")

        q(alg, E,
          "Which value of a satisfies the equation 7a − 364 = 126?",
          "34", "70", "364", "483", "B",
          "7a = 490 → a = 70")

        q(fun, E,
          "A line is graphed in the xy-plane, passing through the points (0, 5.5) and "
          "(11, 0). What is the y-intercept of the line graphed?",
          "(0, −11/2)", "(0, −2/11)", "(0, 11/2)", "(11/2, 0)", "C",
          "The line crosses the y-axis at (0, 5.5) = (0, 11/2).")

        q(wp, E,
          "The ratio of c to d is 35:22. To maintain this ratio, by what value must d "
          "be divided if c is divided by 5?",
          "4", "5", "7", "22", "B",
          "If c → c/5 and ratio c/d must stay constant, then d → d/5. So d is divided by 5.")

        q(wp, E,
          "In a basket full of grapes, 50% of the grapes are black, and the rest are red. "
          "If there are 280 grapes in the basket, how many of them are black?",
          "50", "100", "140", "180", "C",
          "50% of 280 = 140")

        q(alg, E,
          "The given system of equations has one solution at (x, y).\n"
          "y = x − 5\ny = 18\nWhat is the value of x?",
          "13", "18", "23", "90", "C",
          "y = 18 → 18 = x − 5 → x = 23")

        q(wp, E,
          "How many fathoms are equivalent to 132 feet? (1 fathom = 6 feet)",
          "6", "22", "44", "792", "B",
          "132 ÷ 6 = 22 fathoms")

        q(fun, E,
          "Function h is defined by the equation h(x) = 3x − 10. "
          "What is the value of h(x) when x = 50?",
          "20", "43", "140", "150", "C",
          "h(50) = 3(50) − 10 = 150 − 10 = 140")

        q(wp, E,
          "A robot at an automobile factory performs two tasks: welding seams and drilling "
          "holes. The robot takes 41.2 seconds to weld one seam and 15.5 seconds to drill "
          "one hole. If the robot spends 154.6 seconds welding s seams and drilling h holes, "
          "which equation represents this situation?",
          "s + h = 154.6",
          "3.75s + 9.97h = 154.6",
          "15.5s + 41.2h = 154.6",
          "41.2s + 15.5h = 154.6", "D",
          "41.2 seconds per seam × s seams + 15.5 seconds per hole × h holes = 154.6")

        q(wp, E,
          "There are 2,750 trees in an apple orchard, and there are 110 trees planted per "
          "acre of land. How many acres does the apple orchard cover?",
          "25", "40", "250", "2,860", "A",
          "2,750 ÷ 110 = 25 acres")

        q(wp, E,
          "The ratio of road bikes to mountain bikes at a bicycle shop is 7 to 3. If there "
          "are 24 mountain bikes at the shop, how many road bikes are there at the shop?",
          "8", "24", "56", "72", "C",
          "7/3 = x/24 → x = (7 × 24)/3 = 56")

        q(geo, E,
          "A rectangle has a perimeter of 64 centimeters. What is the length, in centimeters, "
          "of one of the shorter sides of the rectangle if the length of each of the two "
          "longer sides of the rectangle is 22 centimeters?",
          "8", "10", "12", "22", "B",
          "2(22 + w) = 64 → 22 + w = 32 → w = 10")

        q(fun, E,
          "A graph is shown in the xy-plane with a curve passing through (−2, 0), (0, −4), "
          "and (2, 0). Which of the following is the x-intercept of the graph shown?",
          "(0, 0)", "(0, 2)", "(2, 0)", "(3, 3)", "C",
          "The x-intercept is where y = 0; the curve crosses the x-axis at (2, 0).")

        q(fun, E,
          "The graph shows the possible combinations of yards of blue fabric and yards of "
          "red fabric that can be purchased for $14 at a certain store. The line passes "
          "through (0, 7) and (14, 0). How many yards of blue fabric did Jessica purchase "
          "if she purchased blue fabric and 6 yards of red fabric for a total of $14?",
          "2", "4", "8", "11", "A",
          "Line: y = 7 − x/2. When y = 6: 6 = 7 − x/2 → x = 2 yards of blue fabric.")

        q(wp, E,
          "A variety pack containing packets of seeds contains only 600-mg packets and "
          "400-mg packets. The pack contains 20 of the 400-mg packets, and the total mass "
          "of the variety pack is 29,000 mg. How many 600-mg packets of tomato seeds are "
          "in the pack?",
          "20", "35", "400", "600", "B",
          "20 × 400 = 8,000 mg. Remaining: 29,000 − 8,000 = 21,000 mg. 21,000/600 = 35 packets.")

        q(geo, E,
          "A right triangle contains two acute angles. One of the acute angles measures 20°. "
          "What is the measure of the other acute angle, in degrees?",
          "20", "50", "60", "70", "D",
          "Angles in a triangle sum to 180°: 90 + 20 + x = 180 → x = 70°")

        q(fun, E,
          "Line a and line b are graphed in the xy-plane. Line a is defined by 2y = x − 24, "
          "and line b is parallel to line a. What is the slope of line b?",
          "−12", "−2", "1/12", "1/2", "D",
          "2y = x − 24 → y = x/2 − 12, slope = 1/2. Parallel lines have the same slope.")

        q(geo, E,
          "Right Circular Cone 1 has a radius of r₁ and a height of h₁. The volume of "
          "Right Circular Cone 2 is 100 times the volume of Right Circular Cone 1. Right "
          "Circular Cone 2 has a radius of r₂ and a height of h₂. Which of the following "
          "could represent r₂ and h₂, in terms of r₁ and h₁, respectively?",
          "r₂ = 5r₁ and h₂ = 4h₁",
          "r₂ = 25r₁ and h₂ = 4h₁",
          "r₂ = 4r₁ and h₂ = 5h₁",
          "r₂ = 4r₁ and h₂ = 25h₁", "A",
          "V ∝ r²h. (r₂/r₁)²(h₂/h₁) = 100. Check A: 5² × 4 = 100 ✓")

        q(geo, E,
          "What is the area, in square centimeters, of an isosceles triangle with a height "
          "of 25 centimeters and a base length of 44 centimeters?",
          "44", "275", "550", "1,100", "C",
          "Area = (1/2) × base × height = (1/2) × 44 × 25 = 550 cm²")

        q(geo, E,
          "According to the triangle inequality theorem, the length of any side of a "
          "triangle must be greater than the difference between the lengths of the other "
          "two sides. Which inequality represents the possible lengths, p, of the third "
          "side of a triangle with side lengths of 9 and 11?",
          "p < 2", "2 < p < 20", "p > 20", "p < 2 or p > 20", "B",
          "|11 − 9| < p < 11 + 9 → 2 < p < 20")

        q(wp, E,
          "The number t is 30% less than the positive number u. The number v is 50% "
          "greater than t. How many times the value of u is the number v?",
          "0.70", "0.85", "1.05", "1.20", "C",
          "t = 0.70u. v = 1.50t = 1.50 × 0.70u = 1.05u. So v = 1.05 times u.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Section 2, Module 2—Harder
        # ════════════════════════════════════════════════════════════════

        q(wp, H,
          "17 is what percent of 340?",
          "3", "5", "17", "20", "B",
          "(17/340) × 100 = 5%")

        q(alg, H,
          "At a local library, there is a fee of $1.85 for each overdue book. In addition, "
          "the library charges a fine of $0.21 for each day the book is overdue. A patron "
          "has only one overdue book and no other charges. If she is charged a total of $5 "
          "for the overdue book, how many days overdue is the book?",
          "3", "15", "24", "25", "B",
          "$1.85 + $0.21d = $5.00 → $0.21d = $3.15 → d = 15 days")

        q(alg, H,
          "Two teams of employees at a certain factory each produce the same specialized "
          "part. Team A produces the part at an average rate of 725 per day, team B "
          "produces the part at an average rate of 650 per day. The factory produces a "
          "minimum of 10,000 units of this part in one week. Which of the following "
          "inequalities represents this situation, where a and b are the numbers of days "
          "team A and team B produced this part, respectively?",
          "650a + 725b ≤ 10,000",
          "650a + 725b ≥ 10,000",
          "725a + 650b ≤ 10,000",
          "725a + 650b ≥ 10,000", "D",
          "Team A: 725a units. Team B: 650b units. Minimum 10,000: 725a + 650b ≥ 10,000")

        q(dsp, H,
          "A long string of decorative lights has 10 clear lights, 45 solid color lights, "
          "8 multi-color lights, and 45 blinking lights. If a single light is selected at "
          "random, what is the probability that the light selected is neither a clear light "
          "nor a multi-color light?",
          "1/6", "2/5", "5/6", "25/27", "C",
          "Total = 108. Neither clear (10) nor multi-color (8): 108 − 18 = 90. P = 90/108 = 5/6")

        q(geo, H,
          "What is the side length, in inches, of a square that has an area of 5,184 "
          "square inches?",
          "18", "72", "1,296", "2,592", "B",
          "√5,184 = 72 (since 72² = 5,184)")

        q(fun, H,
          "The function f is defined by the equation f(x) = x − 30. "
          "What is the value of f(330)?",
          "11", "30", "300", "360", "C",
          "f(330) = 330 − 30 = 300")

        q(wp, H,
          "Escape velocity is a measure that expresses the minimum speed an object needs "
          "to reach in order to escape the gravity of a planet. If the escape velocity at "
          "the surface of Mercury is 15,300 kilometers per hour, what is the speed that "
          "an object needs to reach in order to escape Mercury's gravity, in kilometers "
          "per second? (1 hour = 3,600 seconds)",
          "0.25", "4.25", "15,300", "55,080,000", "B",
          "15,300 ÷ 3,600 = 4.25 km/s")

        q(wp, H,
          "The ratio of c to d is 35:22. To maintain this ratio, by what value must d "
          "be divided if c is divided by 5?",
          "4", "5", "7", "22", "B",
          "If c is divided by 5, d must also be divided by 5 to maintain the ratio.")

        q(fun, H,
          "Line l passes through the points (1, 15) and (0, 17) in the xy-plane. "
          "Which of the following equations defines line l?",
          "y = −2x + 17",
          "y = −(1/2)x + 17",
          "y = 15x − 2",
          "y = 15x − 1/2", "A",
          "Slope = (17 − 15)/(0 − 1) = −2. y-intercept = 17. Equation: y = −2x + 17")

        q(wp, H,
          "Two of the jets in a decorative water fountain shoot water at specific intervals. "
          "After the fountain is turned on, jet A shoots water every 405 seconds and jet B "
          "shoots water every 330 seconds. How much longer, in seconds, does it take for "
          "jet A to shoot water 64 times than it takes for jet B to shoot water 64 times "
          "after the fountain is turned on?",
          "75", "4,800", "25,920", "21,120", "B",
          "Jet A: 64 × 405 = 25,920 s. Jet B: 64 × 330 = 21,120 s. Difference: 4,800 s")

        q(wp, H,
          "If the value of k is 0.97 times 100, the value of k is what percent less than 100?",
          "3", "9.7", "97", "103", "A",
          "k = 97. Percent less than 100: (100 − 97)/100 × 100 = 3%")

        q(alg, H,
          "What value of a is the solution to the equation −(7/5)(a − 2) + (3/2)(a − 2) = 6?",
          "−100", "−10", "2", "62", "D",
          "Let u = a − 2: −7u/5 + 3u/2 = 6. Multiply by 10: −14u + 15u = 60 → u = 60 → a = 62")

        q(fun, H,
          "Line l has an x-intercept of (95/2, 0) and a y-intercept of (0, −10) when "
          "graphed in the xy-plane. What is the slope of line l?",
          "2/950", "4/19", "19/4", "950/2", "B",
          "Slope = (−10 − 0)/(0 − 95/2) = −10/(−47.5) = 20/95 = 4/19")

        q(alg, H,
          "The given system of equations has one real solution at (x, y).\n"
          "y = −(1/3)x\ny = −5x\n"
          "What is the value of y?",
          "−3", "0", "5", "15", "B",
          "Setting equal: −x/3 = −5x → multiply by −3: x = 15x → 14x = 0 → x = 0 → y = 0")

        q(geo, H,
          "In a figure, the measure of angle JLK is 27°, the measure of angle MNO is 17°, "
          "and LM = MO. Points K, L, O, N lie on a straight line (with J below L and M "
          "above the line). What is the measure of angle NMO, in degrees?",
          "7", "10", "17", "27", "B",
          "Angle MLO = 27° (vertical with JLK). In isosceles △LMO (LM=MO): base angles = 27°. "
          "Angle LMO = 180−54 = 126°. Angle MON = 180−27 = 153°. "
          "In △MNO: 153 + 17 + angle NMO = 180 → angle NMO = 10°")

        q(alg, H,
          "The amount of money in a bank account can be modeled by a linear equation. The "
          "model estimates the account had $2,278 at the end of week 5 and $4,195 at the "
          "end of week 24. What is the amount of money, to the nearest dollar, that was in "
          "the account at the end of week 2?",
          "1,575", "1,975", "2,278", "2,378", "B",
          "Slope = (4195−2278)/(24−5) = 1917/19 ≈ 100.89 per week. "
          "Week 2 = Week 5 − 3 weeks: 2278 − 3 × (1917/19) ≈ 2278 − 302.68 ≈ $1,975")

        q(fun, H,
          "For the linear relationship between x and y, the table shows four values:\n"
          "x = c → y = 0\nx = c−25 → y = 4\nx = c−50 → y = 8\nx = c−75 → y = 12\n\n"
          "If this relationship is represented by a line in the xy-plane, what is the "
          "slope of the line?",
          "−4/(2c+25)", "−25/4", "−4/25", "4/(c−25)", "C",
          "Slope = (4−0)/((c−25)−c) = 4/(−25) = −4/25")

        q(dsp, H,
          "Four data sets are represented by frequency tables. The mean is the least for "
          "which data set?\n\n"
          "A: 5(×3), 10(×3), 15(×3), 20(×3), 25(×3) → mean = 15\n"
          "B: 5(×3), 10(×4), 15(×4), 20(×4), 25(×3) → mean = 15\n"
          "C: 5(×6), 10(×2), 15(×2), 20(×2), 25(×6) → mean = 15\n"
          "D: 5(×6), 10(×5), 15(×4), 20(×3), 25(×2) → mean = 12.5",
          "Data set A", "Data set B", "Data set C", "Data set D", "D",
          "Data set D: (5×6+10×5+15×4+20×3+25×2)/20 = 250/20 = 12.5, the lowest mean.")

        q(geo, H,
          "Right Circular Cone 1 has a radius of r₁ and a height of h₁. The volume of "
          "Right Circular Cone 2 is 100 times the volume of Right Circular Cone 1. Right "
          "Circular Cone 2 has a radius of r₂ and a height of h₂. Which of the following "
          "could represent r₂ and h₂, in terms of r₁ and h₁, respectively?",
          "r₂ = 5r₁ and h₂ = 4h₁",
          "r₂ = 25r₁ and h₂ = 4h₁",
          "r₂ = 4r₁ and h₂ = 5h₁",
          "r₂ = 4r₁ and h₂ = 25h₁", "A",
          "V = (1/3)πr²h. (r₂)²(h₂) = 100(r₁)²(h₁). Check A: (5r₁)²(4h₁) = 100r₁²h₁ ✓")

        q(fun, H,
          "The function g is defined by the equation g(x) = 2cˣ − k, where c and k are "
          "constants. If the graph of y = g(x) in the xy-plane crosses the x-axis at "
          "x = −56 and crosses the y-axis at y = 114, what is the value of k?",
          "−114", "−112", "2", "114", "B",
          "At y-axis (x=0): 2c⁰ − k = 114 → 2 − k = 114 → k = −112")

        q(alg, H,
          "Each student in a class with 25 students chose one of three sizes of slushy at "
          "the year-end party. There were 4 students who chose the 5-ounce slushy. The "
          "number of students that chose the 9-ounce slushy was 6 times the number of "
          "students t that chose the 12-ounce slushy. Which equation must be true for "
          "the value of t?",
          "5t + 9t + 12t = 25",
          "6t + 4 = 25",
          "7t + 4 = 25",
          "9(6t) + 12t + 5(4) = 25", "C",
          "4 + 6t + t = 25 → 7t + 4 = 25 → t = 3")

        q(alg, H,
          "Each equation in the given system is graphed in the xy-plane:\n"
          "−10x + 6y = −22\n−5x + 3y = −11\n\n"
          "Which of the following represents a point that lies on each graph, "
          "for any real number n?",
          "(−3n/5 − 22, 3n/5 − 11)",
          "(n/2 − 11, n/2 − 22)",
          "(n, 3n/5 + 11/5)",
          "(3n/5 + 11/5, n)", "D",
          "Both equations are identical (the second × 2 = the first). "
          "Check D: −5(3n/5 + 11/5) + 3n = −3n − 11 + 3n = −11 ✓ for any n.")

        count = Question.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {count} questions '
            f'({Question.objects.filter(subject=english).count()} English, '
            f'{Question.objects.filter(subject=math).count()} Math)'
        ))
