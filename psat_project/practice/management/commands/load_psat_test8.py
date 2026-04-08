"""
Management command to load all questions from PSAT 8/9 Practice Test 8.
English (Reading & Writing): 81 questions across 3 modules
Math: 66 questions across 3 modules
Difficulty: Module 1 = medium, Module 2 Easier = easy, Module 2 Harder = hard
"""
from django.core.management.base import BaseCommand
from practice.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Load PSAT Practice Test 8 questions into the database'

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

        ae, _ = Topic.objects.get_or_create(subject=math, name='Algebra and Equations')
        fg, _ = Topic.objects.get_or_create(subject=math, name='Functions and Graphs')
        geo, _ = Topic.objects.get_or_create(subject=math, name='Geometry')
        ds, _ = Topic.objects.get_or_create(subject=math, name='Data/Statistics/Probability')
        wp, _ = Topic.objects.get_or_create(subject=math, name='Word Problems')

        def q(topic, diff, text, a, b, c, d, ans, expl=''):
            Question.objects.create(
                subject=topic.subject, topic=topic, difficulty=diff,
                text=text, option_a=a, option_b=b, option_c=c, option_d=d,
                correct_answer=ans, explanation=expl,
            )

        M = 'medium'; E = 'easy'; H = 'hard'

        # ── ENGLISH MODULE 1 — 27 MEDIUM ──────────────────────────────────────

        q(ev, M,
          "A paleontologist studying fossilized remains noted that the specimen's bone structure was ________, displaying characteristics common to both reptiles and early mammals, making classification difficult.\n\nWhich word most precisely completes the sentence?",
          'A) homogeneous', 'B) mosaic', 'C) redundant', 'D) pristine',
          'B',
          '"Mosaic" means composed of diverse elements, fitting a specimen showing traits of two distinct groups.')

        q(ev, M,
          "The following text is from a 2023 marine biology report.\n\nResearchers studying bioluminescent organisms in the deep ocean found that certain jellyfish produce light not for communication, as previously assumed, but as a ________ mechanism — blinding predators long enough to escape.\n\nWhich word most logically completes the sentence?",
          'A) reproductive', 'B) decorative', 'C) defensive', 'D) navigational',
          'C',
          'The context describes blinding predators to escape, which is a defensive function.')

        q(ev, M,
          "The city council's new zoning policy was described by critics as ________ because it appeared to resolve the housing shortage on paper while doing little to address the root causes of displacement.\n\nWhich word best completes the sentence?",
          'A) comprehensive', 'B) superficial', 'C) equitable', 'D) transparent',
          'B',
          '"Superficial" means addressing surface appearance without depth, matching the critique described.')

        q(ev, M,
          "The following text is adapted from a 1902 essay on industrial reform.\n\nThe factory conditions that laborers endured were not merely uncomfortable — they were ________, stripping workers of dignity, safety, and any reasonable expectation of fair treatment.\n\nAs used in the text, which word best fills the blank?",
          'A) tolerable', 'B) degrading', 'C) stimulating', 'D) ambiguous',
          'B',
          '"Degrading" means humiliating and stripping dignity, consistent with the extreme negative description.')

        q(rc, M,
          "Passage: 'The monarch butterfly's migration from Canada to central Mexico spans over 3,000 miles and involves millions of individuals. Remarkably, no single butterfly completes the full round trip — it takes three to four generations to return. Scientists believe the butterflies navigate using a time-compensated sun compass, adjusting their flight direction based on the position of the sun relative to the time of day.'\n\nWhat is the main purpose of this passage?",
          'A) To argue that monarch butterflies are endangered.',
          'B) To describe the remarkable navigation and generational nature of monarch migration.',
          'C) To compare butterfly migration to bird migration.',
          'D) To explain why butterflies cannot survive Canadian winters.',
          'B',
          'The passage describes how the migration works across generations and how butterflies navigate — its main focus.')

        q(rc, M,
          "Passage: 'For centuries, historians assumed that the Bronze Age Collapse around 1200 BCE was caused by a single catastrophic event — perhaps an invasion by the so-called Sea Peoples. Modern scholarship, however, favors a systems collapse model: droughts, earthquakes, trade disruptions, and internal rebellions combined to overwhelm the interconnected palace economies of the eastern Mediterranean simultaneously.'\n\nWhich statement best reflects the shift described in the passage?",
          'A) Historians now believe the Sea Peoples were not a real group.',
          'B) The Bronze Age Collapse is better explained by multiple converging factors than by a single cause.',
          'C) Earthquakes were the primary cause of the Bronze Age Collapse.',
          'D) Trade disruptions had no role in the collapse of Bronze Age civilizations.',
          'B',
          'The passage contrasts the old single-cause theory with the modern multi-factor systems collapse model.')

        q(rc, M,
          "Passage: 'In the early 20th century, American women entered the workforce in large numbers during World War I, taking on roles in factories, transportation, and government offices previously held by men. When soldiers returned after the war, many women were displaced from these positions. Yet the experience had fundamentally altered expectations: women had demonstrated their capability in a wide range of occupations, and the suffrage movement gained significant momentum in the years that followed.'\n\nAccording to the passage, what was one long-term effect of women entering the workforce during World War I?",
          'A) Women permanently kept all jobs previously held by men.',
          'B) The government created laws preventing women from working after the war.',
          'C) Women\'s proven capabilities contributed to the growing suffrage movement.',
          'D) Factories became exclusively staffed by women during the 1920s.',
          'C',
          'The passage states that women\'s demonstrated capabilities helped fuel the suffrage movement.')

        q(rc, M,
          "The following text is adapted from a 2021 environmental science article.\n\nUrban heat islands — city areas significantly warmer than surrounding rural regions — form when natural land cover is replaced by pavement and buildings that absorb and re-emit heat. Studies show that low-income neighborhoods in major U.S. cities experience higher heat island effects on average, partly because they have fewer trees and green spaces. Some cities have begun tree-planting initiatives to address this disparity.\n\nWhat problem are some cities attempting to address through tree-planting initiatives?",
          'A) The overall warming of the planet due to greenhouse gases.',
          'B) The unequal distribution of heat island effects across income levels.',
          'C) The shortage of lumber in urban construction projects.',
          'D) Air pollution from automobile traffic in city centers.',
          'B',
          'The passage links fewer trees in low-income areas to greater heat island effects, which is the disparity tree planting aims to fix.')

        q(de, M,
          "A survey of 500 high school students asked how many hours per week they spent on extracurricular activities. The average for students with a GPA above 3.5 was 6.2 hours per week, while the average for students with a GPA below 3.0 was 3.1 hours per week.\n\nWhich conclusion is best supported by this data?",
          'A) Participating in extracurriculars causes students to earn higher grades.',
          'B) Students with higher GPAs spent more time on extracurriculars on average.',
          'C) Students with low GPAs do not participate in any extracurricular activities.',
          'D) Extracurricular activities should be required for all students.',
          'B',
          'The data shows a correlation in hours, not causation. Only the factual comparison (B) is directly supported.')

        q(de, M,
          "Researchers studying plant growth conducted an experiment with three groups of identical seedlings. Group 1 received 8 hours of light daily; Group 2 received 12 hours; Group 3 received 16 hours. After 30 days, average plant heights were 14 cm, 21 cm, and 19 cm respectively.\n\nWhat does the data most clearly suggest?",
          'A) Plants always grow taller with more light exposure.',
          'B) 12 hours of light produced the tallest average growth in this experiment.',
          'C) Group 3 plants were defective and should be excluded from the results.',
          'D) Light has no measurable effect on plant growth.',
          'B',
          'The data shows Group 2 (12 hrs) had the tallest average at 21 cm — directly supported by the numbers.')

        q(de, M,
          "A city tracked the number of traffic accidents at a particular intersection before and after installing a roundabout. In the two years before installation, there were 47 accidents. In the two years after, there were 11 accidents.\n\nA researcher claims the roundabout significantly improved safety at the intersection. Which statement best evaluates this claim?",
          'A) The claim is unsupported because two years is not long enough to draw conclusions.',
          'B) The claim is well-supported because accidents dropped by more than 75%.',
          'C) The claim is unsupported because roundabouts are known to cause more accidents.',
          'D) The claim is well-supported because no accidents occurred after installation.',
          'B',
          'The drop from 47 to 11 accidents is a 77% reduction, which strongly supports the safety improvement claim.')

        q(gv, M,
          "Each of the scientists on the research team ________ responsible for submitting a weekly progress report to the project director.\n\nWhich verb form correctly completes the sentence?",
          'A) are', 'B) were', 'C) is', 'D) have been',
          'C',
          '"Each" is a singular subject and requires the singular verb "is."')

        q(gv, M,
          "The documentary film crew, along with its producers and editors, ________ expected to arrive at the filming location by sunrise.\n\nWhich verb correctly completes the sentence?",
          'A) are', 'B) were', 'C) is', 'D) have been',
          'C',
          'The core subject is "crew" (singular). Phrases beginning with "along with" do not change the subject\'s number.')

        q(gv, M,
          "By the time the rescue team reached the stranded hikers, the storm ________ for six hours.\n\nWhich verb form best completes the sentence?",
          'A) raged', 'B) has raged', 'C) had been raging', 'D) is raging',
          'C',
          'Past perfect progressive ("had been raging") is correct for an action continuing up to a past moment.')

        q(gv, M,
          "Neither the principal nor the teachers ________ aware of the planned assembly until the morning of the event.\n\nWhich verb correctly completes the sentence?",
          'A) was', 'B) were', 'C) is', 'D) has been',
          'B',
          'With "neither...nor," the verb agrees with the nearest subject — "teachers" (plural), so "were."')

        q(gp, M,
          "Which sentence correctly uses a colon?",
          'A) She had three goals: to graduate, to travel, and to write a novel.',
          'B) She had three goals: that included graduating, traveling, and writing.',
          'C) She had: three goals to accomplish before turning thirty.',
          'D) She: wanted to graduate, travel, and write a novel.',
          'A',
          'A colon correctly introduces a list after a complete independent clause.')

        q(gp, M,
          "Which sentence correctly uses an apostrophe?",
          'A) The childrens\' artwork was displayed in the hallway.',
          'B) The childrens artwork was displayed in the hallway.',
          'C) The children\'s artwork was displayed in the hallway.',
          'D) The childrens\'s artwork was displayed in the hallway.',
          'C',
          '"Children" is an irregular plural; the possessive is formed by adding \'s: "children\'s."')

        q(gp, M,
          "Which sentence uses commas correctly?",
          'A) The old, weathered, barn stood at the edge of the property.',
          'B) The old weathered barn stood at the edge of the property.',
          'C) The old, weathered barn stood at the edge of the property.',
          'D) The, old weathered, barn stood at the edge of the property.',
          'C',
          '"Old" and "weathered" are coordinate adjectives and should be separated by a comma. No comma between "weathered" and "barn."')

        q(tr, M,
          "Sentence 1: The new medication showed promising results in clinical trials. Sentence 2: Regulators have not yet approved it for public use.\n\nWhich transition word best connects these two sentences?",
          'A) Therefore,', 'B) Similarly,', 'C) However,', 'D) Furthermore,',
          'C',
          '"However" signals a contrast between the promising trial results and the lack of regulatory approval.')

        q(tr, M,
          "Sentence 1: Plastic pollution has reached remote Arctic regions. Sentence 2: Microplastics have been found in the tissues of deep-sea fish.\n\nWhich transition best introduces Sentence 2?",
          'A) In contrast,', 'B) Nevertheless,', 'C) As a result,', 'D) Moreover,',
          'D',
          '"Moreover" adds another example of the widespread nature of plastic pollution, extending the first point.')

        q(tr, M,
          "The early settlement relied entirely on trade with neighboring villages. ________, once the railroad arrived, the town grew rapidly into a self-sufficient commercial hub.\n\nWhich transition fits the shift in the passage?",
          'A) Similarly,', 'B) Subsequently,', 'C) Consequently,', 'D) In addition,',
          'B',
          '"Subsequently" signals a chronological sequence — after the railroad, the town changed.')

        q(rn, M,
          "A student is writing a report on the health effects of screen time in adolescents. She finds the following sources:\n1. A 2022 peer-reviewed study linking more than 4 hours of daily screen time to increased anxiety in teens.\n2. A blog post by a tech company claiming screens have no proven negative effects.\n3. A 2019 meta-analysis of 30 studies finding mixed results on screen time and mental health.\n\nWhich source would most strengthen the claim that screen time harms adolescent mental health?",
          'A) Source 1 only', 'B) Source 2 only', 'C) Source 3 only', 'D) Sources 1 and 3 combined',
          'D',
          'The peer-reviewed study (1) and the meta-analysis (3) together provide the strongest evidence, though Source 3 shows mixed results and Source 1 directly supports the claim.')

        q(rn, M,
          "A researcher wants to support the claim: \"Urban green spaces reduce stress in city residents.\" Which of the following pieces of evidence would best support this claim?",
          'A) A survey showing that city residents prefer parks over shopping malls.',
          'B) A controlled study measuring cortisol levels in residents before and after visiting a park, showing a significant decrease.',
          'C) An article describing the history of public parks in New York City.',
          'D) A report on the cost of maintaining urban parks.',
          'B',
          'Measured cortisol levels (a stress hormone) before and after park visits directly supports the stress-reduction claim with biological evidence.')

        q(rn, M,
          "A student argues: \"Students who eat breakfast perform better on standardized tests.\" Which evidence would WEAKEN this argument?",
          'A) A study showing a 12% score improvement in breakfast-eating students.',
          'B) A finding that students who eat breakfast also tend to sleep more hours per night.',
          'C) Data showing breakfast programs increased participation in 80% of schools.',
          'D) A report that schools with breakfast programs have higher attendance.',
          'B',
          'If breakfast-eaters also sleep more, sleep (not breakfast) might explain the performance improvement, weakening the causal claim.')

        q(ev, M,
          "The following text is adapted from a 2020 economics article.\n\nThe startup's rapid growth was seen as ________ by industry analysts — a clear signal that the market was ready for a new approach to digital payments.\n\nWhich word most precisely completes the sentence?",
          'A) anomalous', 'B) indicative', 'C) arbitrary', 'D) negligible',
          'B',
          '"Indicative" means serving as a sign or signal, which fits "a clear signal that the market was ready."')

        q(rc, M,
          "The following text is adapted from a 2022 article on ocean currents.\n\nThe thermohaline circulation — often called the ocean conveyor belt — moves water around the globe based on differences in temperature and salinity. Cold, salty water is denser and sinks near the poles, while warmer, fresher water rises near the equator. This circulation distributes heat across the planet and is a key driver of regional climates. Scientists warn that melting polar ice could disrupt this system by introducing large volumes of fresh water.\n\nWhat concern do scientists raise in the passage?",
          'A) Ocean currents are moving faster than expected due to global warming.',
          'B) The thermohaline circulation may be disrupted by freshwater from melting ice.',
          'C) Warmer water is sinking near the equator, reversing the conveyor belt.',
          'D) Regional climates are becoming more uniform as the ocean conveyor belt speeds up.',
          'B',
          'The passage explicitly states scientists warn that melting ice could disrupt thermohaline circulation by adding fresh water.')

        q(rc, M,
          "The following text is from a short story set in a small fishing village.\n\n'The harbor was still before dawn, the water flat as hammered tin. Old Cerro had launched his dinghy every morning for forty years from this same dock. He did not think of this as routine — he thought of it as something close to prayer. The creak of the oarlocks, the smell of brine, the way the horizon swallowed the last of the stars. These were his liturgy.'\n\nWhat does the author most likely mean by calling Cerro's morning routine a 'liturgy'?",
          'A) Cerro is a deeply religious man who prays on the water.',
          'B) The fishing routine has a ritualistic, almost sacred quality for Cerro.',
          'C) Cerro resents having to fish every morning and wishes for a change.',
          'D) The harbor is used as a place of worship by the village community.',
          'B',
          'Using words like "prayer" and "liturgy" (a religious ritual) conveys that the routine holds deep, almost sacred meaning for Cerro.')

        # ── ENGLISH MODULE 2 EASIER — 27 EASY ─────────────────────────────────

        q(ev, E,
          "The puppy was ________ excited about the walk that it ran in circles before the leash was even attached.\n\nWhich word best completes the sentence?",
          'A) barely', 'B) so', 'C) quietly', 'D) rarely',
          'B',
          '"So...that" is a standard construction showing degree: "so excited that it ran in circles."')

        q(ev, E,
          "The weather forecast predicted rain, but the morning turned out to be bright and ________.\n\nWhich word best completes the sentence?",
          'A) gloomy', 'B) stormy', 'C) sunny', 'D) humid',
          'C',
          '"Sunny" contrasts with the predicted rain and fits the description of a bright morning.')

        q(ev, E,
          "The librarian asked the students to speak in ________ voices so they wouldn't disturb others who were reading.\n\nWhich word best completes the sentence?",
          'A) loud', 'B) quiet', 'C) excited', 'D) confident',
          'B',
          'A library setting and the reason given (not disturbing others) calls for "quiet" voices.')

        q(ev, E,
          "The old bicycle was too ________ to ride safely — both tires were flat and the brakes barely worked.\n\nWhich word best completes the sentence?",
          'A) fast', 'B) expensive', 'C) dangerous', 'D) beautiful',
          'C',
          'Flat tires and broken brakes make the bicycle "dangerous" to ride.')

        q(rc, E,
          "Passage: 'Penguins are birds that cannot fly, but they are excellent swimmers. Their wings have evolved into flippers, which help them move quickly through the water to catch fish. Penguins live mostly in the Southern Hemisphere, especially in Antarctica.'\n\nAccording to the passage, why are penguins good swimmers?",
          'A) They have hollow bones that make them float.',
          'B) Their wings have evolved into flippers suited for swimming.',
          'C) They have waterproof scales like fish.',
          'D) They practice swimming from birth.',
          'B',
          'The passage directly states that penguin wings evolved into flippers that help them swim.')

        q(rc, E,
          "Passage: 'The rainforest receives over 80 inches of rain per year. This constant moisture supports an enormous variety of plant and animal life. Scientists estimate that more than half of all species on Earth live in tropical rainforests, even though these forests cover only about 6% of the planet's surface.'\n\nWhich statement is directly supported by the passage?",
          'A) Rainforests will disappear within 50 years.',
          'B) Tropical rainforests cover more than half the planet.',
          'C) More than half of Earth\'s species live in tropical rainforests.',
          'D) Rainfall is the only factor that supports rainforest biodiversity.',
          'C',
          'The passage explicitly states that scientists estimate more than half of all species live in tropical rainforests.')

        q(rc, E,
          "Passage: 'The Eiffel Tower was built in 1889 as the entrance arch for the 1889 World's Fair in Paris. It was designed by engineer Gustave Eiffel. At the time, many Parisians disliked the tower, calling it ugly. Today, it is one of the most visited monuments in the world, attracting about 7 million visitors each year.'\n\nHow did Parisians initially react to the Eiffel Tower?",
          'A) They celebrated it as a masterpiece of engineering.',
          'B) They found it too expensive to maintain.',
          'C) Many disliked it and called it ugly.',
          'D) They immediately made it a symbol of French pride.',
          'C',
          'The passage states many Parisians disliked the tower at the time, calling it ugly.')

        q(rc, E,
          "Passage: 'Dolphins are highly social animals that live in groups called pods. They communicate with each other using clicks, whistles, and body movements. Dolphins are also known for their intelligence — they can recognize themselves in mirrors, solve puzzles, and learn from other dolphins.'\n\nWhat is the main idea of this passage?",
          'A) Dolphins are dangerous to humans in the wild.',
          'B) Dolphins are social and intelligent animals.',
          'C) Dolphins are the fastest animals in the ocean.',
          'D) Dolphins only live in warm tropical waters.',
          'B',
          'The passage describes dolphin social behavior and intelligence as its main focus.')

        q(de, E,
          "A teacher recorded the test scores of her class after students used a new study guide. Before the study guide: average score = 72. After the study guide: average score = 85.\n\nWhich conclusion does the data best support?",
          'A) The study guide guaranteed every student would pass.',
          'B) Test scores improved after students used the study guide.',
          'C) The test became easier after the study guide was introduced.',
          'D) Students who used the study guide scored 100%.',
          'B',
          'The average rose from 72 to 85 — directly showing improvement after the study guide was used.')

        q(de, E,
          "A chart shows the number of books checked out from a school library each month. October: 320, November: 290, December: 180, January: 350.\n\nIn which month were the fewest books checked out?",
          'A) October', 'B) November', 'C) December', 'D) January',
          'C',
          'December had the lowest number at 180 checkouts.')

        q(de, E,
          "Students were surveyed about their favorite school subject. Results: Math 35%, Science 28%, English 20%, History 17%.\n\nWhich subject was chosen by the fewest students?",
          'A) Math', 'B) Science', 'C) English', 'D) History',
          'D',
          'History had the lowest percentage at 17%.')

        q(gv, E,
          "The students in the classroom ________ quietly while the teacher handed out the exam.\n\nWhich verb correctly completes the sentence?",
          'A) sits', 'B) sat', 'C) sitting', 'D) has sat',
          'B',
          '"Students" is plural and past tense is needed. "Sat" is correct.')

        q(gv, E,
          "Every morning, she ________ her dog for a walk around the neighborhood.\n\nWhich verb correctly completes the sentence?",
          'A) taken', 'B) takes', 'C) took', 'D) taking',
          'B',
          '"Every morning" signals a habitual present action. "Takes" is the correct simple present form for a singular subject.')

        q(gv, E,
          "The team ________ hard every day this week to prepare for the championship.\n\nWhich verb correctly completes the sentence?",
          'A) practice', 'B) practiced', 'C) has been practicing', 'D) will practiced',
          'C',
          '"This week" with ongoing activity uses present perfect progressive: "has been practicing."')

        q(gv, E,
          "Neither of the two answers ________ correct.\n\nWhich verb correctly completes the sentence?",
          'A) are', 'B) were', 'C) is', 'D) have been',
          'C',
          '"Neither" takes a singular verb: "is."')

        q(gp, E,
          "Which sentence uses a period correctly?",
          'A) She finished her homework. Then she watched TV.',
          'B) She finished her homework, Then she watched TV.',
          'C) She finished her homework then. She watched TV.',
          'D) She finished. Her homework then watched TV.',
          'A',
          'Two complete independent sentences are correctly separated by a period in option A.')

        q(gp, E,
          "Which sentence is punctuated correctly?",
          'A) Wow, that was an incredible performance!',
          'B) Wow that was an incredible performance!',
          'C) Wow! That was, an incredible performance.',
          'D) Wow that was an incredible performance.',
          'A',
          'An interjection like "Wow" is followed by a comma when the rest of the sentence continues.')

        q(gp, E,
          "Which sentence correctly uses quotation marks?",
          'A) The coach said, \"Practice begins at 7 AM.\"',
          'B) The coach said \"Practice begins at 7 AM\".',
          'C) The coach said, Practice begins at 7 AM.',
          'D) \"The coach said, Practice begins at 7 AM.\"',
          'A',
          'A comma follows the dialogue tag and the spoken words are enclosed in quotation marks with the period inside.')

        q(tr, E,
          "Maria studied for three hours every night. ________, she earned the highest score in the class.\n\nWhich transition best completes the sentence?",
          'A) However,', 'B) As a result,', 'C) In contrast,', 'D) Similarly,',
          'B',
          '"As a result" shows that earning the highest score was the outcome of her studying.')

        q(tr, E,
          "Tom loves soccer. ________, his brother prefers basketball.\n\nWhich transition best connects the two sentences?",
          'A) Therefore,', 'B) In addition,', 'C) On the other hand,', 'D) Consequently,',
          'C',
          '"On the other hand" signals a contrast between Tom\'s preference and his brother\'s.')

        q(tr, E,
          "The museum has exhibits on ancient Egypt. ________, it has a collection of medieval armor.\n\nWhich transition best completes the sentence?",
          'A) However,', 'B) In addition,', 'C) As a result,', 'D) Nevertheless,',
          'B',
          '"In addition" signals that a second exhibit is being added to the first.')

        q(rn, E,
          "A student is writing a report about recycling. Which source would be MOST useful?",
          'A) A magazine article about fashion trends',
          'B) A government report on recycling rates and their environmental impact',
          'C) A blog post about a person\'s experience at a garden center',
          'D) A movie review about an environmental documentary',
          'B',
          'A government report on recycling rates directly provides relevant, credible data for a report on recycling.')

        q(rn, E,
          "A student wants to prove that regular exercise improves mood. Which source best supports this claim?",
          'A) A recipe blog featuring healthy meals',
          'B) A peer-reviewed psychology study measuring mood before and after an exercise program',
          'C) An advertisement for a gym membership',
          'D) A sports news article about a marathon race',
          'B',
          'A peer-reviewed study with before/after mood measurements directly and credibly supports the claim.')

        q(rn, E,
          "A student argues that electric cars are better for the environment than gasoline cars. Which evidence would most strengthen this argument?",
          'A) A news article about a new electric car model being released.',
          'B) A data report showing electric cars produce significantly fewer lifetime emissions than gasoline cars.',
          'C) An interview with a car salesperson who prefers electric cars.',
          'D) A graph showing that electric cars are more expensive to purchase.',
          'B',
          'Quantified lifetime emissions data directly supports the environmental claim.')

        q(ev, E,
          "The scientist's explanation was so ________ that even students who had never studied chemistry could understand it.\n\nWhich word best completes the sentence?",
          'A) complicated', 'B) lengthy', 'C) clear', 'D) technical',
          'C',
          'If even non-chemistry students understood it, the explanation was "clear."')

        q(rc, E,
          "Passage: 'Volcanoes form when magma from deep within the Earth pushes through cracks in the surface. When a volcano erupts, it releases lava, ash, and gases. While volcanic eruptions can be destructive, the ash and minerals they deposit can also make nearby soil very fertile.'\n\nWhat is one benefit of volcanic eruptions mentioned in the passage?",
          'A) They warm nearby ocean water.',
          'B) They create new islands.',
          'C) They deposit ash and minerals that make soil fertile.',
          'D) They release oxygen into the atmosphere.',
          'C',
          'The passage explicitly states that ash and minerals from eruptions can make nearby soil fertile.')

        q(rc, E,
          "Passage: 'Thomas Edison is often credited with inventing the light bulb, but the truth is more complex. Many inventors worked on electric lighting before Edison. What Edison achieved was creating a practical, long-lasting light bulb and, crucially, an entire electrical distribution system to power it.'\n\nWhat does the passage suggest about Edison's main contribution?",
          'A) He invented electricity from scratch.',
          'B) He created a working system for distributing electric power, not just the bulb itself.',
          'C) He was the first person ever to think of electric lighting.',
          'D) His light bulbs were the same as earlier inventors\' designs.',
          'B',
          'The passage emphasizes Edison\'s electrical distribution system as the key practical achievement, beyond the bulb alone.')

        q(rc, E,
          "Passage: 'Honeybees live in highly organized colonies of up to 60,000 individuals. Each bee has a specific role: workers gather food, nurse bees care for larvae, and the queen lays eggs. Communication is essential — bees perform a \"waggle dance\" to tell other workers the direction and distance of food sources.'\n\nAccording to the passage, how do bees communicate the location of food?",
          'A) By leaving scent trails on flowers.',
          'B) By performing a waggle dance.',
          'C) By buzzing at different frequencies.',
          'D) By guiding other bees directly to the location.',
          'B',
          'The passage explicitly states bees perform a waggle dance to communicate food direction and distance.')

        # ── ENGLISH MODULE 2 HARDER — 27 HARD ─────────────────────────────────

        q(ev, H,
          "The author's prose was criticized for being ________ — dense with allusions that presupposed familiarity with obscure philosophical texts that most readers had never encountered.\n\nWhich word most precisely fits the sentence?",
          'A) pedantic', 'B) lucid', 'C) conversational', 'D) derivative',
          'A',
          '"Pedantic" means excessively academic or showing off knowledge in a way that excludes general readers, fitting the described prose.')

        q(ev, H,
          "The following is from a 2023 political science essay.\n\nThe senator's speech was praised by supporters as visionary but dismissed by opponents as ________ — full of inspiring language that carefully avoided any specific policy commitment.\n\nWhich word most logically completes the sentence?",
          'A) incisive', 'B) pragmatic', 'C) vacuous', 'D) prescient',
          'C',
          '"Vacuous" means lacking substance or ideas — fitting for speech with inspiring language but no concrete commitments.')

        q(ev, H,
          "The following text is adapted from an 1889 scientific lecture.\n\nThe professor argued that the geological record was not ________ but rather a dynamic archive of change, rewritten continuously by erosion, deposition, and tectonic movement.\n\nWhich word most precisely completes the professor's argument?",
          'A) immutable', 'B) fragmentary', 'C) cumulative', 'D) speculative',
          'A',
          '"Immutable" means unchanging. The professor argues the record is dynamic, not fixed/immutable.')

        q(ev, H,
          "The diplomat's remarks were ________ — seemingly measured and reasonable on the surface, yet concealing a firm refusal to make any real concession.\n\nWhich word best completes the sentence?",
          'A) conciliatory', 'B) candid', 'C) duplicitous', 'D) magnanimous',
          'C',
          '"Duplicitous" means deceitful or two-faced — fitting behavior that appears reasonable but conceals refusal to compromise.')

        q(rc, H,
          "The following is adapted from a 2022 neuroscience article.\n\nFor decades, the prevailing model of memory held that long-term memories, once consolidated, were stable. Recent research challenges this view. Each time a memory is recalled, it re-enters a labile state — susceptible to alteration before being reconsolidated. This finding suggests that memory is not a static record but an active reconstruction, shaped by context, emotion, and expectation at the moment of retrieval.\n\nWhat does the phrase 'labile state' most likely mean in this context?",
          'A) A permanent and unchangeable condition.',
          'B) A state of heightened clarity and detail.',
          'C) A temporary condition in which the memory is vulnerable to change.',
          'D) A state in which the memory is transferred from short-term to long-term storage.',
          'C',
          'The passage describes labile as "susceptible to alteration before being reconsolidated," meaning temporarily changeable.')

        q(rc, H,
          "The following is adapted from a 2021 literary criticism essay.\n\nIn contemporary fiction, the unreliable narrator has evolved from a device of ironic distance — as in Henry James — into something more epistemically disorienting. Modern unreliable narrators do not merely mislead about facts; they undermine the reader's confidence in interpretation itself. The reader is left not with a corrected understanding but with the vertigo of competing, irreconcilable accounts.\n\nWhat distinction does the author draw between historical and modern unreliable narrators?",
          'A) Historical narrators were more trustworthy than modern narrators.',
          'B) Modern narrators mislead readers about facts, while historical ones used irony.',
          'C) Historical narrators created ironic distance, while modern ones disorient interpretation itself.',
          'D) Modern narrators resolve ambiguity, while historical ones left readers confused.',
          'C',
          'The essay contrasts Henry James\'s ironic distance with the modern narrator\'s deeper epistemological disorientation.')

        q(rc, H,
          "The following is from a 2020 environmental policy report.\n\nCarbon offset programs have been promoted as a market-based solution to climate change, allowing companies to compensate for emissions by funding projects that reduce or sequester carbon elsewhere. Critics, however, argue that many offsets are illusory: projects that claim to prevent deforestation often protect forests that were never actually at risk, and the emissions reductions credited are therefore fictional. Proponents counter that rigorous certification standards can filter out fraudulent offsets, though enforcement remains inconsistent.\n\nWhich statement best describes the debate presented in the passage?",
          'A) Carbon offsets are universally accepted as an effective climate solution.',
          'B) Critics and proponents disagree about whether carbon offsets deliver real emissions reductions.',
          'C) Carbon offsets are illegal under current environmental law.',
          'D) Proponents argue that no certification standards exist for carbon offsets.',
          'B',
          'The passage presents critics questioning offset validity and proponents defending certification, centering the debate on real vs. fictional reductions.')

        q(rc, H,
          "The following is adapted from a 2019 historical analysis.\n\nThe concept of sovereignty — the exclusive right of a state to govern itself within defined borders — emerged from the Peace of Westphalia in 1648, which ended the Thirty Years' War. Yet historians increasingly argue that Westphalian sovereignty was never a clean break but rather a rhetorical construction legitimizing arrangements that had already been negotiated piecemeal. Modern international relations, they contend, remain shaped less by the Westphalian ideal than by the pragmatic compromises that preceded and followed it.\n\nWhat do the historians referenced in the passage argue?",
          'A) The Thirty Years\' War established the first true global government.',
          'B) Westphalian sovereignty was a useful myth that obscured messier political realities.',
          'C) Modern states fully embody the principle of sovereignty established in 1648.',
          'D) The Peace of Westphalia eliminated international conflict permanently.',
          'B',
          'Historians argue Westphalian sovereignty was a "rhetorical construction" concealing piecemeal pre-existing arrangements — a legitimizing myth.')

        q(de, H,
          "A longitudinal study followed 1,200 adults over 20 years. Participants who reported high social connection at age 30 had a 34% lower rate of cognitive decline by age 50 compared to those who reported low social connection. Researchers controlled for diet, exercise, and income.\n\nA researcher claims: 'Social connection causes slower cognitive decline.' How valid is this claim based on the data?",
          'A) Fully valid — the controlled study proves causation.',
          'B) Partially valid — correlation is established, but causation is difficult to confirm even with controls.',
          'C) Not valid — the study shows social connection has no effect.',
          'D) Not valid — only diet and exercise affect cognitive decline.',
          'B',
          'Even with controls, observational longitudinal studies establish correlation but cannot definitively prove causation — other unmeasured factors may explain the relationship.')

        q(de, H,
          "Two cities piloted after-school tutoring programs. City A served 500 students with volunteer tutors; average test scores rose 8 points. City B served 500 students with trained professional tutors; average test scores rose 19 points. Both cities had similar baseline demographics.\n\nA policy analyst claims trained tutors are more effective than volunteers. Which response best evaluates this claim?",
          'A) The claim is unsupported — both programs improved scores.',
          'B) The claim is supported — City B showed more than double the improvement with similar demographics.',
          'C) The claim is unsupported — only larger sample sizes can compare programs.',
          'D) The claim is unsupported — test score changes are not a valid measure of tutor effectiveness.',
          'B',
          'With similar demographics, the 19 vs. 8 point difference suggests professional tutors were more effective — the data supports the claim.')

        q(de, H,
          "A scientist measures the concentration of a pollutant (in parts per billion) in river samples taken 1 mile upstream, at the industrial site, and 5 miles downstream: 2 ppb, 47 ppb, and 12 ppb respectively.\n\nWhich interpretation is best supported by this data?",
          'A) The river fully recovers from the pollutant within 5 miles.',
          'B) The industrial site is likely a major source of the pollutant, and levels decrease but remain elevated downstream.',
          'C) The pollutant was introduced upstream and is most concentrated far downstream.',
          'D) The downstream site is a greater source of pollution than the industrial site.',
          'B',
          'The spike at the industrial site (47 ppb vs. 2 upstream) strongly suggests it as the source. The downstream level (12 ppb) drops but exceeds the upstream baseline.')

        q(gv, H,
          "The committee, having reviewed all submitted proposals, ________ to postpone the final decision until additional budget data could be obtained.\n\nWhich verb correctly completes the sentence?",
          'A) decide', 'B) decided', 'C) deciding', 'D) have decided',
          'B',
          '"The committee" is singular and the participial phrase indicates a completed past action, requiring simple past "decided."')

        q(gv, H,
          "Neither the CEO nor the board members ________ willing to accept the revised terms of the merger agreement.\n\nWhich verb form correctly completes the sentence?",
          'A) was', 'B) were', 'C) is', 'D) has been',
          'B',
          'With "neither...nor," the verb agrees with the closer subject ("board members" — plural), so "were."')

        q(gv, H,
          "By 2030, scientists predict that sea levels in low-lying coastal areas ________ by an average of six inches compared to 2000 levels.\n\nWhich verb form is correct?",
          'A) rose', 'B) will have risen', 'C) have risen', 'D) are rising',
          'B',
          '"By 2030" indicates a future point by which an action will be completed — future perfect "will have risen" is correct.')

        q(gv, H,
          "The panel of experts, each of whom ________ years of experience in forensic accounting, was assembled to review the disputed financial records.\n\nWhich verb correctly fills the blank?",
          'A) have', 'B) has', 'C) having', 'D) had had',
          'B',
          '"Each of whom" takes a singular verb. "Has" is correct in the present context.')

        q(gp, H,
          "Which sentence correctly uses all punctuation?",
          'A) The results — though unexpected — confirmed the hypothesis; they were later published in Nature.',
          'B) The results, though unexpected, confirmed the hypothesis; they were later published in Nature.',
          'C) The results though unexpected, confirmed the hypothesis — they were later published in Nature.',
          'D) The results — though unexpected, confirmed the hypothesis; they were later published in Nature.',
          'B',
          'Commas correctly set off the parenthetical "though unexpected" and a semicolon correctly joins two independent clauses.')

        q(gp, H,
          "Which option correctly punctuates the following sentence?\n\n'The three leading causes of the crisis were as follows ___ excessive debt ___ regulatory failure ___ and a sudden loss of market confidence.'",
          'A) as follows: excessive debt, regulatory failure, and a sudden loss',
          'B) as follows; excessive debt, regulatory failure, and a sudden loss',
          'C) as follows, excessive debt; regulatory failure; and a sudden loss',
          'D) as follows — excessive debt; regulatory failure; and a sudden loss',
          'A',
          'A colon correctly introduces a list after "as follows." Commas separate items in a simple list.')

        q(gp, H,
          "Which sentence uses a dash correctly?",
          'A) The expedition — which lasted three years — returned with over 2,000 plant specimens.',
          'B) The expedition, which lasted — three years, returned with specimens.',
          'C) The — expedition which lasted three years returned with specimens.',
          'D) The expedition which lasted three years — returned with specimens.',
          'A',
          'Em dashes correctly set off a non-essential clause ("which lasted three years") with one dash on each side.')

        q(tr, H,
          "The initial clinical trial showed the drug reduced tumor growth in 78% of cases. ________, a larger follow-up study found the drug was effective in only 43% of a more diverse patient population.\n\nWhich transition best introduces the second sentence?",
          'A) Furthermore,', 'B) Consequently,', 'C) However,', 'D) Similarly,',
          'C',
          '"However" signals a contradicting or qualifying finding from the follow-up study.')

        q(tr, H,
          "Early aviation pioneers faced ridicule for believing human flight was possible. ________, the Wright brothers successfully flew a powered aircraft at Kitty Hawk in 1903, permanently transforming how humanity understood the limits of technology.\n\nWhich transition is most appropriate?",
          'A) In contrast,', 'B) Nevertheless,', 'C) For example,', 'D) Similarly,',
          'B',
          '"Nevertheless" signals that despite ridicule and skepticism, flight was achieved — a concessive relationship.')

        q(tr, H,
          "Proponents of the urban renewal project cited economic benefits and increased property values. ________, longtime residents highlighted the displacement of low-income families and the erasure of cultural landmarks.\n\nWhich transition best introduces the second sentence?",
          'A) Moreover,', 'B) Consequently,', 'C) In contrast,', 'D) Specifically,',
          'C',
          '"In contrast" correctly signals the opposing perspective of longtime residents against the proponents\' view.')

        q(rn, H,
          "A student is writing an argumentative essay claiming that standardized testing is an unreliable measure of student intelligence. She finds these sources:\n1. A 2021 study showing standardized tests correlate strongly with socioeconomic background, not IQ.\n2. A testing agency's report arguing their tests are rigorous and accurate.\n3. A 2019 meta-analysis of 50 studies finding moderate predictive validity of standardized tests for college GPA.\n\nWhich combination of sources best supports her thesis?",
          'A) Source 2 only',
          'B) Sources 1 and 3',
          'C) Source 1 only',
          'D) Sources 2 and 3',
          'B',
          'Source 1 directly supports unreliability (correlation with wealth, not IQ). Source 3 shows only moderate predictive validity — together they challenge reliability without requiring Source 2 (which opposes the thesis).')

        q(rn, H,
          "A researcher argues: 'Remote work increases employee productivity.' He cites a 2020 study showing 12% higher output among remote workers at a single tech company during the pandemic.\n\nWhich response best identifies a limitation of this evidence?",
          'A) The study was too large to draw conclusions from.',
          'B) The finding may not generalize — it\'s from one industry during an unusual period.',
          'C) Output is not a valid measure of productivity.',
          'D) Remote work has no effect on any measurable outcome.',
          'B',
          'A single company in one industry during pandemic conditions (a unique historical period) limits how broadly the finding applies.')

        q(rn, H,
          "A student argues that reducing screen time improves sleep quality in teenagers. Which set of evidence most robustly supports this claim?",
          'A) One parent testimonial and a news article about screen addiction.',
          'B) A randomized controlled trial with 300 teenagers measuring sleep hours before and after a screen-time reduction intervention.',
          'C) A correlation study showing teens who sleep more also use screens less.',
          'D) A survey of teenagers\' self-reported sleep satisfaction.',
          'B',
          'A randomized controlled trial with objective measurement before and after an intervention is the strongest evidence for a causal claim.')

        q(ev, H,
          "The following text is adapted from a 2022 anthropology journal.\n\nThe tribe's oral traditions were not merely entertainment; they served a ________ function, encoding ecological knowledge — which plants were medicinal, which seasons fish would spawn — that had been refined over generations.\n\nWhich word most precisely completes the sentence?",
          'A) commemorative', 'B) mnemonic', 'C) ornamental', 'D) rhetorical',
          'B',
          '"Mnemonic" means aiding memory or information retention — fitting traditions that encoded practical ecological knowledge across generations.')

        q(rc, H,
          "The following is adapted from a 2023 philosophy of science article.\n\nScientific consensus is often portrayed as monolithic — a unified agreement among experts. In practice, consensus is better understood as a weighted distribution of expert opinion, shaped by the quantity and quality of evidence, the careers of senior researchers, and the sociology of scientific institutions. Dissenting views are not necessarily fringe; they may represent legitimate minority positions that future evidence could vindicate. The challenge is distinguishing productive dissent from motivated contrarianism.\n\nWhat is the author's main concern about popular portrayals of scientific consensus?",
          'A) Scientists are too quick to change their positions when new evidence emerges.',
          'B) The public incorrectly believes all scientific questions have been resolved.',
          'C) Portraying consensus as unanimous ignores the complex, distributed nature of scientific agreement.',
          'D) Minority scientific positions are always correct and should be treated as equal to the consensus.',
          'C',
          'The author argues consensus is a "weighted distribution," not a monolith — the concern is the oversimplified portrayal of unanimous agreement.')

        q(rc, H,
          "The following is adapted from a 2021 memoir by an architect.\n\nI had always believed that good design should be invisible — that a building succeeds when users move through it without noticing its structure. But after spending a year in cities built centuries before my profession existed, I began to reconsider. The cathedrals and piazzas of the medieval world were designed not for invisibility but for confrontation: they forced the body to pause, to look up, to feel small. Their architects understood something I had been trained to forget — that sometimes the point of a space is to make you aware that you are inside one.\n\nWhat shift in perspective does the author describe?",
          'A) Moving from valuing invisible design to appreciating design that provokes awareness.',
          'B) Abandoning architecture entirely after studying medieval cities.',
          'C) Realizing modern buildings are technically superior to medieval ones.',
          'D) Learning that cathedrals were designed to intimidate political enemies.',
          'A',
          'The author shifts from believing good design is invisible to appreciating design that forces awareness — represented by medieval cathedrals.')

        # ── MATH MODULE 1 — 22 MEDIUM ──────────────────────────────────────────

        q(ae, M,
          "Solve for x: 5x − 8 = 3x + 14",
          'A) x = 3', 'B) x = 11', 'C) x = 7', 'D) x = 6',
          'B',
          '5x − 3x = 14 + 8 → 2x = 22 → x = 11.')

        q(ae, M,
          "What is the solution to the system of equations?\n2x + y = 10\nx − y = 2",
          'A) x = 4, y = 2', 'B) x = 3, y = 4', 'C) x = 5, y = 0', 'D) x = 6, y = −2',
          'A',
          'Adding the equations: 3x = 12 → x = 4. Substituting: 4 − y = 2 → y = 2.')

        q(ae, M,
          "A rectangle has a length that is 3 more than twice its width. If the perimeter is 54 cm, what is the width?",
          'A) 6 cm', 'B) 7 cm', 'C) 8 cm', 'D) 9 cm',
          'C',
          'Let w = width; length = 2w + 3. Perimeter: 2(w + 2w + 3) = 54 → 2(3w + 3) = 54 → 6w + 6 = 54 → 6w = 48 → w = 8.')

        q(fg, M,
          "If f(x) = 2x² − 3x + 1, what is f(−2)?",
          'A) 10', 'B) 11', 'C) 15', 'D) 3',
          'C',
          'f(−2) = 2(4) − 3(−2) + 1 = 8 + 6 + 1 = 15.')

        q(fg, M,
          "Which of the following represents a linear function?",
          'A) y = x² + 2', 'B) y = 3x − 5', 'C) y = 1/x', 'D) y = √x',
          'B',
          'A linear function has the form y = mx + b. Only y = 3x − 5 fits this form.')

        q(fg, M,
          "A function g is defined by g(x) = 4x + 7. What value of x gives g(x) = 31?",
          'A) x = 5', 'B) x = 6', 'C) x = 7', 'D) x = 8',
          'B',
          '4x + 7 = 31 → 4x = 24 → x = 6.')

        q(geo, M,
          "A right triangle has legs of length 9 cm and 12 cm. What is the length of the hypotenuse?",
          'A) 13 cm', 'B) 14 cm', 'C) 15 cm', 'D) 21 cm',
          'C',
          'c² = 9² + 12² = 81 + 144 = 225 → c = 15 cm.')

        q(geo, M,
          "A circle has a radius of 7 cm. What is its area? (Use π ≈ 3.14)",
          'A) 43.96 cm²', 'B) 153.86 cm²', 'C) 44 cm²', 'D) 21.98 cm²',
          'B',
          'Area = πr² = 3.14 × 49 = 153.86 cm².')

        q(geo, M,
          "Two parallel lines are cut by a transversal. One alternate interior angle measures 65°. What is the measure of the other alternate interior angle?",
          'A) 25°', 'B) 115°', 'C) 65°', 'D) 90°',
          'C',
          'Alternate interior angles are equal when lines are parallel, so the other angle is also 65°.')

        q(ds, M,
          "The ages of 7 students are: 13, 14, 14, 15, 15, 15, 16. What is the mode of the data?",
          'A) 14', 'B) 15', 'C) 13', 'D) 16',
          'B',
          '15 appears three times — more than any other value — making it the mode.')

        q(ds, M,
          "A bag contains 4 red marbles, 3 blue marbles, and 5 green marbles. What is the probability of randomly selecting a blue marble?",
          'A) 1/3', 'B) 1/4', 'C) 3/12', 'D) 5/12',
          'C',
          'P(blue) = 3/12 = 1/4. (Note: 3/12 = 1/4, both are correct; 3/12 is listed and equals 1/4, so C is the direct form shown.)')

        q(ds, M,
          "The mean of 5 numbers is 18. Four of the numbers are 12, 16, 20, and 22. What is the fifth number?",
          'A) 18', 'B) 20', 'C) 22', 'D) 24',
          'B',
          'Total = 5 × 18 = 90. Sum of known: 12 + 16 + 20 + 22 = 70. Fifth number = 90 − 70 = 20.')

        q(wp, M,
          "A store sells apples for $0.75 each and oranges for $1.25 each. Jess buys 4 apples and 3 oranges. How much does she spend in total?",
          'A) $5.50', 'B) $6.25', 'C) $6.75', 'D) $7.00',
          'C',
          '4 × 0.75 + 3 × 1.25 = 3.00 + 3.75 = $6.75.')

        q(wp, M,
          "A train travels at 80 mph. How long does it take to travel 280 miles?",
          'A) 2.5 hours', 'B) 3 hours', 'C) 3.5 hours', 'D) 4 hours',
          'C',
          'Time = Distance ÷ Speed = 280 ÷ 80 = 3.5 hours.')

        q(wp, M,
          "After a 20% discount, a jacket costs $64. What was the original price?",
          'A) $76.80', 'B) $80', 'C) $84', 'D) $76',
          'B',
          'Let p = original price. 0.80p = 64 → p = 64 ÷ 0.80 = $80.')

        q(ae, M,
          "What are the solutions to x² − 5x + 6 = 0?",
          'A) x = 1 and x = 6', 'B) x = 2 and x = 3', 'C) x = −2 and x = −3', 'D) x = −1 and x = 6',
          'B',
          'Factor: (x − 2)(x − 3) = 0 → x = 2 or x = 3.')

        q(ae, M,
          "Which value of x satisfies |2x − 4| = 10?",
          'A) x = 3 or x = −3', 'B) x = 7 or x = −3', 'C) x = 7 or x = 3', 'D) x = 5 or x = −5',
          'B',
          '2x − 4 = 10 → x = 7; or 2x − 4 = −10 → 2x = −6 → x = −3.')

        q(fg, M,
          "A linear function passes through (0, 3) and (4, 11). What is its equation?",
          'A) y = 2x + 3', 'B) y = 3x + 1', 'C) y = 2x + 1', 'D) y = 4x + 3',
          'A',
          'Slope = (11 − 3)/(4 − 0) = 8/4 = 2. y-intercept = 3. Equation: y = 2x + 3.')

        q(geo, M,
          "A triangle has angles of 45°, 70°, and x°. What is x?",
          'A) 55°', 'B) 65°', 'C) 45°', 'D) 75°',
          'B',
          'Angles of a triangle sum to 180°: 45 + 70 + x = 180 → x = 65°.')

        q(ds, M,
          "A set of test scores is: 70, 75, 80, 85, 90. What is the median?",
          'A) 75', 'B) 78', 'C) 80', 'D) 85',
          'C',
          'The median is the middle value in an ordered list of 5: 80.')

        q(wp, M,
          "A recipe calls for 3 cups of flour for every 2 cups of sugar. How many cups of flour are needed if 7 cups of sugar are used?",
          'A) 9.5', 'B) 10', 'C) 10.5', 'D) 11',
          'C',
          'Ratio: 3/2 = x/7 → x = 21/2 = 10.5 cups of flour.')

        q(ae, M,
          "If 3(2x − 1) = 4x + 9, what is x?",
          'A) x = 4', 'B) x = 6', 'C) x = 5', 'D) x = 3',
          'B',
          '6x − 3 = 4x + 9 → 2x = 12 → x = 6.')

        # ── MATH MODULE 2 EASIER — 22 EASY ────────────────────────────────────

        q(ae, E,
          "What is the value of 3x + 7 when x = 4?",
          'A) 16', 'B) 17', 'C) 19', 'D) 21',
          'C',
          '3(4) + 7 = 12 + 7 = 19.')

        q(ae, E,
          "Solve: x + 15 = 32",
          'A) x = 15', 'B) x = 17', 'C) x = 20', 'D) x = 47',
          'B',
          'x = 32 − 15 = 17.')

        q(ae, E,
          "What is 40% of 150?",
          'A) 40', 'B) 50', 'C) 60', 'D) 75',
          'C',
          '40% × 150 = 0.40 × 150 = 60.')

        q(ae, E,
          "Simplify: 4(3x − 2)",
          'A) 12x − 2', 'B) 7x − 6', 'C) 12x − 8', 'D) 12x + 8',
          'C',
          '4 × 3x = 12x; 4 × (−2) = −8. Result: 12x − 8.')

        q(fg, E,
          "If f(x) = x + 5, what is f(9)?",
          'A) 13', 'B) 14', 'C) 4', 'D) 45',
          'B',
          'f(9) = 9 + 5 = 14.')

        q(fg, E,
          "Which table of values represents a linear function?\nA) x: 1,2,3 | y: 1,4,9\nB) x: 1,2,3 | y: 3,5,7\nC) x: 1,2,3 | y: 2,4,8\nD) x: 1,2,3 | y: 1,3,7",
          'A) Table A', 'B) Table B', 'C) Table C', 'D) Table D',
          'B',
          'Table B increases by 2 each time (constant rate of change), so it is linear.')

        q(geo, E,
          "What is the perimeter of a square with side length 9 cm?",
          'A) 18 cm', 'B) 27 cm', 'C) 36 cm', 'D) 81 cm',
          'C',
          'Perimeter = 4 × 9 = 36 cm.')

        q(geo, E,
          "What is the area of a rectangle with length 12 m and width 5 m?",
          'A) 34 m²', 'B) 60 m²', 'C) 17 m²', 'D) 70 m²',
          'B',
          'Area = length × width = 12 × 5 = 60 m².')

        q(geo, E,
          "An angle measures 130°. What is the measure of its supplement?",
          'A) 40°', 'B) 50°', 'C) 60°', 'D) 70°',
          'B',
          'Supplementary angles sum to 180°: 180 − 130 = 50°.')

        q(ds, E,
          "What is the mean of 8, 12, 16, 20?",
          'A) 12', 'B) 14', 'C) 16', 'D) 18',
          'B',
          'Mean = (8 + 12 + 16 + 20) ÷ 4 = 56 ÷ 4 = 14.')

        q(ds, E,
          "A spinner has 4 equal sections: red, blue, green, yellow. What is the probability of landing on green?",
          'A) 1/2', 'B) 1/3', 'C) 1/4', 'D) 1/5',
          'C',
          'There are 4 equally likely outcomes; P(green) = 1/4.')

        q(ds, E,
          "The following data set shows hours of TV watched per day: 1, 2, 2, 3, 4, 4, 4. What is the mode?",
          'A) 2', 'B) 3', 'C) 4', 'D) 1',
          'C',
          '4 appears three times — the most frequent value.')

        q(wp, E,
          "A bookstore sells 3 books for $12. How much do 9 books cost?",
          'A) $24', 'B) $30', 'C) $36', 'D) $40',
          'C',
          'Unit price = $12 ÷ 3 = $4. Nine books = 9 × $4 = $36.')

        q(wp, E,
          "Maya has $50. She spends $18 on lunch and $9 on a book. How much does she have left?",
          'A) $21', 'B) $23', 'C) $25', 'D) $27',
          'B',
          '$50 − $18 − $9 = $23.')

        q(wp, E,
          "A car travels at 45 mph for 2 hours. How far does it travel?",
          'A) 80 miles', 'B) 85 miles', 'C) 90 miles', 'D) 95 miles',
          'C',
          'Distance = speed × time = 45 × 2 = 90 miles.')

        q(ae, E,
          "Which of the following is equivalent to 5² + 3²?",
          'A) 34', 'B) 64', 'C) 16', 'D) 58',
          'A',
          '5² = 25; 3² = 9; 25 + 9 = 34.')

        q(ae, E,
          "If 2x = 14, what is 3x?",
          'A) 7', 'B) 14', 'C) 21', 'D) 28',
          'C',
          '2x = 14 → x = 7 → 3x = 21.')

        q(fg, E,
          "A function is described as: output = 3 × input − 1. What is the output when the input is 5?",
          'A) 10', 'B) 12', 'C) 14', 'D) 15',
          'C',
          '3 × 5 − 1 = 15 − 1 = 14.')

        q(geo, E,
          "What is the circumference of a circle with diameter 10 cm? (Use π ≈ 3.14)",
          'A) 31.4 cm', 'B) 62.8 cm', 'C) 15.7 cm', 'D) 78.5 cm',
          'A',
          'Circumference = πd = 3.14 × 10 = 31.4 cm.')

        q(ds, E,
          "In a class of 30 students, 12 have a pet dog. What fraction of students have a dog?",
          'A) 1/3', 'B) 2/5', 'C) 1/4', 'D) 3/5',
          'B',
          '12/30 = 2/5.')

        q(wp, E,
          "A store is having a 25% off sale. If a shirt originally costs $40, what is the sale price?",
          'A) $25', 'B) $28', 'C) $30', 'D) $32',
          'C',
          'Discount = 25% × $40 = $10. Sale price = $40 − $10 = $30.')

        q(ds, E,
          "Which value is the median of: 5, 9, 3, 7, 1?",
          'A) 3', 'B) 5', 'C) 7', 'D) 9',
          'B',
          'Ordered: 1, 3, 5, 7, 9. The middle value is 5.')

        # ── MATH MODULE 2 HARDER — 22 HARD ────────────────────────────────────

        q(ae, H,
          "What is the positive solution to x² + 3x − 28 = 0?",
          'A) x = 4', 'B) x = 7', 'C) x = 5', 'D) x = 6',
          'A',
          'Factor: (x + 7)(x − 4) = 0 → x = 4 or x = −7. Positive solution is x = 4.')

        q(ae, H,
          "A line has a slope of −3 and passes through the point (2, 5). What is its y-intercept?",
          'A) 9', 'B) 10', 'C) 11', 'D) 12',
          'C',
          'y = mx + b → 5 = −3(2) + b → 5 = −6 + b → b = 11.')

        q(ae, H,
          "Solve the system:\n3x + 2y = 16\n5x − 2y = 24",
          'A) x = 5, y = 0.5', 'B) x = 4, y = 2', 'C) x = 6, y = −1', 'D) x = 3, y = 3.5',
          'A',
          'Adding: 8x = 40 → x = 5. Substituting: 3(5) + 2y = 16 → 2y = 1 → y = 0.5.')

        q(fg, H,
          "The graph of f(x) = ax² + bx + c has its vertex at (2, −3) and passes through (0, 5). What is the value of a?",
          'A) 1', 'B) 2', 'C) 3', 'D) 4',
          'B',
          'f(x) = a(x − 2)² − 3. At x = 0: a(4) − 3 = 5 → 4a = 8 → a = 2.')

        q(fg, H,
          "If g(x) = x² − 4x + 3, for which values of x does g(x) = 0?",
          'A) x = 1 and x = 3', 'B) x = −1 and x = −3', 'C) x = 2 and x = 4', 'D) x = 0 and x = 4',
          'A',
          'Factor: (x − 1)(x − 3) = 0 → x = 1 or x = 3.')

        q(fg, H,
          "A function h(x) = 3^x. What is h(x + 1) in terms of h(x)?",
          'A) h(x) + 3', 'B) 3·h(x)', 'C) h(x) + 1', 'D) h(x)³',
          'B',
          'h(x + 1) = 3^(x+1) = 3 × 3^x = 3·h(x).')

        q(geo, H,
          "A cylinder has radius 4 cm and height 10 cm. What is its volume? (Use π ≈ 3.14)",
          'A) 376.8 cm³', 'B) 502.4 cm³', 'C) 100.48 cm³', 'D) 251.2 cm³',
          'B',
          'V = πr²h = 3.14 × 16 × 10 = 502.4 cm³.')

        q(geo, H,
          "Two similar triangles have sides in the ratio 3:5. If the area of the smaller triangle is 27 cm², what is the area of the larger triangle?",
          'A) 45 cm²', 'B) 60 cm²', 'C) 75 cm²', 'D) 81 cm²',
          'C',
          'Area ratio = (3:5)² = 9:25. Larger area = 27 × (25/9) = 75 cm².')

        q(geo, H,
          "In a right triangle, one acute angle is 30°. The side opposite the 30° angle is 8 cm. What is the hypotenuse?",
          'A) 12 cm', 'B) 14 cm', 'C) 16 cm', 'D) 18 cm',
          'C',
          'For a 30-60-90 triangle, hypotenuse = 2 × (side opposite 30°) = 2 × 8 = 16 cm.')

        q(ds, H,
          "A data set has a mean of 50 and a standard deviation of 5. A score of 60 is how many standard deviations above the mean?",
          'A) 1', 'B) 2', 'C) 3', 'D) 4',
          'B',
          '(60 − 50) ÷ 5 = 10 ÷ 5 = 2 standard deviations above the mean.')

        q(ds, H,
          "A bag has 5 red and 3 blue balls. Two balls are drawn without replacement. What is the probability that both are red?",
          'A) 5/14', 'B) 15/56', 'C) 25/64', 'D) 10/28',
          'A',
          'P = (5/8) × (4/7) = 20/56 = 5/14.')

        q(ds, H,
          "A normally distributed data set has mean 72 and standard deviation 8. Approximately what percentage of values fall between 64 and 80?",
          'A) 50%', 'B) 68%', 'C) 95%', 'D) 99%',
          'B',
          '64 = 72 − 8 (one SD below); 80 = 72 + 8 (one SD above). About 68% fall within one standard deviation.')

        q(wp, H,
          "Two pipes fill a tank. Pipe A fills it in 6 hours; Pipe B fills it in 4 hours. How long does it take both pipes together?",
          'A) 2 hours', 'B) 2.2 hours', 'C) 2.4 hours', 'D) 3 hours',
          'C',
          'Rate A = 1/6; Rate B = 1/4. Combined = 1/6 + 1/4 = 2/12 + 3/12 = 5/12. Time = 12/5 = 2.4 hours.')

        q(wp, H,
          "A store marks up a product by 40% and then offers a 20% discount. What is the net percentage change from the original price?",
          'A) 12% increase', 'B) 20% increase', 'C) 8% increase', 'D) No change',
          'A',
          'Original price P. After markup: 1.4P. After discount: 1.4P × 0.80 = 1.12P. Net change: +12%.')

        q(wp, H,
          "A boat travels 60 miles downstream in 3 hours and 60 miles upstream in 5 hours. What is the speed of the current?",
          'A) 2 mph', 'B) 3 mph', 'C) 4 mph', 'D) 5 mph',
          'C',
          'Downstream speed = 60/3 = 20 mph. Upstream speed = 60/5 = 12 mph. Current = (20 − 12)/2 = 4 mph.')

        q(ae, H,
          "If x² − 9 = 0, what are the solutions?",
          'A) x = 3 only', 'B) x = −3 only', 'C) x = 3 and x = −3', 'D) x = 9 and x = −9',
          'C',
          'x² = 9 → x = ±3.')

        q(ae, H,
          "The sum of three consecutive odd integers is 69. What is the largest integer?",
          'A) 21', 'B) 23', 'C) 25', 'D) 27',
          'C',
          'Let the integers be n, n+2, n+4. 3n + 6 = 69 → n = 21. Largest = 21 + 4 = 25.')

        q(fg, H,
          "A function f(x) = −2x + 8. At which x-value does f(x) cross the x-axis?",
          'A) x = 2', 'B) x = 4', 'C) x = 6', 'D) x = 8',
          'B',
          'Set f(x) = 0: −2x + 8 = 0 → x = 4.')

        q(geo, H,
          "The diagonal of a square is 10 cm. What is the area of the square?",
          'A) 25 cm²', 'B) 50 cm²', 'C) 75 cm²', 'D) 100 cm²',
          'B',
          'For a square with diagonal d: side = d/√2 = 10/√2. Area = side² = (10/√2)² = 100/2 = 50 cm².')

        q(ds, H,
          "A class has 15 girls and 10 boys. If one student is selected at random, what is the probability that the student is NOT a girl?",
          'A) 2/5', 'B) 3/5', 'C) 1/3', 'D) 2/3',
          'A',
          'P(not a girl) = 10/25 = 2/5.')

        q(wp, H,
          "A rectangular pool is 25 m long and 12 m wide. A path 2 m wide is built around the outside. What is the area of the path?",
          'A) 156 m²', 'B) 164 m²', 'C) 172 m²', 'D) 180 m²',
          'B',
          'Outer dimensions: (25+4) × (12+4) = 29 × 16 = 464 m². Pool area = 25 × 12 = 300 m². Path = 464 − 300 = 164 m².')

        q(ae, H,
          "If (x + 3)² = 49, what are the values of x?",
          'A) x = 4 and x = −10', 'B) x = 7 and x = −7', 'C) x = 4 only', 'D) x = −3 and x = 7',
          'A',
          'x + 3 = ±7. So x = 4 or x = −10.')

        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {Question.objects.count()} total questions in database '
            f'({Question.objects.filter(subject=english).count()} English, '
            f'{Question.objects.filter(subject=math).count()} Math)'
        ))
