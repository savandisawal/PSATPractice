"""
PSAT 8/9-style Practice Test 2 — generated questions.
English (Reading & Writing): 81 questions across 3 modules
Math: 66 questions across 3 modules
Difficulty: Module 1 = medium, Module 2 Easier = easy, Module 2 Harder = hard
"""
from django.core.management.base import BaseCommand
from practice.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Load PSAT-style Practice Test 2 questions into the database'

    def handle(self, *args, **options):
        math = Subject.objects.get(slug='math')
        english = Subject.objects.get(slug='english')

        ev, _ = Topic.objects.get_or_create(subject=english, name='Vocabulary in Context')
        rc, _ = Topic.objects.get_or_create(subject=english, name='Reading Comprehension')
        de, _ = Topic.objects.get_or_create(subject=english, name='Data and Evidence')
        gv, _ = Topic.objects.get_or_create(subject=english, name='Grammar: Verb Usage')
        gp, _ = Topic.objects.get_or_create(subject=english, name='Grammar: Punctuation')
        tr, _ = Topic.objects.get_or_create(subject=english, name='Transitions')
        rn, _ = Topic.objects.get_or_create(subject=english, name='Research Notes')

        alg, _ = Topic.objects.get_or_create(subject=math, name='Algebra and Equations')
        fun, _ = Topic.objects.get_or_create(subject=math, name='Functions and Graphs')
        geo, _ = Topic.objects.get_or_create(subject=math, name='Geometry')
        dsp, _ = Topic.objects.get_or_create(subject=math, name='Data, Statistics, and Probability')
        wp,  _ = Topic.objects.get_or_create(subject=math, name='Word Problems')

        def q(topic, diff, text, a, b, c, d, ans, expl=''):
            Question.objects.create(
                subject=topic.subject, topic=topic, difficulty=diff,
                text=text, option_a=a, option_b=b, option_c=c, option_d=d,
                correct_answer=ans, explanation=expl,
            )

        M = 'medium'; E = 'easy'; H = 'hard'

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(ev, M,
          "Novelist Toni Morrison is widely regarded as one of the most important American "
          "writers of the twentieth century. Her works ________ the African American "
          "experience, exploring themes of identity, trauma, and community with unmatched "
          "depth and linguistic precision.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "ignore", "chronicle", "simplify", "contradict", "B",
          "'Chronicle' means to record or describe events in detail — Morrison's novels do exactly this for the African American experience.")

        q(ev, M,
          "Botanists have discovered that certain rainforest plants ________ chemical "
          "compounds that repel harmful insects while simultaneously attracting beneficial "
          "pollinators, a finding that could transform pest management in agriculture.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "dissolve", "ignore", "emit", "discard", "C",
          "Plants 'emit' (release) chemicals — the most precise word for producing and releasing chemical compounds.")

        q(ev, M,
          "The documentary filmmaker carefully ________ hours of recorded interviews, "
          "selecting only the most compelling moments to include in the final cut, ensuring "
          "the narrative remained both concise and emotionally resonant.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "created", "sifted through", "duplicated", "ignored", "B",
          "'Sifted through' means to examine carefully in order to select what is useful — perfect for reviewing hours of footage.")

        q(ev, M,
          "Despite receiving no formal training, the self-taught painter developed a deeply "
          "________ style that critics found impossible to categorize but equally impossible "
          "to overlook.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "conventional", "predictable", "idiosyncratic", "ordinary", "C",
          "'Idiosyncratic' means having a distinctive, unusual personal style — matching an artist who defies categorization.")

        q(rc, M,
          "Hummingbirds are remarkable for their ability to hover in place and fly backward, "
          "feats made possible by their uniquely flexible wing structure. Unlike most birds, "
          "whose wings pivot only at the shoulder, a hummingbird's wing rotates at the "
          "shoulder, elbow, and wrist, allowing rapid figure-eight strokes that generate lift "
          "on both the downstroke and the upstroke.\n\n"
          "Which choice best states the main idea of the text?",
          "Hummingbirds are the only birds capable of sustained backward flight.",
          "The flexibility of hummingbirds' wings allows them to perform aerial maneuvers other birds cannot.",
          "Hummingbirds' wings pivot at the shoulder, unlike most birds that pivot at the wrist.",
          "Most birds generate lift only on the downstroke, making hovering impossible.", "B",
          "The text focuses on how hummingbirds' unique multi-joint wing structure enables their special flying abilities.")

        q(rc, M,
          "The following text is adapted from Charlotte Bronte's 1847 novel Jane Eyre. Jane, "
          "a governess, reflects on her feelings.\n\n"
          "I had not intended to love him; the reader knows I had labored hard to extirpate "
          "from my soul the germs of love there detected; and now, at the first renewed view "
          "of him, they spontaneously arrived, green and strong! He made me love him without "
          "looking at me.\n\n"
          "Which choice best describes the function of the last sentence in the text?",
          "It explains the specific method Rochester used to charm Jane.",
          "It suggests that Rochester was deliberately manipulating Jane's feelings.",
          "It emphasizes the involuntary and mysterious nature of Jane's emotions.",
          "It contradicts the narrator's earlier claim about not intending to love.", "C",
          "The sentence stresses how Jane's love arose without any direct effort from Rochester, reinforcing its involuntary nature.")

        q(rc, M,
          "Sleep researcher Matthew Walker has argued that modern society has created "
          "conditions profoundly hostile to adequate rest. Electric lighting, irregular work "
          "schedules, and the pervasive presence of screens have collectively disrupted the "
          "natural rhythms that once governed human sleep. Walker contends that widespread "
          "dismissal of sleep as unimportant has contributed to increased rates of anxiety, "
          "obesity, and heart disease.\n\n"
          "Which choice best states the main idea of the text?",
          "Walker's research proves that screens are the primary cause of sleep deprivation.",
          "Modern lifestyles have disrupted sleep patterns, with serious health consequences, according to Walker.",
          "Walker argues that electric lighting is the most harmful modern invention.",
          "Heart disease is directly caused by irregular work schedules.", "B",
          "The text describes how modern conditions disrupt sleep and Walker's argument that this has serious health consequences.")

        q(rc, M,
          "Studies of the Great Barrier Reef have revealed that bleaching events — periods "
          "when high water temperatures cause corals to expel the algae that give them color "
          "and nutrients — have increased in frequency since the 1980s. Researchers analyzing "
          "historical records concluded that bleaching now occurs approximately every six "
          "years, compared to every 25 to 30 years before 1980. This shift suggests "
          "that ________\n\n"
          "Which choice most logically completes the text?",
          "future coral bleaching events will be impossible to predict without advanced modeling.",
          "the reef's recovery time between bleaching events has become insufficient.",
          "the algae expelled during bleaching eventually return to healthy corals within months.",
          "rising ocean temperatures have had no measurable effect on reef health.", "B",
          "If bleaching occurs every 6 years (vs. 25-30 before), the reef no longer has adequate time to fully recover between events.")

        q(rc, M,
          "Linguist Daniel Everett spent years among the Piraha people of the Amazon and "
          "became fluent in their language. He reported that Piraha lacks several features "
          "considered universal by many linguists, including numbers, color terms, and "
          "recursive grammatical structures. His findings sparked intense debate, with some "
          "scholars arguing his methodology was flawed and that the absent features are "
          "simply expressed differently in Piraha.\n\n"
          "Which choice best states the main idea of the text?",
          "Everett's years of fieldwork made him the world's foremost authority on Piraha.",
          "Everett's claims about Piraha challenge assumptions about linguistic universals, though not without controversy.",
          "Piraha is notable for its highly developed system of color terminology.",
          "Most linguists agree that Everett's methodology was flawed.", "B",
          "The text presents Everett's challenging findings and the scholarly controversy they provoked.")

        q(de, M,
          "The table below shows average annual salaries by occupation in one state:\n\n"
          "Teacher: $52,000 | Nurse: $71,000 | Software Engineer: $98,000 | "
          "Electrician: $61,000 | Accountant: $67,000\n\n"
          "A researcher claims that software engineers earn significantly more than educators. "
          "Which choice most effectively uses data from the table to support this claim?",
          "Software engineers earn $98,000 annually, which is $46,000 more than what teachers earn.",
          "Electricians earn $61,000, which is between the salaries of teachers and nurses.",
          "Accountants earn $67,000, which falls below nurses but above teachers.",
          "Nurses earn $71,000, which is less than software engineers earn.", "A",
          "Option A directly uses data to quantify the difference: software engineers ($98,000) earn $46,000 more than teachers ($52,000), strongly supporting the claim.")

        q(de, M,
          "Text 1: Urban green spaces — parks, gardens, and tree-lined streets — play a "
          "critical role in city residents' mental health. Studies consistently show that "
          "access to nature reduces stress hormones, improves mood, and enhances cognitive "
          "function. Cities should prioritize expanding green spaces as an investment in "
          "public health.\n\n"
          "Text 2: While green spaces offer environmental benefits, their mental health "
          "effects are often overstated. Many studies rely on self-reported data rather than "
          "objective measures. Furthermore, the correlation between green space access and "
          "wellbeing may simply reflect wealth: affluent neighborhoods tend to have both "
          "better parks and healthier residents.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond to the "
          "claim in Text 1 that cities should prioritize expanding green spaces?",
          "Cities should expand green spaces primarily in affluent neighborhoods where residents can afford to use them.",
          "The mental health benefits of green spaces may not be as clear-cut as Text 1 suggests, given methodological concerns and potential confounding factors.",
          "Green spaces are unnecessary because self-reported data shows residents prefer other public investments.",
          "Text 1 is correct that nature reduces stress, but its policy recommendation is flawed.", "B",
          "Text 2 challenges the evidence by citing unreliable data and the confounding variable of wealth, suggesting the relationship is less clear than Text 1 claims.")

        q(de, M,
          "The table below shows books published by genre in one year:\n\n"
          "Mystery/Thriller: 12,450 | Romance: 15,200 | Science Fiction: 8,300 | "
          "Biography: 6,700 | Children's: 11,100\n\n"
          "A publishing analyst claims that romance novels lead all genres and that "
          "mystery/thriller and children's books combined exceed romance. Which choice "
          "most accurately uses data from the table to evaluate the analyst's claim?",
          "The analyst is correct that romance (15,200) leads; and mystery/thriller (12,450) plus children's (11,100) combined (23,550) does exceed romance.",
          "The analyst is incorrect; science fiction and biography together exceed romance.",
          "The analyst is correct that romance leads but incorrect that the other two genres combined exceed it.",
          "The analyst is incorrect; mystery/thriller alone exceeds romance.", "A",
          "Romance (15,200) leads all genres, and mystery/thriller + children's = 23,550 > 15,200. Both parts of the claim are correct.")

        q(de, M,
          "Researchers studying migration patterns of monarch butterflies have found that "
          "populations ________ by approximately 80% over the past two decades. Scientists "
          "attributed this decline to habitat loss in both their North American breeding "
          "grounds and their winter habitat in Mexican forests.\n\n"
          "Which choice most effectively uses the information to complete the claim?",
          "have increased", "have remained stable", "have declined", "have fluctuated unpredictably", "C",
          "The sentence later refers to 'this decline,' so the blank must indicate that populations have declined.")

        q(de, M,
          "A survey of 200 students asked which season they prefer:\n\n"
          "Winter: 30 | Spring: 55 | Summer: 80 | Fall: 35\n\n"
          "A student claims that more than half of respondents preferred either spring or "
          "summer. Which choice most effectively uses data from the survey to support "
          "this claim?",
          "Summer was the most popular season, with 80 students preferring it.",
          "Spring and summer together accounted for 135 of 200 respondents (67.5%), which is more than half.",
          "Winter was the least popular, with only 30 students preferring it.",
          "Fall attracted 35 respondents, more than winter but fewer than spring.", "B",
          "Spring (55) + Summer (80) = 135 out of 200 = 67.5%, which directly supports the claim that more than half preferred spring or summer.")

        q(gv, M,
          "Mathematician Maryam Mirzakhani, who became the first woman to win the prestigious "
          "Fields Medal in 2014, ________ in groundbreaking research on the geometry of "
          "Riemann surfaces and their moduli spaces.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "specialize", "specialized", "are specializing", "have specialized", "B",
          "'Specialized' is the correct simple past tense — Mirzakhani passed away in 2017, and the singular subject requires 'specialized.'")

        q(gv, M,
          "The city's new transit plan, which includes expanded bus routes and additional "
          "bike lanes, ________ expected to reduce traffic congestion by approximately 20% "
          "within three years.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "were", "is", "have been", "C",
          "'Is' agrees with the singular subject 'plan' — the relative clause 'which includes...' is parenthetical and does not affect subject-verb agreement.")

        q(gv, M,
          "________ the challenges of limited supplies and harsh weather, the expedition "
          "team pressed forward, determined to reach the summit before the seasonal "
          "storms arrived.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Acknowledging", "Acknowledged", "To acknowledge", "They acknowledged", "A",
          "'Acknowledging' is the correct participial phrase modifying the subject 'the expedition team.'")

        q(gv, M,
          "Each of the twenty students in the advanced chemistry class ________ required to "
          "submit a detailed laboratory report by the end of the semester.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "were", "is", "have been", "C",
          "'Each' is a singular indefinite pronoun and takes a singular verb: 'is.'")

        q(gp, M,
          "The renowned chef combined three unexpected ________ cinnamon, black pepper, "
          "and citrus zest — into a balanced and complex sauce.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "ingredients;", "ingredients,", "ingredients:", "ingredients", "C",
          "A colon correctly introduces the list of three ingredients that follows.")

        q(gp, M,
          "The Amazon rainforest produces approximately 20 percent of the world's "
          "oxygen ________ it is often called 'the lungs of the Earth.'\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "and", ", and", "; and", ":", "B",
          "A comma + coordinating conjunction (', and') correctly joins two independent clauses.")

        q(gp, M,
          "The museum's new wing ________ which features interactive exhibits on the history "
          "of space exploration—opened to widespread public enthusiasm last spring.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", "—", ":", "C",
          "The parenthetical 'which features...' is set off by dashes. Since the closing dash is present, the opening punctuation must also be a dash.")

        q(gp, M,
          "The museum's new wing opened last ________ attracting more than 10,000 visitors "
          "in its first week alone.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "month,", "month;", "month:", "month", "A",
          "A comma after 'month' introduces the participial phrase 'attracting more than 10,000 visitors,' which correctly modifies the main clause.")

        q(tr, M,
          "Training for a marathon requires months of gradual mileage increases, careful "
          "nutrition planning, and sufficient rest. ________ many first-time marathon runners "
          "underestimate the importance of recovery days in their training schedules.\n\n"
          "Which choice completes the text with the most logical transition?",
          "As a result,", "Nevertheless,", "For instance,", "Instead,", "B",
          "'Nevertheless' introduces a contrasting observation — despite the knowledge required, many runners still overlook recovery.")

        q(tr, M,
          "The new software update significantly improved the application's loading speed. "
          "________ it introduced several new features that users had been requesting "
          "for years.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "On the contrary,", "Furthermore,", "Despite this,", "C",
          "'Furthermore' adds an additional positive development — faster loading AND new features.")

        q(tr, M,
          "The ancient Maya developed an accurate calendar, sophisticated mathematics, and "
          "monumental architecture. ________ their astronomical observations were remarkably "
          "precise, allowing them to predict celestial events centuries in advance.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Otherwise,", "Instead,", "Similarly,", "In addition,", "D",
          "'In addition' introduces another achievement of the Maya — the astronomical observations.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- The blue whale (Balaenoptera musculus) is the largest animal ever known to exist.\n"
          "- Adult blue whales can reach 100 feet and weigh up to 200 tons.\n"
          "- Blue whales communicate using low-frequency sounds that travel thousands of miles.\n"
          "- Their primary diet consists of krill, tiny shrimp-like crustaceans.\n"
          "- Blue whales are endangered, with only approximately 10,000-25,000 remaining.\n\n"
          "The student wants to highlight the contrast between the blue whale's enormous "
          "size and its diet. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "Blue whales can reach 100 feet and 200 tons, and their sounds travel thousands of miles.",
          "Despite being the largest animals ever known, blue whales feed almost exclusively on krill, tiny crustaceans.",
          "Blue whales are endangered, with only 10,000-25,000 individuals remaining despite their massive size.",
          "Blue whales communicate using low-frequency sounds and are classified as endangered.", "B",
          "Option B directly contrasts the whale's enormous size with its tiny prey, accomplishing the student's stated goal.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Colosseum in Rome was completed in 80 CE under Emperor Titus.\n"
          "- It could hold between 50,000 and 80,000 spectators.\n"
          "- Events included gladiatorial contests, animal hunts, and public executions.\n"
          "- It was built using concrete, sand, and volcanic rock.\n"
          "- Earthquakes and stone-robbers have damaged much of the original structure.\n\n"
          "The student wants to emphasize the Colosseum's capacity to accommodate large "
          "audiences. Which choice most effectively uses relevant information from the "
          "notes to accomplish this goal?",
          "The Colosseum, completed in 80 CE, was constructed using concrete, sand, and volcanic rock.",
          "The Colosseum hosted gladiatorial contests, animal hunts, and public executions.",
          "Built under Emperor Titus, the Colosseum could hold between 50,000 and 80,000 spectators, demonstrating its massive capacity.",
          "Earthquakes and stone-robbers have damaged much of the Colosseum's original structure.", "C",
          "Option C directly addresses capacity (50,000-80,000 spectators) while providing context — the most effective choice for the student's goal.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(ev, E,
          "The community garden has become a beloved gathering place for neighbors. Each "
          "spring, volunteers ________ colorful flowers throughout the space, creating a "
          "welcoming environment for everyone.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "remove", "plant", "ignore", "buy", "B",
          "'Plant' is the most logical action for volunteers who want to create a garden full of colorful flowers.")

        q(ev, E,
          "The school play received enthusiastic applause at the end of each performance. "
          "The drama teacher said she was proud of how ________ the students had worked to "
          "prepare for the show.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "carelessly", "briefly", "diligently", "reluctantly", "C",
          "'Diligently' (working hard and carefully) matches the outcome of enthusiastic applause and a proud teacher.")

        q(ev, E,
          "Scientists were excited by their latest finding: a species of frog previously "
          "thought to be extinct was ________ living in the mountain forests of Ecuador.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "sometimes", "still", "barely", "never", "B",
          "'Still' indicates the frog is alive — consistent with being rediscovered after being thought extinct.")

        q(ev, E,
          "After weeks of cloudy weather, the sky finally ________ and residents of the "
          "small coastal town headed outside to enjoy the sunshine.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "darkened", "collapsed", "cleared", "closed", "C",
          "'Cleared' — the sky clearing up is what allows the sunshine to emerge and people to go outside.")

        q(rc, E,
          "The giant panda eats mostly bamboo, consuming up to 80 pounds per day. Despite "
          "being classified as carnivores, giant pandas have adapted to a nearly plant-based "
          "diet. Their digestive systems, however, are still suited for meat, making bamboo "
          "a somewhat inefficient food source.\n\n"
          "Which choice best states the main idea of the text?",
          "Giant pandas are unable to survive without eating meat regularly.",
          "Bamboo is the only plant that giant pandas can digest properly.",
          "Although classified as carnivores, giant pandas have adapted to eat bamboo despite it being an inefficient food source.",
          "Giant pandas are the only carnivores that have learned to eat plants.", "C",
          "The text focuses on the contrast between the panda's carnivore classification and its plant-based diet, noting the digestive inefficiency.")

        q(rc, E,
          "Thomas Edison is often credited with inventing the lightbulb, but in truth he "
          "improved upon earlier designs. Edison's contribution was developing a practical "
          "bulb with a long-lasting filament that could be produced affordably and used in "
          "homes. This made him the first to make electric lighting accessible to "
          "ordinary people.\n\n"
          "Which choice best states the main idea of the text?",
          "Edison stole credit for inventing the lightbulb from other inventors.",
          "Edison's work on improving existing designs made electric lighting practical and widely accessible.",
          "Edison's lightbulb was less effective than the earlier designs he improved upon.",
          "Before Edison, no one had ever thought about using electric lighting in homes.", "B",
          "The text emphasizes that Edison improved existing designs to make electric lighting practical and accessible — that is the main idea.")

        q(rc, E,
          "Honeybees communicate the location of flowers to other bees through a behavior "
          "called the 'waggle dance.' The bee performs a figure-eight movement, and the angle "
          "and duration of the dance indicate both the direction and distance of food. This "
          "remarkable form of communication was first decoded by scientist Karl von Frisch "
          "in the 1960s.\n\n"
          "Which choice best describes the function of the last sentence in the text?",
          "It explains why bees perform the waggle dance.",
          "It introduces Karl von Frisch as the inventor of the waggle dance.",
          "It provides historical context for when scientists first understood the waggle dance.",
          "It suggests that the waggle dance is no longer performed by modern bees.", "C",
          "The final sentence tells us when (the 1960s) and by whom (von Frisch) the waggle dance communication was decoded — historical context.")

        q(rc, E,
          "Many ancient civilizations tracked time using the phases of the moon. Because a "
          "lunar month is approximately 29.5 days, early calendars based on lunar cycles "
          "were slightly shorter than the solar year. Over centuries, astronomers developed "
          "methods to align lunar calendars with the seasons.\n\n"
          "Which choice best states the main idea of the text?",
          "The moon's phases are too irregular to be used in any calendar system.",
          "Ancient civilizations invented the concept of the solar year by observing the moon.",
          "Lunar cycles served as the basis for early timekeeping, and astronomers worked to reconcile lunar and solar calendars.",
          "Astronomers prefer solar calendars because they are more accurate than lunar ones.", "C",
          "The text describes lunar-based timekeeping as ancient practice and notes astronomers' efforts to reconcile it with the solar year.")

        q(rc, E,
          "The Great Wall of China was built over many centuries, with major construction "
          "occurring during the Ming dynasty (1368-1644). The wall stretches thousands of "
          "miles and was originally designed to protect against northern invasions. Today, "
          "it is one of China's most visited tourist attractions.\n\n"
          "Which choice best states the main idea of the text?",
          "The Great Wall was entirely built during the Ming dynasty.",
          "The Great Wall is no longer useful for protection but remains a cultural landmark.",
          "The Great Wall of China, constructed over centuries, was built for defense and is now a major tourist site.",
          "China built the Great Wall specifically to attract tourists in modern times.", "C",
          "The text covers the Wall's multi-century construction, its defensive purpose, and its current status as a tourist attraction.")

        q(de, E,
          "The table below shows the number of animals at a small zoo:\n\n"
          "Lions: 4 | Elephants: 3 | Zebras: 8 | Giraffes: 5 | Penguins: 12\n\n"
          "A visitor states that penguins are the most common animal at the zoo. Which choice "
          "most effectively uses data from the table to support this statement?",
          "The zoo has 4 lions and 3 elephants, making mammals the largest group.",
          "Penguins (12) outnumber every other animal species at the zoo.",
          "Zebras (8) are the second-most common animal at the zoo.",
          "The zoo has a total of 32 animals across all species.", "B",
          "Option B directly uses the data to confirm that penguins (12) have the highest count of any single species.")

        q(de, E,
          "The table shows students' preferred after-school activities:\n\n"
          "Reading: 15 | Sports: 22 | Gaming: 18 | Art: 10 | Total: 65\n\n"
          "A school counselor claims that more than a third of students prefer either reading "
          "or art. Which choice most effectively uses data from the table to evaluate "
          "this claim?",
          "Sports is the most popular activity with 22 students.",
          "Reading (15) and Art (10) combined equal 25 students out of 65 total, which is approximately 38.5% — more than a third. The claim is correct.",
          "Gaming (18) is more popular than Art (10).",
          "Sports and gaming together account for 40 students.", "B",
          "15 + 10 = 25; 25/65 = 38.5% > 33.3% (one third). Option B correctly evaluates the claim using the table data.")

        q(de, E,
          "Text 1: Homework is an essential part of education. Regular assignments help "
          "students practice skills, reinforce concepts, and develop time management habits.\n\n"
          "Text 2: Research suggests that excessive homework can cause stress and reduce "
          "students' enjoyment of learning. Balance is important, and too much work outside "
          "of school can actually harm academic performance.\n\n"
          "Based on the texts, which statement would both authors most likely agree with?",
          "Students should never be given homework.",
          "All homework should be eliminated from schools immediately.",
          "Homework has some role in education, but its quantity matters.",
          "Homework always improves academic performance.", "C",
          "Text 1 supports homework while Text 2 warns against excess — both imply some homework is acceptable but the amount is important.")

        q(de, E,
          "The table below shows reading speeds of five students:\n\n"
          "Student A: 180 wpm | B: 210 wpm | C: 150 wpm | D: 225 wpm | E: 195 wpm\n\n"
          "A teacher claims that the class average reading speed is 192 words per minute. "
          "Which choice most accurately evaluates this claim?",
          "The claim is incorrect; the average is 185 words per minute.",
          "The claim is correct: (180+210+150+225+195) divided by 5 equals 192 words per minute.",
          "The claim is incorrect; Student D reads much faster than the stated average.",
          "The claim is incorrect; the average is 200 words per minute.", "B",
          "180+210+150+225+195 = 960; 960/5 = 192. The teacher's claim is exactly correct.")

        q(de, E,
          "Text 1: Daily exercise has numerous health benefits, including improved "
          "cardiovascular health, stronger muscles, and better mood.\n\n"
          "Text 2: While exercise is beneficial, it is important not to overdo it. "
          "Excessive exercise without adequate rest can lead to injuries and burnout.\n\n"
          "Based on the texts, the authors would most likely agree that ________",
          "Exercise should be avoided unless supervised by a doctor.",
          "Exercise has benefits but should be practiced in moderation.",
          "Daily exercise always leads to improved mood and energy.",
          "Too much exercise is more harmful than no exercise at all.", "B",
          "Both texts agree that exercise is beneficial but that excess can be harmful — pointing to moderation as the common ground.")

        q(gv, E,
          "The team of scientists ________ their findings at the international conference "
          "last month.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "present", "presents", "presented", "presenting", "C",
          "'Presented' is the correct simple past tense — the action occurred 'last month.'")

        q(gv, E,
          "Each of the contestants ________ given exactly ten minutes to complete "
          "the challenge.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "were", "is", "was", "D",
          "'Each' is a singular indefinite pronoun; 'was' is the correct singular past tense form.")

        q(gv, E,
          "The students in the class ________ looking forward to the field trip to the "
          "science museum.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "is", "are", "was", "has been", "B",
          "'Students' is a plural noun and requires the plural verb 'are.'")

        q(gv, E,
          "After finishing her homework, Maya ________ outside to play with her friends.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "goes", "went", "going", "has gone", "B",
          "'Went' is the correct simple past tense — it is consistent with the completed action of 'finishing' homework.")

        q(gp, E,
          "The three ingredients in this simple recipe ________ flour, sugar, and butter.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are:", "are;", "are,", "are", "A",
          "A colon after 'are' correctly introduces the list of ingredients that follows.")

        q(gp, E,
          "Mia loves hiking ________ every weekend she explores a different trail near "
          "her home.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", "and", "B",
          "A semicolon correctly joins two independent clauses ('Mia loves hiking' and 'every weekend she explores...').")

        q(gp, E,
          "Dr. Huang, a marine biologist with over thirty years of experience ________ has "
          "dedicated her career to studying coral reef ecosystems in the Pacific.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", "—", "A",
          "A comma closes the appositive phrase 'a marine biologist with over thirty years of experience,' setting it off from the main clause.")

        q(gp, E,
          "We visited Paris ________ we also toured the Eiffel Tower, the Louvre, and "
          "Notre Dame.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ", where", "; where", ": where", "where,", "A",
          "A comma before the relative adverb 'where' correctly introduces the relative clause describing Paris.")

        q(tr, E,
          "The hiking trail is known for its beautiful views. ________ the path can be "
          "quite steep in places, making it challenging for beginners.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "Therefore,", "However,", "Similarly,", "C",
          "'However' introduces a contrasting detail — the trail is beautiful but also steep and difficult.")

        q(tr, E,
          "Jada practices piano for an hour every day. ________ she has greatly improved "
          "her playing skills over the past year.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "Instead,", "As a result,", "On the other hand,", "C",
          "'As a result' shows that daily practice led to improvement — a cause-and-effect relationship.")

        q(tr, E,
          "The school cafeteria now offers more vegetarian options. ________ the new salad "
          "bar has become very popular with students.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Despite this,", "In fact,", "On the contrary,", "Nevertheless,", "B",
          "'In fact' reinforces and intensifies the point — the salad bar's popularity confirms the success of the new options.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- Dolphins are intelligent marine mammals that live in oceans worldwide.\n"
          "- They communicate using a system of clicks, whistles, and other sounds.\n"
          "- Dolphins work together in groups called pods to hunt fish.\n"
          "- A dolphin's brain is larger relative to body size than almost any other animal.\n"
          "- They have been observed helping injured companions and even humans in distress.\n\n"
          "The student wants to emphasize dolphins' intelligence. Which choice most "
          "effectively uses relevant information from the notes to accomplish this goal?",
          "Dolphins live in oceans worldwide and travel in groups called pods.",
          "Dolphins communicate using clicks and whistles.",
          "Dolphins have a large brain relative to their body size and have been observed helping injured companions, suggesting high intelligence.",
          "Dolphins hunt fish by working cooperatively in groups.", "C",
          "Option C combines two pieces of evidence for intelligence: the large brain and the observed helping behavior.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Eiffel Tower was built for the 1889 World's Fair in Paris.\n"
          "- It was designed by engineer Gustave Eiffel and his team.\n"
          "- The tower stands 330 meters tall.\n"
          "- It was originally intended to be temporary and demolished after 20 years.\n"
          "- Today it is the most-visited paid monument in the world.\n\n"
          "The student wants to highlight the unexpected longevity of the Eiffel Tower. "
          "Which choice most effectively uses relevant information from the notes to "
          "accomplish this goal?",
          "The Eiffel Tower stands 330 meters tall and was designed by Gustave Eiffel.",
          "Though originally planned for demolition after 20 years, the Eiffel Tower is now the most-visited paid monument in the world.",
          "The Eiffel Tower was built for the 1889 World's Fair in Paris.",
          "Gustave Eiffel and his team designed the tower for the World's Fair.", "B",
          "Option B directly captures the contrast between the tower's originally temporary purpose and its enduring popularity — the student's stated goal.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(ev, H,
          "The philosopher's arguments were so ________ that even his most ardent supporters "
          "struggled to follow the chain of reasoning without rereading certain passages "
          "multiple times.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "lucid", "abstruse", "repetitive", "straightforward", "B",
          "'Abstruse' means difficult to understand — it precisely matches the idea that even supporters struggled to follow the reasoning.")

        q(ev, H,
          "Unlike many contemporaries who relied on elaborate metaphors and ornamentation, "
          "the poet favored a ________ style: short, unadorned lines that derived their "
          "power from precision rather than decoration.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "verbose", "flamboyant", "spare", "convoluted", "C",
          "'Spare' means minimal, plain, and unornamented — exactly matching the description of short, unadorned lines.")

        q(ev, H,
          "The researcher's insistence on conducting experiments under ________ conditions — "
          "controlling every possible variable and documenting each procedure with meticulous "
          "detail — set a new standard for reproducibility in the field.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "haphazard", "rigorous", "casual", "approximate", "B",
          "'Rigorous' means extremely thorough and careful — matching the careful, controlled experimental approach described.")

        q(ev, H,
          "The senator's speech was remarkable not for its dramatic revelations but for its "
          "________ — every word chosen with apparent care, every claim supported by "
          "specific evidence, leaving little room for misinterpretation.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "ambiguity", "exaggeration", "precision", "brevity", "C",
          "'Precision' best captures carefully chosen words supported by specific evidence — the opposite of ambiguity.")

        q(rc, H,
          "The following text is adapted from Henry James's 1903 novel The Ambassadors. "
          "Lambert Strether, an American man, reflects on his time in Paris.\n\n"
          "It was the word 'home' that did it, and the sound of it had been a sort of "
          "deep-toned bell. He had not heard it for a long time — not since the beginning "
          "of his life in Woollett. But now the word rang out across the world, and rang "
          "out in a way that made him feel, not that he had escaped Woollett, but that "
          "he had found something it had left out.\n\n"
          "Which choice best describes what the passage conveys about Strether's reaction "
          "to the word 'home'?",
          "He hears the word and becomes desperate to return to Woollett immediately.",
          "The word makes him realize that his time in Europe allowed him to discover something missing from his former life.",
          "The word reminds him that he has failed to accomplish what he intended to do in Europe.",
          "He feels that 'home' no longer has any meaning for him after time abroad.", "B",
          "Strether feels he found what Woollett 'left out' — Paris gave him something his old home lacked, suggesting Europe opened new understanding.")

        q(rc, H,
          "In studying urban heat islands — cities significantly warmer than surrounding "
          "rural areas — scientists found the effect is most pronounced at night. During "
          "the day, both urban and rural surfaces absorb solar radiation. At night, rural "
          "surfaces cool quickly, while urban structures of concrete and asphalt retain heat "
          "and release it slowly. This asymmetry has implications for energy use, public "
          "health, and ecosystem disruption.\n\n"
          "The passage implies that urban heat islands are particularly concerning at night "
          "primarily because ________",
          "cities receive more solar radiation than rural areas during the day.",
          "concrete and asphalt are ineffective at absorbing heat during daytime.",
          "urban areas remain warm while surrounding rural areas cool, creating the largest temperature differential.",
          "ecosystems within cities are unable to function during nighttime hours.", "C",
          "At night rural areas cool while cities stay warm — this divergence creates the maximum temperature differential, which is why the nighttime effect is most pronounced.")

        q(rc, H,
          "Historian Barbara Tuchman argued that World War I was not inevitable — it "
          "resulted from miscalculations, failures of communication, and the rigidity of "
          "military mobilization plans. Tuchman contended that key decision-makers in 1914 "
          "were not pursuing war as a rational policy goal but stumbled into it through "
          "pride, miscommunication, and an inability to reverse decisions once set in "
          "motion. Her argument challenged the view that the war was a product of deep "
          "structural forces beyond any individual's control.\n\n"
          "Based on the passage, Tuchman's view of the war's origins differs from the "
          "alternative historical view primarily in that Tuchman ________",
          "believes the war was inevitable, while others see it as preventable.",
          "attributes the war to specific human decisions and errors, while others point to structural forces.",
          "argues that military mobilization plans were well designed but misused.",
          "claims that communication failures occurred only among military leaders.", "B",
          "Tuchman attributes WWI to human error and contingency; the alternative view sees it as driven by structural forces beyond individuals' control.")

        q(rc, H,
          "The following text is adapted from Mary Shelley's 1818 novel Frankenstein. "
          "Victor Frankenstein reflects on his responsibility.\n\n"
          "I, not in deed, but in effect, was the true murderer. Elizabeth, Justine, "
          "William — how many more must suffer through my hubris? I felt the weight of "
          "each name like a stone pressed upon my chest, and yet I could not bring myself "
          "to confess. To do so would be to abandon the only purpose that kept me moving "
          "forward: revenge.\n\n"
          "Which choice best describes the function of the question in the text?",
          "It reveals that Victor cannot remember the names of all his victims.",
          "It demonstrates Victor's callousness toward those who have died because of him.",
          "It emphasizes Victor's guilt and his fear that more people will be harmed.",
          "It suggests that Victor blames his creation for the deaths, not himself.", "C",
          "The rhetorical question ('how many more must suffer?') expresses Victor's guilt while foreshadowing his fear of causing additional harm.")

        q(rc, H,
          "Cognitive scientist Gary Marcus argued that the human brain is not optimally "
          "designed but 'jerry-rigged' — built through evolutionary compromise that layered "
          "new structures onto old ones rather than redesigning from scratch. He suggests "
          "many cognitive biases stem from this ad hoc architecture. Critics argue that "
          "Marcus overstates the case: the brain's flexibility and learning ability far "
          "exceed those of any engineered system, and calling it 'jerry-rigged' "
          "misrepresents the elegant solutions evolution has found.\n\n"
          "Which choice best states the main idea of the text?",
          "Marcus has definitively proven that the human brain is inferior to engineered systems.",
          "The human brain's cognitive biases are entirely explained by its evolutionary history.",
          "Marcus argues that the brain's evolutionary origins cause its weaknesses, though critics dispute this characterization.",
          "Critics of Marcus agree the brain is poorly designed but disagree about the reasons.", "C",
          "The text presents Marcus's argument and the critics who challenge it — the main idea is the debate over whether the brain's flaws are explained by its evolutionary architecture.")

        q(de, H,
          "Text 1: The reintroduction of wolves to Yellowstone National Park in 1995 had "
          "dramatic positive effects. Wolves reduced elk populations, which had overgrazed "
          "riverbanks. With less grazing, vegetation recovered along streams, stabilizing "
          "banks and altering river behavior — a phenomenon ecologists call a 'trophic "
          "cascade.'\n\n"
          "Text 2: While wolf reintroduction has been celebrated as an ecological success, "
          "researchers urge caution about attributing all observed changes to wolves. Some "
          "studies suggest that drought conditions and park management decisions also "
          "contributed to vegetation recovery. Attributing all changes to wolves may "
          "oversimplify a complex set of interacting factors.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond to the "
          "claim in Text 1 that wolves caused dramatic positive effects?",
          "The observed effects may have been caused by multiple factors, not wolves alone.",
          "Wolves were ineffective in reducing elk populations significantly.",
          "Drought conditions were more damaging to the ecosystem than overgrazed riverbanks.",
          "The author of Text 1 is entirely correct that wolves deserve full credit.", "A",
          "Text 2 argues that wolves may not be the sole cause — drought and management also contributed — so it challenges the simplicity of Text 1's attribution.")

        q(de, H,
          "The table below shows population data for four cities over 20 years:\n\n"
          "City A: Year 1 = 250,000; Year 20 = 310,000\n"
          "City B: Year 1 = 180,000; Year 20 = 165,000\n"
          "City C: Year 1 = 420,000; Year 20 = 505,000\n"
          "City D: Year 1 = 95,000; Year 20 = 142,000\n\n"
          "A demographer claims that City D showed the greatest percentage population "
          "increase over the 20-year period. Which choice most effectively uses data "
          "from the table to evaluate this claim?",
          "City D grew from 95,000 to 142,000, an absolute increase of 47,000 people.",
          "City D's growth of 47,000 people exceeds City B's decline, supporting the claim.",
          "City D grew by approximately 49.5% (47,000/95,000), while City A grew by 24% and City C grew by 20.2%, confirming the claim.",
          "City C had the largest absolute increase of 85,000 people, so City C showed the greatest growth.", "C",
          "Percentage growth: D = 49.5%, A = 24%, C = 20.2%. City D has the highest percentage increase, confirming the demographer's claim.")

        q(de, H,
          "The following data shows the results of a study on reading habits:\n\n"
          "Adults who read daily: 42% report high life satisfaction\n"
          "Adults who read weekly: 35% report high life satisfaction\n"
          "Adults who read monthly: 28% report high life satisfaction\n"
          "Adults who rarely read: 21% report high life satisfaction\n\n"
          "A researcher concludes that reading causes higher life satisfaction. A student "
          "challenges this conclusion by pointing out that ________\n\n"
          "Which choice most logically completes the text?",
          "adults who read daily have the highest satisfaction, supporting a causal claim.",
          "the data shows correlation between reading frequency and satisfaction, but correlation does not prove causation.",
          "monthly readers should be removed from the study because their habits are inconsistent.",
          "the researcher's conclusion is supported by the regularly increasing percentages.", "B",
          "Correlation (reading more associates with higher satisfaction) does not prove causation (that reading causes satisfaction). Other factors could explain the relationship.")

        q(de, H,
          "Text 1: Recent studies suggest that sleep deprivation significantly impairs "
          "cognitive performance. Participants who slept fewer than six hours per night "
          "scored, on average, 25% lower on tests of attention and working memory than "
          "those who slept eight hours.\n\n"
          "Text 2: The relationship between sleep and cognitive performance is more complex "
          "than simple comparisons suggest. Individual baseline cognitive ability, task type, "
          "and habitual sleep needs vary widely. Furthermore, some participants show "
          "remarkable resilience to sleep deprivation while others are highly vulnerable.\n\n"
          "Based on the texts, the author of Text 2 would most likely agree that ________",
          "sleep deprivation has no effect on cognitive performance.",
          "the cognitive effects of sleep deprivation are consistent across all individuals.",
          "while sleep deprivation may affect cognition, the relationship is too variable to support simple generalizations.",
          "sleeping fewer than six hours per night causes permanent cognitive damage.", "C",
          "Text 2 emphasizes individual variation and complexity — it doesn't deny sleep deprivation's effects but says the relationship resists simple generalizations.")

        q(de, H,
          "A survey of 500 high school students asked which subjects they find most "
          "challenging:\n\nMathematics: 42% | Foreign Language: 28% | Science: 18% | "
          "History: 8% | English: 4%\n\n"
          "A researcher claims that the majority of students find STEM subjects "
          "(Mathematics and Science) most challenging. Which choice most effectively "
          "uses the data to evaluate this claim?",
          "Mathematics alone (42%) represents the most challenging subject for the largest share of students.",
          "Mathematics (42%) and Science (18%) together account for 60% of students, representing a majority, which supports the researcher's claim.",
          "Foreign Language (28%) is more challenging than Science (18%) for students.",
          "History and English together (12%) represent a small fraction of challenges.", "B",
          "42% + 18% = 60% > 50%, so a majority do find STEM subjects most challenging. Option B directly evaluates the claim using the combined data.")

        q(gv, H,
          "Recent archaeological discoveries, along with previously unexamined historical "
          "records, ________ begun to challenge the long-held assumption that ancient Rome's "
          "decline was primarily driven by barbarian invasions.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "has", "have", "is", "was", "B",
          "The compound subject 'discoveries' and 'records' is plural — 'have' is the correct plural verb form.")

        q(gv, H,
          "The committee, after reviewing hundreds of applications from candidates across "
          "five continents, ________ to announce its decision at the annual conference "
          "in Geneva.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "plan", "are planning", "plans", "have planned", "C",
          "'The committee' is a singular noun — 'plans' is the correct singular verb form.")

        q(gv, H,
          "________ the award for three consecutive years, the novelist was considered the "
          "frontrunner for the lifetime achievement prize.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Having won", "She won", "To have won", "Winning", "A",
          "'Having won' is the correct perfect participial phrase, indicating a prior completed action that explains the subsequent recognition.")

        q(gv, H,
          "The results of the landmark study, which contradicted decades of accepted medical "
          "consensus, ________ the research community to reassess its approach to treating "
          "the condition.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "compelling", "compel", "compelled", "to compel", "C",
          "'Compelled' is the correct simple past tense verb — the study results prompted/compelled the reassessment.")

        q(gp, H,
          "The scientist's groundbreaking paper introduced two novel concepts ________ the "
          "measurement of quantum decoherence in room-temperature conditions and the "
          "application of these measurements to error correction in quantum computing.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ":", ";", "—and", "B",
          "A colon correctly introduces the list that explains and elaborates on the 'two novel concepts.'")

        q(gp, H,
          "Although the treaty was signed in ________ its terms remained contested for "
          "decades, with several signatory nations disputing the interpretation of key "
          "clauses.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "1847,", "1847;", "1847:", "1847", "A",
          "A comma after '1847' closes the subordinate 'Although...' clause before the main clause begins.")

        q(gp, H,
          "The architect's portfolio, which spanned five decades and included structures on "
          "three continents ________ was praised by critics for its remarkable consistency "
          "of vision despite stylistic evolution.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "—", ",", ";", ":", "B",
          "The relative clause 'which spanned five decades...' is set off by commas. A comma is needed to close it before the main verb 'was praised.'")

        q(gp, H,
          "For centuries, natural philosophy — what we now call science ________ was "
          "practiced primarily by wealthy individuals who could afford books, instruments, "
          "and the leisure time required for sustained inquiry.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ":", "—", ";", "C",
          "The phrase 'what we now call science' is a parenthetical set off by dashes. Since the opening dash is present, a closing dash is required.")

        q(tr, H,
          "The philosopher Immanuel Kant spent his entire life within a few miles of "
          "Konigsberg, Prussia, maintaining a schedule of remarkable regularity and rarely "
          "traveling. ________ his intellectual influence stretched across continents, "
          "fundamentally reshaping Western philosophy.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Consequently,", "Similarly,", "Nevertheless,", "Specifically,", "C",
          "'Nevertheless' highlights the contrast between Kant's physically limited life and his vast intellectual influence.")

        q(tr, H,
          "Early astronomers had difficulty distinguishing planets from stars because both "
          "appeared as points of light. ________ the development of telescopes in the early "
          "seventeenth century allowed observers to see that planets showed measurable discs "
          "and moved differently against the background of fixed stars.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "However,", "As a result,", "By contrast,", "B",
          "'However' introduces the solution to the prior difficulty — the telescope changed what observers could see.")

        q(tr, H,
          "The new pharmaceutical compound showed remarkable effectiveness in laboratory "
          "trials, reducing tumor growth by 60% in animal models. ________ researchers "
          "cautioned that results in animal studies frequently do not translate directly "
          "to human patients, and that clinical trials would be necessary.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "In addition,", "Similarly,", "Nevertheless,", "D",
          "'Nevertheless' signals that despite the promising lab results, researchers still urge caution about translating findings to humans.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- Mary Shelley wrote Frankenstein in 1818 when she was only 18 years old.\n"
          "- The novel is considered one of the first works of science fiction.\n"
          "- It explores themes of creation, responsibility, and scientific ethics.\n"
          "- The novel was partially inspired by a ghost-story competition among Shelley, "
          "Percy Bysshe Shelley, and Lord Byron.\n"
          "- Upon publication, the book appeared anonymously; many readers assumed the "
          "author was male.\n\n"
          "The student wants to emphasize the circumstances that make Frankenstein's "
          "creation particularly remarkable. Which choice most effectively uses relevant "
          "information from the notes to accomplish this goal?",
          "Mary Shelley explored themes of creation, responsibility, and ethics in Frankenstein.",
          "Frankenstein is considered one of the first science fiction novels, published in 1818.",
          "Written when its author was only 18 years old and emerging from a ghost-story competition, Frankenstein went on to become a foundational work of science fiction.",
          "Many readers assumed Frankenstein's author was male because the book appeared anonymously.", "C",
          "Option C combines the most remarkable details — the author's young age, the unusual origin, and the novel's lasting significance — making the creation of Frankenstein stand out.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- Marie Curie was the first woman to win a Nobel Prize.\n"
          "- She won the prize twice: in Physics (1903) and Chemistry (1911), making her "
          "the only person to win in two different sciences.\n"
          "- Her research on radioactivity led to early cancer treatments.\n"
          "- Despite her achievements, she faced significant gender discrimination.\n"
          "- Curie was born in Poland but conducted most research in France.\n\n"
          "The student wants to highlight what makes Curie's Nobel Prize achievements "
          "uniquely significant. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "Marie Curie was born in Poland but conducted her research in France, where she faced gender discrimination.",
          "Curie's research on radioactivity led to medical advances in cancer treatment.",
          "Marie Curie won the Nobel Prize twice — in Physics and Chemistry — making her the only person ever to win in two different scientific fields.",
          "Despite facing gender discrimination, Curie was the first woman to win a Nobel Prize.", "C",
          "Option C highlights the unique distinction: winning twice and in two different sciences, which no other person has achieved — directly addressing what makes her achievement uniquely significant.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(alg, M, "Solve for x: 4x − 9 = 19",
          "4", "7", "11", "5", "B",
          "4x = 28; x = 7. Check: 4(7) − 9 = 28 − 9 = 19.")

        q(alg, M, "If 3(2x + 1) = 5x + 10, what is the value of x?",
          "7", "3", "5", "9", "A",
          "6x + 3 = 5x + 10; x = 7. Check: 3(15) = 45; 5(7) + 10 = 45.")

        q(alg, M, "Which of the following is equivalent to 2(x + 3) − (x − 4)?",
          "x + 10", "x + 2", "3x + 10", "x + 1", "A",
          "2x + 6 − x + 4 = x + 10.")

        q(alg, M,
          "Which value of x satisfies the inequality 5 < 2x + 1 ≤ 13?",
          "2", "5", "7", "1", "B",
          "5 < 2x + 1 ≤ 13 → 4 < 2x ≤ 12 → 2 < x ≤ 6. Of the choices, x = 5 satisfies: 5 < 11 ≤ 13.")

        q(alg, M,
          "A line passes through the points (2, 5) and (4, 11). What is the y-intercept of the line?",
          "−1", "1", "3", "−3", "A",
          "Slope = (11−5)/(4−2) = 3. Using (2, 5): 5 = 3(2) + b → b = −1.")

        q(fun, M, "If f(x) = 3x² − 2x + 1, what is f(2)?",
          "5", "9", "11", "13", "B",
          "f(2) = 3(4) − 2(2) + 1 = 12 − 4 + 1 = 9.")

        q(fun, M,
          "The function g is defined as g(x) = 2x + 5. If g(a) = 17, what is the value of a?",
          "4", "6", "8", "11", "B",
          "2a + 5 = 17 → 2a = 12 → a = 6.")

        q(fun, M,
          "The graph of y = f(x) passes through (3, 7). If h(x) = f(x) + 2, what is h(3)?",
          "5", "7", "9", "14", "C",
          "h(3) = f(3) + 2 = 7 + 2 = 9.")

        q(fun, M,
          "The table shows values of function f:\n"
          "x: 1, 2, 3, 4 | f(x): 3, 7, 11, 15\n\nWhich equation defines f(x)?",
          "f(x) = 2x + 1", "f(x) = 4x − 1", "f(x) = 3x", "f(x) = 4x + 1", "B",
          "f(1) = 4(1)−1 = 3 ✓; f(2) = 7 ✓; f(3) = 11 ✓; f(4) = 15 ✓.")

        q(geo, M, "A right triangle has legs of length 9 and 12. What is the length of the hypotenuse?",
          "21", "13", "15", "17", "C",
          "c = √(81 + 144) = √225 = 15.")

        q(geo, M,
          "A circle has a diameter of 10. What is its area? (Use π ≈ 3.14)",
          "31.4", "78.5", "157", "314", "B",
          "r = 5; A = π(25) ≈ 78.5.")

        q(geo, M,
          "In a triangle, two angles measure 47° and 83°. What is the third angle?",
          "40°", "50°", "60°", "70°", "B",
          "180° − 47° − 83° = 50°.")

        q(geo, M,
          "A rectangle has a perimeter of 36 and a width of 7. What is its length?",
          "9", "11", "14", "22", "B",
          "2(l + 7) = 36 → l + 7 = 18 → l = 11.")

        q(dsp, M,
          "The ages of five students are: 12, 14, 13, 15, 11. What is the mean age?",
          "12", "13", "14", "15", "B",
          "(12 + 14 + 13 + 15 + 11) / 5 = 65 / 5 = 13.")

        q(dsp, M,
          "A bag contains 4 red, 3 blue, and 5 green marbles. If one marble is drawn at "
          "random, what is the probability it is blue?",
          "1/3", "1/4", "5/12", "1/6", "B",
          "P(blue) = 3/(4+3+5) = 3/12 = 1/4.")

        q(dsp, M,
          "The scores on a math test were: 72, 85, 91, 68, 74, 91, 88. What is the mode?",
          "74", "85", "91", "88", "C",
          "91 appears twice; all other values appear once. Mode = 91.")

        q(dsp, M,
          "Of 30 students surveyed, 18 said they prefer reading to watching TV. What "
          "percent of students prefer reading?",
          "18%", "40%", "60%", "66%", "C",
          "18/30 × 100 = 60%.")

        q(dsp, M,
          "A data set shows weekly study hours for five students: 4, 7, x, 12, 15. "
          "If the mean is 9, what is the value of x?",
          "6", "7", "8", "9", "B",
          "Sum = 9 × 5 = 45; 4 + 7 + x + 12 + 15 = 38 + x = 45; x = 7.")

        q(wp, M,
          "A store sells notebooks for $3 each and pens for $1.50 each. Maria buys "
          "4 notebooks and some pens and spends exactly $18. How many pens did she buy?",
          "2", "3", "4", "6", "C",
          "4 × $3 = $12; remaining = $6; $6 ÷ $1.50 = 4 pens.")

        q(wp, M,
          "A car travels at a constant speed of 60 miles per hour. How many minutes does "
          "it take to travel 40 miles?",
          "40", "45", "30", "50", "A",
          "Time = 40/60 hours = 2/3 hour = 40 minutes.")

        q(wp, M,
          "Jamal is saving to buy a video game costing $65. He has $32 saved and earns "
          "$8.50 per hour. How many full hours must he work to have enough money?",
          "3", "4", "5", "6", "B",
          "Needs $33 more; $33 ÷ $8.50 ≈ 3.88 → 4 full hours.")

        q(wp, M,
          "In a class, the ratio of girls to boys is 3:2. If there are 30 students total, "
          "how many are girls?",
          "12", "15", "18", "20", "C",
          "Total parts = 5; each part = 6; girls = 3 × 6 = 18.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(alg, E, "Solve for x: 2x + 3 = 11",
          "2", "3", "4", "5", "C",
          "2x = 8; x = 4.")

        q(alg, E, "If y = 2x − 1, what is y when x = 5?",
          "7", "8", "9", "11", "C",
          "y = 2(5) − 1 = 10 − 1 = 9.")

        q(alg, E, "Which value of x satisfies x + 7 < 12?",
          "3", "5", "6", "7", "A",
          "x + 7 < 12 → x < 5. Of the choices, only x = 3 satisfies (3 + 7 = 10 < 12).")

        q(alg, E, "What is the value of 3x + 2y when x = 4 and y = 3?",
          "14", "18", "20", "21", "B",
          "3(4) + 2(3) = 12 + 6 = 18.")

        q(alg, E, "If 2x = y + 5 and y = 7, what is x?",
          "3", "5", "6", "9", "C",
          "2x = 7 + 5 = 12; x = 6.")

        q(fun, E, "If f(x) = x + 8, what is f(5)?",
          "8", "10", "13", "40", "C",
          "f(5) = 5 + 8 = 13.")

        q(fun, E, "Which of the following points lies on the line y = 2x + 1?",
          "(1, 2)", "(2, 5)", "(3, 8)", "(0, 2)", "B",
          "y = 2(2) + 1 = 5. Check: (1,2): 2(1)+1=3≠2; (3,8): 2(3)+1=7≠8; (0,2): 1≠2.")

        q(fun, E, "A function is defined by f(x) = 4 − x. What is f(−2)?",
          "2", "6", "−6", "−2", "B",
          "f(−2) = 4 − (−2) = 4 + 2 = 6.")

        q(fun, E, "The line y = 3x − 2 crosses the y-axis at which point?",
          "(0, 3)", "(0, −2)", "(2/3, 0)", "(3, 0)", "B",
          "At x = 0: y = 3(0) − 2 = −2. The y-intercept is (0, −2).")

        q(geo, E, "What is the area of a rectangle with length 8 and width 5?",
          "13", "20", "26", "40", "D",
          "Area = 8 × 5 = 40.")

        q(geo, E, "A triangle has angles of 60° and 90°. What is the third angle?",
          "20°", "30°", "45°", "50°", "B",
          "180° − 60° − 90° = 30°.")

        q(geo, E, "The perimeter of a square is 28. What is the length of one side?",
          "4", "6", "7", "8", "C",
          "28 ÷ 4 = 7.")

        q(geo, E, "Two legs of a right triangle measure 3 and 4. What is the hypotenuse?",
          "5", "6", "7", "12", "A",
          "This is a 3-4-5 right triangle: √(9 + 16) = √25 = 5.")

        q(dsp, E, "The data set is: 5, 8, 12, 8, 10, 7. What is the mode?",
          "7", "8", "10", "12", "B",
          "8 appears twice; all other values appear once. Mode = 8.")

        q(dsp, E,
          "A spinner has 5 equal sections: red, blue, green, yellow, purple. What is the "
          "probability of landing on blue?",
          "1/4", "1/5", "2/5", "1/2", "B",
          "1 section out of 5 equal sections: P(blue) = 1/5.")

        q(dsp, E,
          "The high temperatures for five days were: 72, 68, 75, 70, 80. What is the "
          "mean temperature?",
          "70", "72", "73", "75", "C",
          "(72+68+75+70+80) = 365; 365 ÷ 5 = 73.")

        q(dsp, E,
          "In a class of 20 students, 8 students wear glasses. What percentage wear glasses?",
          "8%", "20%", "40%", "80%", "C",
          "8/20 × 100 = 40%.")

        q(dsp, E,
          "What is the median of the data set: 3, 7, 9, 12, 15?",
          "7", "9", "12", "15", "B",
          "With 5 values, the median is the 3rd value: 9.")

        q(wp, E, "A store sells apples for $0.50 each. Sam wants to buy 6 apples. How much will Sam pay?",
          "$2.00", "$2.50", "$3.00", "$3.50", "C",
          "6 × $0.50 = $3.00.")

        q(wp, E,
          "Each bracelet requires 15 beads. If the class has 90 beads, how many complete "
          "bracelets can they make?",
          "4", "5", "6", "7", "C",
          "90 ÷ 15 = 6.")

        q(wp, E, "A train travels 150 miles in 3 hours at constant speed. What is its speed in mph?",
          "30 mph", "45 mph", "50 mph", "60 mph", "C",
          "150 ÷ 3 = 50 mph.")

        q(wp, E,
          "At a school fair, 3 out of every 5 students bought a ticket. If there are "
          "200 students, how many bought a ticket?",
          "80", "100", "120", "150", "C",
          "3/5 × 200 = 120.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(alg, H,
          "If 2x + 3y = 12 and x − y = 1, what is the value of x?",
          "3", "4", "5", "2", "A",
          "From x = y + 1, substitute: 2(y+1) + 3y = 12 → 5y = 10 → y = 2; x = 3.")

        q(alg, H,
          "The equation 3x² − 12 = 0 has solutions x = a and x = −a. What is the value of a?",
          "2", "3", "4", "6", "A",
          "3x² = 12 → x² = 4 → x = ±2. Therefore a = 2.")

        q(alg, H,
          "If (x + 4)(x − 2) = 0 and x > 0, what is the value of 3x − 1?",
          "3", "4", "5", "6", "C",
          "x = −4 or x = 2. Since x > 0, x = 2. Then 3(2) − 1 = 5.")

        q(alg, H,
          "A store applies a 15% discount to the original price p, then adds 10% sales "
          "tax. Which expression gives the final price?",
          "0.85p + 0.10p", "0.85(1.10)p", "0.85p − 0.10p", "0.90(0.85p)", "B",
          "After 15% off: 0.85p. After 10% tax: 0.85p × 1.10 = 0.935p.")

        q(alg, H,
          "The system of equations below has no solution:\n3x + ay = 6\n6x + 4y = 7\n\n"
          "What is the value of a?",
          "1", "2", "3", "4", "B",
          "For no solution, lines must be parallel: slopes must be equal. Slope of line 2 = −3/2. "
          "Slope of line 1 = −3/a = −3/2 → a = 2. With a=2, lines are parallel (not identical).")

        q(fun, H,
          "The function f is defined by f(x) = x² − 4x + 3. For what values of x does f(x) = 0?",
          "x = 1 and x = 3", "x = −1 and x = −3",
          "x = 1 and x = −3", "x = 4 and x = 3", "A",
          "x² − 4x + 3 = (x−1)(x−3) = 0 → x = 1 or x = 3.")

        q(fun, H,
          "If f(x) = 2x + 1 and g(x) = x², what is f(g(3))?",
          "13", "19", "25", "10", "B",
          "g(3) = 9; f(9) = 2(9) + 1 = 19.")

        q(fun, H,
          "The function h(x) = −(x + 2)² + 5. What is the maximum value of h(x)?",
          "2", "4", "5", "7", "C",
          "Maximum is at the vertex: h(−2) = −(0) + 5 = 5.")

        q(fun, H,
          "A linear function f satisfies f(0) = 3 and f(4) = 11. What is f(−2)?",
          "−1", "0", "1", "−2", "A",
          "Slope = (11−3)/(4−0) = 2. f(x) = 2x + 3. f(−2) = 2(−2) + 3 = −1.")

        q(geo, H,
          "A circle has center (2, −1) and passes through the point (5, 3). What is the "
          "radius of the circle?",
          "4", "5", "6", "7", "B",
          "r = √((5−2)² + (3−(−1))²) = √(9 + 16) = √25 = 5.")

        q(geo, H,
          "Two parallel lines are cut by a transversal. One angle measures 3x + 10 and its "
          "corresponding angle measures 5x − 30. What is the value of x?",
          "10", "15", "20", "25", "C",
          "Corresponding angles are equal: 3x + 10 = 5x − 30 → 40 = 2x → x = 20.")

        q(geo, H,
          "A cylinder has radius 3 and height 10. What is its volume? (Use π ≈ 3.14)",
          "94.2", "188.4", "282.6", "376.8", "C",
          "V = πr²h = 3.14 × 9 × 10 = 282.6.")

        q(geo, H,
          "The diagonal of a square is 8√2. What is the area of the square?",
          "32", "48", "64", "128", "C",
          "Diagonal = s√2 = 8√2 → s = 8. Area = 8² = 64.")

        q(dsp, H,
          "The mean of five numbers is 16. Four of the numbers are 12, 14, 17, and 19. "
          "What is the fifth number?",
          "14", "16", "18", "20", "C",
          "Sum = 16 × 5 = 80; 12+14+17+19 = 62; fifth = 80 − 62 = 18.")

        q(dsp, H,
          "A fair six-sided die is rolled twice. What is the probability that both rolls "
          "show an even number?",
          "1/4", "1/3", "1/2", "2/3", "A",
          "P(even on one roll) = 3/6 = 1/2. P(both even) = 1/2 × 1/2 = 1/4.")

        q(dsp, H,
          "A data set has a mean of 50 and a standard deviation of 5. A new data set is "
          "created by adding 10 to every value. What are the mean and standard deviation "
          "of the new data set?",
          "Mean = 50, SD = 15", "Mean = 60, SD = 5",
          "Mean = 60, SD = 15", "Mean = 50, SD = 5", "B",
          "Adding a constant shifts the mean by that constant (50+10=60) but does not change the spread (SD stays 5).")

        q(dsp, H,
          "In a class, 40% of students play sports, 30% play instruments, and 15% do "
          "both. What percent of students do neither?",
          "25%", "30%", "35%", "45%", "D",
          "Sports or instruments = 40 + 30 − 15 = 55%. Neither = 100 − 55 = 45%.")

        q(dsp, H,
          "Ten employees' ages are: 22, 25, 28, 31, 35, 38, 42, 47, 51, 58. A new "
          "employee aged 22 joins. What is the median age of the group now?",
          "31", "33", "35", "38", "C",
          "New sorted list (11 values): 22,22,25,28,31,35,38,42,47,51,58. Median = 6th value = 35.")

        q(wp, H,
          "A store sells apples for $2 each and oranges for $3 each. A customer spent "
          "$26 buying 10 pieces of fruit total. How many apples did the customer buy?",
          "2", "4", "6", "8", "B",
          "a + o = 10, 2a + 3o = 26. Substituting: 2a + 3(10−a) = 26 → −a = −4 → a = 4.")

        q(wp, H,
          "A tank fills at 3 gallons per minute and drains at 1.5 gallons per minute. "
          "Starting empty, how many minutes to fill a 90-gallon tank?",
          "30", "45", "60", "90", "C",
          "Net fill rate = 3 − 1.5 = 1.5 gal/min. Time = 90 ÷ 1.5 = 60 minutes.")

        q(wp, H,
          "A jacket was reduced by 20%, then the sale price was reduced by another 10%. "
          "If the final price was $108, what was the original price?",
          "$140", "$145", "$150", "$160", "C",
          "Final = original × 0.80 × 0.90 = 0.72 × original = $108. Original = $108 ÷ 0.72 = $150.")

        q(wp, H,
          "Two trains start from cities 300 miles apart and travel toward each other. "
          "Train A travels at 60 mph and Train B at 90 mph. How many hours until they meet?",
          "1", "2", "3", "4", "B",
          "Combined speed = 60 + 90 = 150 mph. Time = 300 ÷ 150 = 2 hours.")

        count = Question.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {count} total questions in database '
            f'({Question.objects.filter(subject=english).count()} English, '
            f'{Question.objects.filter(subject=math).count()} Math)'
        ))
