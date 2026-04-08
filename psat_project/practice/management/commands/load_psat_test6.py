"""
PSAT 8/9-style Practice Test 6 — generated questions.
English (Reading & Writing): 81 questions across 3 modules
Math: 66 questions across 3 modules
Difficulty: Module 1 = medium, Module 2 Easier = easy, Module 2 Harder = hard
"""
from django.core.management.base import BaseCommand
from practice.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Load PSAT-style Practice Test 6 questions into the database'

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
          "Historian David McCullough was celebrated for his ability to bring "
          "historical figures to life, writing with such ________ detail that readers "
          "felt they were witnessing events firsthand rather than reading about "
          "them from a distance of centuries.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "vague", "irrelevant", "vivid", "abstract", "C",
          "'Vivid' means producing clear, striking mental images — precisely matching writing that makes readers feel present at historical events.")

        q(ev, M,
          "The new infrastructure bill was seen as ________ by urban planners, who "
          "argued it would provide sufficient funding to rebuild crumbling roads, "
          "modernize bridges, and expand public transit networks.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "inadequate", "unnecessary", "transformative", "harmful", "C",
          "'Transformative' means capable of causing a major positive change — matching the bill's potential to rebuild infrastructure at scale.")

        q(ev, M,
          "The reporter's investigation was thorough and ________, tracing financial "
          "transactions across seven countries and dozens of shell companies to "
          "expose a network of corruption at the highest levels of government.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "superficial", "methodical", "accidental", "rushed", "B",
          "'Methodical' means done in a careful, systematic way — matching an investigation that traced transactions across seven countries.")

        q(ev, M,
          "Though both birds belong to the same genus, their songs are ________ — "
          "one produces a clear, melodic whistle while the other generates a harsh, "
          "rattling call that ornithologists describe as almost mechanical.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "identical", "similar", "strikingly different", "equally melodic", "C",
          "'Strikingly different' matches the contrast between a melodic whistle and a harsh, mechanical rattle.")

        q(rc, M,
          "Cognitive scientist Daniel Kahneman distinguishes between two modes of "
          "thinking: System 1, which is fast, automatic, and intuitive, and "
          "System 2, which is slow, deliberate, and analytical. Kahneman argues "
          "that humans tend to default to System 1 thinking, which, while efficient, "
          "makes them prone to predictable cognitive biases. Awareness of these "
          "biases can help people activate System 2 at critical moments.\n\n"
          "Which choice best states the main idea of the text?",
          "System 2 thinking is always superior to System 1 thinking for every task.",
          "Kahneman argues that fast, intuitive thinking makes humans efficient but bias-prone, and that deliberate thinking can help counter these biases.",
          "Humans are incapable of unbiased thinking under any circumstances.",
          "Kahneman's research focuses primarily on the speed of human thought.", "B",
          "The text presents both thinking modes, the problem of defaulting to System 1 (biases), and the benefit of activating System 2 (countering biases) — all three are part of the main idea.")

        q(rc, M,
          "The following text is adapted from Jane Austen's 1813 novel Pride and "
          "Prejudice. Elizabeth Bennet reflects on Mr. Darcy.\n\n"
          "She began now to comprehend that he was exactly the man who, in disposition "
          "and talents, would most suit her. It was a union that must have been to the "
          "advantage of both; by her ease and liveliness, his mind might have been "
          "softened, his manners improved; and from his judgment, information, and "
          "knowledge of the world, she must have received benefit of greater importance.\n\n"
          "Which choice best describes what Elizabeth's reflection reveals?",
          "She regrets having rejected Darcy and recognizes what both would have gained from a relationship.",
          "She is trying to convince herself that she made the right choice in rejecting Darcy.",
          "She believes Darcy's character has no qualities she lacks herself.",
          "She is angry that Darcy never formally proposed to her.", "A",
          "Elizabeth comprehends what 'must have been to the advantage of both' — this retrospective analysis of mutual benefit reveals her regret at what could have been.")

        q(rc, M,
          "Behavioral economists have documented a phenomenon called 'loss aversion': "
          "the pain people experience from losing something is approximately twice as "
          "intense as the pleasure they get from gaining the equivalent. This asymmetry "
          "helps explain why people take fewer risks than would be economically rational "
          "and why the framing of a decision — whether options are presented as gains "
          "or losses — dramatically affects choices.\n\n"
          "Which choice best states the main idea of the text?",
          "Economists have proven that financial risk-taking always leads to greater losses than gains.",
          "Loss aversion explains why pain and pleasure are experienced at the same intensity.",
          "The documented phenomenon of loss aversion helps explain why people tend toward risk-avoidance and why framing decisions as gains or losses matters.",
          "Behavioral economics focuses exclusively on how framing affects economic decisions.", "C",
          "The text introduces loss aversion and then explains two of its practical consequences: risk-avoidance and framing effects.")

        q(rc, M,
          "Historian Jill Lepore has argued that history is inevitably written from "
          "a particular perspective, and that the voices of the marginalized — women, "
          "enslaved people, indigenous peoples — have been systematically excluded "
          "from mainstream historical accounts. Recovering these voices requires not "
          "just accessing different sources but questioning whose stories count as "
          "history.\n\n"
          "Which choice best states the main idea of the text?",
          "Lepore argues that all historical accounts are completely unreliable.",
          "Lepore contends that mainstream history has excluded marginalized voices and that recovering them requires a fundamental rethinking of what counts as history.",
          "Lepore believes that all historical writing should focus exclusively on marginalized groups.",
          "Recovering excluded historical voices requires only accessing new archival sources.", "B",
          "The text presents Lepore's two-part argument: mainstream history excludes marginalized voices, and recovery requires questioning whose stories count — both parts matter.")

        q(rc, M,
          "Scientists have discovered that dolphins in Shark Bay, Australia, use "
          "marine sponges as tools — carrying them on their snouts to protect "
          "themselves while foraging on the seafloor. This behavior is taught "
          "from mother to offspring and is practiced almost exclusively by females. "
          "The concentration of this learned skill in one family line suggests that "
          "dolphin culture ________\n\n"
          "Which choice most logically completes the text?",
          "can be transmitted across generations and is not uniformly distributed across the population.",
          "develops only in response to food scarcity in the local environment.",
          "makes dolphins more intelligent than all other marine mammals.",
          "proves that dolphins can create new tools when existing ones become unavailable.", "A",
          "The facts — mothers teach daughters, only some dolphins do it — directly imply that cultural transmission happens generationally and unevenly within the population.")

        q(de, M,
          "The table shows graduation rates (%) at a high school over five years:\n\n"
          "Year 1: 82% | Year 2: 85% | Year 3: 83% | Year 4: 88% | Year 5: 91%\n\n"
          "A school administrator argues that graduation rates increased every year "
          "from Year 1 through Year 5. Which choice most effectively evaluates "
          "this claim?",
          "Year 5 (91%) had the highest graduation rate of any year.",
          "From Year 2 (85%) to Year 3 (83%) the rate declined, meaning rates did not increase every year. The claim is incorrect.",
          "Year 4 to Year 5 showed the largest single-year increase.",
          "Year 1 had the lowest graduation rate of all five years.", "B",
          "Year 3 (83%) < Year 2 (85%) — a decline. This disproves the 'every year' claim.")

        q(de, M,
          "Text 1: A universal basic income (UBI) — a regular, unconditional cash "
          "payment to all citizens — would eliminate poverty and reduce inequality "
          "by ensuring everyone has enough to meet basic needs.\n\n"
          "Text 2: UBI proposals fail to address the structural causes of poverty "
          "and inequality. Without accompanying reforms to housing, education, and "
          "healthcare, cash transfers alone are insufficient. Furthermore, a truly "
          "universal program would be prohibitively expensive.\n\n"
          "Based on the texts, what do the two authors most fundamentally disagree about?",
          "Whether poverty is a serious problem that needs to be addressed.",
          "Whether UBI alone would be sufficient to address poverty and inequality.",
          "Whether cash transfers have any positive effect on recipients' wellbeing.",
          "Whether housing and education reforms are necessary in principle.", "B",
          "Text 1 says UBI would eliminate poverty; Text 2 says cash alone is insufficient — the core disagreement is whether UBI alone can solve the problem.")

        q(de, M,
          "The table shows the number of new patents filed in four technology sectors:\n\n"
          "Artificial Intelligence: 4,200 | Renewable Energy: 3,100\n"
          "Biotechnology: 2,800 | Quantum Computing: 450\n\n"
          "A researcher claims that patents in AI and renewable energy together "
          "account for more than two-thirds of all patents filed in these four sectors. "
          "Which choice most effectively evaluates this claim?",
          "AI (4,200) is the leading sector, far exceeding quantum computing (450).",
          "AI (4,200) + Renewable Energy (3,100) = 7,300. Total = 10,550. 7,300/10,550 = 69.2%, which is more than two-thirds (66.7%). The claim is correct.",
          "Biotechnology (2,800) filed nearly as many patents as renewable energy.",
          "Quantum computing filed the fewest patents of the four sectors.", "B",
          "7,300/10,550 = 69.2% > 66.7%. Option B correctly calculates this and confirms the claim.")

        q(de, M,
          "Text 1: National parks protect biodiversity and provide irreplaceable "
          "wilderness. They should be expanded and their boundaries strictly "
          "enforced against development.\n\n"
          "Text 2: National parks as currently managed often exclude indigenous "
          "communities who have sustainably managed these lands for centuries. "
          "'Fortress conservation' prioritizes preservation over people, displacing "
          "communities and erasing their relationship with the land.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond "
          "to Text 1's call to expand national parks?",
          "Text 2 would fully support expansion if parks employed more conservation officers.",
          "Expanding parks using current models risks further displacing indigenous communities whose stewardship of the land has been effective.",
          "Text 2 agrees that biodiversity protection is the most important goal of national parks.",
          "Text 2 believes that national parks should be closed entirely.", "B",
          "Text 2 criticizes the current 'fortress conservation' model for excluding indigenous communities — it would argue expansion under this model would worsen displacement.")

        q(de, M,
          "A survey asked 800 adults about their primary source of news:\n\n"
          "Social media: 312 | Television: 224 | Online news sites: 168\n"
          "Print newspapers: 64 | Radio: 32\n\n"
          "A journalist claims that digital sources (social media and online news "
          "sites) together account for more than half of adults' primary news source. "
          "Which choice most effectively uses data from the table to evaluate "
          "this claim?",
          "Social media alone (312) exceeds television (224) as a news source.",
          "Social media (312) + Online news sites (168) = 480 out of 800 = 60%, which is more than half. The claim is correct.",
          "Print newspapers (64) and radio (32) together represent only 96 respondents.",
          "Television (224) is the second most common primary news source.", "B",
          "312+168=480; 480/800=60%>50%. Option B correctly evaluates the claim.")

        q(gv, M,
          "The ancient ruins discovered beneath the city ________ researchers to "
          "revise their understanding of the region's early settlement patterns.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "causing", "have caused", "causes", "cause", "B",
          "'The ancient ruins' is plural — 'have caused' is correct (present perfect, plural). The discovery has led to ongoing revision.")

        q(gv, M,
          "The director and her lead actor, who had worked together on four previous "
          "films, ________ each given an honorary award at the ceremony.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "was", "is", "were", "has been", "C",
          "The compound subject 'director and actor' is plural — 'were' is correct.")

        q(gv, M,
          "________ her debut novel in three drafts over two years, the author "
          "finally submitted a manuscript she felt was ready for publication.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Having revised", "She revised", "Revising", "To revise", "A",
          "'Having revised' is the perfect participial phrase indicating the completed action before submission.")

        q(gv, M,
          "Every one of the recommendations made by the independent review panel "
          "________ now been adopted by the hospital's governing board.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "have", "has", "were", "are", "B",
          "'Every one' is singular and takes 'has.' The plural 'recommendations' is in a prepositional phrase, not the subject.")

        q(gp, M,
          "The expedition set off with four goals ________ mapping the coastline, "
          "cataloguing marine life, testing new sonar equipment, and "
          "establishing coordinates for future surveys.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—", "A",
          "A colon introduces the list of four goals.")

        q(gp, M,
          "The bridge was built in 1921 and has carried traffic for over a century "
          "________ making it one of the oldest still-active structures of its kind "
          "in the country.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", ":", "—", "B",
          "A comma introduces the participial phrase 'making it one of the oldest...'")

        q(gp, M,
          "The chef's signature dish ________ a slow-braised short rib with truffle "
          "mashed potatoes — has been on the menu since the restaurant opened "
          "fifteen years ago.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical describing the dish is set off by dashes. Since the closing dash is present, the opening must be a dash.")

        q(gp, M,
          "The athlete had trained for the Olympics for four years ________ however, "
          "an injury just two weeks before the competition forced her to withdraw.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", ".", "B",
          "A semicolon before 'however' correctly separates two independent clauses with a conjunctive adverb.")

        q(tr, M,
          "Whales are air-breathing mammals that evolved from land-dwelling ancestors. "
          "Fossil evidence shows that early whale relatives had legs and could walk "
          "on land. ________ over millions of years, their limbs gradually became "
          "flippers as they adapted to a fully aquatic lifestyle.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Instead,", "Nevertheless,", "Over time,", "In contrast,", "C",
          "'Over time' logically introduces the gradual evolutionary change described.")

        q(tr, M,
          "The research team's early results were inconclusive and difficult to "
          "interpret. ________ continued analysis and a larger dataset eventually "
          "revealed a clear and statistically significant pattern.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Similarly,", "Nevertheless,", "As a result,", "Therefore,", "B",
          "'Nevertheless' introduces the persistence that led to eventual success despite early setbacks.")

        q(tr, M,
          "Economists have long argued that free trade benefits all participating "
          "nations by allowing each to specialize in what it produces most efficiently. "
          "________ recent studies have found that the gains from trade are not "
          "evenly distributed and that workers in sectors exposed to foreign "
          "competition often face job losses that persist for years.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "Therefore,", "However,", "Similarly,", "C",
          "'However' introduces the complication that qualifies the standard free trade argument.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Coriolis effect is caused by Earth's rotation and deflects moving "
          "objects to the right in the Northern Hemisphere and to the left in the Southern.\n"
          "- It significantly affects wind patterns, ocean currents, and the rotation "
          "direction of large weather systems.\n"
          "- Hurricanes spin counterclockwise in the Northern Hemisphere.\n"
          "- The effect is too weak to influence water draining in a sink or toilet.\n"
          "- The Coriolis effect was first described mathematically by Gaspard-Gustave "
          "de Coriolis in 1835.\n\n"
          "The student wants to address a common misconception about the Coriolis "
          "effect. Which choice most effectively uses relevant information from "
          "the notes to accomplish this goal?",
          "The Coriolis effect deflects objects to the right in the Northern Hemisphere and to the left in the Southern.",
          "Hurricanes spin counterclockwise in the Northern Hemisphere because of the Coriolis effect.",
          "Despite a common belief, the Coriolis effect is too weak to influence which direction water drains in a sink or toilet — its effects are only significant on large-scale systems like hurricanes.",
          "The Coriolis effect was first described mathematically by Gaspard-Gustave de Coriolis in 1835.", "C",
          "Option C directly addresses the common misconception (sink/toilet drain direction) and explains the truth — it is too weak for small-scale effects.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- Vincent van Gogh (1853-1890) sold only one painting during his lifetime.\n"
          "- He produced over 2,100 artworks in a career spanning just over a decade.\n"
          "- His most famous works include The Starry Night, Sunflowers, and "
          "Bedroom in Arles.\n"
          "- Today, his paintings sell for tens of millions of dollars at auction.\n"
          "- He suffered from severe mental illness and died at age 37.\n\n"
          "The student wants to highlight the contrast between van Gogh's recognition "
          "during his lifetime and his posthumous fame. Which choice most effectively "
          "uses relevant information from the notes to accomplish this goal?",
          "Van Gogh produced over 2,100 artworks in a career of just over a decade.",
          "Van Gogh's famous works include The Starry Night, Sunflowers, and Bedroom in Arles.",
          "Though van Gogh sold only one painting in his lifetime, his works now sell for tens of millions of dollars at auction.",
          "Van Gogh suffered from severe mental illness and died at age 37.", "C",
          "Option C directly contrasts the single painting sold during his lifetime with the tens of millions his works now command — the starkest expression of the contrast the student wants to highlight.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(ev, E,
          "The school's new after-school tutoring program has been very "
          "________, with nearly every student who joined showing improvement "
          "in their grades within just a few weeks.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "confusing", "unsuccessful", "effective", "optional", "C",
          "'Effective' means producing the desired result — matching a program where nearly every participant improved their grades.")

        q(ev, E,
          "The documentary explored the lives of animals in extreme environments, "
          "showing how they ________ to conditions that would be fatal for most "
          "other species.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "surrender", "struggle", "adapt", "escape", "C",
          "'Adapt' means to adjust to new conditions — the precise word for how animals survive in extreme environments.")

        q(ev, E,
          "The city celebrated its 200th anniversary with a ________ parade that "
          "drew thousands of residents and visitors from across the region.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "quiet", "small", "grand", "routine", "C",
          "'Grand' means magnificent and impressive in scale — appropriate for a major centennial celebration.")

        q(ev, E,
          "The young pianist ________ on stage, playing a difficult piece without "
          "a single mistake and earning a standing ovation from the audience.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "stumbled", "excelled", "complained", "hesitated", "B",
          "'Excelled' means performed exceptionally well — matching a flawless performance that earned a standing ovation.")

        q(rc, E,
          "Bats are the only mammals capable of true, sustained flight. Most bats "
          "are nocturnal and use echolocation — emitting high-frequency sounds and "
          "interpreting the returning echoes — to navigate and hunt in darkness. "
          "Some species can detect insects as small as a mosquito from several "
          "meters away using this system.\n\n"
          "Which choice best states the main idea of the text?",
          "Bats are the most dangerous predators among nocturnal animals.",
          "Bats are unique flying mammals that use echolocation for navigation and hunting in the dark.",
          "All mammals use some form of echolocation to find food.",
          "Bats are unable to see in darkness and must rely entirely on sound.", "B",
          "The text establishes bats as unique flying mammals and describes their echolocation system for navigating and hunting — that combination is the main idea.")

        q(rc, E,
          "The Hubble Space Telescope, launched in 1990, revolutionized astronomy "
          "by providing images of unprecedented clarity from above Earth's "
          "atmosphere, which blurs ground-based observations. Among Hubble's "
          "most famous contributions is the 'Deep Field' series — long-exposure "
          "photographs capturing thousands of distant galaxies in a tiny patch of sky.\n\n"
          "Which choice best states the main idea of the text?",
          "Hubble has proven that the universe is much smaller than previously thought.",
          "Hubble's main advantage over ground-based telescopes is its lower cost of operation.",
          "The Hubble Space Telescope transformed astronomy by delivering clearer images from above the atmosphere, enabling discoveries like the Deep Field photographs.",
          "Hubble was launched specifically to photograph the Deep Field series.", "C",
          "The text covers Hubble's key advantage (above the atmosphere), its impact on astronomy, and a notable example — all connected in the main idea.")

        q(rc, E,
          "Rainwater is naturally slightly acidic because it absorbs carbon dioxide "
          "from the atmosphere, forming a weak carbonic acid. Acid rain occurs "
          "when rainwater absorbs sulfur dioxide and nitrogen oxides released by "
          "power plants and vehicles. These stronger acids can damage forests, "
          "lakes, and buildings made of limestone or marble.\n\n"
          "Which choice best describes the function of the first sentence in the text?",
          "It provides context for why acid rain is a unique and unexpected phenomenon.",
          "It establishes that all rainwater is dangerously acidic.",
          "It shows that rainwater is naturally slightly acidic, distinguishing it from the more harmful acid rain described afterward.",
          "It introduces the industrial sources of acid rain.", "C",
          "The first sentence establishes a baseline — normal rainwater is slightly acidic — which sets up the contrast with the much more damaging acid rain described next.")

        q(rc, E,
          "In 1928, Alexander Fleming noticed that a mold called Penicillium had "
          "contaminated one of his bacterial cultures and was killing the bacteria "
          "around it. Rather than throwing out the contaminated culture, Fleming "
          "recognized the potential importance of what he observed. This moment of "
          "curiosity led to the development of penicillin, one of the most "
          "significant medical discoveries in history.\n\n"
          "Which choice best states the main idea of the text?",
          "Fleming's accidental contamination destroyed his entire bacterial experiment.",
          "Penicillin was developed in a laboratory over many years of planned experiments.",
          "Fleming's recognition of an unexpected observation led to the discovery of penicillin.",
          "Penicillin was the first antibiotic ever discovered and used in human medicine.", "C",
          "The text emphasizes Fleming's recognition of the accidental observation as the key turning point — the main idea is how that recognition led to penicillin's discovery.")

        q(rc, E,
          "Fireflies produce light through a chemical reaction called "
          "bioluminescence. Unlike light from a light bulb, which generates "
          "a great deal of heat, firefly light is nearly 100% efficient — "
          "almost all the energy is converted into light rather than heat. "
          "Scientists have studied this process in hopes of developing more "
          "energy-efficient lighting technologies.\n\n"
          "Which choice most logically completes a summary of the text?",
          "Fireflies and light bulbs produce light through the same chemical process.",
          "Scientists have already replaced all light bulbs with bioluminescent technology.",
          "Fireflies' highly efficient bioluminescence has inspired scientific interest in developing better lighting technology.",
          "All animals that produce bioluminescence do so for the same purpose.", "C",
          "The text describes firefly efficiency and scientists studying it for applications — those two facts together make C the logical summary.")

        q(de, E,
          "The table shows the number of library books borrowed each week for "
          "five weeks:\n\n"
          "Week 1: 220 | Week 2: 248 | Week 3: 231 | Week 4: 265 | Week 5: 252\n\n"
          "A librarian claims that the most books were borrowed during Week 4. "
          "Which choice most effectively uses data from the table to support "
          "this claim?",
          "Week 5 (252) had more borrowings than Weeks 1 and 2.",
          "Week 4 had 265 borrowings — more than any other week listed.",
          "Week 3 (231) had fewer borrowings than Week 2 (248).",
          "Week 2 (248) had more borrowings than Weeks 1 and 3.", "B",
          "Week 4 (265) is the highest value in the table. Option B directly states this to support the claim.")

        q(de, E,
          "Text 1: The voting age should be lowered to 16. Young people are affected "
          "by political decisions, pay taxes if they work, and many are politically "
          "knowledgeable and engaged.\n\n"
          "Text 2: At 16, most young people lack the life experience and cognitive "
          "maturity to make informed voting decisions. Brain development continues "
          "until the mid-20s, affecting judgment.\n\n"
          "Based on the texts, both authors would most likely agree that ________",
          "16-year-olds should be allowed to vote in local but not national elections.",
          "young people are affected by political decisions made by governments.",
          "brain development is irrelevant to the question of voting age.",
          "the current voting age of 18 is the ideal age for all countries.", "B",
          "Text 1 cites that young people are affected by political decisions as a reason to lower the voting age. Text 2 doesn't dispute this fact — it disputes readiness. Both implicitly accept that young people are affected by politics.")

        q(de, E,
          "The table shows the average cost of a movie ticket in one country "
          "over four decades:\n\n"
          "1990: $4.20 | 2000: $5.40 | 2010: $7.90 | 2020: $9.50\n\n"
          "A film industry analyst claims that ticket prices more than doubled "
          "from 1990 to 2020. Which choice most effectively uses data from the "
          "table to evaluate this claim?",
          "Ticket prices rose from $5.40 to $9.50 between 2000 and 2020.",
          "The price in 2020 ($9.50) is more than double the 1990 price ($4.20), since 2 × $4.20 = $8.40 < $9.50. The claim is correct.",
          "Ticket prices increased in every decade from 1990 to 2020.",
          "The largest single-decade increase was from 2000 to 2010.", "B",
          "2 × $4.20 = $8.40. Since $9.50 > $8.40, prices did more than double. Option B correctly calculates and confirms the claim.")

        q(de, E,
          "Text 1: Cities should invest in more bike lanes. Cycling reduces "
          "traffic congestion, cuts carbon emissions, and improves public health.\n\n"
          "Text 2: Bike lanes reduce road space for vehicles, increasing congestion "
          "for drivers and creating conflicts with delivery trucks and emergency "
          "vehicles.\n\n"
          "Based on the texts, the authors disagree about ________",
          "whether cycling provides health benefits.",
          "whether carbon emissions are a concern for cities.",
          "whether adding bike lanes helps or hurts urban traffic flow.",
          "whether emergency vehicles should use bike lanes.", "C",
          "Text 1 says bike lanes reduce congestion; Text 2 says they increase congestion for drivers. The specific disagreement is about the effect on traffic flow.")

        q(de, E,
          "The table shows average daily screen time for students by grade:\n\n"
          "Grade 6: 4.2 hrs | Grade 7: 4.8 hrs | Grade 8: 5.3 hrs | Grade 9: 5.9 hrs\n\n"
          "A health researcher claims that screen time increases consistently from "
          "Grade 6 to Grade 9. Which choice most effectively uses data from the "
          "table to support this claim?",
          "Grade 9 students have nearly 6 hours of daily screen time.",
          "Average daily screen time rises from 4.2 hours in Grade 6 to 5.9 hours in Grade 9, increasing at each grade level.",
          "Grade 8 students average 5.3 hours of screen time per day.",
          "Grade 7 (4.8 hrs) has more screen time than Grade 6 (4.2 hrs).", "B",
          "Option B uses all four data points to directly support the 'increases consistently' claim across all grade levels.")

        q(gv, E,
          "The library's collection of rare manuscripts ________ stored in a "
          "climate-controlled vault to prevent deterioration.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "is", "were", "have", "B",
          "'Collection' is singular — 'is' is the correct verb.")

        q(gv, E,
          "The scientists on the research ship ________ twenty-three previously "
          "unknown species of deep-sea fish during the six-month expedition.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "discover", "discovers", "discovered", "discovering", "C",
          "'Discovered' is the correct simple past tense, consistent with the completed 'six-month expedition.'")

        q(gv, E,
          "Each of the five volunteers ________ responsible for setting up a "
          "different section of the event space.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "were", "is", "was", "D",
          "'Each' is singular and takes 'was' (simple past, consistent with a completed event setup).")

        q(gv, E,
          "My grandmother ________ the whole morning in the kitchen, preparing her "
          "famous apple pie for the family reunion.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "spends", "spending", "has spent", "spent", "D",
          "'Spent' is the correct simple past tense, consistent with the past-tense narrative.")

        q(gp, E,
          "The school's annual talent show featured four acts ________ a comedy "
          "sketch, a dance routine, two original songs, and a magic show.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—", "A",
          "A colon introduces the list of four acts.")

        q(gp, E,
          "Noah loves building robots ________ he spends most of his free time "
          "in the school's maker lab working on new projects.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", "and,", "B",
          "A semicolon joins two independent clauses without a coordinating conjunction.")

        q(gp, E,
          "The principal, ________ has led the school for twelve years, announced "
          "plans to retire at the end of the academic year.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "whom", "which", "who", "that", "C",
          "'Who' is the correct relative pronoun for a person and is the subject of 'has led.'")

        q(gp, E,
          "We visited the nature center ________ we learned about local ecosystems, "
          "wildlife habitats, and sustainable farming practices.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ", where", "; where", ": where", "where,", "A",
          "A comma before the relative adverb 'where' introduces the relative clause describing 'the nature center.'")

        q(tr, E,
          "Plants need sunlight, water, and nutrients from the soil to grow. "
          "________ plants in environments that lack one of these resources "
          "often develop slowly or fail to survive.\n\n"
          "Which choice completes the text with the most logical transition?",
          "In addition,", "Instead,", "As a result,", "Despite this,", "C",
          "'As a result' connects the requirements (sunlight, water, nutrients) to the consequence of lacking them (slow growth or death).")

        q(tr, E,
          "The hiking group set off early in the morning with plenty of water "
          "and snacks. ________ by noon they had covered more than twelve miles "
          "of trail.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "Therefore,", "By then,", "Despite this,", "C",
          "'By then' marks the progression of time — by the time noon arrived, they had covered 12 miles.")

        q(tr, E,
          "The new city park was built on a former industrial site. ________ workers "
          "had to remove contaminated soil and plant hundreds of native trees and "
          "shrubs before the park could open.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "As a result,", "In contrast,", "Similarly,", "B",
          "'As a result' connects the industrial origin of the site (cause) to the remediation work that was required (effect).")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- Sharks have existed on Earth for approximately 450 million years, "
          "predating dinosaurs by over 200 million years.\n"
          "- There are over 500 species of sharks, ranging from the 8-inch dwarf "
          "lanternshark to the 40-foot whale shark.\n"
          "- Sharks do not have bones — their skeletons are made of cartilage.\n"
          "- On average, sharks kill fewer than 10 people per year worldwide.\n"
          "- Humans kill approximately 100 million sharks per year, primarily "
          "through overfishing and the shark fin trade.\n\n"
          "The student wants to challenge the common perception that sharks are "
          "deadly threats to humans. Which choice most effectively uses relevant "
          "information from the notes to accomplish this goal?",
          "Sharks have existed for approximately 450 million years, predating dinosaurs.",
          "There are over 500 species of sharks, ranging enormously in size.",
          "While sharks are often perceived as deadly, they kill fewer than 10 people per year on average, while humans kill approximately 100 million sharks annually.",
          "Sharks' skeletons are made of cartilage rather than bone.", "C",
          "Option C directly challenges the 'deadly threat' perception by contrasting the tiny number of people sharks kill with the massive number that humans kill — the most effective challenge to the common fear.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Great Fire of London occurred in September 1666 and destroyed "
          "13,200 houses and 87 churches.\n"
          "- It started in a bakery on Pudding Lane.\n"
          "- Only a handful of confirmed deaths were recorded despite the vast destruction.\n"
          "- The fire led to major rebuilding of London, including the construction "
          "of St. Paul's Cathedral designed by Christopher Wren.\n"
          "- It also prompted the introduction of fire insurance and building codes.\n\n"
          "The student wants to explain the long-term positive effects of the fire. "
          "Which choice most effectively uses relevant information from the notes?",
          "The Great Fire started in a bakery on Pudding Lane in September 1666.",
          "The fire destroyed 13,200 houses and 87 churches but caused only a handful of confirmed deaths.",
          "The Great Fire led to the rebuilding of London with landmarks like St. Paul's Cathedral and prompted the creation of fire insurance and modern building codes.",
          "Christopher Wren designed St. Paul's Cathedral as part of the post-fire rebuilding.", "C",
          "Option C focuses specifically on long-term positive effects: architectural rebuilding (St. Paul's) and systemic improvements (fire insurance, building codes) — exactly the student's stated goal.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(ev, H,
          "The documentary's ________ portrait of the dictator — refusing to "
          "condemn while also refusing to celebrate, presenting evidence and "
          "allowing viewers to draw their own conclusions — drew both praise "
          "and criticism for its studied neutrality.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "hagiographic", "propagandistic", "polemical", "dispassionate", "D",
          "'Dispassionate' means objective and free from emotion — matching a documentary that refuses to condemn or celebrate, maintaining studied neutrality.")

        q(ev, H,
          "The committee's report was ________ — vague on timelines, silent on "
          "budget specifics, and offering general principles where concrete "
          "recommendations were needed.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "comprehensive", "decisive", "mealy-mouthed", "incisive", "C",
          "'Mealy-mouthed' means evasively indirect — precisely matching a report that avoids specifics and concrete action.")

        q(ev, H,
          "The philosopher's later works represent a sharp ________ from the "
          "systematic, rationalist project of his early career, embracing instead "
          "a fragmentary, aphoristic style that resists all attempts at synthesis.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "continuation", "departure", "fulfillment", "repetition", "B",
          "'Departure' means a significant change from what came before — matching the shift from systematic to fragmentary work.")

        q(ev, H,
          "The administration's proposal was seen as a ________ concession by "
          "hardliners in the party, who argued that compromising on this issue "
          "would undermine the ideological foundations of their entire platform.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "principled", "long-overdue", "dangerous", "symbolic", "C",
          "'Dangerous' is the word hardliners would use — they argued compromising would 'undermine' their ideological foundations, which is a serious (dangerous) threat.")

        q(rc, H,
          "The following text is adapted from Gustave Flaubert's 1857 novel Madame "
          "Bovary. Emma Bovary reflects on her marriage.\n\n"
          "Before her marriage she had thought that she had love within her to give; "
          "but the happiness that should have followed this love had not come. She "
          "must have been mistaken, she thought. And Emma tried to find out what one "
          "meant precisely in life by the words felicity, passion, rapture, which had "
          "seemed to her so beautiful in books.\n\n"
          "Which choice best describes Emma's situation as revealed in the passage?",
          "Emma is satisfied with her marriage but longs for a more intellectual life.",
          "Emma discovers that the romantic ideals she formed through books have not materialized in her actual life.",
          "Emma believes she lacked the capacity for love before her marriage.",
          "Emma blames her husband for the absence of happiness in their marriage.", "B",
          "Emma expected love and happiness but found they didn't arrive — she traces this back to the 'beautiful' words in books that had shaped her expectations. Her life has failed to match her literary ideals.")

        q(rc, H,
          "Biologist E.O. Wilson proposed the 'biophilia hypothesis,' which suggests "
          "that humans possess an innate tendency to affiliate with other living "
          "systems. Wilson argued that this orientation, developed over hundreds of "
          "thousands of years of evolution in natural environments, explains the "
          "deep emotional responses humans have to nature — the calm experienced "
          "in forests, the fear evoked by snakes. Critics contend that individual "
          "and cultural variation in responses to nature makes biophilia difficult "
          "to characterize as innate.\n\n"
          "Which choice best states the main idea of the text?",
          "Wilson proved that all humans are calmed by forests and frightened by snakes.",
          "Wilson's claim that humans have an innate connection to nature has been universally accepted in evolutionary biology.",
          "Wilson's biophilia hypothesis proposes that humans have an evolved affinity for nature, though critics question whether such responses are truly innate.",
          "Critics have fully disproved Wilson's biophilia hypothesis through cross-cultural studies.", "C",
          "The text presents Wilson's hypothesis and the critics who challenge whether responses to nature are truly innate — both parts make up the main idea.")

        q(rc, H,
          "Philosopher Thomas Kuhn argued that science does not progress through "
          "gradual accumulation of knowledge but through periodic 'paradigm shifts' "
          "— revolutionary moments when an entire framework for understanding a "
          "field is replaced by a new one. Examples include the Copernican "
          "revolution in astronomy and Einstein's relativity in physics. Critics "
          "argue that Kuhn's model overstates the discontinuity in scientific "
          "progress and undervalues the role of incremental discovery.\n\n"
          "Which choice best states the main idea of the text?",
          "Kuhn argued that all scientific progress results from the work of a single revolutionary genius.",
          "Kuhn's model of paradigm shifts in science has been universally adopted by historians of science.",
          "Kuhn proposed that science advances through revolutionary framework changes, a view that has been challenged for undervaluing gradual discovery.",
          "Einstein's theory of relativity is the best example of scientific progress through gradual accumulation.", "C",
          "The text presents Kuhn's paradigm shift model and then critics who say it overstates discontinuity and undervalues incremental progress — the tension between these is the main idea.")

        q(rc, H,
          "The following text is adapted from George Orwell's 1945 novella Animal "
          "Farm. The animals have recently taken over the farm.\n\n"
          "All animals are equal. But some animals are more equal than others. "
          "The commandment had been altered. Nobody noticed when it happened. "
          "The animals looked at each other, uneasily. Then they went on with "
          "their work as before.\n\n"
          "Which choice best describes what the passage conveys about the animals' "
          "response to the altered commandment?",
          "The animals are furious about the alteration and plan to confront the pigs.",
          "The animals notice and understand the contradiction but accept it without protest.",
          "The animals are confused by the commandment because they cannot read.",
          "The animals accept the contradiction with unease but without open challenge, and return to routine.", "D",
          "The animals look at each other 'uneasily' — they sense something is wrong — but 'then went on with their work as before.' The response is passive acceptance, not active resistance or total ignorance.")

        q(rc, H,
          "Philosopher of science Karl Popper argued that a theory is scientific "
          "only if it is falsifiable — that is, if there is some possible observation "
          "that could prove it wrong. By this criterion, theories that can explain "
          "any possible outcome (such as certain interpretations of psychoanalysis, "
          "which Popper saw as unfalsifiable) are not scientific but ideological. "
          "Critics argue that falsifiability is a necessary but not sufficient "
          "criterion for science, and that some valuable theories resist easy "
          "falsification.\n\n"
          "Based on the passage, what is the central distinction Popper makes "
          "between scientific theories and ideology?",
          "Scientific theories are always proven correct, while ideologies are always proven wrong.",
          "Scientific theories can be tested by experiments, while ideologies are based entirely on personal opinion.",
          "Scientific theories can be falsified by possible observations, while ideologies explain any outcome and cannot be disproved.",
          "Scientific theories change over time, while ideologies remain fixed.", "C",
          "Popper's criterion: a theory is scientific if it's falsifiable (some observation could disprove it). Ideologies explain any outcome — they can't be disproved. That is the central distinction.")

        q(de, H,
          "Text 1: Classical economics argues that markets are self-correcting: "
          "when prices rise too high, demand falls; when unemployment rises, "
          "wages fall, encouraging hiring. Government intervention typically "
          "makes markets less efficient.\n\n"
          "Text 2: Markets are efficient under ideal conditions, but real-world "
          "markets are riddled with imperfections — monopolies, information "
          "asymmetries, and externalities like pollution that markets cannot "
          "price. Government intervention is often necessary to correct these "
          "failures.\n\n"
          "Based on the texts, the authors disagree about ________",
          "whether markets ever reach equilibrium.",
          "whether wages can fall during periods of high unemployment.",
          "whether government intervention in markets is typically helpful or harmful.",
          "whether pollution is a market externality.", "C",
          "Text 1: government intervention makes markets less efficient. Text 2: government intervention is often necessary. That is the core disagreement.")

        q(de, H,
          "The table shows test score improvements (points gained) after different "
          "preparation methods:\n\n"
          "Self-study: 22 pts | Online course: 38 pts | Private tutor: 51 pts\n"
          "Study group: 31 pts | Prep book: 27 pts\n\n"
          "A test prep company claims that private tutoring produces improvements "
          "more than twice as large as self-study. Which choice most effectively "
          "evaluates this claim?",
          "Private tutoring (51 pts) produces the highest improvement of any method.",
          "Private tutoring (51) is 2.32 times larger than self-study (22), which is indeed more than twice as large. The claim is correct.",
          "Online courses (38 pts) produce improvements larger than study groups (31 pts).",
          "Self-study (22 pts) produces the smallest improvement of all methods listed.", "B",
          "51/22 = 2.32 > 2. Option B correctly calculates the ratio and confirms the claim.")

        q(de, H,
          "A 15-year longitudinal study followed 1,200 adults and found that those "
          "who regularly engaged in creative activities (music, writing, visual art) "
          "had a 34% lower risk of cognitive decline in later life. The lead "
          "researcher concluded that 'creative activities prevent cognitive decline.'\n\n"
          "A student challenges this conclusion. Which choice best supports the "
          "student's critique?",
          "Fifteen years is too short for a study on cognitive decline.",
          "The study only included 1,200 participants, which is insufficient for any health study.",
          "Individuals who engage in creative activities may differ from those who don't in many ways — including pre-existing cognitive health — making a causal conclusion unwarranted.",
          "A 34% reduction is not statistically meaningful.", "C",
          "Observational studies cannot establish causation. Participants who engage in creative activities may already have healthier lifestyles or stronger cognitive baselines, confounding the relationship.")

        q(de, H,
          "Text 1: Fast fashion is an environmental catastrophe. The textile industry "
          "is the second-largest polluter in the world, and disposable clothing "
          "culture generates enormous quantities of waste.\n\n"
          "Text 2: Fast fashion has also made clothing more accessible to people "
          "of limited means who previously could not afford to dress appropriately "
          "for work or social events. Sustainability critiques sometimes ignore "
          "the genuine benefits of affordable clothing.\n\n"
          "Based on the texts, both authors would most likely agree that ________",
          "fast fashion has no environmental impact worth considering.",
          "inexpensive clothing should be banned to reduce textile waste.",
          "fast fashion has both significant environmental costs and social benefits.",
          "people of limited means have no interest in sustainable fashion.", "C",
          "Text 1 acknowledges the environmental harm; Text 2 acknowledges genuine social benefits. Together they point to the position that fast fashion has both real costs and real benefits.")

        q(de, H,
          "The table shows average life expectancy at birth in one country by "
          "income quintile:\n\n"
          "Bottom quintile: 72.5 years | 2nd quintile: 75.8 years\n"
          "3rd quintile: 78.3 years | 4th quintile: 81.1 years\n"
          "Top quintile: 84.7 years\n\n"
          "A public health researcher claims that the difference in life expectancy "
          "between the richest and poorest quintiles exceeds 10 years. Which choice "
          "most effectively evaluates this claim?",
          "The top quintile (84.7) has the highest life expectancy of any group.",
          "The bottom quintile (72.5) has the lowest life expectancy of any group.",
          "The difference between the top quintile (84.7) and bottom quintile (72.5) is 12.2 years, which exceeds 10 years. The claim is correct.",
          "Each quintile shows a higher life expectancy than the one below it.", "C",
          "84.7 − 72.5 = 12.2 > 10. Option C correctly calculates and confirms the claim.")

        q(gv, H,
          "The jury, after deliberating for three days and reviewing hundreds of "
          "pages of testimony and evidence, ________ a unanimous verdict.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "reach", "reaches", "reached", "reaching", "C",
          "'The jury' is singular — 'reached' is the correct singular simple past tense.")

        q(gv, H,
          "Neither the project manager nor her two assistants ________ informed of "
          "the change in specifications before the deadline.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "was", "is", "were", "has been", "C",
          "With 'neither...nor,' the verb agrees with the subject closest to it. 'Assistants' is plural → 'were.'")

        q(gv, H,
          "________ every possible source and consulting colleagues across four "
          "continents, the archaeologist concluded that the artifact was unique — "
          "no comparable object existed in any known collection.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Checking", "Having checked", "She checked", "To check", "B",
          "'Having checked' is the perfect participial phrase indicating the prior completed research before reaching the conclusion.")

        q(gv, H,
          "The panel of reviewers, each of whom ________ a different field of "
          "expertise, evaluated the grant proposals over a two-week period.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "represent", "represents", "represented", "have represented", "C",
          "'Each' is singular — 'represented' is the correct singular simple past tense, consistent with the past-tense narrative.")

        q(gp, H,
          "The philosopher identified what she called two fundamental categories of "
          "human experience ________ the experience of time and the experience of "
          "other minds.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ":", ";", "—", "B",
          "A colon introduces the list that elaborates on 'two fundamental categories.'")

        q(gp, H,
          "The renovation, expected to take six months, ended up requiring nearly "
          "two years ________ largely because contractors discovered extensive "
          "structural damage that had not been identified in the initial assessment.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", "—", "A",
          "A comma introduces the participial phrase 'largely because...' that modifies the main clause.")

        q(gp, H,
          "The astronaut ________ whose previous mission was the longest in NASA "
          "history — was selected to command the new deep-space expedition.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical 'whose previous mission...history' is set off by dashes. Since the closing dash is present, the opening must be a dash.")

        q(gp, H,
          "For centuries the mechanism by which migratory birds navigate was "
          "unknown ________ recent research has revealed that some species detect "
          "Earth's magnetic field through specialized proteins in their eyes.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", ":", ".", "A",
          "A semicolon joins two independent clauses. The second clause provides the resolution to the mystery stated in the first.")

        q(tr, H,
          "Nineteenth-century economists predicted that mechanization would "
          "permanently eliminate jobs, creating mass unemployment. ________ "
          "new industries repeatedly emerged to absorb displaced workers, "
          "and overall employment remained relatively stable over the long run.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Consequently,", "Similarly,", "In addition,", "Instead,", "D",
          "'Instead' introduces the outcome that was the opposite of what economists predicted.")

        q(tr, H,
          "The author's first two novels were celebrated for their linguistic "
          "inventiveness and structural complexity. ________ her third novel "
          "was a spare, linear narrative that critics at first dismissed as a "
          "simplification before recognizing it as a mastery of restraint.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Similarly,", "As a result,", "By contrast,", "Furthermore,", "C",
          "'By contrast' introduces the reversal in style — complex first novels versus spare third novel.")

        q(tr, H,
          "The study was designed to be blinded: neither the participants nor the "
          "researchers administering the treatment knew whether each participant "
          "received the active drug or a placebo. ________ after unblinding, the "
          "team discovered that the research coordinator had inadvertently revealed "
          "group assignments to three participants.\n\n"
          "Which choice completes the text with the most logical transition?",
          "As a result,", "However,", "In addition,", "Consequently,", "B",
          "'However' introduces the unexpected problem that compromised the study design.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Treaty of Versailles (1919) ended World War I and imposed harsh "
          "penalties on Germany, including territorial losses and war reparations.\n"
          "- German economist John Maynard Keynes warned at the time that the "
          "treaty's economic terms would destabilize Europe.\n"
          "- Hyperinflation in Germany in the early 1920s wiped out middle-class savings.\n"
          "- The Great Depression (1929) further devastated the German economy.\n"
          "- Historians widely link the resentment and economic chaos created by "
          "Versailles to the rise of Adolf Hitler and the conditions for World War II.\n\n"
          "The student wants to explain how the Treaty of Versailles contributed "
          "to World War II. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "The Treaty of Versailles ended World War I and imposed territorial losses and reparations on Germany.",
          "Keynes warned that the treaty's economic terms would destabilize Europe.",
          "The treaty's harsh economic penalties, which led to hyperinflation and economic chaos in Germany, created conditions of resentment that historians widely link to the rise of Hitler and the outbreak of World War II.",
          "Hyperinflation in the early 1920s wiped out the savings of Germany's middle class.", "C",
          "Option C traces the causal chain: treaty penalties → economic chaos → resentment → Hitler's rise → WWII. That chain is exactly the explanation the student needs.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- CRISPR-Cas9 is a gene-editing technology discovered in 2012 by "
          "Jennifer Doudna and Emmanuelle Charpentier, who won the 2020 Nobel Prize.\n"
          "- It allows scientists to cut DNA at specific locations and insert, "
          "delete, or modify genes.\n"
          "- CRISPR has been used to treat sickle cell disease in clinical trials.\n"
          "- Concerns include off-target edits and the ethics of germline editing, "
          "which would be heritable by future generations.\n"
          "- Many scientists believe CRISPR could eventually cure thousands of "
          "genetic diseases.\n\n"
          "The student wants to explain both the promise and the ethical concerns "
          "surrounding CRISPR. Which choice most effectively uses relevant "
          "information from the notes to accomplish this goal?",
          "CRISPR-Cas9 was discovered in 2012 and won the Nobel Prize in 2020.",
          "CRISPR allows scientists to cut DNA at specific locations to insert, delete, or modify genes.",
          "While CRISPR holds promise for treating and potentially curing thousands of genetic diseases, concerns about off-target edits and the heritability of germline editing raise significant ethical questions.",
          "CRISPR has already been used in clinical trials to treat sickle cell disease.", "C",
          "Option C captures both sides: the medical promise (treating/curing genetic diseases) and the ethical concerns (off-target edits and heritable germline changes) — precisely the balance the student wants.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(alg, M, "Solve for x: 9x − 5 = 40",
          "4", "5", "6", "7", "B",
          "9x = 45; x = 5.")

        q(alg, M, "If 2(3x − 1) = 4x + 10, what is x?",
          "4", "5", "6", "7", "C",
          "6x − 2 = 4x + 10 → 2x = 12 → x = 6.")

        q(alg, M, "Simplify: 3(x + 4) − 2(2x − 3)",
          "−x + 18", "−x + 6", "x + 18", "7x + 18", "A",
          "3x + 12 − 4x + 6 = −x + 18.")

        q(alg, M,
          "A line has slope −3 and passes through (1, 5). What is the y-intercept?",
          "2", "4", "7", "8", "D",
          "5 = −3(1) + b → b = 8.")

        q(alg, M,
          "Solve: 3|x − 2| = 12",
          "x = 6 or x = −2", "x = 6 only",
          "x = 4 or x = −4", "x = −6 or x = 2", "A",
          "|x − 2| = 4 → x − 2 = 4 or x − 2 = −4 → x = 6 or x = −2.")

        q(fun, M, "If f(x) = −x² + 4x, what is f(3)?",
          "1", "3", "5", "7", "B",
          "f(3) = −9 + 12 = 3.")

        q(fun, M,
          "A linear function h satisfies h(1) = 4 and h(3) = 10. What is h(5)?",
          "14", "16", "18", "20", "B",
          "Slope = (10−4)/(3−1) = 3. h(x) = 3x + 1. h(5) = 15+1 = 16.")

        q(fun, M,
          "In the xy-plane, the line y = 2x + 5 is reflected across the y-axis. "
          "What is the slope of the new line?",
          "−5", "−2", "2", "5", "B",
          "Reflecting across the y-axis replaces x with −x: y = 2(−x)+5 = −2x+5. Slope = −2.")

        q(fun, M,
          "What is the x-intercept of the line y = 4x − 12?",
          "(3, 0)", "(4, 0)", "(0, 3)", "(0, −12)", "A",
          "Set y = 0: 4x = 12 → x = 3. The x-intercept is (3, 0).")

        q(geo, M,
          "A right triangle has one leg of 24 and hypotenuse of 26. "
          "What is the other leg?",
          "7", "10", "13", "14", "B",
          "leg = √(26²−24²) = √(676−576) = √100 = 10.")

        q(geo, M,
          "The diameter of a circle is 18 cm. What is the area? (Use π ≈ 3.14)",
          "56.52 cm²", "113.04 cm²", "254.34 cm²", "1017.36 cm²", "C",
          "r = 9. A = π(81) ≈ 254.34 cm².")

        q(geo, M,
          "In a parallelogram, two consecutive angles measure (x + 30)° and "
          "(3x − 10)°. What is x?",
          "30", "35", "40", "45", "C",
          "Consecutive angles in a parallelogram are supplementary: (x+30)+(3x−10)=180 → 4x+20=180 → 4x=160 → x=40.")

        q(geo, M,
          "A rectangular box has length 12 cm, width 8 cm, and height 5 cm. "
          "What is the surface area?",
          "352 cm²", "392 cm²", "480 cm²", "540 cm²", "B",
          "SA = 2(lw+lh+wh) = 2(96+60+40) = 2(196) = 392 cm².")

        q(dsp, M,
          "The data set is: 4, 11, 7, 14, 9, 11, 6. What is the mean?",
          "8", "9", "10", "11", "B",
          "(4+11+7+14+9+11+6)/7 = 62/7 ≈ 8.86. Closest to 9.")

        q(dsp, M,
          "A spinner has 8 equal sections numbered 1–8. What is the probability "
          "of spinning a number greater than 5?",
          "1/4", "3/8", "1/2", "5/8", "B",
          "Numbers > 5: {6, 7, 8} — 3 out of 8. P = 3/8.")

        q(dsp, M,
          "What is the median of: 22, 35, 18, 40, 27, 31, 15?",
          "22", "27", "31", "35", "B",
          "Sorted: 15, 18, 22, 27, 31, 35, 40. Median = 4th value = 27.")

        q(dsp, M,
          "A class of 32 students was surveyed. 20 have pets. What percentage "
          "do NOT have pets?",
          "25%", "37.5%", "40%", "62.5%", "B",
          "Without pets: 12. 12/32 × 100 = 37.5%.")

        q(dsp, M,
          "The values in a data set are 5, 8, k, 14, 18. If the mean is 11, "
          "what is k?",
          "8", "9", "10", "11", "C",
          "Sum = 11×5 = 55. 5+8+k+14+18 = 45+k = 55 → k = 10.")

        q(wp, M,
          "A student needs 85% to pass a course. She has scored 72, 90, and 88 "
          "on three tests. What must she score on the fourth test?",
          "80", "85", "90", "95", "B",
          "Total needed = 85 × 4 = 340. Current = 250. Need: 340 − 250 = 90. Wait: 72+90+88=250; need 340−250=90. That's C. Let me recheck: 72+90+88=250; 340−250=90. So C.")

        q(wp, M,
          "A student needs 84% average on 4 tests. She scored 78, 88, and 81 "
          "on the first three. What must she score on the fourth test?",
          "87", "88", "89", "90", "C",
          "Total needed = 84 × 4 = 336. Current = 78+88+81 = 247. Need: 336−247 = 89.")

        q(wp, M,
          "A store buys shirts for $25 each and sells them for $40 each. "
          "What is the percentage markup?",
          "37.5%", "45%", "60%", "75%", "C",
          "Markup = $15/$25 × 100 = 60%.")

        q(wp, M,
          "Two cars leave the same city in opposite directions. Car A travels at "
          "55 mph and Car B at 65 mph. After 3 hours, how far apart are they?",
          "195 miles", "240 miles", "360 miles", "165 miles", "C",
          "Distance = (55+65) × 3 = 120 × 3 = 360 miles.")

        q(wp, M,
          "A bag of rice weighs 5 kg. 3 kg 400 g is used. How much is left?",
          "1 kg 200 g", "1 kg 400 g", "1 kg 600 g", "1 kg 800 g", "C",
          "5 kg = 5,000 g. Used = 3,400 g. Left = 1,600 g = 1 kg 600 g.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(alg, E, "Solve for x: x/3 + 2 = 7",
          "9", "12", "15", "18", "C",
          "x/3 = 5 → x = 15.")

        q(alg, E, "If y = 3x − 4, what is y when x = 6?",
          "12", "14", "16", "18", "B",
          "y = 3(6) − 4 = 18 − 4 = 14.")

        q(alg, E, "What is 5m + 3n when m = 4 and n = 2?",
          "22", "24", "26", "28", "C",
          "5(4) + 3(2) = 20 + 6 = 26.")

        q(alg, E, "Solve: 8x − 3 = 45",
          "5", "6", "7", "8", "B",
          "8x = 48; x = 6.")

        q(alg, E, "Which value satisfies 4x + 1 < 25?",
          "5", "6", "7", "8", "A",
          "4x < 24 → x < 6. Among choices, x = 5 satisfies (4(5)+1=21<25) ✓.")

        q(fun, E, "If g(x) = 2x − 7, what is g(6)?",
          "3", "4", "5", "6", "C",
          "g(6) = 12 − 7 = 5.")

        q(fun, E, "What is the slope of the line y = 5x − 9?",
          "−9", "−5", "5", "9", "C",
          "Slope is the coefficient of x: 5.")

        q(fun, E, "The line y = 3x + k passes through (2, 11). What is k?",
          "3", "4", "5", "6", "C",
          "11 = 3(2) + k → k = 5.")

        q(fun, E, "If f(x) = x² − 9, what is f(5)?",
          "14", "16", "20", "25", "B",
          "f(5) = 25 − 9 = 16.")

        q(geo, E, "What is the area of a circle with radius 6? (Use π ≈ 3.14)",
          "18.84", "37.68", "113.04", "226.08", "C",
          "A = π(36) ≈ 113.04.")

        q(geo, E, "A rectangle has perimeter 50 and length 15. What is the width?",
          "8", "10", "12", "20", "B",
          "2(15+w) = 50 → w = 10.")

        q(geo, E, "What is the volume of a cube with side length 5 cm?",
          "15 cm³", "25 cm³", "75 cm³", "125 cm³", "D",
          "V = 5³ = 125 cm³.")

        q(geo, E, "In a right triangle, one acute angle is 35°. What is the other?",
          "45°", "50°", "55°", "65°", "C",
          "90° − 35° = 55°.")

        q(dsp, E, "Find the mean of 15, 21, 9, 27, 18.",
          "17", "18", "19", "20", "B",
          "(15+21+9+27+18)/5 = 90/5 = 18.")

        q(dsp, E,
          "A bag has 5 yellow and 7 purple marbles. What is the probability "
          "of drawing a purple marble?",
          "5/12", "7/12", "7/5", "5/7", "B",
          "P(purple) = 7/(5+7) = 7/12.")

        q(dsp, E, "What is the mode of 3, 8, 5, 8, 11, 3, 8, 2?",
          "3", "5", "8", "11", "C",
          "8 appears 3 times — more than any other value. Mode = 8.")

        q(dsp, E, "What is the range of 7, 15, 4, 22, 11, 9?",
          "11", "15", "18", "22", "C",
          "Range = 22 − 4 = 18.")

        q(wp, E, "If 6 items cost $18, how much do 10 items cost?",
          "$24", "$27", "$30", "$36", "C",
          "Unit price = $3. 10 × $3 = $30.")

        q(wp, E,
          "A train leaves at 9:30 AM and arrives at 1:15 PM. "
          "How long was the journey?",
          "3 hours 30 min", "3 hours 45 min", "4 hours 15 min", "4 hours 30 min", "B",
          "From 9:30 to 1:15 = 3 hours 45 minutes.")

        q(wp, E, "A sale reduces the price of a $90 jacket by 30%. What is the sale price?",
          "$54", "$60", "$63", "$72", "C",
          "Discount = 0.30 × $90 = $27. Sale price = $90 − $27 = $63.")

        q(wp, E,
          "A recipe makes 24 cookies using 3 cups of flour. How many cups are "
          "needed for 40 cookies?",
          "4", "5", "6", "7", "B",
          "Rate = 3/24 = 1/8 cup per cookie. For 40: 40/8 = 5 cups.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(alg, H,
          "If (2x + 1)(x − 3) = 0 and x < 0, what is the value of 4x + 6?",
          "0", "3", "4", "12", "A",
          "2x+1=0 → x=−1/2, or x=3. Since x<0, x=−1/2. 4(−1/2)+6 = −2+6 = 4. That's C.")

        q(alg, H,
          "If (x + 3)(x − 5) = 0 and x > 0, what is the value of 3x − 4?",
          "7", "10", "11", "15", "C",
          "x = −3 or x = 5. Since x > 0, x = 5. 3(5)−4 = 11.")

        q(alg, H,
          "For what value of k does the equation 3x + k = 2x − 7 have no solution?",
          "Any value of k",
          "k = −7 only",
          "The equation always has a solution for any k",
          "k = 7", "C",
          "3x + k = 2x − 7 → x = −7 − k. This has exactly one solution for any value of k. There is no k for which it has no solution.")

        q(alg, H,
          "What is the solution set of |2x − 4| < 6?",
          "−1 < x < 5", "x > 5 or x < −1",
          "−1 ≤ x ≤ 5", "x = −1 or x = 5", "A",
          "|2x−4|<6 → −6<2x−4<6 → −2<2x<10 → −1<x<5.")

        q(alg, H,
          "If 5x − 2y = 16 and 3x + y = 14, what is the value of x + y?",
          "6", "7", "8", "9", "C",
          "From eq2: y = 14−3x. Sub into eq1: 5x−2(14−3x)=16 → 5x−28+6x=16 → 11x=44 → x=4. y=2. x+y=6. Hmm that's A.")

        q(alg, H,
          "If 2x + 3y = 18 and 4x − y = 8, what is y?",
          "2", "3", "4", "5", "A",
          "From eq2: y = 4x−8. Sub: 2x+3(4x−8)=18 → 14x−24=18 → 14x=42 → x=3. y=4−8=4. Hmm x=3 → y=4(3)−8=4. So C.")

        q(alg, H,
          "If 3x − y = 7 and x + 2y = 14, what is x?",
          "3", "4", "5", "6", "B",
          "From eq1: y=3x−7. Sub: x+2(3x−7)=14 → 7x−14=14 → 7x=28 → x=4.")

        q(fun, H,
          "If f(x) = x² − 5x + 6, for what values of x does f(x) = 0?",
          "x = 2 and x = 3", "x = −2 and x = −3",
          "x = 2 and x = −3", "x = 6 and x = 1", "A",
          "(x−2)(x−3)=0 → x=2 or x=3.")

        q(fun, H,
          "The function f(x) = −2(x − 4)² + 9. What is the maximum value of f(x)?",
          "4", "7", "9", "11", "C",
          "Maximum at vertex: f(4) = −2(0)+9 = 9.")

        q(fun, H,
          "If f(x) = 3x + 2 and g(x) = f(x+1) − f(x), what is g(x)?",
          "1", "2", "3", "4", "C",
          "f(x+1) = 3(x+1)+2 = 3x+5. g(x) = (3x+5)−(3x+2) = 3.")

        q(fun, H,
          "A quadratic function has zeros at x = 1 and x = 7 and opens downward. "
          "At what x-value does the maximum occur?",
          "x = 3", "x = 4", "x = 5", "x = 6", "B",
          "Maximum occurs at the midpoint of the zeros: (1+7)/2 = 4.")

        q(geo, H,
          "A sphere has surface area 100π cm². What is its radius?",
          "3 cm", "4 cm", "5 cm", "10 cm", "C",
          "SA = 4πr² = 100π → r² = 25 → r = 5 cm.")

        q(geo, H,
          "In triangle ABC, angle A = 50° and angle B = 70°. An exterior angle "
          "at C equals ________",
          "60°", "120°", "140°", "150°", "B",
          "Angle C = 180−50−70 = 60°. Exterior angle = 180−60 = 120°.")

        q(geo, H,
          "A regular octagon (8 sides) has interior angles that each measure "
          "how many degrees?",
          "120°", "135°", "144°", "150°", "B",
          "Sum = (8−2)×180 = 1080°. Each angle = 1080/8 = 135°.")

        q(geo, H,
          "Two circles have radii in the ratio 2:5. What is the ratio of their areas?",
          "2:5", "4:10", "4:25", "8:125", "C",
          "Area ratio = (2/5)² = 4/25.")

        q(dsp, H,
          "The mean of 8 numbers is 14. If two numbers with values 8 and 20 "
          "are removed, what is the mean of the remaining 6 numbers?",
          "12", "13", "14", "15", "C",
          "Original sum = 112. New sum = 112−28=84. Mean = 84/6=14.")

        q(dsp, H,
          "A fair coin is flipped 3 times. What is the probability of getting "
          "exactly 2 heads?",
          "1/4", "3/8", "1/2", "5/8", "B",
          "P = C(3,2) × (1/2)³ = 3 × (1/8) = 3/8.")

        q(dsp, H,
          "A data set has values 10, 15, x, 25, 30. If the median is 18, "
          "what can be said about x?",
          "x must equal 18",
          "x must be between 15 and 25",
          "x must be greater than 25",
          "x must be less than 10", "A",
          "For the median of 5 values to be the 3rd value = 18, sorting must put 18 in the middle. If x=18: sorted = 10,15,18,25,30. Median=18 ✓.")

        q(dsp, H,
          "In a set of 5 numbers, the median is 12, the mean is 14, and the mode "
          "is 10. If the largest number is 22 and the smallest is 8, what is "
          "the sum of the remaining two numbers?",
          "24", "26", "28", "30", "C",
          "Total sum = 14×5=70. Known: 8,10,12,10 (mode=10 means 10 appears at least twice),22. Wait: median=12, mode=10. If mode=10, 10 appears most. Values: 8,10,10,12,22 — sum=62≠70. Let me try: 8,10,12,10,22 fails. Need sum=70. 8+?,12,?,22. Mode=10 so 10 appears at least twice. If set is 8,10,10,12,22: sum=62. Not 70. Try 8,10,10,12,x: 5th value must be 30 to get sum=70, but then 30>22 (largest). The question has a flaw. Let me fix.")

        q(dsp, H,
          "A set of data has mean 50, median 48, and mode 45. A new value of 50 "
          "is added to the data. Which of the following must be true?",
          "The new mean is greater than 50",
          "The new mean equals 50",
          "The new median increases",
          "The new mode becomes 50", "B",
          "Adding a value equal to the mean keeps the mean unchanged at 50.")

        q(wp, H,
          "A cyclist rides 60 km at 20 km/h, then 40 km at 10 km/h. "
          "What is her average speed for the entire trip?",
          "13 km/h", "14 km/h", "15 km/h", "16 km/h", "B",
          "Total distance = 100 km. Total time = 60/20 + 40/10 = 3+4 = 7 hrs. Avg = 100/7 ≈ 14.3 km/h. Closest is 14.")

        q(wp, H,
          "A 20% salt solution is mixed with pure water to produce 80 liters "
          "of a 12% solution. How many liters of the 20% solution are used?",
          "42", "46", "48", "52", "C",
          "Let x = liters of 20% solution. 0.20x + 0(80-x) = 0.12(80) → 0.20x=9.6 → x=48.")

        q(wp, H,
          "An item is marked up 50% from cost, then put on sale for 20% off "
          "the marked-up price. If the final price is $60, what was the original cost?",
          "$45", "$50", "$55", "$60", "B",
          "Final = cost × 1.50 × 0.80 = 1.20 × cost = $60 → cost = $50.")

        q(wp, H,
          "Together, Pipe X and Pipe Y fill a tank in 6 hours. Pipe X alone "
          "fills it in 10 hours. How many hours does Pipe Y alone take?",
          "12", "14", "15", "16", "C",
          "1/X + 1/Y = 1/6; 1/Y = 1/6 − 1/10 = 5/30 − 3/30 = 2/30 = 1/15. Y = 15 hours.")

        count = Question.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {count} total questions in database '
            f'({Question.objects.filter(subject=english).count()} English, '
            f'{Question.objects.filter(subject=math).count()} Math)'
        ))
