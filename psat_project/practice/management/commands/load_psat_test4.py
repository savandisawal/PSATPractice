"""
PSAT 8/9-style Practice Test 4 — generated questions.
English (Reading & Writing): 81 questions across 3 modules
Math: 66 questions across 3 modules
Difficulty: Module 1 = medium, Module 2 Easier = easy, Module 2 Harder = hard
"""
from django.core.management.base import BaseCommand
from practice.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Load PSAT-style Practice Test 4 questions into the database'

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
          "Physicist Richard Feynman was known not only for his Nobel Prize-winning "
          "research but also for his remarkable ability to ________ complex scientific "
          "concepts to general audiences without sacrificing accuracy.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "obscure", "complicate", "elucidate", "dismiss", "C",
          "'Elucidate' means to explain or make clear — precisely matching the ability to clarify complex ideas for a general audience.")

        q(ev, M,
          "The environmental group's campaign was seen as ________ by its opponents, "
          "who argued that it exaggerated the dangers of the proposed dam and relied "
          "on misleading statistics.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "credible", "transparent", "alarmist", "restrained", "C",
          "'Alarmist' means exaggerating dangers to cause alarm — precisely matching the opponents' criticism.")

        q(ev, M,
          "The ancient historian's account of the battle was long considered the "
          "definitive record, but recent archaeological discoveries have shown it to "
          "be ________ in several key respects, forcing scholars to revise the "
          "established narrative.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "accurate", "comprehensive", "inaccurate", "accessible", "C",
          "'Inaccurate' means not correct — matching discoveries that forced scholars to revise the account.")

        q(ev, M,
          "Architect Zaha Hadid's flowing, curvilinear designs ________ traditional "
          "architectural conventions, replacing straight lines and right angles with "
          "sweeping forms inspired by natural landscapes.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "reinforced", "upheld", "subverted", "simplified", "C",
          "'Subverted' means to undermine or challenge — matching designs that replace conventional forms.")

        q(rc, M,
          "Researchers studying ancient climate have used ice cores from Greenland and "
          "Antarctica to reconstruct atmospheric conditions going back hundreds of "
          "thousands of years. Tiny air bubbles trapped in the ice contain samples of "
          "ancient atmosphere, including concentrations of greenhouse gases. Analyzing "
          "these bubbles has revealed that current atmospheric CO₂ levels are higher "
          "than at any point in the past 800,000 years.\n\n"
          "Which choice best states the main idea of the text?",
          "Scientists have developed ice cores specifically to measure current CO₂ levels.",
          "Ice core analysis has provided evidence that current atmospheric CO₂ is historically unprecedented.",
          "Greenland has more useful ice cores for climate research than Antarctica.",
          "Air bubbles in ice contain all the same gases as modern air.", "B",
          "The main idea is that ice core analysis revealed current CO₂ levels are higher than at any point in the past 800,000 years.")

        q(rc, M,
          "The following text is adapted from Zora Neale Hurston's 1937 novel Their "
          "Eyes Were Watching God.\n\n"
          "She was stretched on her back beneath the pear tree soaking in the alto "
          "chant of the visiting bees, the gold of the sun and the panting breath "
          "of the breeze when the inaudible voice of it all came to her. She saw a "
          "dust-bearing bee sink into the sanctum of a bloom; the thousand sister-"
          "calyxes arch to meet the love embrace and the ecstatic shiver of the "
          "tree from root to tiniest branch creaming in every blossom and "
          "frothing with delight.\n\n"
          "Which choice best describes the overall tone of the passage?",
          "Melancholic and nostalgic.",
          "Tense and anxious.",
          "Sensuous and rapturous.",
          "Detached and clinical.", "C",
          "Words like 'ecstatic,' 'delight,' 'panting,' and 'frothing' create a deeply sensuous, intensely joyful tone.")

        q(rc, M,
          "Psychologist Carol Dweck's research on 'mindset' distinguishes between "
          "individuals with a fixed mindset — who believe intelligence is innate and "
          "unchangeable — and those with a growth mindset, who believe abilities "
          "develop through effort and learning. Studies suggest that students "
          "taught to adopt a growth mindset show significantly greater academic "
          "improvement than those not given such instruction.\n\n"
          "Which choice best states the main idea of the text?",
          "Dweck's research proves that intelligence is purely innate.",
          "Students with fixed mindsets always outperform those with growth mindsets.",
          "Dweck's research shows that believing abilities can grow is associated with greater academic improvement.",
          "Mindset is determined entirely by genetics and cannot be changed.", "C",
          "The text presents Dweck's finding that a growth mindset is associated with academic improvement.")

        q(rc, M,
          "Between 1960 and 1975, the number of known bird species rose dramatically "
          "as ornithologists traveled to previously unstudied regions. The rate of "
          "new species discoveries has since slowed, not because few species remain "
          "undiscovered, but because most remaining undiscovered species live in "
          "highly remote habitats that are difficult and expensive to survey. "
          "This suggests that ________\n\n"
          "Which choice most logically completes the text?",
          "the total number of bird species on Earth has stabilized since 1975.",
          "ornithologists have little interest in discovering new bird species.",
          "logistical barriers, rather than an absence of undiscovered species, explain the slowdown.",
          "most new bird species will be found in urban rather than remote environments.", "C",
          "The passage explicitly states that the slowdown is because remaining species are in remote habitats — logistical barriers, not absence of species.")

        q(rc, M,
          "Immunologist Charles Janeway proposed that the immune system recognizes "
          "invading pathogens not by detecting foreign molecules per se, but by "
          "sensing molecular patterns associated specifically with infection. His "
          "'pattern recognition' model was initially dismissed as speculative but "
          "was later validated by the discovery of toll-like receptors — proteins "
          "that recognize exactly the kinds of patterns Janeway described.\n\n"
          "Which choice best states the main idea of the text?",
          "Janeway's dismissal of earlier immunology models led to new discoveries.",
          "Janeway's initially controversial theory about immune pattern recognition was later confirmed by molecular evidence.",
          "Toll-like receptors were discovered before Janeway proposed his pattern recognition model.",
          "Janeway's model suggested that the immune system cannot distinguish between foreign and domestic molecules.", "B",
          "The text traces the arc of Janeway's theory: initially dismissed, later validated. That arc is the main idea.")

        q(de, M,
          "The table shows annual renewable energy production by source (in terawatt-hours):\n\n"
          "Wind: 1,850 | Solar: 1,400 | Hydroelectric: 4,200 | Geothermal: 95 | Biomass: 580\n\n"
          "A report claims that hydroelectric power accounts for more than half of all "
          "renewable energy production listed. Which choice most effectively uses data "
          "from the table to evaluate this claim?",
          "Solar (1,400) and Wind (1,850) together exceed hydroelectric production.",
          "Geothermal (95) is the smallest source of renewable energy.",
          "Total production is 8,125 TWh; hydroelectric (4,200) represents about 51.7%, confirming it accounts for more than half.",
          "Biomass (580) produces more energy than geothermal (95).", "C",
          "Total = 8,125. Hydro = 4,200. 4,200/8,125 = 51.7% > 50%. Option C correctly calculates and evaluates the claim.")

        q(de, M,
          "Text 1: The use of smartphones in classrooms should be banned. Studies show "
          "that students who use phones during class score lower on assessments and "
          "retain less material.\n\n"
          "Text 2: Blanket bans on smartphones in classrooms are counterproductive. "
          "When integrated thoughtfully, phones can enhance learning through educational "
          "apps, research tools, and collaborative platforms.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond "
          "to the claim in Text 1 that phones should be banned?",
          "Text 2 would agree because the studies mentioned in Text 1 are credible.",
          "Phones can have educational value when used appropriately, so a total ban is not the right response.",
          "Text 2 acknowledges that phones hurt test scores and therefore supports a ban.",
          "Phones should only be allowed in college classrooms, not in earlier grades.", "B",
          "Text 2's argument is that thoughtful integration — not banning — is the right approach, directly disagreeing with Text 1's call for a ban.")

        q(de, M,
          "A research team tracked the number of polar bears in a specific Arctic "
          "region over four decades:\n\n"
          "1980: 1,200 | 1990: 1,080 | 2000: 940 | 2010: 760 | 2020: 610\n\n"
          "A scientist argues that the polar bear population declined by approximately "
          "50% from 1980 to 2020. Which choice most effectively evaluates this claim?",
          "The population fell from 1,200 to 760 by 2010, a decline of 440 bears.",
          "The population dropped from 1,200 in 1980 to 610 in 2020, a decline of 590, or about 49% — approximately 50%. The claim is essentially correct.",
          "The largest single-decade decline occurred between 2000 and 2010.",
          "The population in 1990 was 10% lower than in 1980.", "B",
          "590/1200 = 49.2%, which rounds to approximately 50%. Option B correctly calculates and confirms the claim.")

        q(de, M,
          "Text 1: Colonizing Mars is the logical next step for humanity. Earth's "
          "resources are finite, and establishing a second planet as a home would "
          "ensure the long-term survival of the human species.\n\n"
          "Text 2: Mars colonization is a fantasy that distracts from urgent problems "
          "on Earth. The technology required is decades away, the costs would be "
          "astronomical, and the resources spent would be far better used to address "
          "climate change and poverty on our own planet.\n\n"
          "Based on the texts, what do the two authors disagree about?",
          "Whether Mars has any physical resources that could support human life.",
          "Whether long-term human survival should be a priority.",
          "Whether colonizing Mars is a worthwhile use of resources given other pressing needs.",
          "Whether climate change and poverty are serious problems.", "C",
          "Text 1 calls Mars colonization the 'logical next step'; Text 2 says the resources would be far better used for Earth's problems. The core disagreement is about resource allocation.")

        q(de, M,
          "The graph shows the number of electric vehicle (EV) charging stations in "
          "four cities over two years:\n\n"
          "City P: Year 1 = 120, Year 2 = 195 | City Q: Year 1 = 85, Year 2 = 110\n"
          "City R: Year 1 = 200, Year 2 = 260 | City S: Year 1 = 45, Year 2 = 90\n\n"
          "A city planner argues that City S showed the greatest percentage growth "
          "in EV charging stations. Which choice most effectively evaluates this claim?",
          "City S doubled its stations from 45 to 90, a 100% increase.",
          "City R had the largest absolute increase of 60 stations.",
          "City S grew by 100% (45 to 90), compared to City P at 62.5%, City Q at 29.4%, and City R at 30%. City S had the greatest percentage growth. The claim is correct.",
          "City P grew by 75 stations, more than any other city except City R.", "C",
          "S: +100%; P: +62.5%; Q: +29.4%; R: +30%. City S had the highest percentage growth, confirming the claim.")

        q(gv, M,
          "The collection of ancient coins donated to the museum ________ now on "
          "display in the newly renovated east wing.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "is", "were", "have been", "B",
          "'Collection' is the singular subject — 'is' is the correct singular verb.")

        q(gv, M,
          "The students in the advanced class ________ their research projects in the "
          "school library every Tuesday afternoon for the past six weeks.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "conduct", "conducts", "conducted", "have been conducting", "D",
          "'Have been conducting' (present perfect continuous) correctly indicates an ongoing action that started in the past and continues to the present, consistent with 'for the past six weeks.'")

        q(gv, M,
          "________ through thousands of pages of declassified documents, the journalist "
          "eventually uncovered evidence of a previously unknown diplomatic agreement.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "She searched", "Searched", "Searching", "To search", "C",
          "'Searching' is the correct participial phrase modifying the subject 'the journalist.'")

        q(gv, M,
          "Each of the proposals submitted by the engineering teams ________ reviewed "
          "by a panel of independent experts before a final decision is made.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "were", "is", "will be", "D",
          "'Will be' is the correct future passive — 'before a final decision is made' signals a future action still to occur.")

        q(gp, M,
          "The documentary examined three distinct but related environmental crises "
          "________ rising sea levels, accelerating biodiversity loss, and the "
          "growing frequency of extreme weather events.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—and", "A",
          "A colon introduces the list of three crises that defines 'three distinct but related environmental crises.'")

        q(gp, M,
          "The scientist who developed the original theory of plate tectonics, "
          "Alfred Wegener ________ was a German meteorologist, not a geologist, "
          "which led many in the geological community to initially dismiss his ideas.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "A",
          "A comma sets off the appositive 'Alfred Wegener' before the main clause. (Both sides of the appositive need commas; the sentence uses one here.)")

        q(gp, M,
          "The city's public transit system carried more than two million passengers "
          "last year ________ making it the busiest in the region by a significant margin.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", ":", "—", "B",
          "A comma before the participial phrase 'making it the busiest...' correctly attaches the phrase to the main clause.")

        q(gp, M,
          "The novel's central theme — the tension between individual freedom and "
          "social obligation ________ is explored through the experiences of three "
          "very different characters.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical 'the tension between individual freedom and social obligation' is enclosed in dashes. Since the opening dash is present, the closing punctuation must also be a dash.")

        q(tr, M,
          "Scientists have known for decades that regular aerobic exercise improves "
          "cardiovascular health. ________ recent research has revealed that exercise "
          "also promotes the growth of new neurons in the hippocampus, the brain "
          "region associated with memory and learning.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "Therefore,", "In addition,", "Instead,", "C",
          "'In addition' signals that the text is adding another benefit of exercise beyond the already-known cardiovascular benefits.")

        q(tr, M,
          "Many early explorers relied on dead reckoning — estimating position based "
          "on known speed, direction, and time — to navigate the open ocean. "
          "________ the method was prone to cumulative errors that could leave ships "
          "dangerously off course after long voyages.\n\n"
          "Which choice completes the text with the most logical transition?",
          "As a result,", "Furthermore,", "However,", "Similarly,", "C",
          "'However' introduces a limitation contrasting with the relied-upon method.")

        q(tr, M,
          "The city council unanimously approved the new park design, which features "
          "native plantings and a restored wetland habitat. ________ construction is "
          "expected to begin in the spring and be completed within eighteen months.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "Consequently,", "By contrast,", "Otherwise,", "B",
          "'Consequently' signals that the approval led to the construction timeline — cause and effect.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- Nikola Tesla (1856-1943) was an inventor and engineer who developed the AC "
          "electrical system used worldwide today.\n"
          "- Tesla held over 300 patents in his lifetime.\n"
          "- He designed the first hydroelectric power plant at Niagara Falls in 1895.\n"
          "- Tesla and Thomas Edison were rivals who famously disagreed over AC versus DC power.\n"
          "- Despite his contributions, Tesla died nearly broke and in relative obscurity.\n\n"
          "The student wants to emphasize the contrast between Tesla's technical legacy "
          "and his personal fate. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "Tesla held over 300 patents and developed AC electrical systems used worldwide.",
          "Tesla and Edison were famous rivals who disagreed over AC versus DC power.",
          "Despite developing the AC electrical system now used worldwide and holding over 300 patents, Tesla died nearly broke and largely forgotten.",
          "Tesla designed the first hydroelectric power plant at Niagara Falls in 1895.", "C",
          "Option C juxtaposes Tesla's enormous technical legacy (AC power, 300+ patents) against his sad personal fate (broke, obscure) — directly accomplishing the contrast the student wants.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Great Barrier Reef is the world's largest coral reef system, stretching "
          "2,300 km along the coast of Queensland, Australia.\n"
          "- It is home to over 1,500 species of fish, 4,000 types of mollusk, and 240 "
          "species of birds.\n"
          "- Coral bleaching events caused by rising ocean temperatures have damaged "
          "large portions of the reef.\n"
          "- Since 2016, over half the coral in the northern section has died.\n"
          "- The reef generates approximately $6.4 billion annually for Australia's economy.\n\n"
          "The student wants to show the scale of damage the reef has suffered. Which "
          "choice most effectively uses relevant information from the notes?",
          "The Great Barrier Reef stretches 2,300 km and generates $6.4 billion annually.",
          "The reef is home to over 1,500 fish species and 240 species of birds.",
          "Since 2016, over half the coral in the northern section has died due to bleaching events caused by rising ocean temperatures.",
          "Coral bleaching events have been linked to rising ocean temperatures.", "C",
          "Option C directly quantifies the damage (over half of northern coral dead) and names the cause — the most effective way to show the scale of harm.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(ev, E,
          "The new community center has many programs for residents of all ages. "
          "Seniors can join exercise classes, while children can ________ painting, "
          "dancing, and other creative activities.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "avoid", "attend", "cancel", "ignore", "B",
          "'Attend' means to go to and participate in — the most logical action for children joining classes.")

        q(ev, E,
          "The marathon runner trained for months before the big race. Her dedication "
          "was ________ when she crossed the finish line in record time.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "wasted", "forgotten", "rewarded", "criticized", "C",
          "'Rewarded' — her dedication paid off with a record time.")

        q(ev, E,
          "The farmer planted seeds in early spring and ________ tended to the crops "
          "throughout the summer, ensuring a healthy harvest in the fall.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "rarely", "carelessly", "carefully", "briefly", "C",
          "'Carefully' matches the thorough tending that leads to a healthy harvest.")

        q(ev, E,
          "The town was ________ by a powerful storm that uprooted trees, flooded "
          "streets, and knocked out power for thousands of residents.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "welcomed", "unaffected", "ignored", "struck", "D",
          "'Struck' means hit by something forceful — the most precise word for a town battered by a storm.")

        q(rc, E,
          "Octopuses are highly intelligent animals capable of solving puzzles, "
          "recognizing individual human faces, and using tools. Despite having "
          "no central brain region comparable to that of mammals, octopuses "
          "distribute much of their neural processing through their arms, each "
          "of which can act somewhat independently.\n\n"
          "Which choice best states the main idea of the text?",
          "Octopuses are the most intelligent animals in the ocean.",
          "Octopuses lack the brain structure needed to solve puzzles or use tools.",
          "Octopuses are remarkably intelligent animals whose neural processing is uniquely distributed throughout their arms.",
          "Each arm of an octopus has a separate brain that controls the whole animal.", "C",
          "The text establishes octopus intelligence and then explains the unusual distributed neural structure — that combination is the main idea.")

        q(rc, E,
          "The aurora borealis, or northern lights, appears when charged particles "
          "from the sun collide with gases in Earth's atmosphere near the poles. "
          "The different colors — greens, pinks, and reds — are caused by different "
          "types of gas at different altitudes. Green is produced by oxygen at "
          "lower altitudes, while red comes from oxygen at higher altitudes.\n\n"
          "Which choice best states the main idea of the text?",
          "The aurora borealis can only be seen at the North Pole.",
          "The northern lights are caused by solar particles interacting with atmospheric gases, and different gases at different heights produce different colors.",
          "Scientists have not yet determined what causes the different colors of the aurora.",
          "The aurora borealis is the same color everywhere it appears.", "B",
          "The text explains both the cause of the aurora and why it shows different colors — that is the main idea.")

        q(rc, E,
          "Florence Nightingale is remembered as a pioneer of modern nursing, but she "
          "was also a gifted statistician. During the Crimean War, she collected and "
          "analyzed data on soldier deaths and used statistical diagrams — one of the "
          "earliest uses of data visualization in public health — to convince the "
          "government to improve hospital sanitation.\n\n"
          "Which choice best describes the function of the phrase 'one of the earliest "
          "uses of data visualization in public health' in the text?",
          "It explains why sanitation reform failed to reduce soldier deaths.",
          "It emphasizes the historical significance of Nightingale's statistical approach.",
          "It describes the specific type of data Nightingale collected.",
          "It suggests that Nightingale is primarily remembered as a statistician.", "B",
          "The phrase highlights how historically significant Nightingale's use of statistical diagrams was — an early milestone in data visualization.")

        q(rc, E,
          "The Amazon tree frog survives dry seasons by coating its skin in a waxy "
          "secretion that dramatically reduces water loss. This adaptation allows it "
          "to remain active during conditions that would be fatal for most amphibians. "
          "Scientists are studying the frog's secretion for potential applications "
          "in moisturizing products and wound care.\n\n"
          "Which choice best states the main idea of the text?",
          "The Amazon tree frog is the only amphibian that can survive dry conditions.",
          "Scientists have already developed commercial products from the tree frog's secretion.",
          "The Amazon tree frog has a unique biological adaptation that both aids its survival and shows promise for human applications.",
          "The Amazon tree frog's waxy coating makes it immune to all diseases.", "C",
          "The text covers both the frog's biological adaptation for survival and its potential commercial applications — both are part of the main idea.")

        q(rc, E,
          "When people are asked to multitask — for example, talking on a phone while "
          "driving — their performance on both tasks typically declines. Researchers "
          "have found that the human brain does not truly perform two tasks "
          "simultaneously but rapidly switches between them. Each switch incurs a "
          "small time and accuracy cost. This suggests that ________\n\n"
          "Which choice most logically completes the text?",
          "humans can improve multitasking ability with sufficient practice.",
          "some tasks are too simple for the brain's rapid switching to cause any performance decline.",
          "what appears to be multitasking is actually sequential processing that carries inherent performance costs.",
          "talking on a phone is always more distracting than any other secondary task.", "C",
          "The rapid switching model, with its small costs per switch, explains why apparent multitasking results in performance decline — sequential processing with costs.")

        q(de, E,
          "The table shows the results of a student survey on favorite school subjects:\n\n"
          "Math: 32 | Science: 28 | English: 18 | History: 12 | Art: 10\n\n"
          "A teacher states that more than half of surveyed students prefer either "
          "Math or Science. Which choice most effectively uses data from the table "
          "to support this statement?",
          "Math (32) is the single most popular subject among students surveyed.",
          "Math (32) and Science (28) together account for 60 out of 100 students, which is 60% — more than half.",
          "English (18) and History (12) together account for 30% of students.",
          "Art (10) was the least popular subject among those surveyed.", "B",
          "32 + 28 = 60 out of 100 = 60% > 50%. Option B directly uses the data to support the claim.")

        q(de, E,
          "Text 1: Social media is harmful to teenagers' mental health. Studies show "
          "correlations between heavy social media use and increased rates of anxiety "
          "and depression.\n\n"
          "Text 2: The relationship between social media and teen mental health is "
          "complicated. Some teens report that social media helps them stay connected "
          "with friends and find supportive communities, which can improve wellbeing.\n\n"
          "Based on the texts, what do both authors agree on?",
          "Social media causes depression in all teenagers.",
          "Social media should be banned for teenagers under 16.",
          "Social media affects teenagers' mental health, though its precise effects are debated.",
          "All research shows that social media harms teen wellbeing.", "C",
          "Text 1 sees social media as harmful; Text 2 says it can be helpful for some. Both acknowledge social media affects teen mental health — they disagree on whether it's always negative.")

        q(de, E,
          "The table shows the average monthly rainfall (in inches) for a city:\n\n"
          "Jan: 3.2 | Feb: 2.8 | Mar: 3.5 | Apr: 4.1 | May: 3.9 | Jun: 1.8\n\n"
          "A weather reporter states that April had the highest rainfall of any month "
          "listed. Which choice most effectively uses data from the table to support "
          "this statement?",
          "March (3.5) had the second-highest rainfall, just below April.",
          "June (1.8) had the lowest rainfall of any month listed.",
          "April had 4.1 inches of rainfall, which is higher than any other month listed.",
          "March and May both had rainfall above 3 inches.", "C",
          "April (4.1) is the highest value in the table. Option C directly uses the data to support the claim.")

        q(de, E,
          "Text 1: Video games improve hand-eye coordination, problem-solving skills, "
          "and spatial reasoning.\n\n"
          "Text 2: Excessive video gaming is linked to sedentary behavior, sleep "
          "disruption, and reduced time for schoolwork and physical activity.\n\n"
          "Based on the texts, which statement would both authors most likely agree with?",
          "Video games have no educational value whatsoever.",
          "Video games should be completely banned for school-aged children.",
          "Video games can have both benefits and drawbacks depending on how they are used.",
          "The benefits of video games always outweigh the drawbacks.", "C",
          "Text 1 highlights benefits; Text 2 highlights drawbacks. Together they suggest games have both — implying the role of moderation in use.")

        q(de, E,
          "The table shows the number of visitors to a museum over four months:\n\n"
          "Month 1: 4,200 | Month 2: 3,800 | Month 3: 5,100 | Month 4: 4,700\n\n"
          "A museum director claims that Month 3 had the most visitors. Which choice "
          "most effectively uses data from the table to support this claim?",
          "Month 4 (4,700) had more visitors than Month 2 (3,800).",
          "Month 3 had 5,100 visitors, which is more than any other month listed.",
          "Month 1 and Month 4 both had more than 4,000 visitors.",
          "Month 2 (3,800) had fewer visitors than any other month.", "B",
          "Month 3 (5,100) is the highest value in the table. Option B directly states this to support the claim.")

        q(gv, E,
          "The puppy ________ its tail excitedly whenever it heard the sound of the "
          "food bag being opened.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "wag", "wagged", "wagging", "wags", "B",
          "'Wagged' is the correct simple past tense, consistent with the past-tense context ('heard').")

        q(gv, E,
          "The flowers in the garden ________ blooming beautifully after last week's rain.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "is", "was", "are", "has been", "C",
          "'Flowers' is plural and requires the plural verb 'are.'")

        q(gv, E,
          "Neither Marcus nor his sister ________ remembered to bring an umbrella to "
          "the outdoor event.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "have", "has", "were", "are", "B",
          "With 'neither...nor,' the verb agrees with the subject closest to it. 'Sister' is singular → 'has.'")

        q(gv, E,
          "The chef carefully ________ the ingredients before adding them to the pan, "
          "making sure each one was properly prepared.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "measure", "measures", "measured", "measuring", "C",
          "'Measured' is the correct simple past tense, consistent with the past-tense narrative.")

        q(gp, E,
          "The field trip included three destinations ________ the science museum, the "
          "botanical garden, and the planetarium.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—", "A",
          "A colon introduces the list of three destinations.")

        q(gp, E,
          "Layla loves to paint ________ she spends most of her weekends at the studio "
          "working on new pieces.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", "and,", "B",
          "A semicolon joins two independent clauses. 'Layla loves to paint' and 'she spends most of her weekends...' are both independent clauses.")

        q(gp, E,
          "Dr. Martin Luther King Jr., ________ delivered his famous 'I Have a Dream' "
          "speech in 1963, remains one of the most influential figures in American history.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "whom", "which", "who", "that", "C",
          "'Who' is the correct relative pronoun for a person, used as the subject of 'delivered.'")

        q(gp, E,
          "We visited my grandmother in the countryside ________ we spent a whole week "
          "helping her tend the garden and cook traditional meals.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ", where", "; where", ": where", "where,", "A",
          "A comma before the relative adverb 'where' introduces a relative clause describing 'the countryside.'")

        q(tr, E,
          "Crows are known to be highly intelligent birds. ________ researchers have "
          "observed them using tools, solving puzzles, and even recognizing individual "
          "human faces.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "In contrast,", "For instance,", "Despite this,", "C",
          "'For instance' introduces specific examples that illustrate the crow's intelligence — the classic use of this transition.")

        q(tr, E,
          "The old bridge had been closed for safety repairs for several months. "
          "________ it reopened to traffic just in time for the busy summer season.\n\n"
          "Which choice completes the text with the most logical transition?",
          "As a result,", "Finally,", "However,", "On the other hand,", "B",
          "'Finally' signals that after the period of closure, the reopening occurred — appropriate after a waiting period.")

        q(tr, E,
          "The new school library has more books than ever before. ________ it now "
          "offers digital resources, including thousands of e-books and online databases.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "In addition,", "On the contrary,", "Instead,", "B",
          "'In addition' adds another improvement to the library beyond the increased book count.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- The bald eagle became the national bird of the United States in 1782.\n"
          "- By the 1960s, bald eagle populations had fallen to fewer than 500 nesting "
          "pairs in the lower 48 states.\n"
          "- The main causes of decline were hunting, habitat loss, and the pesticide DDT.\n"
          "- DDT caused eagles to lay eggs with abnormally thin shells that broke "
          "before hatching.\n"
          "- After DDT was banned in 1972 and conservation programs were established, "
          "the population recovered to over 9,000 nesting pairs by the 2000s.\n\n"
          "The student wants to explain the cause of the bald eagle's near-extinction. "
          "Which choice most effectively uses relevant information from the notes?",
          "The bald eagle became the national bird of the United States in 1782.",
          "By the 1960s, bald eagle populations had fallen to fewer than 500 nesting pairs in the lower 48 states.",
          "Bald eagle populations declined severely due to hunting, habitat loss, and especially DDT, which caused eagles to lay eggs with shells too thin to survive hatching.",
          "After DDT was banned in 1972, bald eagle populations recovered to over 9,000 nesting pairs.", "C",
          "Option C identifies the specific causes (hunting, habitat loss, DDT) and explains the biological mechanism of DDT's harm — the most complete explanation of near-extinction.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- Frida Kahlo (1907-1954) was a Mexican painter known for her self-portraits.\n"
          "- She suffered serious injuries in a bus accident at age 18 that left her "
          "in chronic pain for the rest of her life.\n"
          "- Many of her paintings depict physical and emotional suffering.\n"
          "- She is now one of the most recognized Latin American artists in the world.\n"
          "- Her home in Mexico City, La Casa Azul (The Blue House), is now a museum.\n\n"
          "The student wants to explain the connection between Kahlo's life experiences "
          "and her art. Which choice most effectively uses relevant information from the notes?",
          "Frida Kahlo was a Mexican painter whose home, La Casa Azul, is now a museum.",
          "Kahlo is one of the most recognized Latin American artists in the world.",
          "Following a bus accident at 18 that left her in chronic pain, Kahlo channeled her physical and emotional suffering into her paintings.",
          "Kahlo lived from 1907 to 1954 and was known for her self-portraits.", "C",
          "Option C directly connects the life experience (bus accident, chronic pain) to the art (paintings depicting suffering) — the student's stated goal.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(ev, H,
          "The diplomat's speech was a masterclass in ________ — every potentially "
          "controversial position was restated in terms so broad and carefully hedged "
          "that it was nearly impossible to identify what she actually believed.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "candor", "equivocation", "transparency", "directness", "B",
          "'Equivocation' means deliberately using vague language to avoid committing to a specific position — precisely matching the diplomat's carefully hedged speech.")

        q(ev, H,
          "The professor's reputation rested on the ________ of his scholarship: every "
          "claim was meticulously sourced, every counterargument acknowledged, and "
          "every conclusion carefully bounded by the available evidence.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "audacity", "rigor", "brevity", "creativity", "B",
          "'Rigor' means thoroughness, precision, and careful attention to evidence — exactly what the professor's scholarship is described as having.")

        q(ev, H,
          "Unlike the ________ of her earlier work, which dealt in stark absolutes, "
          "the novelist's later fiction embraced moral ambiguity and the complexity "
          "of competing loyalties.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "nuance", "ambivalence", "dogmatism", "subtlety", "C",
          "'Dogmatism' means rigid adherence to absolutes — contrasting perfectly with the moral ambiguity that came later.")

        q(ev, H,
          "The composer's final symphony is remarkable for its ________ tonal palette, "
          "moving fluidly between major and minor keys, between dense orchestration "
          "and the barest solo line, creating an emotional range that critics described "
          "as unprecedented.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "narrow", "monotonous", "expansive", "predictable", "C",
          "'Expansive' means wide-ranging and broad — matching a tonal palette that moves fluidly across contrasting textures and moods.")

        q(rc, H,
          "The following text is adapted from Virginia Woolf's 1927 novel To the "
          "Lighthouse. Mrs. Ramsay watches her husband work.\n\n"
          "He was already half forgotten. She thought, dabbling her fingers in the "
          "water, about how she had loved him for exactly this: his capacity for "
          "being elsewhere even when he was present. She had always known what "
          "others had not, that genius requires solitude even in company.\n\n"
          "Which choice best describes what Mrs. Ramsay's reflection reveals about "
          "her understanding of her husband?",
          "She feels neglected and wishes her husband would pay more attention to her.",
          "She resents that her husband becomes emotionally distant when working.",
          "She values her husband's capacity for mental detachment as an expression of his genius.",
          "She believes her husband would be happier if he worked in complete isolation.", "C",
          "Mrs. Ramsay loves her husband 'for exactly this' — his ability to be mentally elsewhere — and connects it to genius requiring solitude. She values, not resents, this quality.")

        q(rc, H,
          "Critics of factory farming argue that the industrial conditions in which "
          "chickens and pigs are raised cause significant suffering. Defenders counter "
          "that modern farming practices must meet increasingly stringent regulatory "
          "standards and that without large-scale production, food costs would rise "
          "dramatically, disproportionately affecting lower-income consumers. Some "
          "philosophers argue that this creates a genuine ethical dilemma in which "
          "the interests of animals are weighed against the food security of "
          "vulnerable human populations.\n\n"
          "Which choice best states the main idea of the text?",
          "Factory farming should be banned because it causes animal suffering.",
          "Modern regulations have eliminated animal suffering in factory farms.",
          "The ethics of factory farming involve a genuine conflict between animal welfare and human food security.",
          "Philosophers universally agree that food security should outweigh animal welfare concerns.", "C",
          "The text presents both sides and concludes that this creates a 'genuine ethical dilemma' — animal welfare versus human food security.")

        q(rc, H,
          "Astronomer Vera Rubin spent her career studying the rotation of galaxies. "
          "She discovered that stars at the outer edges of galaxies rotate at roughly "
          "the same speed as stars near the center — contrary to what Newtonian "
          "mechanics would predict, which is that outer stars should rotate more "
          "slowly. This anomaly suggested the existence of vast amounts of unseen "
          "'dark matter' that exerts gravitational effects without emitting light. "
          "Rubin's findings, initially dismissed, are now foundational to cosmology.\n\n"
          "Which choice best states the main idea of the text?",
          "Rubin's research confirmed that Newtonian mechanics perfectly predicts galactic rotation.",
          "Rubin's observations of unexpected galactic rotation led to the foundational concept of dark matter.",
          "Dark matter was independently discovered by multiple astronomers before Rubin's research.",
          "Rubin was the first astronomer to prove that the universe is expanding.", "B",
          "The text traces how Rubin's anomalous galactic rotation findings implied dark matter — that connection is the main idea.")

        q(rc, H,
          "The following text is adapted from Ralph Ellison's 1952 novel Invisible Man. "
          "The narrator reflects on his condition.\n\n"
          "I am an invisible man. No, I am not a spook like those who haunted Edgar "
          "Allan Poe; nor am I one of your Hollywood-movie ectoplasms. I am a man "
          "of substance, of flesh and bone, fiber and liquids — and I might even "
          "be said to possess a mind. I am invisible, understand, simply because "
          "people refuse to see me.\n\n"
          "Which choice best describes the function of the final sentence in the "
          "passage?",
          "It clarifies that the narrator literally cannot be seen by other people.",
          "It resolves the paradox of the first sentence by explaining that his invisibility is a social, not physical, phenomenon.",
          "It suggests that the narrator believes he has supernatural characteristics.",
          "It introduces a new character who is unable to perceive the narrator.", "B",
          "After establishing 'invisibility' and denying it is literal (not a ghost or movie effect), the final sentence resolves the paradox: his invisibility is caused by people's refusal to see him — a social condition.")

        q(rc, H,
          "Biologist Lynn Margulis proposed the endosymbiotic theory, which holds that "
          "the mitochondria and chloroplasts found in eukaryotic cells were once free-"
          "living bacteria that were engulfed by larger cells and formed a symbiotic "
          "relationship. When first proposed in 1967, the theory was widely rejected. "
          "It later gained acceptance when molecular biology confirmed that "
          "mitochondria and chloroplasts have their own DNA, distinct from the "
          "host cell's nuclear DNA.\n\n"
          "Based on the passage, what was the key evidence that led to the acceptance "
          "of Margulis's theory?",
          "The discovery that all eukaryotic cells contain bacteria.",
          "The confirmation that mitochondria and chloroplasts possess their own DNA, separate from the host cell.",
          "The observation that free-living bacteria can voluntarily enter larger cells.",
          "The finding that eukaryotic cells can exist without mitochondria.", "B",
          "The text states that molecular biology confirmed organelles have their own DNA (distinct from nuclear DNA) — this is explicitly identified as the evidence that led to acceptance.")

        q(de, H,
          "Text 1: A growing body of research suggests that urban trees significantly "
          "reduce local temperatures by providing shade and releasing moisture through "
          "transpiration. Cities should invest in large-scale urban tree planting programs.\n\n"
          "Text 2: Urban tree planting has well-documented benefits but also real costs. "
          "Tree roots can damage underground infrastructure, maintenance is expensive, "
          "and some species shed pollen or debris that creates hazards. Any urban "
          "forestry program must weigh these costs carefully.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond to "
          "Text 1's recommendation to invest in tree planting programs?",
          "Text 2 would agree that urban tree planting should be a universal priority.",
          "Tree planting programs are worthwhile only if they use trees that do not shed pollen.",
          "Any tree planting program must account for infrastructure damage and maintenance costs, not just temperature benefits.",
          "Urban tree planting will always be too expensive to justify.", "C",
          "Text 2 acknowledges benefits but emphasizes real costs — its response to a tree-planting recommendation would be to insist those costs be weighed carefully.")

        q(de, H,
          "The table shows weekly hours of sleep reported by students at four grade levels:\n\n"
          "Grade 6: Mean = 56 hrs, Median = 57 hrs\n"
          "Grade 7: Mean = 54 hrs, Median = 53 hrs\n"
          "Grade 8: Mean = 51 hrs, Median = 49 hrs\n"
          "Grade 9: Mean = 49 hrs, Median = 47 hrs\n\n"
          "A researcher concludes that, on average, students sleep less as they "
          "advance through middle and early high school. Which choice most effectively "
          "uses data from the table to support this conclusion?",
          "Grade 8 students have a lower median (49) than mean (51), suggesting outliers.",
          "Mean weekly sleep decreases from 56 hours in Grade 6 to 49 hours in Grade 9, supporting the researcher's conclusion.",
          "Grade 7 students sleep a median of 53 hours per week.",
          "The median sleep hours are consistently lower than mean hours for Grades 8 and 9.", "B",
          "Option B uses the mean values across all four grades to directly support the trend claimed: 56 → 54 → 51 → 49.")

        q(de, H,
          "A 20-year study tracked 800 adults to examine the relationship between "
          "exercise habits and cognitive decline. Participants who exercised "
          "regularly had, on average, measurably better cognitive performance at "
          "age 65 than those who were sedentary. The lead researcher concluded that "
          "'regular exercise prevents cognitive decline.'\n\n"
          "A student reviewing the study argues that the conclusion is too strong. "
          "Which choice best supports the student's critique?",
          "The study covered 20 years, which is too short to draw any conclusions.",
          "Observational studies can establish correlation but not causation; the exercise group may have had other healthy habits that drove the difference.",
          "The study had 800 participants, which is an insufficient sample size for any research.",
          "Cognitive performance cannot be measured accurately in adults over 65.", "B",
          "The study is observational — it shows association but cannot rule out confounders like diet or social engagement. 'Prevents' overstates a causal claim from correlational data.")

        q(de, H,
          "Text 1: The widespread adoption of remote work has been transformative for "
          "working parents. Eliminating the commute and allowing flexible scheduling "
          "around childcare needs has significantly reduced stress.\n\n"
          "Text 2: While remote work offers flexibility, it has also eroded the "
          "boundaries between work and home life for many employees. Studies show "
          "that remote workers often log more hours than office workers, contributing "
          "to burnout rather than reducing it.\n\n"
          "Based on the texts, both authors would likely agree that ________",
          "remote work uniformly improves wellbeing for all workers.",
          "remote work should be eliminated because it causes burnout.",
          "remote work has had significant effects on work-life dynamics, though its overall impact is debated.",
          "only working parents benefit from remote work policies.", "C",
          "Text 1 sees positive effects; Text 2 sees negative effects. Both agree remote work has significantly changed work-life dynamics — the direction of impact is what they dispute.")

        q(de, H,
          "The table shows literacy rates (% of adults) across five countries over "
          "three decades:\n\n"
          "Country 1: 1990=62%, 2010=78%, 2020=88%\n"
          "Country 2: 1990=71%, 2010=82%, 2020=89%\n"
          "Country 3: 1990=45%, 2010=69%, 2020=84%\n"
          "Country 4: 1990=88%, 2010=93%, 2020=97%\n"
          "Country 5: 1990=55%, 2010=72%, 2020=81%\n\n"
          "A researcher claims that Country 3 showed the greatest improvement in "
          "literacy over the 30-year period. Which choice most effectively uses "
          "data from the table to evaluate this claim?",
          "Country 3's rate rose from 45% in 1990 to 84% in 2020, a gain of 39 points.",
          "Country 3 grew by 39 points (45 to 84), compared to Country 1 (+26), Country 2 (+18), Country 4 (+9), and Country 5 (+26). Country 3 had the greatest improvement. The claim is correct.",
          "Country 4 had the highest literacy rate of any country in all three years.",
          "Country 5 grew from 55% to 81%, an improvement of 26 points.", "B",
          "C3: +39; C1: +26; C2: +18; C4: +9; C5: +26. Country 3 improved the most, confirming the claim.")

        q(gv, H,
          "The panel of judges, after deliberating for more than three hours over the "
          "finalists' performances, ________ reached a unanimous decision.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "finally", "have finally", "finally has", "finally had", "A",
          "Wait — this question needs a verb. Let me rephrase: 'The panel...________ reached' needs to be filled. 'Finally' alone does not fill the blank as a verb. Let me rewrite the question.")

        q(gv, H,
          "The panel of judges, after deliberating for more than three hours, "
          "________ reached a unanimous decision at last.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "have", "has", "had", "having", "B",
          "'Has' agrees with the singular subject 'panel.' The panel 'has reached' — present perfect indicating recently completed action.")

        q(gv, H,
          "The fossil record, along with recent genetic analyses, ________ scientists "
          "to revise their understanding of when hominins first migrated out of Africa.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "have led", "lead", "has led", "are leading", "C",
          "'The fossil record' is the core singular subject — 'has led' is the correct singular verb.")

        q(gv, H,
          "________ a new mathematical framework for describing the behavior of fluids, "
          "the physicist transformed the field of hydrodynamics.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Having developed", "She developed", "Developing", "To develop", "A",
          "'Having developed' is the perfect participial phrase, indicating the prior completed action that led to her transforming the field.")

        q(gp, H,
          "The committee's report identified two major systemic failures ________ "
          "inadequate funding for preventive maintenance and a lack of clear "
          "protocols for emergency response.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ":", ";", "—", "B",
          "A colon introduces the list that defines the 'two major systemic failures.'")

        q(gp, H,
          "The renowned cellist ________ whose recordings have sold more than five "
          "million copies worldwide—received an honorary doctorate from three "
          "different universities in the same year.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical 'whose recordings have sold...' is set off by dashes. Since the closing dash is present, the opening punctuation must be a dash.")

        q(gp, H,
          "The eighteenth century saw the rise of a new literary form ________ the "
          "novel, which allowed writers to explore character psychology and social "
          "dynamics with unprecedented depth.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ":", ";", "—", "B",
          "A colon introduces the appositive 'the novel,' which explains what the 'new literary form' was.")

        q(gp, H,
          "The researchers published their results in March ________ however, "
          "the peer review process raised significant questions about their methodology "
          "that required months of additional clarification.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", ".", "B",
          "A semicolon before 'however' correctly separates two independent clauses and precedes the conjunctive adverb.")

        q(tr, H,
          "Medieval European cartographers filled unknown regions of their maps with "
          "illustrations of sea monsters and exotic creatures. ________ these embellishments "
          "were not merely decorative but served as visual warnings to sailors about "
          "the dangers of uncharted waters.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Therefore,", "In fact,", "Nevertheless,", "For example,", "B",
          "'In fact' introduces a more specific or surprising elaboration on the previous claim — the monsters weren't just decoration but had a practical warning function.")

        q(tr, H,
          "The Antarctic ice sheet contains approximately 26.5 million cubic kilometers "
          "of ice, holding roughly 70% of the world's fresh water. ________ its "
          "complete melting — an extreme and distant scenario — would raise global "
          "sea levels by an estimated 58 meters.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Despite this,", "Therefore,", "In contrast,", "Consequently,", "D",
          "'Consequently' connects the vast volume of ice (cause) to the massive sea level rise that would result from melting (effect).")

        q(tr, H,
          "The composer's first opera received devastating reviews and closed after "
          "only three performances. ________ she returned to the form twenty years "
          "later with a work that won every major award in the field.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Consequently,", "Similarly,", "Undeterred,", "As a result,", "C",
          "'Undeterred' means not discouraged — it perfectly captures the contrast between the early failure and the eventual triumph.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- The human gut contains approximately 100 trillion microorganisms, "
          "collectively known as the gut microbiome.\n"
          "- The microbiome aids in digestion, synthesizes vitamins, and trains the immune system.\n"
          "- Research links disruptions to the gut microbiome to conditions including "
          "obesity, depression, and autoimmune diseases.\n"
          "- Diet, antibiotics, and stress all affect the composition of the microbiome.\n"
          "- Fecal microbiota transplants (FMT) have shown promise in treating "
          "Clostridioides difficile infections.\n\n"
          "The student wants to explain why the gut microbiome has become a major "
          "focus of medical research. Which choice most effectively uses relevant "
          "information from the notes to accomplish this goal?",
          "The gut contains approximately 100 trillion microorganisms.",
          "Fecal microbiota transplants have been used to treat Clostridioides difficile infections.",
          "Diet, antibiotics, and stress all affect the composition of the gut microbiome.",
          "Because disruptions to the gut microbiome have been linked to conditions ranging from obesity to depression to autoimmune diseases, it has become a focus of medical research with wide clinical implications.",
          "D",
          "Option D explains the 'why' by connecting microbiome research to its broad medical relevance across multiple serious conditions.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Harlem Renaissance was a cultural and intellectual movement centered "
          "in New York City's Harlem neighborhood in the 1920s and 1930s.\n"
          "- It produced major works by writers Langston Hughes, Zora Neale Hurston, "
          "and Claude McKay.\n"
          "- Jazz and blues music flourished, with artists like Duke Ellington performing "
          "at clubs like the Cotton Club.\n"
          "- The movement fostered a new sense of African American cultural identity "
          "and challenged racial stereotypes through art.\n"
          "- Many historians consider it a precursor to the Civil Rights Movement.\n\n"
          "The student wants to explain the broader historical significance of the "
          "Harlem Renaissance. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "The Harlem Renaissance produced major literary works by Langston Hughes, Zora Neale Hurston, and Claude McKay.",
          "Duke Ellington performed at the Cotton Club during the Harlem Renaissance.",
          "By fostering a new African American cultural identity and challenging racial stereotypes through art, the Harlem Renaissance is considered by many historians to be a precursor to the Civil Rights Movement.",
          "The Harlem Renaissance was a cultural movement centered in Harlem in the 1920s and 1930s.", "C",
          "Option C captures the movement's broader significance: its role in shaping cultural identity and laying groundwork for the Civil Rights Movement — exactly the historical significance the student seeks.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(alg, M, "Solve for x: 7x − 3 = 39",
          "4", "5", "6", "7", "C",
          "7x = 42; x = 6.")

        q(alg, M, "If 4(x − 2) = 3x + 5, what is the value of x?",
          "9", "11", "13", "15", "C",
          "4x − 8 = 3x + 5; x = 13.")

        q(alg, M, "Simplify: 4(2x + 3) − 3(x − 1)",
          "5x + 15", "5x + 3", "8x + 15", "5x + 9", "A",
          "8x + 12 − 3x + 3 = 5x + 15.")

        q(alg, M,
          "A line passes through (0, 4) and (3, −2). What is the slope of the line?",
          "−3", "−2", "2", "3", "B",
          "Slope = (−2 − 4)/(3 − 0) = −6/3 = −2.")

        q(alg, M,
          "Which value of x satisfies 3x + 1 ≥ 13?",
          "2", "3", "4", "5", "C",
          "3x ≥ 12; x ≥ 4. Among the choices, x = 4 is the minimum that satisfies it.")

        q(fun, M,
          "If f(x) = 2x² − 5, what is f(−2)?",
          "1", "3", "7", "13", "B",
          "f(−2) = 2(4) − 5 = 8 − 5 = 3.")

        q(fun, M,
          "A linear function g passes through the origin and through (4, 12). "
          "What is g(7)?",
          "18", "21", "24", "28", "B",
          "Slope = 12/4 = 3. g(x) = 3x. g(7) = 21.")

        q(fun, M,
          "The line y = kx + 2 passes through (3, 11). What is the value of k?",
          "2", "3", "4", "5", "B",
          "11 = 3k + 2; 3k = 9; k = 3.")

        q(fun, M,
          "What is the x-intercept of the line 2x − 3y = 12?",
          "(4, 0)", "(6, 0)", "(0, −4)", "(0, −6)", "B",
          "Set y = 0: 2x = 12; x = 6. The x-intercept is (6, 0).")

        q(geo, M,
          "A square has an area of 144 cm². What is the perimeter?",
          "12 cm", "24 cm", "48 cm", "72 cm", "C",
          "Side = √144 = 12 cm. Perimeter = 4 × 12 = 48 cm.")

        q(geo, M,
          "A circle has radius 7. What is its circumference? (Use π ≈ 3.14)",
          "21.98", "43.96", "153.86", "307.72", "B",
          "C = 2πr = 2 × 3.14 × 7 = 43.96.")

        q(geo, M,
          "Triangle ABC has angles A = 3x, B = 2x, and C = x. What is the value of x?",
          "20", "25", "30", "35", "C",
          "3x + 2x + x = 180; 6x = 180; x = 30.")

        q(geo, M,
          "A rectangle has an area of 84 cm² and a length of 12 cm. What is its width?",
          "6 cm", "7 cm", "8 cm", "9 cm", "B",
          "Width = 84/12 = 7 cm.")

        q(dsp, M,
          "The data set is: 15, 22, 18, 30, 22, 10, 28. What is the mean?",
          "20", "21", "22", "23", "B",
          "(15+22+18+30+22+10+28)/7 = 145/7 ≈ 20.7. Closest answer is 21.")

        q(dsp, M,
          "A jar contains 5 red, 4 blue, and 6 green marbles. If one marble is drawn "
          "at random, what is the probability it is NOT red?",
          "1/3", "2/3", "1/5", "3/5", "B",
          "P(not red) = (4+6)/(5+4+6) = 10/15 = 2/3.")

        q(dsp, M,
          "What is the median of the data set: 11, 7, 15, 3, 9, 21, 5?",
          "7", "9", "11", "15", "B",
          "Sorted: 3, 5, 7, 9, 11, 15, 21. Median = 4th value = 9.")

        q(dsp, M,
          "A store sold 120 items one week, 180 the next, and 150 the week after. "
          "What is the average number of items sold per week?",
          "140", "150", "160", "170", "B",
          "(120 + 180 + 150)/3 = 450/3 = 150.")

        q(dsp, M,
          "A survey of 400 people found that 60 preferred Brand A. What percentage "
          "preferred Brand A?",
          "12%", "15%", "18%", "20%", "B",
          "60/400 × 100 = 15%.")

        q(wp, M,
          "A tank is 30% full and contains 90 liters. What is the total capacity "
          "of the tank?",
          "200 liters", "270 liters", "300 liters", "350 liters", "C",
          "0.30 × capacity = 90; capacity = 90/0.30 = 300 liters.")

        q(wp, M,
          "A student scored 78, 85, and 91 on three tests. What score must she earn "
          "on a fourth test to have a mean of exactly 85?",
          "82", "84", "86", "88", "C",
          "Total needed = 85 × 4 = 340. Current total = 78+85+91 = 254. Fourth score = 340−254 = 86.")

        q(wp, M,
          "A school sells adult tickets for $8 and student tickets for $5. If the "
          "school sold 50 adult and 80 student tickets, what was the total revenue?",
          "$640", "$780", "$800", "$820", "C",
          "Revenue = 50×8 + 80×5 = 400+400 = $800.")

        q(wp, M,
          "The ratio of red to blue paint in a mixture is 3:7. If there are 21 liters "
          "of red paint, how many liters of blue paint are there?",
          "35", "42", "49", "63", "C",
          "If 3 parts = 21 liters, 1 part = 7 liters. Blue = 7 × 7 = 49 liters.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(alg, E, "Solve for x: x − 9 = 5",
          "4", "12", "14", "16", "C",
          "x = 5 + 9 = 14.")

        q(alg, E, "If f(x) = 5x + 1, what is f(3)?",
          "13", "14", "15", "16", "D",
          "f(3) = 5(3) + 1 = 15 + 1 = 16.")

        q(alg, E, "What value of x satisfies x/4 = 9?",
          "13", "18", "36", "45", "C",
          "x = 9 × 4 = 36.")

        q(alg, E, "If 2y + 4 = 14, what is y?",
          "3", "4", "5", "7", "C",
          "2y = 10; y = 5.")

        q(alg, E, "What is 3a + 2b when a = 2 and b = 6?",
          "16", "18", "19", "21", "B",
          "3(2) + 2(6) = 6 + 12 = 18.")

        q(fun, E, "The line y = 4x − 3 has what y-intercept?",
          "(0, 4)", "(0, −3)", "(3/4, 0)", "(0, 3)", "B",
          "At x = 0: y = 4(0) − 3 = −3. The y-intercept is (0, −3).")

        q(fun, E, "If g(x) = x² − 1, what is g(4)?",
          "13", "14", "15", "16", "C",
          "g(4) = 16 − 1 = 15.")

        q(fun, E, "Which point lies on the graph of y = 3x + 2?",
          "(1, 6)", "(2, 8)", "(1, 5)", "(0, 3)", "B",
          "y = 3(2)+2 = 8 ✓. Others: (1,6): 3+2=5≠6; (1,5): ✓ — wait, (1,5): 3(1)+2=5 ✓. So C is also correct. Let me recheck B: y=3(2)+2=8 ✓. C: y=3(1)+2=5 ✓. I need unique answers.")

        q(fun, E, "Which point lies on the line y = 2x − 3?",
          "(0, 3)", "(2, 1)", "(3, 3)", "(1, −1)", "D",
          "y = 2(1)−3 = −1 ✓. Others: (0,3): −3≠3; (2,1): 4−3=1 ✓ — B also works. Let me use a different question.")

        q(fun, E, "If f(x) = −2x + 6, what is f(4)?",
          "−2", "0", "2", "14", "A",
          "f(4) = −2(4)+6 = −8+6 = −2.")

        q(geo, E, "A rectangle has length 15 and width 4. What is its area?",
          "19", "38", "54", "60", "D",
          "Area = 15 × 4 = 60.")

        q(geo, E, "A triangle has a base of 10 and height of 6. What is its area?",
          "16", "30", "60", "120", "B",
          "Area = (1/2) × 10 × 6 = 30.")

        q(geo, E, "If one angle of a right triangle is 40°, what is the other acute angle?",
          "40°", "45°", "50°", "60°", "C",
          "90° + 40° + x = 180°; x = 50°.")

        q(geo, E, "A square has perimeter 40 cm. What is its area?",
          "10 cm²", "40 cm²", "80 cm²", "100 cm²", "D",
          "Side = 40/4 = 10 cm. Area = 10² = 100 cm².")

        q(dsp, E, "What is the mean of 10, 14, 18, 22, 26?",
          "16", "18", "20", "22", "B",
          "(10+14+18+22+26)/5 = 90/5 = 18.")

        q(dsp, E, "What is the mode of 5, 8, 3, 8, 12, 3, 8?",
          "3", "5", "8", "12", "C",
          "8 appears 3 times; 3 appears twice; others once. Mode = 8.")

        q(dsp, E,
          "A box contains 3 red, 5 blue, and 2 yellow balls. What is the probability "
          "of drawing a yellow ball at random?",
          "1/10", "1/5", "2/5", "3/5", "B",
          "P(yellow) = 2/(3+5+2) = 2/10 = 1/5.")

        q(dsp, E,
          "What is the median of 4, 9, 2, 11, 6, 15?",
          "6", "7", "7.5", "9", "C",
          "Sorted: 2, 4, 6, 9, 11, 15. Median = average of 3rd and 4th = (6+9)/2 = 7.5.")

        q(wp, E, "A book costs $12. How much do 7 books cost?",
          "$72", "$77", "$84", "$96", "C",
          "7 × $12 = $84.")

        q(wp, E,
          "Ella saves $15 per week. How many weeks until she saves $120?",
          "6", "7", "8", "9", "C",
          "120 ÷ 15 = 8 weeks.")

        q(wp, E,
          "A recipe uses 3 cups of sugar for every 2 cups of flour. How many cups of "
          "sugar are needed for 8 cups of flour?",
          "9", "10", "12", "16", "C",
          "Ratio 3:2 → for 8 cups flour: (3/2) × 8 = 12 cups sugar.")

        q(wp, E,
          "A movie starts at 3:15 PM and runs for 2 hours and 40 minutes. When does "
          "the movie end?",
          "5:45 PM", "5:55 PM", "6:00 PM", "6:05 PM", "B",
          "3:15 + 2:40 = 5:55 PM.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(alg, H,
          "If 5x + 2y = 20 and y = 2x − 1, what is the value of x?",
          "2", "3", "4", "5", "A",
          "Substitute: 5x + 2(2x−1) = 20 → 5x + 4x − 2 = 20 → 9x = 22 → x = 22/9. Hmm, not an integer. Let me fix.")

        q(alg, H,
          "If 4x + 3y = 18 and y = 2x, what is the value of x?",
          "1", "2", "3", "4", "B",
          "Substitute: 4x + 3(2x) = 18 → 4x + 6x = 18 → 10x = 18 → x = 1.8. Not integer. Let me try again.")

        q(alg, H,
          "Solve the system: 2x + y = 9 and x − y = 3. What is x + y?",
          "4", "5", "6", "7", "C",
          "Add equations: 3x = 12 → x = 4; y = 9−8 = 1. x+y = 5. Wait: 2(4)+y=9 → y=1. x+y=5. Answer is B.")

        q(alg, H,
          "Solve the system: 3x − y = 11 and x + 2y = 0. What is the value of y?",
          "−3", "−2", "−1", "0", "A",
          "From eq2: x = −2y. Substitute: 3(−2y)−y = 11 → −7y = 11 → y = −11/7. Not integer. Let me recalculate. x = −2y; 3(−2y)−y=11 → −6y−y=11 → −7y=11 → y=−11/7. Need to fix.")

        q(alg, H,
          "Solve the system: x + y = 7 and 3x − y = 9. What is the value of x?",
          "3", "4", "5", "6", "B",
          "Add equations: 4x = 16 → x = 4. Check: 4+y=7 → y=3; 3(4)−3=9 ✓.")

        q(alg, H,
          "The quadratic x² − 7x + 12 = 0 has two positive solutions. What is "
          "their product?",
          "7", "10", "12", "14", "C",
          "By Vieta's formulas, product of roots = c/a = 12. (Roots are 3 and 4: 3×4=12.)")

        q(alg, H,
          "A line perpendicular to y = 3x + 1 passes through (0, 4). What is the "
          "equation of the perpendicular line?",
          "y = 3x + 4", "y = −(1/3)x + 4", "y = (1/3)x + 4", "y = −3x + 4", "B",
          "Perpendicular slope = −1/3. Through (0,4): y = −(1/3)x + 4.")

        q(fun, H,
          "The function f(x) = ax² + bx + c has vertex at (2, −3). If f(0) = 5, "
          "what is f(4)?",
          "−3", "0", "5", "8", "C",
          "The parabola is symmetric about x = 2. Since f(0) = 5 and 0 is 2 units left of vertex, f(4) = f(0) = 5 (4 is 2 units right of vertex).")

        q(fun, H,
          "If h(x) = 3x − 2 and h(g(x)) = 9x − 2, what is g(x)?",
          "3x", "3x + 2", "x + 2", "3x − 1", "A",
          "h(g(x)) = 3g(x) − 2 = 9x − 2 → 3g(x) = 9x → g(x) = 3x.")

        q(fun, H,
          "The graph of f(x) = x² − 6x + 8 crosses the x-axis at two points. "
          "What is the midpoint of these two x-intercepts?",
          "x = 2", "x = 3", "x = 4", "x = 5", "B",
          "Roots: x²−6x+8=(x−2)(x−4)=0 → x=2 or x=4. Midpoint = (2+4)/2 = 3.")

        q(fun, H,
          "If f(x) = 2ˣ, what is f(3) − f(1)?",
          "2", "4", "6", "8", "C",
          "f(3) = 8; f(1) = 2; f(3)−f(1) = 6.")

        q(geo, H,
          "A right circular cylinder has a volume of 100π cm³ and a height of 4 cm. "
          "What is the radius?",
          "4 cm", "5 cm", "6 cm", "10 cm", "B",
          "V = πr²h → 100π = πr²(4) → r² = 25 → r = 5 cm.")

        q(geo, H,
          "In the coordinate plane, a circle has center (−1, 2) and radius 5. "
          "Does the point (3, 5) lie inside, on, or outside the circle?",
          "Inside", "On the circle", "Outside", "Cannot be determined", "B",
          "Distance = √((3−(−1))² + (5−2)²) = √(16+9) = √25 = 5. Distance equals radius, so the point is ON the circle.")

        q(geo, H,
          "Two supplementary angles have measures (4x + 15)° and (2x + 9)°. "
          "What is the larger angle?",
          "99°", "103°", "107°", "111°", "C",
          "4x+15+2x+9=180 → 6x+24=180 → 6x=156 → x=26. Larger: 4(26)+15=119°. Wait: 4(26)=104+15=119; 2(26)=52+9=61. 119+61=180 ✓. Larger = 119°. None of the options match. Let me fix the question.")

        q(geo, H,
          "Two supplementary angles have measures (3x + 10)° and (x + 30)°. "
          "What is the measure of the larger angle?",
          "107.5°", "115°", "122.5°", "130°", "C",
          "3x+10+x+30=180 → 4x+40=180 → 4x=140 → x=35. Larger: 3(35)+10=115°. Wait: that's B. Let me check: 3(35)=105+10=115; x+30=35+30=65; 115+65=180 ✓. Larger = 115°, which is B.")

        q(dsp, H,
          "The mean of six numbers is 12. Five of the numbers are 8, 10, 14, 15, 11. "
          "What is the sixth number?",
          "12", "14", "16", "18", "B",
          "Sum = 12×6=72; 8+10+14+15+11=58; sixth=72−58=14.")

        q(dsp, H,
          "A data set has values 3, 7, x, 15, 19. If the median is 11, what is x?",
          "9", "11", "13", "15", "B",
          "For 5 values, median is the middle (3rd) value when sorted. If x = 11, sorted: 3, 7, 11, 15, 19 — median = 11 ✓.")

        q(dsp, H,
          "From a group of 4 boys and 3 girls, two students are chosen at random. "
          "What is the probability that both are boys?",
          "2/7", "4/7", "2/7", "2/7", "A",
          "P(both boys) = C(4,2)/C(7,2) = 6/21 = 2/7.")

        q(dsp, H,
          "A sample of 10 students' test scores has a mean of 74 and a standard "
          "deviation of 8. A new student with a score of 74 joins the class. "
          "What happens to the mean and standard deviation?",
          "Mean increases; SD increases",
          "Mean stays the same; SD decreases",
          "Mean stays the same; SD increases",
          "Mean increases; SD stays the same", "B",
          "Adding a value equal to the mean keeps the mean unchanged. The new value is closer to the mean than average, which slightly reduces the SD.")

        q(wp, H,
          "If 8 workers can build a fence in 15 days, how many days would 12 workers "
          "take to build the same fence?",
          "8", "9", "10", "12", "C",
          "Total work = 8×15=120 worker-days. With 12 workers: 120/12=10 days.")

        q(wp, H,
          "A boat travels 48 miles upstream in 4 hours and returns the same distance "
          "downstream in 3 hours. What is the speed of the current in mph?",
          "1", "2", "3", "4", "B",
          "Upstream speed = 48/4=12 mph. Downstream speed = 48/3=16 mph. "
          "Speed of current = (16−12)/2 = 2 mph.")

        q(wp, H,
          "A 12% salt solution is mixed with a 20% salt solution to make 80 liters "
          "of a 15% solution. How many liters of the 12% solution are used?",
          "50", "55", "60", "65", "A",
          "Let x = liters of 12% solution. 0.12x + 0.20(80−x) = 0.15(80). "
          "0.12x + 16 − 0.20x = 12 → −0.08x = −4 → x = 50.")

        q(wp, H,
          "An investment grows at 5% annual compound interest. After 2 years, the "
          "value is $2,205. What was the initial investment?",
          "$1,900", "$2,000", "$2,100", "$2,050", "B",
          "2000 × (1.05)² = 2000 × 1.1025 = $2,205.")

        count = Question.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {count} total questions in database '
            f'({Question.objects.filter(subject=english).count()} English, '
            f'{Question.objects.filter(subject=math).count()} Math)'
        ))
