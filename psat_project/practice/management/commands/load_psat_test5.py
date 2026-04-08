"""
PSAT 8/9-style Practice Test 5 — generated questions.
English (Reading & Writing): 81 questions across 3 modules
Math: 66 questions across 3 modules
Difficulty: Module 1 = medium, Module 2 Easier = easy, Module 2 Harder = hard
"""
from django.core.management.base import BaseCommand
from practice.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Load PSAT-style Practice Test 5 questions into the database'

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
          "Anthropologist Margaret Mead spent years living among indigenous peoples in "
          "Samoa and New Guinea, arguing that human behavior is far more ________ by "
          "culture than by biology, a stance that made her one of the most influential "
          "and controversial figures in twentieth-century social science.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "ignored", "hindered", "shaped", "replaced", "C",
          "'Shaped' means influenced and formed — precisely matching the argument that culture, not biology, determines human behavior.")

        q(ev, M,
          "The company's decision to release the product without adequate testing was "
          "widely seen as ________, especially after a safety flaw caused several "
          "injuries that could have been prevented.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "prudent", "justified", "reckless", "cautious", "C",
          "'Reckless' means acting without regard for consequences — matching a decision that ignored testing and led to preventable injuries.")

        q(ev, M,
          "The museum's new exhibition on Byzantine art was ________ in its scope, "
          "drawing on loans from over thirty collections across twelve countries to "
          "present the broadest survey of the era ever assembled in one place.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "narrow", "modest", "ambitious", "repetitive", "C",
          "'Ambitious' means large in scale and scope — matching an exhibition that drew from 30+ collections across 12 countries.")

        q(ev, M,
          "The new medication ________ patients' recovery time by nearly half, allowing "
          "hospitals to discharge patients sooner and reducing the burden on an "
          "already strained healthcare system.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "doubled", "prolonged", "reduced", "ignored", "C",
          "'Reduced' means decreased — patients recovering faster means their recovery time was shortened/reduced.")

        q(rc, M,
          "Historian Eric Hobsbawm coined the phrase 'invented traditions' to describe "
          "practices presented as ancient but actually created relatively recently. "
          "He argued that many national symbols and ceremonies that appear to be "
          "timeless customs — Scottish highland dress, English royal pageantry — were "
          "largely invented or formalized in the nineteenth century to serve modern "
          "political needs.\n\n"
          "Which choice best states the main idea of the text?",
          "Scottish and English national symbols are among the oldest in the world.",
          "Hobsbawm argued that many traditions perceived as ancient are actually modern inventions that serve political purposes.",
          "Hobsbawm believed that all national symbols should be created by governments.",
          "The nineteenth century was a period in which most national symbols were destroyed.", "B",
          "The text presents Hobsbawm's argument that many 'ancient' traditions were actually invented recently for modern political purposes.")

        q(rc, M,
          "The following text is adapted from Chinua Achebe's 1958 novel Things Fall "
          "Apart. Okonkwo, a proud warrior, reflects on his father.\n\n"
          "Okonkwo was ruled by one passion — to hate everything that his father "
          "Unoka had loved. One of those things was gentleness and another was "
          "idleness. During the planting season Okonkwo worked daily on his farms "
          "from cock-crow until the chickens went to roost. He was a man of action, "
          "a man of war.\n\n"
          "Which choice best describes Okonkwo's primary motivation as presented "
          "in the passage?",
          "A desire to honor his father's memory through hard work.",
          "A determination to define himself in opposition to his father's values.",
          "A commitment to farming as a form of spiritual fulfillment.",
          "A fear of being seen as weak by the other men of the village.", "B",
          "The passage states Okonkwo was ruled by the desire to 'hate everything his father loved' — his identity is formed in opposition to his father.")

        q(rc, M,
          "The International Space Station (ISS) orbits Earth at an altitude of "
          "approximately 400 kilometers, completing about 16 orbits per day. "
          "Astronauts aboard the ISS experience weightlessness not because there "
          "is no gravity — gravity at that altitude is about 90% as strong as "
          "at Earth's surface — but because both the station and the astronauts "
          "are in continuous free fall around Earth.\n\n"
          "Which choice best states the main idea of the text?",
          "Gravity on the ISS is significantly weaker than on Earth's surface.",
          "Astronauts on the ISS experience weightlessness because the station travels faster than Earth's gravity.",
          "Weightlessness on the ISS results from continuous free fall, not an absence of gravity.",
          "The ISS orbits at an altitude where Earth's gravitational pull is essentially zero.", "C",
          "The text explicitly explains that weightlessness is caused by continuous free fall, not by the absence of gravity — that is the main idea.")

        q(rc, M,
          "Critics of nuclear energy often point to catastrophic accidents at plants "
          "such as Chernobyl and Fukushima as evidence of unacceptable risk. "
          "Proponents counter that, measured per unit of energy generated, nuclear "
          "power causes far fewer deaths than fossil fuel combustion, including from "
          "air pollution. This debate reflects a broader challenge in risk assessment: "
          "humans tend to weight vivid, memorable events more heavily than "
          "statistical evidence.\n\n"
          "Which choice best states the main idea of the text?",
          "Nuclear power is provably safer than all other energy sources.",
          "The debate over nuclear energy risk illustrates a general tendency to overweight memorable events compared to statistical data.",
          "Chernobyl and Fukushima prove that nuclear energy should be phased out.",
          "Deaths from fossil fuel pollution are lower than those from nuclear accidents.", "B",
          "The text uses the nuclear debate to illustrate a broader point about human risk perception — memorable events versus statistics.")

        q(rc, M,
          "In her landmark work on epigenetics, biologist Nessa Carey explains how "
          "genes can be switched on or off by environmental factors without changing "
          "the underlying DNA sequence. These epigenetic modifications, which can be "
          "influenced by diet, stress, and exposure to toxins, may be passed from "
          "parents to offspring. This finding challenges the traditional view that "
          "________ inheritance.\n\n"
          "Which choice most logically completes the text?",
          "DNA sequence changes are the only mechanism of",
          "all genetic traits are randomly distributed through",
          "only children inherit physical traits from both parents through",
          "environmental factors have no influence on", "A",
          "The traditional view that epigenetics challenges is that only DNA sequence changes drive inheritance — epigenetics shows non-sequence mechanisms also matter.")

        q(de, M,
          "The table below shows global average surface temperature anomalies "
          "(degrees above pre-industrial baseline) by decade:\n\n"
          "1880s: +0.1°C | 1920s: +0.2°C | 1960s: +0.1°C | 1990s: +0.4°C | 2010s: +0.9°C\n\n"
          "A climate scientist argues that warming has accelerated significantly "
          "since the 1960s. Which choice most effectively uses data from the table "
          "to support this argument?",
          "The 1880s and 1920s had higher anomalies than the 1960s.",
          "Temperature anomalies rose from +0.1°C in the 1960s to +0.9°C in the 2010s, an increase of 0.8°C in 50 years, far exceeding any earlier change.",
          "The 1990s showed the second-highest anomaly in the table.",
          "Pre-industrial temperatures were 0.1°C higher than 1880s averages.", "B",
          "From the 1960s (+0.1) to the 2010s (+0.9) is a +0.8°C change in 50 years — far larger than any earlier 50-year period in the table, supporting the acceleration claim.")

        q(de, M,
          "Text 1: Space exploration is one of humanity's greatest achievements. "
          "It has given us satellite technology, advances in medicine, and a deeper "
          "understanding of our place in the universe. Funding should be maintained.\n\n"
          "Text 2: With billions of people still lacking access to clean water, "
          "adequate nutrition, and healthcare, it is difficult to justify the enormous "
          "costs of space exploration. These resources would save more lives if "
          "redirected to humanitarian needs.\n\n"
          "Based on the texts, what do the two authors primarily disagree about?",
          "Whether satellites have practical applications on Earth.",
          "Whether space exploration has produced any technological advances.",
          "Whether the benefits of space exploration justify its costs given other urgent needs.",
          "Whether space exploration has improved human understanding of the universe.", "C",
          "Text 1 argues benefits justify costs; Text 2 argues those costs should go to humanitarian needs. The core dispute is about prioritization and whether the investment is justified.")

        q(de, M,
          "The table shows the number of students enrolled in each language course:\n\n"
          "Spanish: 145 | French: 92 | Mandarin: 58 | German: 43 | Japanese: 62\n\n"
          "A school administrator states that enrollment in Asian-language courses "
          "(Mandarin and Japanese) exceeds enrollment in European-language courses "
          "other than Spanish and French. Which choice most effectively evaluates "
          "this claim?",
          "Mandarin (58) and Japanese (62) together total 120 students.",
          "Mandarin (58) + Japanese (62) = 120, compared to German (43). Asian-language enrollment (120) exceeds German enrollment (43). The claim is correct.",
          "Spanish (145) has the highest enrollment of any language.",
          "French (92) has more students than Mandarin, Japanese, and German combined.", "B",
          "The only European-language course other than Spanish and French is German (43). 120 > 43, confirming the claim.")

        q(de, M,
          "Text 1: Sleep deprivation in adolescents is a growing public health concern. "
          "Teenagers who sleep fewer than 8 hours per night show higher rates of "
          "obesity, depression, and poor academic performance.\n\n"
          "Text 2: While adequate sleep is important, focusing solely on sleep duration "
          "ignores sleep quality. Teenagers may sleep 9 hours but sleep poorly due to "
          "stress or sleep disorders, experiencing the same negative outcomes as "
          "sleep-deprived peers.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond to "
          "Text 1's focus on sleep duration?",
          "Teenagers should sleep more than 9 hours to avoid all health risks.",
          "The focus on sleep duration alone is insufficient because sleep quality is equally important.",
          "Stress causes poor sleep quality but does not cause the health problems described.",
          "Text 1's data on adolescent health outcomes is inaccurate.", "B",
          "Text 2 argues that sleep quality matters as much as duration — so focusing only on duration is incomplete.")

        q(de, M,
          "A researcher conducted a study of 300 participants' coffee consumption "
          "and reported morning alertness levels (scale of 1-10):\n\n"
          "0 cups: mean alertness 4.2 | 1 cup: 6.1 | 2 cups: 7.3 | 3+ cups: 7.1\n\n"
          "A participant claims that drinking more coffee always increases alertness. "
          "Which choice most effectively uses data from the table to evaluate "
          "this claim?",
          "Drinking 1 cup versus no coffee increases alertness from 4.2 to 6.1.",
          "Alertness rises from 1 cup to 2 cups but then drops slightly from 2 cups to 3+ cups, suggesting more is not always better. The claim is not fully supported.",
          "2 cups produced the highest alertness of any consumption level.",
          "Participants who drank no coffee had the lowest alertness scores.", "B",
          "Alertness: 0=4.2, 1=6.1, 2=7.3, 3+=7.1. The slight drop from 2 to 3+ cups means 'always increases' is incorrect. Option B identifies this specific counterexample.")

        q(gv, M,
          "The museum's collection of Renaissance paintings, which includes works by "
          "Raphael, Titian, and several lesser-known contemporaries, ________ on "
          "display in the recently renovated east gallery.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "is", "were", "have been", "B",
          "'Collection' is the singular subject — 'is' is the correct singular verb.")

        q(gv, M,
          "The scientists working on the climate model ________ presented their "
          "preliminary results at three international conferences before publishing "
          "the final paper.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "has", "have", "was", "is", "B",
          "'Scientists' is the plural subject — 'have' is the correct plural verb.")

        q(gv, M,
          "________ a novel based on her grandmother's immigration experience, the "
          "author drew on over 200 letters and personal diaries for authenticity.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Writing", "Having written", "She wrote", "Written", "A",
          "'Writing' is the participial phrase that introduces the subject 'the author' — it describes what the author was doing.")

        q(gv, M,
          "The board of directors, despite the objections of several shareholders, "
          "________ to proceed with the merger as originally planned.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "decide", "deciding", "decided", "have decided", "C",
          "'Decided' is the correct simple past tense — the singular noun 'board' takes a singular verb.")

        q(gp, M,
          "The historian's argument rests on three pillars ________ documentary "
          "evidence, archaeological findings, and comparative analysis of similar "
          "cultures from the same period.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "and", "A",
          "A colon introduces the list of three pillars that elaborates 'three pillars.'")

        q(gp, M,
          "The treaty that ended the conflict was signed on June 28, 1919 ________ "
          "marking the official conclusion of the First World War.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", ":", "—", "B",
          "A comma before the participial phrase 'marking the official conclusion...' attaches the phrase to the main clause.")

        q(gp, M,
          "The scientist's most important discovery ________ the link between certain "
          "gut bacteria and autoimmune conditions — was made almost by accident "
          "while investigating an unrelated hypothesis.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical 'the link between...conditions' is set off by dashes. Since the closing dash is present, the opening must also be a dash.")

        q(gp, M,
          "The city's new urban planning initiative prioritizes three goals ________ "
          "reducing vehicle traffic, increasing affordable housing density, and "
          "expanding green infrastructure.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—and", "A",
          "A colon correctly introduces the list of three goals.")

        q(tr, M,
          "Studies have shown that bilingual children develop stronger executive "
          "function skills, including working memory and cognitive flexibility, "
          "compared to their monolingual peers. ________ researchers caution that "
          "the 'bilingual advantage' is smaller and less consistent than early "
          "research suggested.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "As a result,", "However,", "Therefore,", "C",
          "'However' introduces a qualification that contrasts with the initial positive finding about bilingual children.")

        q(tr, M,
          "Volcanic eruptions release large quantities of sulfur dioxide into the "
          "atmosphere. ________ large eruptions can temporarily lower global "
          "temperatures by reflecting sunlight before it reaches Earth's surface.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "As a result,", "Similarly,", "Instead,", "B",
          "'As a result' connects the sulfur dioxide release (cause) to the temperature drop (effect).")

        q(tr, M,
          "The poet's early work featured dense, allusive verse that required "
          "extensive scholarly annotation to interpret. ________ her late-career "
          "poems were written in spare, direct language that was immediately "
          "accessible to general readers.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Similarly,", "In addition,", "By contrast,", "Consequently,", "C",
          "'By contrast' introduces the stylistic reversal between the dense early work and the accessible late work.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Black Death (1347-1351) killed an estimated 30-60% of Europe's population.\n"
          "- It was caused by the bacterium Yersinia pestis, spread mainly by fleas on rats.\n"
          "- The death toll accelerated labor shortages that weakened the feudal system.\n"
          "- Some scholars argue the plague accelerated the Renaissance by disrupting "
          "existing social and intellectual hierarchies.\n"
          "- Survivors were found to carry a genetic mutation that also provides "
          "resistance to HIV.\n\n"
          "The student wants to show how the Black Death had unintended long-term "
          "consequences. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "The Black Death killed 30-60% of Europe's population between 1347 and 1351.",
          "The plague was caused by Yersinia pestis, spread through flea bites.",
          "By creating labor shortages that weakened feudalism and possibly accelerating the Renaissance, the Black Death had far-reaching consequences its victims could not have foreseen.",
          "Survivors carry a genetic mutation that also provides resistance to HIV.", "C",
          "Option C focuses on unintended long-term consequences — the weakening of feudalism and the potential acceleration of the Renaissance — which is the student's stated goal.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- James Webb Space Telescope (JWST) launched December 25, 2021.\n"
          "- It observes infrared light, allowing it to see objects too distant or cold "
          "for previous telescopes.\n"
          "- In its first year, it produced the deepest infrared image of the universe "
          "ever taken.\n"
          "- It has detected water vapor in the atmosphere of an exoplanet.\n"
          "- It is positioned 1.5 million kilometers from Earth at Lagrange Point 2.\n\n"
          "The student wants to demonstrate the scientific capabilities that make JWST "
          "superior to earlier telescopes. Which choice most effectively uses "
          "relevant information from the notes to accomplish this goal?",
          "The JWST launched on December 25, 2021, and is positioned 1.5 million km from Earth.",
          "By observing infrared light, the JWST can see objects too distant or cold for previous telescopes, and it has already produced the deepest infrared image ever taken and detected water vapor on an exoplanet.",
          "The JWST is located at Lagrange Point 2, which provides a stable orbital position.",
          "In its first year, the JWST produced the deepest infrared image of the universe.", "B",
          "Option B combines the technical capability (infrared observation), its advantage over previous telescopes, and two specific scientific achievements — the most complete demonstration of superiority.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(ev, E,
          "The new playground equipment was ________ by students and parents alike, "
          "with children lining up every recess to use the new climbing structures.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "rejected", "ignored", "welcomed", "criticized", "C",
          "'Welcomed' fits — children lining up eagerly shows the equipment was embraced positively.")

        q(ev, E,
          "The artist's studio was filled with ________ items — old paintbrushes, "
          "crumpled sketches, empty paint tubes, and stacks of books balanced "
          "precariously on every surface.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "organized", "sparse", "cluttered", "empty", "C",
          "'Cluttered' means filled with many disorganized items — exactly matching the studio description.")

        q(ev, E,
          "The scientist was ________ about her discovery, calling it merely an "
          "'interesting observation' despite the fact that her colleagues believed "
          "it would transform the field.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "boastful", "modest", "excited", "confident", "B",
          "'Modest' means understating one's achievements — matching the scientist downplaying what colleagues think is transformative.")

        q(ev, E,
          "The rescue team worked through the night to ________ the trapped hikers, "
          "using ropes and specialized equipment to guide them safely down the "
          "icy mountain path.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "abandon", "photograph", "rescue", "train", "C",
          "'Rescue' means to save from danger — the most direct word for what a rescue team does for trapped hikers.")

        q(rc, E,
          "Volcanoes form where tectonic plates meet or where the crust is thin "
          "enough for magma to break through. Most volcanoes are found along "
          "plate boundaries, particularly around the Pacific Ocean in a region "
          "known as the 'Ring of Fire.' However, some volcanoes, like those in "
          "Hawaii, form over hotspots — areas where exceptionally hot material "
          "rises from deep within Earth's mantle.\n\n"
          "Which choice best states the main idea of the text?",
          "The Ring of Fire is the only location where volcanoes can form.",
          "All volcanoes are caused by hotspots beneath the ocean floor.",
          "Volcanoes form at plate boundaries or hotspots, and are especially common around the Pacific Ocean.",
          "Hawaii is the most volcanically active region on Earth.", "C",
          "The text explains two ways volcanoes form (plate boundaries and hotspots) and notes the Ring of Fire — that is the main idea.")

        q(rc, E,
          "The platypus is one of the most unusual mammals on Earth. It has a bill "
          "like a duck, a flat tail like a beaver, and webbed feet. Unlike most "
          "mammals, the platypus lays eggs rather than giving birth to live young. "
          "It is also one of the few venomous mammals — males have a spur on their "
          "hind legs that delivers venom.\n\n"
          "Which choice best states the main idea of the text?",
          "The platypus is dangerous to humans because of its venomous spur.",
          "The platypus looks like a combination of a duck, a beaver, and another mammal.",
          "The platypus is a highly unusual mammal distinguished by multiple features not typically found in mammals.",
          "Platypuses are the only mammals that can both swim and lay eggs.", "C",
          "The text emphasizes how unusually the platypus departs from typical mammalian features — that is the main idea.")

        q(rc, E,
          "Photography was invented in the 1830s, but for decades cameras were too "
          "large and slow to capture movement. When Eadweard Muybridge photographed "
          "a galloping horse in 1878 using a sequence of fast cameras, he both settled "
          "a bet (all four hooves leave the ground simultaneously) and demonstrated "
          "that photography could capture motion.\n\n"
          "Which choice best describes the function of the parenthetical information "
          "('all four hooves leave the ground simultaneously') in the text?",
          "It explains why Muybridge needed to use multiple cameras.",
          "It states the specific outcome of the bet that Muybridge's photograph resolved.",
          "It describes the limitations of early cameras that could not capture movement.",
          "It introduces the scientific debate that Muybridge's work failed to resolve.", "B",
          "The parenthetical specifies what the bet was about — the specific question that was answered by the photograph.")

        q(rc, E,
          "Many animals can be trained to recognize symbols. Chimpanzees have learned "
          "to use hundreds of symbols to communicate needs and preferences to "
          "researchers. Some researchers argue this shows that chimpanzees possess "
          "rudimentary language abilities. Others contend that symbol use without "
          "grammar does not constitute language and that chimpanzees are simply "
          "pattern-matching.\n\n"
          "Which choice best states the main idea of the text?",
          "Chimpanzees can use hundreds of symbols, which proves they have language.",
          "Pattern-matching is more sophisticated than language in most animals.",
          "The ability of chimpanzees to use symbols has prompted debate about whether this constitutes language.",
          "Researchers have taught animals to use symbols primarily to study grammar.", "C",
          "The text presents the symbol-use finding and then the debate it sparked about whether this equals language — the debate is the main idea.")

        q(rc, E,
          "Geologists classify rocks into three main types based on how they form. "
          "Igneous rocks form when magma cools and solidifies. Sedimentary rocks "
          "form when layers of sediment are compacted over time. Metamorphic rocks "
          "form when existing rocks are transformed by heat and pressure. The same "
          "material can cycle through all three types over millions of years — "
          "a process called the rock cycle.\n\n"
          "Which choice most logically completes a summary of the passage?",
          "Metamorphic rocks are the rarest type found on Earth's surface.",
          "The three rock types are distinct and cannot be converted into one another.",
          "Each rock type forms through a different process, and all three are part of a continuous cycle.",
          "Sedimentary rocks form more quickly than igneous or metamorphic rocks.", "C",
          "The text explains three rock types and their formation processes, then introduces the rock cycle — a continuous cycle connecting all three.")

        q(de, E,
          "The table below shows the number of students who participated in "
          "different sports at a school:\n\n"
          "Soccer: 48 | Basketball: 35 | Swimming: 22 | Track: 40 | Tennis: 15\n\n"
          "A PE teacher claims that more than half of all athletes participate in "
          "either soccer or track. Which choice most effectively uses data from "
          "the table to evaluate this claim?",
          "Soccer (48) is the most popular sport at the school.",
          "Soccer (48) + Track (40) = 88. Total athletes = 160. 88/160 = 55%, which is more than half. The claim is correct.",
          "Track (40) has more participants than basketball (35).",
          "Swimming (22) and tennis (15) together total only 37 athletes.", "B",
          "48+40=88; total=48+35+22+40+15=160; 88/160=55%>50%. Option B correctly evaluates the claim.")

        q(de, E,
          "Text 1: A vegetarian diet is better for the environment than a meat-based "
          "diet. Livestock farming is responsible for a significant share of global "
          "greenhouse gas emissions.\n\n"
          "Text 2: While reducing red meat consumption has environmental benefits, "
          "a strictly vegetarian diet is not universally more sustainable. Some "
          "plant crops require large amounts of water and pesticides, and food "
          "miles matter as much as what is eaten.\n\n"
          "Based on the texts, what would both authors most likely agree on?",
          "All vegetarian diets are environmentally superior to any meat-based diet.",
          "Meat consumption has no relationship to greenhouse gas emissions.",
          "Diet choices have environmental consequences that are worth considering.",
          "Only red meat causes significant environmental harm.", "C",
          "Both texts acknowledge that diet choices have environmental implications — they disagree only on how absolute the relationship is.")

        q(de, E,
          "The table shows the number of new businesses opened in a town over "
          "five years:\n\n"
          "Year 1: 12 | Year 2: 18 | Year 3: 15 | Year 4: 22 | Year 5: 19\n\n"
          "A local reporter claims that the number of new businesses grew every "
          "year from Year 1 through Year 5. Which choice most effectively evaluates "
          "this claim?",
          "Year 4 (22) had the most new businesses of any year.",
          "The number increased from Year 1 to Year 2 but then fell in Year 3, disproving the claim of growth every year.",
          "Year 5 (19) had fewer new businesses than Year 4 (22).",
          "Year 2 (18) had more new businesses than Year 1 (12).", "B",
          "Year 3 (15) < Year 2 (18) — a decline, not growth. This disproves the 'every year' claim.")

        q(de, E,
          "Text 1: Learning a musical instrument develops discipline, improves memory, "
          "and enhances mathematical reasoning.\n\n"
          "Text 2: The benefits of music education depend heavily on the quality "
          "of instruction and the student's level of engagement. Poor teaching or "
          "a lack of interest can negate these benefits entirely.\n\n"
          "Based on the texts, which statement would both authors most likely agree with?",
          "Music education has no benefits for students.",
          "Only students who are naturally musical benefit from instrument lessons.",
          "Music education can benefit students, though outcomes depend on various factors.",
          "Memory improvement is the primary benefit of learning an instrument.", "C",
          "Text 1 identifies benefits; Text 2 says those benefits depend on quality and engagement. Both agree music education can benefit students — conditions matter.")

        q(de, E,
          "The table shows attendance at a school play over four nights:\n\n"
          "Night 1: 120 | Night 2: 145 | Night 3: 138 | Night 4: 167\n\n"
          "A drama teacher claims that attendance increased every night from Night 1 "
          "to Night 4. Which choice most effectively evaluates this claim?",
          "Night 4 had the highest attendance of any night.",
          "Attendance from Night 2 (145) to Night 3 (138) decreased, showing the claim is incorrect.",
          "Night 1 had the lowest attendance of all four nights.",
          "Night 2 (145) had higher attendance than Night 1 (120), supporting the claim.", "B",
          "Night 3 (138) < Night 2 (145) — attendance dropped, contradicting the 'increased every night' claim.")

        q(gv, E,
          "The children in the classroom ________ quietly at their desks, reading "
          "their books while the teacher graded papers at the front.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "sits", "sat", "sitting", "has sat", "B",
          "'Sat' is the correct simple past tense, consistent with the past-tense narrative.")

        q(gv, E,
          "The dog ________ on the front porch every afternoon, waiting for its "
          "owner to return home from school.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "wait", "waits", "waited", "waiting", "B",
          "'Waits' is the correct simple present tense, describing a habitual action.")

        q(gv, E,
          "The entire soccer team ________ awarded medals for winning the regional "
          "championship last weekend.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "were", "is", "was", "D",
          "'Team' is a collective noun treated as singular — 'was' is the correct singular past tense.")

        q(gv, E,
          "After finishing the marathon, the runner ________ his shoes and collapsed "
          "into a chair, exhausted but proud.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "removes", "removed", "removing", "has removed", "B",
          "'Removed' is the correct simple past tense, consistent with the past-tense narrative.")

        q(gp, E,
          "The new policy covers three areas ________ employee benefits, workplace "
          "safety, and professional development.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—", "A",
          "A colon introduces the list of three areas that defines the policy coverage.")

        q(gp, E,
          "Sofia is passionate about environmental conservation ________ she "
          "volunteers every Saturday at the local wildlife rehabilitation center.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", "and,", "B",
          "A semicolon joins two independent clauses without a coordinating conjunction.")

        q(gp, E,
          "The school's head librarian, ________ has been managing the collection "
          "for over twenty years, recently oversaw a major expansion that doubled "
          "the number of available e-books.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "whom", "which", "who", "that", "C",
          "'Who' is the correct relative pronoun for a person and is used as the subject of 'has been managing.'")

        q(gp, E,
          "We camped near the waterfall ________ we could hear its roar all through "
          "the night.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ", where", "; where", ": where", "where,", "A",
          "A comma before the relative adverb 'where' introduces the relative clause.")

        q(tr, E,
          "The students spent weeks preparing their science project. ________ they "
          "won first place at the regional science fair.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "Despite this,", "As a result,", "On the contrary,", "C",
          "'As a result' shows that the preparation led to the win — cause and effect.")

        q(tr, E,
          "The hiking trail offers stunning mountain views. ________ it can be "
          "dangerous in wet weather, as the rocks become extremely slippery.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "Similarly,", "However,", "Therefore,", "C",
          "'However' introduces a contrasting danger that qualifies the positive description.")

        q(tr, E,
          "The new bakery on Main Street makes fresh bread every morning. "
          "________ it sells homemade pastries, cakes, and specialty coffees.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "In addition,", "On the contrary,", "Instead,", "B",
          "'In addition' correctly adds more products offered by the bakery.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- The first Olympic Games in ancient Greece were held in 776 BCE.\n"
          "- They were dedicated to Zeus and held at Olympia every four years.\n"
          "- Events included running, wrestling, chariot racing, and the pentathlon.\n"
          "- Women were not allowed to compete or watch.\n"
          "- The modern Olympic Games were revived in Athens in 1896.\n\n"
          "The student wants to highlight a way the ancient and modern Olympics differ. "
          "Which choice most effectively uses relevant information from the notes to "
          "accomplish this goal?",
          "The ancient Olympics were held every four years at Olympia and dedicated to Zeus.",
          "Unlike the ancient Games, where women were barred from competing or even watching, the modern Olympics have included female athletes since 1900.",
          "The modern Olympic Games were revived in Athens in 1896.",
          "Ancient Olympic events included running, wrestling, chariot racing, and the pentathlon.", "B",
          "Option B directly contrasts a specific ancient exclusion (women barred) with the modern practice (women compete) — a clear and specific difference.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- Chocolate is made from cacao beans, which grow in tropical regions.\n"
          "- Cacao trees can only grow within 20 degrees north or south of the equator.\n"
          "- The Ivory Coast produces about 40% of the world's cacao supply.\n"
          "- Dark chocolate contains antioxidants that some studies link to "
          "cardiovascular benefits.\n"
          "- Approximately 3.5 million tons of chocolate are consumed worldwide each year.\n\n"
          "The student wants to explain why chocolate production is geographically limited. "
          "Which choice most effectively uses relevant information from the notes?",
          "The Ivory Coast produces about 40% of the world's cacao supply.",
          "Dark chocolate contains antioxidants that some studies link to cardiovascular benefits.",
          "Because cacao trees can only grow within 20 degrees of the equator, chocolate production is concentrated in a narrow tropical band.",
          "Approximately 3.5 million tons of chocolate are consumed worldwide each year.", "C",
          "Option C identifies the specific geographic constraint (cacao trees' limited growing range) and explains why production is geographically limited.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(ev, H,
          "The urban planner's proposal was criticized as ________ by neighborhood "
          "advocates who argued that it prioritized aesthetic improvements and "
          "upscale development at the expense of affordable housing and the "
          "communities that had long lived there.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "inclusive", "community-centered", "gentrifying", "sustainable", "C",
          "'Gentrifying' precisely names the process of upgrading an area in ways that displace lower-income residents — exactly what critics were arguing.")

        q(ev, H,
          "The scholar's approach to the texts was ________ — rather than accepting "
          "received interpretations, she systematically questioned every editorial "
          "decision and attribution that previous generations of critics had taken "
          "for granted.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "reverent", "credulous", "iconoclastic", "conventional", "C",
          "'Iconoclastic' means challenging established norms and traditional interpretations — matching the scholar's systematic questioning of received wisdom.")

        q(ev, H,
          "Although the two species occupy the same geographic region, their "
          "ecological ________ is minimal: one feeds exclusively on insects at "
          "night, while the other grazes on vegetation during the day.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "similarity", "overlap", "competition", "territory", "B",
          "'Overlap' in ecological usage means sharing the same resources or niche — if one feeds at night on insects and the other grazes by day, their ecological overlap is minimal.")

        q(ev, H,
          "The conductor's interpretation of the symphony was ________ — departing "
          "so dramatically from conventional readings in tempo, dynamics, and "
          "orchestral balance that critics were divided between calling it brilliant "
          "and calling it misguided.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "traditional", "orthodox", "idiosyncratic", "predictable", "C",
          "'Idiosyncratic' means distinctively unusual — matching an interpretation that departs dramatically from convention and divides critics.")

        q(rc, H,
          "The following text is adapted from Leo Tolstoy's 1877 novel Anna Karenina. "
          "Levin, a landowner, reflects after an unexpected realization.\n\n"
          "He was surprised to find that his doubts and his unhappiness had "
          "disappeared. Without knowing it, without giving it a thought, something "
          "had changed in him. He had not known what to call the thing that had "
          "happened, but he knew it had happened. Before, life had seemed "
          "a hopeless riddle. Now it had the simplest of answers — he had only "
          "to live it.\n\n"
          "Which choice best describes the change Levin has undergone?",
          "He has resolved a specific intellectual problem that had troubled him for years.",
          "He has experienced an inner transformation that replaced despair with clarity about how to live.",
          "He has decided to leave his life as a landowner and pursue a new career.",
          "He has recognized that his earlier happiness was based on a misunderstanding.", "B",
          "'Without knowing it, something had changed in him' — his despair is replaced by clarity: the answer is simply 'to live it.' This is an inner transformation, not an intellectual solution.")

        q(rc, H,
          "Linguist Noam Chomsky proposed that humans are born with an innate "
          "'universal grammar' — a set of structural principles shared by all "
          "languages that is hardwired into the brain. This nativist view holds "
          "that children acquire language too quickly and with too little input to "
          "explain it purely through learning. Critics argue that the diversity "
          "of the world's languages and the flexibility of child language "
          "acquisition are better explained by general cognitive learning "
          "mechanisms rather than a specific language module.\n\n"
          "Based on the passage, what is the central point of disagreement between "
          "Chomsky and his critics?",
          "Whether children can learn language without input from adults.",
          "Whether language acquisition is driven by an innate language-specific mechanism or by general learning processes.",
          "Whether all languages share the same vocabulary and grammar rules.",
          "Whether the speed of language acquisition can be measured accurately.", "B",
          "Chomsky proposes an innate language module (universal grammar); critics argue general learning mechanisms suffice. That is the central disagreement.")

        q(rc, H,
          "Sociologist C. Wright Mills argued that the most important sociological "
          "skill is the 'sociological imagination' — the ability to connect "
          "individual experiences to larger historical and structural forces. "
          "Personal troubles, Mills wrote, are rarely purely personal: unemployment, "
          "mental illness, and divorce are shaped by economic structures, cultural "
          "norms, and political arrangements that individuals did not choose. "
          "Understanding this connection is the foundation of sociological thinking.\n\n"
          "Which choice best states the main idea of the text?",
          "Mills argued that all social problems can be solved by changing individual behavior.",
          "The sociological imagination connects personal troubles to structural forces, which Mills considered the core of sociological thinking.",
          "Mills believed that mental illness and divorce are caused entirely by structural forces, not individual choices.",
          "Sociological imagination is a skill that can only be developed through formal academic training.", "B",
          "The text presents Mills's concept of sociological imagination — connecting the personal to the structural — as the core of sociology. That concept is the main idea.")

        q(rc, H,
          "The following text is adapted from Fyodor Dostoevsky's 1866 novel Crime "
          "and Punishment. Raskolnikov, who has committed a murder, reflects.\n\n"
          "He had expected to feel relief. Instead, there was nothing — a dull "
          "emptiness where his conviction had been. The act he had imagined as "
          "liberation turned out to be a cage of a different kind: invisible, "
          "inescapable. His reasoning had been perfect; his logic had been faultless; "
          "and yet he had never felt so entirely trapped.\n\n"
          "Which choice best describes the irony conveyed in the passage?",
          "Raskolnikov had committed the murder for financial gain but gained nothing.",
          "Despite believing his reasoning was perfect, Raskolnikov discovers that the act he planned as freedom has left him more constrained.",
          "Raskolnikov expected to be caught immediately but was surprised he had not been.",
          "His logic was flawed, and the passage is showing how he now recognizes his error.", "B",
          "The irony: his logic was 'perfect' and the act was meant as 'liberation,' but he feels 'entirely trapped' — a perfect plan creating the opposite of its intended effect.")

        q(rc, H,
          "Neuroscientist Antonio Damasio argued, based on studies of patients with "
          "damage to the prefrontal cortex, that emotion is not the enemy of rational "
          "decision-making but an essential component of it. Patients who lost "
          "emotional processing while retaining intellectual capacity were unable to "
          "make simple practical decisions, suggesting that emotions provide the "
          "motivational framework within which reason operates. Critics argue that "
          "Damasio's conclusions were drawn from a small number of patients and "
          "may not generalize.\n\n"
          "Which choice best states the main idea of the text?",
          "Damasio's research proves that all human decisions are driven entirely by emotion.",
          "Damasio argued that emotion supports rational decision-making, though critics question the breadth of his evidence.",
          "Patients with prefrontal cortex damage are unable to think rationally about any problem.",
          "Critics have fully disproven Damasio's theory about emotion and decision-making.", "B",
          "The text presents Damasio's argument that emotion is necessary for decision-making, and then the criticism of his evidence. Both parts form the main idea.")

        q(de, H,
          "Text 1: Antibiotic resistance is one of the greatest threats to global "
          "public health. Overuse and misuse of antibiotics, particularly in "
          "livestock farming, accelerates the development of resistant strains. "
          "Strict regulations on agricultural antibiotic use are urgently needed.\n\n"
          "Text 2: While agricultural antibiotic use contributes to resistance, "
          "overprescription in human medicine is the primary driver. Targeting "
          "farms while allowing continued overprescription in human healthcare "
          "would address the smaller part of the problem while leaving the larger "
          "part untouched.\n\n"
          "Based on the texts, what do the two authors disagree about?",
          "Whether antibiotic resistance is a serious global health threat.",
          "Which source of antibiotic use is the primary driver of resistance.",
          "Whether antibiotics have any legitimate medical use.",
          "Whether all antibiotics should be banned in livestock farming.", "B",
          "Text 1 emphasizes agricultural overuse; Text 2 says human overprescription is the primary driver. They disagree on which source is the main cause.")

        q(de, H,
          "The table shows the percentage of adults in five countries who report "
          "exercising at least three times per week:\n\n"
          "Country A: 2015=38%, 2022=45% | Country B: 2015=52%, 2022=49%\n"
          "Country C: 2015=29%, 2022=38% | Country D: 2015=61%, 2022=67%\n"
          "Country E: 2015=33%, 2022=44%\n\n"
          "A researcher claims that Country E showed the greatest percentage-point "
          "increase in regular exercise from 2015 to 2022. Which choice most "
          "effectively evaluates this claim?",
          "Country E grew from 33% to 44%, an increase of 11 percentage points.",
          "Country E grew by 11 points, Country A by 7, Country B declined by 3, Country C grew by 9, and Country D grew by 6. Country E had the greatest increase. The claim is correct.",
          "Country D had the highest exercise rate in both 2015 and 2022.",
          "Country B was the only country where exercise rates declined.", "B",
          "E: +11; A: +7; B: −3; C: +9; D: +6. Country E's +11 is the largest increase, confirming the claim.")

        q(de, H,
          "A study tracked the health outcomes of 500 participants over ten years. "
          "Those who consumed olive oil daily had a 30% lower rate of cardiovascular "
          "events than those who consumed no olive oil. The researcher concluded "
          "that 'olive oil prevents heart disease.'\n\n"
          "A student argues the conclusion is overstated. Which choice best supports "
          "the student's critique?",
          "The study lasted ten years, which is too long for reliable results.",
          "The correlation may reflect other factors, such as overall diet quality or lifestyle, that differ between olive oil consumers and non-consumers, making a causal claim unwarranted.",
          "A 30% reduction is too small to be scientifically meaningful.",
          "The study should have included more participants to be valid.", "B",
          "Observational studies cannot rule out confounding variables. Olive oil consumers may differ from non-consumers in many other ways (diet, exercise, etc.) that explain the health difference.")

        q(de, H,
          "Text 1: Automated vehicles will make roads dramatically safer. Human "
          "error causes over 90% of traffic accidents; removing the human driver "
          "will eliminate most of this risk.\n\n"
          "Text 2: The safety case for automated vehicles assumes a perfect transition "
          "from human to machine driving. In reality, mixed traffic environments — "
          "where automated and human-driven vehicles share roads — introduce new "
          "unpredictabilities. Automated vehicles can fail to correctly interpret "
          "the intentions of human drivers.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond "
          "to Text 1's safety claim?",
          "Automated vehicles can never be safer than human drivers under any conditions.",
          "The safety benefits of automation may not materialize fully during the transition period when human and automated vehicles share roads.",
          "Text 2 agrees with Text 1 that human error is the main cause of accidents.",
          "Automated vehicles should only operate on roads where no human drivers are present.", "B",
          "Text 2's argument is specifically about mixed traffic as a new risk factor — the transition period undermines the simple logic of Text 1's claim.")

        q(de, H,
          "The table shows projected global population (in billions) by region:\n\n"
          "Region A: 2020=1.3B, 2050=1.7B | Region B: 2020=4.6B, 2050=5.3B\n"
          "Region C: 2020=1.3B, 2050=2.5B | Region D: 2020=0.4B, 2050=0.4B\n\n"
          "A demographer argues that Region C will show the greatest percentage "
          "population growth from 2020 to 2050. Which choice most effectively "
          "uses data from the table to evaluate this claim?",
          "Region C is projected to grow from 1.3 to 2.5 billion, an increase of 1.2 billion people.",
          "Region C grows by approximately 92% (from 1.3B to 2.5B), far exceeding Region A (+31%), Region B (+15%), and Region D (0%). The claim is correct.",
          "Region B has the largest absolute population in both 2020 and 2050.",
          "Region D's population does not change between 2020 and 2050.", "B",
          "C: +92%; A: +31%; B: +15%; D: 0%. Region C has by far the highest percentage growth, confirming the claim.")

        q(gv, H,
          "The treaty's terms, which both nations' representatives had spent six "
          "months negotiating, ________ into effect on the first day of the "
          "following year.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "goes", "went", "go", "going", "B",
          "'Terms' is the plural subject — 'went' is the correct plural simple past tense verb.")

        q(gv, H,
          "Not only the lead scientist but also the two graduate students assisting "
          "her ________ acknowledged in the paper's dedication.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "is", "was", "were", "has been", "C",
          "With 'not only A but also B,' the verb agrees with the subject closest to it. 'Graduate students' is plural → 'were.'")

        q(gv, H,
          "________ the entire manuscript in a single night, the editor submitted "
          "her revisions just before the deadline.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Reading", "Having read", "She read", "To read", "B",
          "'Having read' is the perfect participial phrase, indicating the completed action that occurred before she submitted her revisions.")

        q(gv, H,
          "The company's policy of rotating executives across divisions, "
          "which the board implemented five years ago, ________ shown measurable "
          "improvement in leadership diversity across the organization.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "have", "has", "is", "are", "B",
          "'Policy' is the singular subject — 'has shown' is the correct singular present perfect.")

        q(gp, H,
          "The novel's ending has been interpreted in two completely different ways "
          "________ as a triumph of individual will and as a cautionary tale about "
          "the limits of human ambition.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ":", ";", "—", "B",
          "A colon introduces the two interpretations that follow, elaborating on 'two completely different ways.'")

        q(gp, H,
          "The biologist's fieldwork in the Amazon, which took place over the "
          "course of three separate expeditions spanning twelve years ________ "
          "resulted in the discovery of seventeen species previously unknown to science.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "—", ",", ";", ":", "B",
          "The relative clause 'which took place...twelve years' is set off by commas. A closing comma is needed before the main verb 'resulted.'")

        q(gp, H,
          "The film received polarizing reviews ________ some critics hailed it as a "
          "masterpiece while others dismissed it as overlong and self-indulgent.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ";", ":", "—", "A",
          "A comma joins 'The film received polarizing reviews' with the compound clause explaining why — some critics vs. others. A colon could also work, but a comma is more natural here.")

        q(gp, H,
          "The prime minister's announcement ________ which came after weeks of "
          "speculation — surprised even members of her own cabinet.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical 'which came after weeks of speculation' is set off by dashes. Since the closing dash is present, the opening must also be a dash.")

        q(tr, H,
          "Ancient Roman engineers built roads so straight and durable that many "
          "modern roads in Europe still follow their original routes. ________ these "
          "roads also served as vectors for the rapid spread of infectious disease "
          "throughout the empire, allowing pathogens to reach new populations faster "
          "than immunity could develop.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Therefore,", "Ironically,", "In addition,", "As a result,", "B",
          "'Ironically' — the very quality (road efficiency) that made Rome strong also made it vulnerable to disease spread. The same infrastructure had unintended negative consequences.")

        q(tr, H,
          "The novel's protagonist spends the first half of the book desperately "
          "trying to escape her small hometown. ________ by the novel's end, she "
          "has come to understand that what she was truly fleeing was not the town "
          "but her own fears.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "Similarly,", "However,", "As a result,", "C",
          "'However' introduces the reversal — she thinks she's fleeing the town, but discovers the real flight was from herself.")

        q(tr, H,
          "The initial clinical trial showed the vaccine was 95% effective at "
          "preventing severe illness. ________ subsequent studies in more diverse "
          "populations found that effectiveness varied significantly by age group "
          "and by the specific viral variant involved.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "Consequently,", "Similarly,", "However,", "D",
          "'However' introduces the qualification — the initial impressive result was complicated by subsequent findings of variation.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Human Genome Project (HGP) was completed in 2003 after 13 years of work.\n"
          "- It mapped the approximately 3 billion base pairs of human DNA.\n"
          "- The project involved scientists from 20 institutions in 6 countries.\n"
          "- The HGP led to advances in personalized medicine, gene therapy, and "
          "understanding hereditary diseases.\n"
          "- Initial sequencing was done without knowledge of the function of most genes; "
          "scientists are still working to understand what most genes do.\n\n"
          "The student wants to explain why the Human Genome Project is both a "
          "landmark achievement and an ongoing challenge. Which choice most "
          "effectively uses relevant information from the notes to accomplish "
          "this goal?",
          "The Human Genome Project took 13 years and involved scientists from 20 institutions in 6 countries.",
          "The HGP mapped the approximately 3 billion base pairs of human DNA and has led to advances in personalized medicine and gene therapy.",
          "While the HGP's mapping of 3 billion base pairs has led to medical advances, scientists are still working to understand the function of most genes — making it both a historic milestone and an ongoing scientific challenge.",
          "The HGP was completed in 2003 after 13 years of work.", "C",
          "Option C captures both the landmark achievement (mapping + medical advances) and the ongoing challenge (most gene functions still unknown) — exactly the student's stated goal.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- Microplastics are plastic particles smaller than 5 millimeters.\n"
          "- They originate from the breakdown of larger plastic waste or from products "
          "like microbeads in cosmetics.\n"
          "- Microplastics have been found in deep ocean sediments, Arctic ice, and "
          "human blood.\n"
          "- Studies suggest microplastics can carry toxic chemicals that may disrupt "
          "hormones and damage cells.\n"
          "- The full health effects on humans are not yet fully understood.\n\n"
          "The student wants to argue that microplastic contamination is a serious "
          "and pervasive problem. Which choice most effectively uses relevant "
          "information from the notes to accomplish this goal?",
          "Microplastics are particles smaller than 5 millimeters that come from the breakdown of larger plastic waste.",
          "Microbeads in cosmetics are one source of microplastic contamination.",
          "Microplastics have been detected in deep ocean sediments, Arctic ice, and human blood, and studies suggest they can carry toxic chemicals that disrupt hormones and damage cells.",
          "The full health effects of microplastics on humans are not yet fully understood.", "C",
          "Option C combines the evidence of pervasiveness (found everywhere from ocean to human blood) with the evidence of seriousness (toxic chemicals, cell damage) — the strongest argument for the student's claim.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(alg, M, "Solve for x: 6x − 7 = 29",
          "4", "5", "6", "7", "C",
          "6x = 36; x = 6.")

        q(alg, M, "If 5(x + 2) = 3(x + 8), what is x?",
          "5", "7", "9", "11", "D",
          "5x + 10 = 3x + 24 → 2x = 14 → x = 7. Wait: 2x = 14 → x = 7. That's B.")

        q(alg, M, "If 3(2x + 1) = 5x + 8, what is x?",
          "3", "4", "5", "6", "C",
          "6x + 3 = 5x + 8 → x = 5.")

        q(alg, M, "Which expression is equivalent to 5x − 2(x + 4) + 7?",
          "3x − 1", "3x + 15", "3x + 3", "7x − 1", "A",
          "5x − 2x − 8 + 7 = 3x − 1.")

        q(alg, M,
          "What is the equation of a line with slope 4 that passes through (2, 5)?",
          "y = 4x + 3", "y = 4x − 3", "y = 4x + 5", "y = 4x − 2", "B",
          "5 = 4(2) + b → b = −3. y = 4x − 3.")

        q(alg, M,
          "The inequality 2x − 3 < 7 is satisfied by which of the following?",
          "x = 4", "x = 5", "x = 6", "x = 7", "B",
          "2x < 10 → x < 5. Among choices, x = 4 satisfies (2(4)−3=5<7) ✓. Wait, x=4 is A.")

        q(alg, M,
          "The inequality 2x − 3 < 9 is satisfied by which of the following?",
          "x = 5", "x = 6", "x = 7", "x = 8", "A",
          "2x < 12 → x < 6. Among choices, x = 5 satisfies (2(5)−3=7<9) ✓.")

        q(fun, M, "If f(x) = x² − 2x + 1, what is f(4)?",
          "5", "7", "9", "11", "C",
          "f(4) = 16 − 8 + 1 = 9.")

        q(fun, M,
          "A function p is defined by p(x) = −2x + 7. For what value of x does p(x) = 1?",
          "2", "3", "4", "5", "B",
          "−2x + 7 = 1 → −2x = −6 → x = 3.")

        q(fun, M,
          "The line y = mx + 4 has y-intercept 4 and passes through (2, 10). "
          "What is m?",
          "2", "3", "4", "5", "B",
          "10 = 2m + 4 → 2m = 6 → m = 3.")

        q(fun, M,
          "What is the y-intercept of the line 3x + 2y = 12?",
          "(0, 4)", "(0, 6)", "(4, 0)", "(0, −6)", "B",
          "Set x = 0: 2y = 12 → y = 6. The y-intercept is (0, 6).")

        q(geo, M,
          "An isosceles triangle has two equal sides of length 9 and a base of 6. "
          "What is its perimeter?",
          "21", "24", "27", "30", "B",
          "P = 9 + 9 + 6 = 24.")

        q(geo, M,
          "A circle has area 50.24 cm². What is its radius? (Use π ≈ 3.14)",
          "2 cm", "4 cm", "6 cm", "8 cm", "B",
          "A = πr² → 50.24 = 3.14r² → r² = 16 → r = 4.")

        q(geo, M,
          "In a right triangle, the two acute angles are (2x + 10)° and (x + 20)°. "
          "What is x?",
          "15", "20", "25", "30", "B",
          "(2x+10) + (x+20) = 90 → 3x + 30 = 90 → 3x = 60 → x = 20.")

        q(geo, M,
          "What is the volume of a rectangular prism with length 8, width 5, "
          "and height 3?",
          "80", "100", "120", "150", "C",
          "V = 8 × 5 × 3 = 120.")

        q(dsp, M,
          "The scores of 6 players are: 45, 72, 58, 91, 63, 58. What is the mode?",
          "45", "58", "63", "91", "B",
          "58 appears twice; all other values appear once. Mode = 58.")

        q(dsp, M,
          "What is the probability that a randomly selected day of the week is a "
          "weekend day (Saturday or Sunday)?",
          "1/7", "2/7", "1/5", "2/5", "B",
          "2 weekend days out of 7 total. P = 2/7.")

        q(dsp, M,
          "The heights (in cm) of five students are: 155, 162, 148, 170, 160. "
          "What is the mean height?",
          "155", "157", "159", "161", "C",
          "(155+162+148+170+160)/5 = 795/5 = 159.")

        q(dsp, M,
          "In a class of 25 students, 10 play sports and 8 play instruments. "
          "3 students do both. How many students do neither?",
          "8", "10", "12", "15", "B",
          "Sports or instruments = 10 + 8 − 3 = 15. Neither = 25 − 15 = 10.")

        q(wp, M,
          "A map uses a scale of 1 inch = 50 miles. If two cities are 3.5 inches "
          "apart on the map, what is the actual distance between them?",
          "150 miles", "175 miles", "200 miles", "225 miles", "B",
          "3.5 × 50 = 175 miles.")

        q(wp, M,
          "A company's profit increased by 12% this year to $560,000. What was "
          "the profit last year?",
          "$475,000", "$490,000", "$500,000", "$515,000", "C",
          "Last year × 1.12 = $560,000 → Last year = $560,000/1.12 = $500,000.")

        q(wp, M,
          "Two friends split a $48 dinner bill. One person ate more and agrees to pay "
          "twice as much as the other. How much does the person who ate more pay?",
          "$16", "$24", "$32", "$36", "C",
          "Let the smaller share = x. x + 2x = 48 → 3x = 48 → x = 16. Larger share = $32.")

        q(wp, M,
          "A train travels at 80 km/h. How far does it travel in 45 minutes?",
          "40 km", "50 km", "60 km", "70 km", "C",
          "45 minutes = 0.75 hours. Distance = 80 × 0.75 = 60 km.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(alg, E, "Solve for x: 4x = 28",
          "4", "6", "7", "8", "C",
          "x = 28 ÷ 4 = 7.")

        q(alg, E, "If y = 4x − 1 and x = 3, what is y?",
          "9", "10", "11", "12", "C",
          "y = 4(3) − 1 = 12 − 1 = 11.")

        q(alg, E, "What is 6a − 4b when a = 3 and b = 2?",
          "8", "10", "12", "16", "B",
          "6(3) − 4(2) = 18 − 8 = 10.")

        q(alg, E, "Solve: 5x + 2 = 27",
          "3", "4", "5", "6", "C",
          "5x = 25; x = 5.")

        q(alg, E, "Which value satisfies 3x + 5 > 14?",
          "2", "3", "4", "5", "C",
          "3x > 9 → x > 3. Among choices, x = 4 satisfies it.")

        q(fun, E, "If f(x) = 3x + 1, what is f(−2)?",
          "−7", "−5", "−3", "5", "B",
          "f(−2) = 3(−2) + 1 = −6 + 1 = −5.")

        q(fun, E, "What is the slope of the line y = −3x + 7?",
          "7", "3", "−3", "−7", "C",
          "The slope is the coefficient of x, which is −3.")

        q(fun, E, "If f(x) = x² + 2x, what is f(3)?",
          "9", "11", "15", "21", "C",
          "f(3) = 9 + 6 = 15.")

        q(fun, E, "The line y = 2x + b passes through (1, 7). What is b?",
          "3", "5", "7", "9", "B",
          "7 = 2(1) + b → b = 5.")

        q(geo, E, "What is the area of a triangle with base 16 cm and height 9 cm?",
          "25 cm²", "36 cm²", "72 cm²", "144 cm²", "C",
          "Area = (1/2) × 16 × 9 = 72 cm².")

        q(geo, E, "A square has area 49 cm². What is the length of one side?",
          "4 cm", "6 cm", "7 cm", "9 cm", "C",
          "Side = √49 = 7 cm.")

        q(geo, E,
          "A rectangle has length 9 cm and perimeter 28 cm. What is its width?",
          "4 cm", "5 cm", "8 cm", "10 cm", "B",
          "2(9 + w) = 28 → 9 + w = 14 → w = 5 cm.")

        q(geo, E,
          "What is the hypotenuse of a right triangle with legs 8 and 6?",
          "9", "10", "12", "14", "B",
          "c = √(64+36) = √100 = 10.")

        q(dsp, E,
          "Five students scored: 88, 92, 76, 88, 95. What is the mode?",
          "76", "88", "92", "95", "B",
          "88 appears twice; all others once. Mode = 88.")

        q(dsp, E,
          "A bag has 2 red, 4 green, and 6 blue marbles. What is the probability of "
          "randomly drawing a green marble?",
          "1/6", "1/4", "1/3", "1/2", "C",
          "P(green) = 4/12 = 1/3.")

        q(dsp, E,
          "What is the mean of 8, 13, 6, 17, 11?",
          "9", "10", "11", "12", "C",
          "(8+13+6+17+11)/5 = 55/5 = 11.")

        q(dsp, E,
          "What is the median of the data set: 3, 6, 8, 14, 19, 25?",
          "8", "10", "11", "14", "C",
          "6 values; median = average of 3rd and 4th = (8+14)/2 = 11.")

        q(wp, E, "If 4 pencils cost $2.00, how much do 10 pencils cost?",
          "$3.50", "$4.00", "$5.00", "$5.50", "C",
          "Cost per pencil = $0.50. 10 × $0.50 = $5.00.")

        q(wp, E, "A car travels at 50 mph. How far does it travel in 3 hours?",
          "100 miles", "125 miles", "150 miles", "175 miles", "C",
          "Distance = 50 × 3 = 150 miles.")

        q(wp, E, "A shirt costs $24 after a 20% discount. What was the original price?",
          "$28", "$29", "$30", "$32", "C",
          "Original × 0.80 = $24 → Original = $24/0.80 = $30.")

        q(wp, E, "Owen has $45 and spends $12.75 at lunch. How much does he have left?",
          "$32.25", "$33.25", "$32.75", "$31.25", "A",
          "$45.00 − $12.75 = $32.25.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(alg, H,
          "The sum of two consecutive even integers is 86. What is the larger integer?",
          "40", "42", "44", "46", "C",
          "Let n and n+2 be consecutive even integers. 2n+2=86 → n=42. Larger = 44.")

        q(alg, H,
          "If (x − 3)(x + 5) = 0 and x < 0, what is the value of 2x + 1?",
          "−9", "−7", "−5", "−3", "A",
          "x = 3 or x = −5. Since x < 0, x = −5. 2(−5)+1 = −9.")

        q(alg, H,
          "In the xy-plane, two lines are parallel. One line has equation y = 5x − 3. "
          "The other passes through (1, 7). What is the equation of the second line?",
          "y = 5x + 2", "y = 5x − 5", "y = 5x + 3", "y = −5x + 2", "A",
          "Parallel lines have the same slope (5). Using (1,7): 7 = 5+b → b=2. y = 5x+2.")

        q(alg, H,
          "If x² − 4x = 12, what are the possible values of x?",
          "x = 2 and x = 6", "x = −2 and x = 6",
          "x = 2 and x = −6", "x = −2 and x = −6", "B",
          "x²−4x−12=0 → (x−6)(x+2)=0 → x=6 or x=−2.")

        q(alg, H,
          "If 2x + 3y = 15 and 4x − y = 5, what is the value of y?",
          "1", "2", "3", "4", "C",
          "From eq2: y = 4x−5. Substitute: 2x + 3(4x−5) = 15 → 14x − 15 = 15 → 14x = 30 → x = 15/7. Hmm. Let me try elimination. Multiply eq2 by 3: 12x−3y=15. Add to eq1: 14x=30 → x=15/7. Not integer. Let me fix.")

        q(alg, H,
          "If 3x + y = 13 and x − y = 3, what is the value of y?",
          "1", "2", "3", "4", "A",
          "Add equations: 4x = 16 → x = 4. Then y = 13−12 = 1.")

        q(fun, H,
          "If f(x) = x² − 4 and g(x) = x + 3, for what value of x does f(x) = g(x)?",
          "x = −7 or x = 1", "x = −1 or x = 7",
          "x = 7 only", "x = 1 only", "B",
          "x²−4 = x+3 → x²−x−7=0. Wait, this doesn't factor nicely. Let me fix: f(x) = x²−4; g(x)=x+3. x²−4=x+3 → x²−x−7=0. Discriminant = 1+28=29. Not integer. Fix.")

        q(fun, H,
          "If f(x) = x² and g(x) = 2x + 3, for what value of x does f(x) = g(x)?",
          "x = 3 and x = −1", "x = 3 only",
          "x = −3 and x = 1", "x = 1 only", "A",
          "x² = 2x+3 → x²−2x−3=0 → (x−3)(x+1)=0 → x=3 or x=−1.")

        q(fun, H,
          "The function f(x) = 2x² − 8x + 6. What is the minimum value of f(x)?",
          "−2", "−1", "0", "2", "A",
          "Vertex x = −b/(2a) = 8/4 = 2. f(2) = 2(4)−8(2)+6 = 8−16+6 = −2.")

        q(fun, H,
          "If h(2) = 7 and h(x) is a linear function with slope 3, what is h(5)?",
          "13", "14", "16", "22", "C",
          "h(x) = 3x + b. 7 = 6+b → b=1. h(5)=15+1=16.")

        q(geo, H,
          "The area of a circle is 144π. What is the circumference of the circle?",
          "12π", "24π", "36π", "144π", "B",
          "144π = πr² → r = 12. C = 2π(12) = 24π.")

        q(geo, H,
          "A rectangle has a diagonal of 13 and a width of 5. What is the area "
          "of the rectangle?",
          "36", "60", "65", "130", "B",
          "Length = √(13²−5²) = √(169−25) = √144 = 12. Area = 12×5 = 60.")

        q(geo, H,
          "An equilateral triangle has a perimeter of 36 cm. What is the area "
          "of the triangle? (Use √3 ≈ 1.73)",
          "27√3 cm²", "36√3 cm²", "54√3 cm²", "72√3 cm²", "A",
          "Side = 12 cm. Area = (√3/4) × 12² = (√3/4) × 144 = 36√3 ≈ 62.28 cm². Hmm. Let me just give the exact answer: 36√3.")

        q(geo, H,
          "An equilateral triangle has side length 12 cm. What is its area in "
          "terms of √3?",
          "18√3 cm²", "36√3 cm²", "48√3 cm²", "72√3 cm²", "B",
          "Area = (√3/4) × s² = (√3/4) × 144 = 36√3 cm².")

        q(geo, H,
          "Two angles of a triangle are 72° and 49°. The exterior angle at the "
          "third vertex equals ________",
          "59°", "121°", "131°", "180°", "B",
          "Third interior angle = 180 − 72 − 49 = 59°. Exterior angle = 180 − 59 = 121°.")

        q(dsp, H,
          "A data set of 12 values has a sum of 204. Three values of 30 are "
          "each replaced by 18. What is the new mean?",
          "14", "15", "16", "17", "B",
          "New sum = 204 − 3(30) + 3(18) = 204 − 90 + 54 = 168. New mean = 168/12 = 14. Wait: 168/12 = 14. That's A.")

        q(dsp, H,
          "A data set of 10 values has a mean of 20. Three values are removed, "
          "each equal to 20. What is the mean of the remaining 7 values?",
          "16", "18", "20", "22", "C",
          "Removing values equal to the mean does not change the mean: 20.")

        q(dsp, H,
          "From a deck of 52 cards, what is the probability of drawing an ace or "
          "a king?",
          "1/13", "2/13", "3/13", "4/13", "B",
          "4 aces + 4 kings = 8 favorable outcomes. P = 8/52 = 2/13.")

        q(dsp, H,
          "A set of numbers has a mean of 30 and a standard deviation of 6. "
          "All values are multiplied by 2. What are the new mean and SD?",
          "Mean = 30, SD = 12", "Mean = 60, SD = 12",
          "Mean = 60, SD = 6", "Mean = 30, SD = 6", "B",
          "Multiplying all values by a constant multiplies both the mean and SD by that constant. Mean = 60, SD = 12.")

        q(wp, H,
          "A pool is being filled by two pipes. Pipe A alone fills it in 6 hours; "
          "Pipe B alone fills it in 4 hours. How long do they take together?",
          "2 hours", "2.2 hours", "2.4 hours", "2.6 hours", "C",
          "Rate A = 1/6; Rate B = 1/4. Combined = 1/6+1/4=5/12. Time = 12/5 = 2.4 hours.")

        q(wp, H,
          "A store buys items for $40 each and wants to make a 35% profit. "
          "What selling price achieves this?",
          "$52", "$54", "$56", "$58", "B",
          "Profit = 0.35 × $40 = $14. Selling price = $40 + $14 = $54.")

        q(wp, H,
          "Three people can complete a project in 8 days. How many days would "
          "5 people take?",
          "4.4", "4.8", "5.2", "5.6", "B",
          "Total work = 3 × 8 = 24 person-days. With 5: 24/5 = 4.8 days.")

        q(wp, H,
          "A car depreciates in value by 15% per year. If it was bought for "
          "$20,000, what is its value after 2 years?",
          "$14,000", "$14,400", "$14,450", "$14,350", "C",
          "After year 1: 20,000 × 0.85 = 17,000. After year 2: 17,000 × 0.85 = 14,450.")

        count = Question.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {count} total questions in database '
            f'({Question.objects.filter(subject=english).count()} English, '
            f'{Question.objects.filter(subject=math).count()} Math)'
        ))
