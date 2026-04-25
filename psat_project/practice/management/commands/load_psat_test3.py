"""
PSAT 8/9-style Practice Test 3 — generated questions.
English (Reading & Writing): 81 questions across 3 modules
Math: 66 questions across 3 modules
Difficulty: Module 1 = medium, Module 2 Easier = easy, Module 2 Harder = hard
"""
from django.core.management.base import BaseCommand
from practice.models import Subject, Topic, Question


class Command(BaseCommand):
    help = 'Load PSAT-style Practice Test 3 questions into the database'

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
          "Marine biologist Sylvia Earle ________ the importance of ocean conservation, "
          "traveling to remote locations and advocating for the protection of marine "
          "ecosystems throughout her five-decade career.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "undermined", "championed", "questioned", "dismissed", "B",
          "'Championed' means to actively support or advocate for — Earle's travel and advocacy align perfectly with this word.")

        q(ev, M,
          "The recently excavated scroll, found in pristine condition despite its age, "
          "provided scholars with ________ evidence that challenged long-held assumptions "
          "about ancient Mediterranean trade routes.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "irrelevant", "inconclusive", "compelling", "confusing", "C",
          "'Compelling' means persuasive and significant — it matches evidence strong enough to challenge established assumptions.")

        q(ev, M,
          "The jazz musician was known for his ________ improvisations — extended solos "
          "that wandered through unexpected key changes and rhythmic patterns before "
          "resolving with a sense of inevitability.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "predictable", "brief", "elaborate", "silent", "C",
          "'Elaborate' describes something intricate and complex — matching the extended, varied solos described.")

        q(ev, M,
          "The city council's plan to close the historic district to vehicle traffic was "
          "initially ________, with many business owners expressing concern about reduced "
          "customer access, but acceptance grew as foot traffic increased.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "celebrated", "overlooked", "contested", "anticipated", "C",
          "'Contested' means disputed or opposed — matching the business owners' initial objections.")

        q(rc, M,
          "Paleontologists have traditionally relied on fossilized bones and teeth to "
          "reconstruct the diets of prehistoric creatures. A newer technique, isotope "
          "analysis of fossilized enamel, can reveal not just what animals ate but also "
          "the geographic range they traveled during their lifetimes. This approach has "
          "overturned several longstanding assumptions about early hominin behavior.\n\n"
          "Which choice best states the main idea of the text?",
          "Paleontologists no longer use fossilized bones to study prehistoric diets.",
          "Isotope analysis of fossilized enamel is unreliable for reconstructing ancient diets.",
          "A newer analytical technique is expanding what paleontologists can learn from prehistoric remains.",
          "Fossilized bones provide more accurate data about ancient animals than enamel.", "C",
          "The text presents a new technique (isotope analysis) that extends what can be learned from fossils — that is the main idea.")

        q(rc, M,
          "The following text is adapted from Edith Wharton's 1905 novel The House of "
          "Mirth. Lily Bart attends a party.\n\n"
          "She was aware that the evening was not going well for her. She had entered the "
          "drawing room prepared to be admired; she had not expected indifference. Worse "
          "than indifference — she sensed a kind of polite disengagement, as if the other "
          "guests had already made their assessments and moved on.\n\n"
          "Which choice best describes the function of the final sentence in the text?",
          "It reveals that the guests are deliberately ignoring Lily out of jealousy.",
          "It clarifies and intensifies the previous statement about indifference.",
          "It contrasts Lily's experience with that of the other guests.",
          "It suggests that Lily is known for her poor social skills.", "B",
          "The final sentence sharpens the idea of 'indifference' into something more specific and more painful — polite disengagement. It intensifies the previous claim.")

        q(rc, M,
          "Social media platforms have transformed how political campaigns reach voters. "
          "Rather than relying solely on television and print, campaigns now use targeted "
          "digital messaging to reach specific demographic groups. Critics argue that "
          "micro-targeting enables the spread of misleading information, while proponents "
          "contend that it democratizes access to political communication.\n\n"
          "Which choice best states the main idea of the text?",
          "Social media has completely replaced television as the primary campaign tool.",
          "Social media micro-targeting is illegal in most democratic countries.",
          "Digital targeting has changed political campaigning, with supporters and critics disagreeing about its effects.",
          "Only large campaigns have benefited from digital micro-targeting.", "C",
          "The text describes how social media changed campaigning and notes the debate between critics and supporters — that tension is the main idea.")

        q(rc, M,
          "The deep ocean remains one of Earth's least explored environments. Pressure "
          "increases, temperatures drop, and sunlight disappears at depth. Yet thousands "
          "of species have adapted, including the anglerfish, whose bioluminescent lure "
          "attracts prey in darkness, and the giant squid, which can grow to over 40 feet. "
          "The abundance of life in these extreme conditions suggests that ________\n\n"
          "Which choice most logically completes the text?",
          "the deep ocean is actually uninhabitable for most marine creatures.",
          "anglerfish are the most intelligent creatures in the ocean.",
          "life can adapt to thrive in environments far beyond what scientists once thought possible.",
          "the giant squid is the largest creature to have ever lived on Earth.", "C",
          "The thriving life in extreme deep-ocean conditions supports the inference that life's adaptability exceeds previous scientific expectations.")

        q(rc, M,
          "Conductor Leonard Bernstein believed classical music should be accessible to "
          "general audiences. Through his Young People's Concerts at Carnegie Hall and "
          "televised broadcasts, he explained musical concepts with enthusiasm and clarity. "
          "His approach is often credited with introducing an entire generation of "
          "Americans to classical music.\n\n"
          "Which choice best states the main idea of the text?",
          "Bernstein believed classical music was too complex for general audiences.",
          "Bernstein's efforts to make classical music accessible are credited with broadening its audience.",
          "Bernstein composed primarily for televised broadcasts rather than live performances.",
          "Carnegie Hall became the primary venue for Young People's Concerts after Bernstein's broadcasts.", "B",
          "The text focuses on Bernstein's mission of accessibility and its result — a broader audience for classical music.")

        q(de, M,
          "The table below shows monthly wildlife sightings in a nature reserve:\n\n"
          "Month: Mar, Apr, May, Jun\n"
          "Deer: 28, 34, 41, 38 | Fox: 14, 17, 19, 16\n\n"
          "A ranger claims that deer sightings exceeded fox sightings by at least 20 in "
          "every month from March through June. Which choice most effectively uses data "
          "from the table to evaluate this claim?",
          "In May, deer (41) exceeded fox (19) by 22. The claim holds for May.",
          "Deer always outnumber foxes, so the claim is correct.",
          "In March, deer (28) exceeded fox (14) by only 14, not at least 20. The claim is incorrect.",
          "In June, deer (38) exceeded fox (16) by 22, supporting the claim.", "C",
          "March: 28−14 = 14 < 20, which disproves the 'at least 20 in every month' claim. Option C correctly identifies this counterexample.")

        q(de, M,
          "Text 1: Standardized testing provides a reliable, objective measure of student "
          "learning. These tests help identify achievement gaps and allocate resources "
          "effectively across schools and districts.\n\n"
          "Text 2: Standardized tests measure only a narrow range of skills and "
          "disadvantage students from lower-income backgrounds who have less access to "
          "test preparation. They also create incentives for 'teaching to the test,' "
          "crowding out richer learning experiences.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond to the "
          "claim in Text 1 that standardized tests reliably measure student learning?",
          "Standardized tests do reliably measure learning, but only for students in well-funded schools.",
          "The tests' narrow focus and socioeconomic bias undermine their reliability as a fair measure of learning.",
          "Policymakers should eliminate all forms of student assessment.",
          "Standardized tests are not useful for any educational purpose.", "B",
          "Text 2 argues that the tests measure narrow skills and disadvantage lower-income students — both points challenge the claim of reliable, objective measurement.")

        q(de, M,
          "Scientists studying ancient Egyptian mummies have used CT scans and DNA analysis "
          "to determine causes of death for individuals who lived more than 3,000 years ago. "
          "One study found evidence of ________ in arterial walls of several mummies, "
          "suggesting that cardiovascular disease is not solely a modern phenomenon.\n\n"
          "Which choice most effectively completes the claim using evidence consistent "
          "with the rest of the text?",
          "ancient surgical procedures", "signs of arthritis",
          "calcification", "infections", "C",
          "Calcification (hardening) of arterial walls is a marker of atherosclerosis — cardiovascular disease — which is exactly what the sentence is claiming to find.")

        q(de, M,
          "A study surveyed 500 participants about their primary mode of transportation:\n\n"
          "Car: 285 | Public Transit: 115 | Bicycle: 60 | Walking: 40\n\n"
          "A researcher states that car travel accounts for more than half of all reported "
          "modes. Which choice most effectively uses data from the table to support "
          "this claim?",
          "Bicycle use (60) and walking (40) together represent 20% of respondents.",
          "Car travel was chosen by 285 of 500 respondents, which is 57% — more than half.",
          "Public transit (115) is the second most common mode after car.",
          "Walking is the least common mode of transportation among respondents.", "B",
          "285/500 = 57%, which is more than half. Option B directly calculates the percentage to support the claim.")

        q(de, M,
          "Text 1: Historical records show that Easter Island's population collapsed "
          "before European contact, attributed to unsustainable exploitation of forest "
          "resources. This 'ecocide' is widely taught as an example of environmental "
          "self-destruction.\n\n"
          "Text 2: Archaeological evidence increasingly suggests the population collapse "
          "was primarily caused by European-introduced diseases and slave raids, not "
          "prior ecological devastation. Pollen data shows deforestation happened "
          "gradually over centuries, not in the sudden manner that a catastrophic "
          "collapse would require.\n\n"
          "Based on the texts, the authors disagree about which of the following?",
          "Whether Europeans ever made contact with Easter Island's inhabitants.",
          "Whether Easter Island's population declined significantly at some point.",
          "The primary cause of Easter Island's population decline.",
          "Whether deforestation occurred at all on Easter Island.", "C",
          "Text 1 attributes the collapse to ecological self-destruction; Text 2 attributes it to European diseases and slave raids — they disagree on the primary cause.")

        q(gv, M,
          "The university's new policies, which aim to improve student wellness and "
          "increase retention rates, ________ expected to take effect at the beginning "
          "of the next academic year.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "is", "was", "have", "A",
          "The plural subject 'policies' requires the plural verb 'are.'")

        q(gv, M,
          "The renowned chef, who trained under several Michelin-starred masters in Paris, "
          "________ her first solo restaurant in 2019 to widespread critical acclaim.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "opens", "opening", "open", "opened", "D",
          "'Opened' is the correct simple past tense — the action occurred 'in 2019.'")

        q(gv, M,
          "________ the first complete map of the human genome, scientists gained "
          "unprecedented insight into the genetic basis of thousands of diseases.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Having completed", "They completed", "Completing", "To complete", "A",
          "'Having completed' is the correct perfect participial phrase, indicating the prior action that enabled the subsequent scientific gains.")

        q(gv, M,
          "Neither the director nor the principal actor ________ aware of the technical "
          "problems with the sound equipment until the premiere screening.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "was", "were", "is", "have been", "A",
          "With 'neither...nor,' the verb agrees with the subject closest to it. 'Principal actor' is singular → 'was.'")

        q(gp, M,
          "The researcher identified three key factors contributing to chronic workplace "
          "stress ________ excessive workload, lack of task autonomy, and poor "
          "communication with supervisors.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—and", "A",
          "A colon correctly introduces the list of three factors that follows.")

        q(gp, M,
          "The ancient library at Alexandria was among the greatest repositories of "
          "knowledge in antiquity ________ scholars from across the Mediterranean traveled "
          "there to access its vast collection of scrolls.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", "and", "because", "A",
          "A semicolon correctly joins two independent clauses without a coordinating conjunction.")

        q(gp, M,
          "The newly discovered species ________ named Cryodrakon boreas — was the largest "
          "flying animal ever found in Canada, with a wingspan estimated at over 30 feet.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical 'named Cryodrakon boreas' is set off by dashes. Since the closing dash is present, the opening punctuation must also be a dash.")

        q(gp, M,
          "The ancient manuscript was discovered in a cave near the Dead Sea in 1947 "
          "________ becoming one of the most significant archaeological finds of the "
          "twentieth century.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", ":", "—", "B",
          "A comma introduces the participial phrase 'becoming one of the most significant...' that modifies the discovery.")

        q(tr, M,
          "Photosynthesis requires sunlight, carbon dioxide, and water to produce glucose "
          "and oxygen. ________ the process can be disrupted by prolonged cloud cover or "
          "air pollution, which reduces the sunlight available to plants.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Similarly,", "However,", "Furthermore,", "Therefore,", "B",
          "'However' introduces a contrasting limitation — despite the requirements described, the process can be disrupted.")

        q(tr, M,
          "Researchers at the university spent three years developing a new water "
          "purification system. ________ the system can now remove 99% of common "
          "contaminants from drinking water at a fraction of the traditional cost.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "In contrast,", "As a result,", "Otherwise,", "C",
          "'As a result' connects the years of research to the successful outcome — cause and effect.")

        q(tr, M,
          "Many species of migratory birds navigate using Earth's magnetic field, which "
          "they sense through specialized proteins in their eyes. ________ some birds also "
          "use the positions of stars and the angle of the sun to navigate.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "In addition,", "Instead,", "Therefore,", "B",
          "'In addition' correctly signals that the text is adding another navigation method used by migratory birds.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Amazon River is the world's largest river by discharge volume, releasing "
          "approximately 20% of all freshwater entering the world's oceans.\n"
          "- It flows approximately 3,976 miles from its source in Peru to its mouth in Brazil.\n"
          "- The Amazon basin is home to approximately 10% of all species on Earth.\n"
          "- The river supports over 30 million people, including hundreds of indigenous communities.\n"
          "- Scientists estimate the Amazon rainforest produces about 6% of Earth's oxygen.\n\n"
          "The student wants to emphasize the Amazon's significance for biodiversity. "
          "Which choice most effectively uses relevant information from the notes?",
          "The Amazon flows 3,976 miles and releases 20% of all freshwater entering the oceans.",
          "The Amazon basin is home to approximately 10% of all species on Earth, making it one of the planet's most biodiverse regions.",
          "The Amazon River supports over 30 million people, including hundreds of indigenous communities.",
          "The Amazon rainforest produces about 6% of Earth's oxygen.", "B",
          "Option B directly addresses biodiversity — 10% of all Earth's species — which is the student's stated goal.")

        q(rn, M,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Wright Brothers' first powered flight was on December 17, 1903, at Kitty Hawk, NC.\n"
          "- The first flight lasted 12 seconds and covered 120 feet.\n"
          "- Later that same day, a flight lasted 59 seconds and covered 852 feet.\n"
          "- Today, commercial aircraft travel at over 500 mph and carry hundreds of passengers.\n\n"
          "The student wants to show the dramatic progress in aviation. Which choice most "
          "effectively uses relevant information from the notes to accomplish this goal?",
          "The Wright Brothers' flight at Kitty Hawk lasted 12 seconds and covered 120 feet.",
          "On the same day, the Wright Brothers achieved a flight of 59 seconds covering 852 feet.",
          "The Wright Brothers' first flight occurred on December 17, 1903, at Kitty Hawk.",
          "Compared to the Wright Brothers' first 12-second, 120-foot flight, modern commercial aircraft fly at over 500 mph and carry hundreds of passengers.", "D",
          "Option D creates a direct comparison across time — the tiny first flight versus today's massive commercial aircraft — which best demonstrates dramatic progress.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(ev, E,
          "The library's new reading program has been very popular. Students ________ books "
          "from many different genres, discovering new interests along the way.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "avoid", "return", "explore", "forget", "C",
          "'Explore' logically fits — students are discovering new interests through reading across genres.")

        q(ev, E,
          "The volunteer firefighters responded quickly to the emergency. Their "
          "________ efforts saved the historic building from complete destruction.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "careless", "heroic", "slow", "unnecessary", "B",
          "'Heroic' describes brave, courageous effort — fitting for firefighters who saved a building.")

        q(ev, E,
          "Scientists made an exciting discovery when they found fossils of a previously "
          "unknown dinosaur species in Montana. The dinosaur is believed to be a "
          "________ predator that lived about 75 million years ago.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "harmless", "tiny", "fierce", "extinct", "C",
          "'Fierce' means aggressive and powerful — fitting for a predatory dinosaur. ('Extinct' would apply to all ancient dinosaurs and is too vague.)")

        q(ev, E,
          "The school's new recycling program has been a great success. Students are "
          "________ the program by separating their waste into the correct bins each day.\n\n"
          "Which choice completes the text with the most logical word or phrase?",
          "ignoring", "destroying", "supporting", "questioning", "C",
          "'Supporting' means helping or backing up — fitting for students who participate actively in the recycling program.")

        q(rc, E,
          "Penguins are found almost exclusively in the Southern Hemisphere, with most "
          "species living in Antarctica and surrounding islands. Though often associated "
          "with ice and snow, some penguin species actually live in temperate or even "
          "subtropical climates, including the Galapagos penguin, which lives near the equator.\n\n"
          "Which choice best states the main idea of the text?",
          "Penguins can only survive in extremely cold climates near Antarctica.",
          "Penguins are found in the Southern Hemisphere, but some species live in surprisingly warm climates.",
          "The Galapagos penguin is the most common penguin species in the world.",
          "Scientists do not fully understand why penguins live in the Southern Hemisphere.", "B",
          "The text explains where penguins live and notes the surprising fact that some live in warm climates — the main idea.")

        q(rc, E,
          "The printing press, invented by Johannes Gutenberg around 1440, transformed "
          "European society by making books affordable and widely available. Before the "
          "printing press, books were copied by hand, a slow and expensive process that "
          "limited access to knowledge. Within 50 years of Gutenberg's invention, millions "
          "of books had been printed across Europe.\n\n"
          "Which choice best states the main idea of the text?",
          "Johannes Gutenberg invented the printing press to make money from book sales.",
          "Books became worthless after the printing press was invented because so many were produced.",
          "The printing press transformed access to knowledge by making books affordable and widely available.",
          "Before Gutenberg, only monks were allowed to copy books by hand.", "C",
          "The main idea is how the printing press changed book availability and access to knowledge.")

        q(rc, E,
          "Rainforests cover only about 6% of Earth's surface but are home to more than "
          "half of the world's plant and animal species. They also play a critical role "
          "in regulating the climate by absorbing carbon dioxide and producing oxygen. "
          "Despite their importance, rainforests continue to be cleared for agriculture "
          "and development.\n\n"
          "Which choice best describes the function of the last sentence in the text?",
          "It explains why rainforests are home to so many species.",
          "It introduces a concern that contrasts with the rainforest's established importance.",
          "It suggests that agriculture is more important than rainforest conservation.",
          "It provides details about how carbon dioxide affects rainforests.", "B",
          "After explaining the rainforest's importance, the final sentence introduces the contrasting problem of continued deforestation.")

        q(rc, E,
          "In ancient Rome, the Forum was the center of public life. Citizens gathered "
          "there to conduct business, watch speeches, and participate in civic ceremonies. "
          "The Forum contained temples, government buildings, and market stalls, making "
          "it a hub for religion, politics, and commerce.\n\n"
          "Which choice best states the main idea of the text?",
          "The Roman Forum was mainly used for religious ceremonies.",
          "The Forum was the center of Roman public life, combining commercial, political, and religious functions.",
          "Only wealthy Roman citizens were allowed to enter the Forum.",
          "The Roman Forum was primarily a marketplace where merchants sold goods.", "B",
          "The text describes the Forum as central to all aspects of Roman public life — religion, politics, and commerce.")

        q(rc, E,
          "Scientists at NASA have been studying the possibility of growing food on Mars. "
          "Plants need sunlight, water, and nutrients to grow, all of which present "
          "challenges on Mars. However, researchers have found that certain crops, "
          "such as potatoes and radishes, could potentially grow in Martian soil with "
          "modifications. This finding ________\n\n"
          "Which choice most logically completes the text?",
          "proves that humans could never survive on Mars.",
          "suggests that long-term human habitation on Mars may be more feasible than previously thought.",
          "shows that potatoes are the only viable food source in space.",
          "indicates that Martian soil is identical to soil found on Earth.", "B",
          "If some crops could grow on Mars, this makes long-term human habitation more plausible — the logical completion of the text.")

        q(de, E,
          "The table below shows the number of students participating in after-school clubs:\n\n"
          "Drama: 24 | Science: 18 | Art: 30 | Chess: 12 | Sports: 36\n\n"
          "A teacher claims that Art and Drama together attract more students than Sports. "
          "Which choice most effectively uses data from the table to evaluate this claim?",
          "Art (30) is the second-most popular club after Sports (36).",
          "Art (30) + Drama (24) = 54, which is greater than Sports (36). The claim is correct.",
          "Chess (12) is the least popular club.",
          "Science (18) has more participants than Chess (12).", "B",
          "30 + 24 = 54 > 36. Option B directly evaluates the claim using the data.")

        q(de, E,
          "Text 1: Zoos play an important role in conservation by protecting endangered "
          "species, funding research, and educating the public about wildlife.\n\n"
          "Text 2: Critics argue that keeping animals in captivity causes psychological "
          "harm and that zoos prioritize entertainment over animal welfare. Many species "
          "breed poorly in captivity and cannot be successfully released into the wild.\n\n"
          "Based on the texts, both authors would likely agree that ________",
          "zoos should be closed immediately.",
          "all animals in zoos can be successfully reintroduced to the wild.",
          "zoos affect wildlife in some way, but whether that effect is positive is debated.",
          "zoos are the most effective conservation strategy available.", "C",
          "Text 1 sees zoos as beneficial; Text 2 sees them as harmful. Both agree zoos affect wildlife — they disagree on whether the effect is positive.")

        q(de, E,
          "The table shows average test scores by study method:\n\n"
          "Studying alone: 72 | Study groups: 81 | Tutoring: 88 | Online videos: 77\n\n"
          "A student claims that using a tutor leads to the highest test scores. Which "
          "choice most effectively uses data from the table to support this claim?",
          "Students who study alone score 72, which is the lowest of all methods.",
          "Tutoring (88) results in the highest average test score of the four methods listed.",
          "Study groups (81) score higher than studying alone (72) or watching online videos (77).",
          "Online video scores (77) fall between studying alone and study groups.", "B",
          "Tutoring at 88 is higher than all other methods (72, 81, 77). Option B directly supports the claim.")

        q(de, E,
          "Text 1: Breakfast is the most important meal of the day. Eating a nutritious "
          "morning meal improves concentration, stabilizes energy levels, and supports "
          "healthy metabolism.\n\n"
          "Text 2: While breakfast can be beneficial for some people, recent research "
          "suggests it is not universally important. Some individuals perform equally well "
          "when skipping breakfast, particularly those who practice intermittent fasting.\n\n"
          "Based on the texts, the authors would most likely agree that ________",
          "skipping breakfast always leads to poor concentration and low energy.",
          "breakfast is harmful to people who practice intermittent fasting.",
          "whether breakfast is beneficial may depend on individual differences.",
          "breakfast should be the largest meal of the day.", "C",
          "Text 1 says breakfast is essential; Text 2 says it depends on the person. Both implicitly acknowledge individual variation.")

        q(de, E,
          "The table shows the number of books borrowed from a school library per month:\n\n"
          "September: 145 | October: 162 | November: 178 | December: 89 | January: 201\n\n"
          "A librarian notes that book borrowing was higher in every month except December. "
          "Which choice best uses data from the table to support this observation?",
          "September had 145 borrowings, which is the lowest month except for December.",
          "October and November both saw increases over September.",
          "All months except December (89) had more than 140 borrowings, while December had the fewest.",
          "January (201) had the highest number of borrowings of any month.", "C",
          "Option C uses the data to show all months exceeded 140 except December (89), directly supporting the librarian's observation.")

        q(gv, E,
          "The birds in the sanctuary ________ every morning just after sunrise, filling "
          "the air with a rich variety of songs.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "sings", "sing", "has sung", "singing", "B",
          "'Birds' is plural and requires the plural verb 'sing.'")

        q(gv, E,
          "Last summer, the community garden ________ more than 500 pounds of vegetables, "
          "which were donated to local food banks.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "produces", "produce", "produced", "producing", "C",
          "'Produced' is the correct simple past tense — the action occurred 'last summer.'")

        q(gv, E,
          "The principal ________ the students for their outstanding performance at the "
          "regional science fair, where they won three first-place awards.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "congratulate", "congratulates", "congratulated", "congratulating", "C",
          "'Congratulated' is the correct simple past tense, consistent with the completed event at the science fair.")

        q(gv, E,
          "Every one of the volunteers ________ asked to wear a reflective vest during "
          "the outdoor event for safety reasons.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "are", "were", "is", "was", "D",
          "'Every one' is singular and takes a singular verb: 'was.'")

        q(gp, E,
          "The science fair had three categories of projects ________ biology, chemistry, "
          "and physics.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ";", ",", "—and", "A",
          "A colon introduces the list of three categories that follows.")

        q(gp, E,
          "The students worked hard on the project all week ________ they presented "
          "their results to the class on Friday.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", "and,", "because", "A",
          "A semicolon correctly joins two independent clauses without a coordinating conjunction.")

        q(gp, E,
          "The school's new principal, ________ has twenty years of experience in "
          "education, started her first day with a schoolwide assembly.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "whom", "which", "who", "that", "C",
          "'Who' is the correct relative pronoun for a person and is used as the subject of 'has.'")

        q(gp, E,
          "We explored the tide pools at the beach ________ we discovered dozens of sea "
          "stars, hermit crabs, and colorful anemones.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ", where", "; where", ": where", "where,", "A",
          "A comma before the relative adverb 'where' correctly introduces a relative clause describing the beach.")

        q(tr, E,
          "The team practiced every afternoon for six weeks. ________ they won the "
          "regional championship by a wide margin.\n\n"
          "Which choice completes the text with the most logical transition?",
          "However,", "Despite this,", "Ultimately,", "Instead,", "C",
          "'Ultimately' signals the final result of the extended preparation — winning the championship.")

        q(tr, E,
          "The new park has beautiful walking trails and a large playground. ________ "
          "it also features a community garden where residents can grow their own vegetables.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "In addition,", "Therefore,", "On the other hand,", "B",
          "'In addition' correctly adds another feature of the park to those already mentioned.")

        q(tr, E,
          "The hurricane caused significant damage to coastal neighborhoods. ________ "
          "emergency services responded quickly, providing shelter and supplies to "
          "thousands of displaced residents.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "Similarly,", "Nevertheless,", "Therefore,", "C",
          "'Nevertheless' introduces the positive response despite the damage — a contrast with the difficulty of the situation.")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- Monarch butterflies migrate up to 3,000 miles between Canada/the US and Mexico.\n"
          "- They navigate using a combination of the sun's position and Earth's magnetic field.\n"
          "- A single monarch lives only a few months, yet the journey is completed over generations.\n"
          "- Monarch populations have declined by more than 80% since the 1980s.\n"
          "- Milkweed, the only plant monarchs breed on, has been greatly reduced by herbicide use.\n\n"
          "The student wants to explain why monarch populations have declined. Which choice "
          "most effectively uses relevant information from the notes to accomplish this goal?",
          "Monarch butterflies migrate up to 3,000 miles between Canada and Mexico.",
          "A single monarch lives only a few months, yet the migration is completed across generations.",
          "Monarch populations have declined by over 80% since the 1980s, largely because milkweed — the only plant monarchs breed on — has been greatly reduced by herbicide use.",
          "Monarchs navigate using the sun and Earth's magnetic field.", "C",
          "Option C directly explains the decline by connecting the population loss (80%) to the specific cause (milkweed reduction from herbicide use).")

        q(rn, E,
          "While researching a topic, a student has taken the following notes:\n"
          "- The Sahara Desert is the largest hot desert in the world, covering about 9.2 million km².\n"
          "- Temperatures can exceed 136°F (58°C) during the day.\n"
          "- At night, temperatures can drop below freezing.\n"
          "- Despite the harsh conditions, about 2 million people live there.\n"
          "- The Sahara has large deposits of oil and natural gas.\n\n"
          "The student wants to highlight the extreme temperature variation in the Sahara. "
          "Which choice most effectively uses relevant information from the notes?",
          "The Sahara is the world's largest hot desert, covering 9.2 million km².",
          "Despite its harsh conditions, approximately 2 million people live in the Sahara.",
          "In the Sahara, daytime temperatures can exceed 136°F while nighttime temperatures can fall below freezing.",
          "The Sahara has large deposits of oil and natural gas beneath its surface.", "C",
          "Option C directly contrasts the extreme daytime heat (136°F) with the below-freezing nighttime cold — the most effective way to highlight temperature variation.")

        # ════════════════════════════════════════════════════════════════
        # ENGLISH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(ev, H,
          "Though the critic's review of the debut novel was ultimately positive, she "
          "described the author's prose style as ________ — dense with subordinate "
          "clauses and parenthetical asides that, while intellectually rewarding, "
          "demanded considerable effort from the reader.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "breezy", "labyrinthine", "sparse", "accessible", "B",
          "'Labyrinthine' means complex and difficult to follow, like a maze — precisely describing prose dense with nested clauses.")

        q(ev, H,
          "The governor's initial response to the scandal was widely criticized as "
          "________ — she acknowledged the problem only in the vaguest terms and "
          "declined to commit to any specific course of corrective action.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "forthright", "evasive", "decisive", "transparent", "B",
          "'Evasive' means deliberately vague and avoiding direct answers — matching the governor's vague acknowledgment and refusal to commit.")

        q(ev, H,
          "Unlike historians who interpret documents cautiously, acknowledging the limits "
          "of available evidence, the author of this popular history adopts a far more "
          "________ approach, presenting speculative reconstructions of events as "
          "established fact.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "circumspect", "assertive", "tentative", "scholarly", "B",
          "'Assertive' means confidently stating things as true — contrasting with the cautious historians and matching the bold, speculative approach described.")

        q(ev, H,
          "The ecosystem of a coral reef is remarkably ________, with each species "
          "playing a distinct role: parrotfish graze on algae, sea urchins control "
          "coral growth, and cleaner shrimp remove parasites from fish.\n\n"
          "Which choice completes the text with the most logical and precise word or phrase?",
          "monotonous", "interdependent", "fragile", "isolated", "B",
          "'Interdependent' means relying on each other — exactly describing an ecosystem where each species serves a distinct function for others.")

        q(rc, H,
          "The following text is adapted from Joseph Conrad's 1899 novella Heart of "
          "Darkness. Marlow, a sailor, reflects on his journey up the Congo River.\n\n"
          "Going up that river was like traveling back to the earliest beginnings of the "
          "world, when vegetation rioted on the earth and the big trees were kings. An "
          "empty stream, a great silence, an impenetrable forest. The air was warm, thick, "
          "heavy, sluggish. There was no joy in the brilliance of sunshine.\n\n"
          "Which choice best describes the mood conveyed by the passage?",
          "Excitement and wonder at the natural beauty of the river.",
          "A sense of oppressive, primordial heaviness and isolation.",
          "Nostalgia for a simpler, more peaceful way of life.",
          "Curiosity about the unknown plants and animals of the Congo.", "B",
          "Conrad uses words like 'impenetrable,' 'thick,' 'heavy,' and 'no joy' to create a sense of oppression and isolation, not wonder or curiosity.")

        q(rc, H,
          "Neuroscientists have debated whether human creativity is localized in a "
          "specific brain region or distributed across multiple networks. Recent imaging "
          "studies suggest the latter: creative thinking involves dynamic interaction "
          "among three large-scale networks — the default mode network, the executive "
          "control network, and the salience network. The default mode generates ideas; "
          "the executive network evaluates them; the salience network determines which "
          "ideas are worth pursuing.\n\n"
          "Which choice best states the main idea of the text?",
          "Creativity is located in a single, identifiable brain region.",
          "The executive control network is the most important of the three networks for creativity.",
          "Recent research suggests that creativity results from the coordinated interaction of three distinct brain networks.",
          "Neuroscientists have definitively proven that creativity cannot be studied using brain imaging.", "C",
          "The text presents the finding that creativity involves three interacting networks — that is the main idea.")

        q(rc, H,
          "Sociologist Erving Goffman argued that everyday social interactions are "
          "fundamentally theatrical performances in which individuals actively manage "
          "the impressions they create. In his 'dramaturgical' model, people present "
          "a carefully curated 'front stage' self to audiences while hiding a more "
          "authentic 'backstage' self. Critics have argued that Goffman's model "
          "overstates the deliberate, calculated nature of social performance and "
          "neglects unconscious, habitual dimensions of behavior.\n\n"
          "Based on the passage, Goffman's critics would most likely argue that his "
          "model is incomplete because it ________",
          "focuses too much on unconscious behavior rather than deliberate choices.",
          "ignores the theatrical performances that occur in formal settings.",
          "treats social behavior as more intentional than it actually is.",
          "does not adequately distinguish between front-stage and backstage selves.", "C",
          "Critics argue Goffman overstates the deliberate, calculated nature of performance — in other words, he makes social behavior seem more intentional than it is.")

        q(rc, H,
          "The following text is adapted from George Eliot's 1871 novel Middlemarch. "
          "Dorothea, a young idealistic woman, reflects on her choices.\n\n"
          "She was ashamed of being so uncertain about her own goodness; she was "
          "inclined to think she had been mistaken in supposing that she could be "
          "good to everyone. What she had supposed was a lamp to guide others had "
          "turned out to be a will-o'-the-wisp, leading herself into bogs and marshes.\n\n"
          "Which choice best describes what the metaphor in the final sentence conveys?",
          "Dorothea believes she has become lost in an actual swamp.",
          "Dorothea feels that her idealism, which she thought would guide others, has instead misled her.",
          "Dorothea is uncertain whether she has helped anyone avoid physical danger.",
          "Dorothea has decided to abandon her effort to be good to others.", "B",
          "The lamp-turned-will-o'-the-wisp metaphor: what she thought was guiding others has actually misled her into 'bogs and marshes' — confusion and failure.")

        q(rc, H,
          "Evolutionary biologist Richard Dawkins proposed that evolution acts not on "
          "organisms but on genes. In his 'selfish gene' theory, genes are the fundamental "
          "units of selection, and organisms are merely 'vehicles' through which genes "
          "propagate themselves. Critics of this view argue that it misrepresents the "
          "level at which selection primarily operates and that whole organisms — not "
          "individual genes — are the appropriate unit of analysis.\n\n"
          "Which choice best states the main idea of the text?",
          "Dawkins proved that organisms, not genes, are the primary unit of natural selection.",
          "Critics agree with Dawkins that genes are the primary unit of natural selection.",
          "Dawkins proposed that evolution acts on genes rather than organisms, a view that has faced scholarly criticism.",
          "Dawkins's theory has been universally accepted in the field of evolutionary biology.", "C",
          "The text presents Dawkins's selfish gene theory and the critics who challenge the level of selection he proposes — the main idea is the theory and its controversy.")

        q(de, H,
          "Text 1: The evidence strongly suggests that reducing class sizes improves "
          "student achievement. Studies show that students in smaller classes — "
          "particularly in early grades — show consistent gains in reading and mathematics "
          "that persist into later school years.\n\n"
          "Text 2: Class size reduction is an expensive intervention with inconsistent "
          "results across studies. Some research shows gains; other studies find minimal "
          "effects. The money spent on reducing class sizes might achieve greater "
          "impact if directed toward teacher training and quality improvement.\n\n"
          "Based on the texts, how would the author of Text 2 most likely respond to "
          "Text 1's claim that class size reduction 'strongly' improves achievement?",
          "Class size reduction is effective only for mathematics, not reading.",
          "The evidence is mixed, and the resources required may be better invested elsewhere.",
          "Teacher training programs are entirely ineffective compared to class size reduction.",
          "Text 1 is correct that class size reduction is the best use of educational funding.", "B",
          "Text 2 says results are inconsistent and questions whether the money could be better spent — directly challenging Text 1's strong claim.")

        q(de, H,
          "The table below shows life expectancy data across four countries:\n\n"
          "Country A: 1950 = 52 years, 2020 = 78 years\n"
          "Country B: 1950 = 46 years, 2020 = 74 years\n"
          "Country C: 1950 = 61 years, 2020 = 83 years\n"
          "Country D: 1950 = 44 years, 2020 = 71 years\n\n"
          "A researcher claims that Country D showed the greatest absolute increase in "
          "life expectancy from 1950 to 2020. Which choice most effectively uses data "
          "from the table to evaluate this claim?",
          "Country D's life expectancy rose from 44 to 71, an increase of 27 years.",
          "Country D grew by 27 years, Country A by 26, Country B by 28, and Country C by 22. Country B showed the greatest increase, not Country D. The claim is incorrect.",
          "Country C had the highest life expectancy in 2020 at 83 years.",
          "All four countries showed increases in life expectancy from 1950 to 2020.", "B",
          "D: 71−44=27; A: 78−52=26; B: 74−46=28; C: 83−61=22. Country B increased the most (28 years), so the claim about Country D is incorrect.")

        q(de, H,
          "A study tracked 1,000 adults over ten years to examine the relationship "
          "between social connection and health outcomes. Participants who reported "
          "having three or more close friendships had significantly lower rates of "
          "cardiovascular disease and depression. The lead researcher concluded that "
          "social connection ________ health outcomes.\n\n"
          "Which choice most effectively and accurately completes the claim based "
          "on what the study can actually show?",
          "causes improvements in",
          "has no relationship to",
          "is associated with better",
          "is the only factor that determines", "C",
          "An observational study can show correlation/association, not causation. 'Is associated with better' accurately reflects what the study found without overclaiming causality.")

        q(de, H,
          "Text 1: Electric vehicles (EVs) are a crucial solution to climate change. "
          "They produce zero tailpipe emissions and, as electricity grids become greener, "
          "their total lifecycle emissions will continue to fall.\n\n"
          "Text 2: The environmental benefits of EVs are often overstated. Manufacturing "
          "EV batteries requires significant energy and raw materials like lithium and "
          "cobalt, the extraction of which causes environmental harm. In regions where "
          "electricity is generated primarily from coal, EVs may not significantly "
          "reduce total emissions.\n\n"
          "Based on the texts, both authors would likely agree that ________",
          "electric vehicles produce no emissions at any stage of their lifecycle.",
          "the environmental impact of electric vehicles depends in part on how their electricity is generated.",
          "lithium and cobalt mining has no effect on the environment.",
          "electric vehicles offer no advantages over traditional gasoline-powered cars.", "B",
          "Text 1 acknowledges that total lifecycle emissions depend on how the grid is powered; Text 2 explicitly states this matters. Both acknowledge the grid's role.")

        q(de, H,
          "The table shows the percentage of adults in four cities who commute by public transit:\n\n"
          "City W: 2015 = 28%, 2022 = 35%\n"
          "City X: 2015 = 41%, 2022 = 38%\n"
          "City Y: 2015 = 19%, 2022 = 27%\n"
          "City Z: 2015 = 53%, 2022 = 58%\n\n"
          "A transit planner argues that City Y showed the largest percentage-point "
          "increase in transit commuters between 2015 and 2022. Which choice most "
          "effectively evaluates this claim using data from the table?",
          "City Y's transit ridership rose from 19% to 27%, an increase of 8 percentage points.",
          "City Y grew by 8 points (27−19), City W by 7 points (35−28), City X declined by 3 points, and City Z grew by 5 points. City Y had the largest increase. The claim is correct.",
          "City Z had the highest transit ridership in both 2015 and 2022.",
          "City X was the only city where transit ridership declined between 2015 and 2022.", "B",
          "Y: +8, W: +7, X: −3, Z: +5. City Y had the largest increase (8 points), confirming the planner's claim.")

        q(gv, H,
          "The committee's final recommendations, presented after months of deliberation "
          "with stakeholders from across the region, ________ a significant departure "
          "from the policies adopted just three years earlier.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "represents", "represent", "is representing", "has represented", "B",
          "The plural subject 'recommendations' requires the plural verb 'represent.'")

        q(gv, H,
          "Not only the lead researcher but also several of her graduate students "
          "________ named as co-authors on the landmark study published in Nature.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "was", "were", "is", "has been", "B",
          "With 'not only A but also B,' the verb agrees with the subject closest to it. 'Graduate students' is plural → 'were.'")

        q(gv, H,
          "________ extensive archival research across three countries, the historian "
          "constructed a nuanced portrait of the diplomatic negotiations leading up "
          "to the armistice.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "Conducting", "Having conducted", "To conduct", "She conducted", "B",
          "'Having conducted' is the perfect participial phrase indicating the prior completed research that enabled the historian's portrait.")

        q(gv, H,
          "The new regulation, which applies to all manufacturers operating within the "
          "state's borders regardless of company size, ________ into effect on January 1 "
          "of next year.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          "go", "goes", "are going", "have gone", "B",
          "The singular subject 'regulation' requires the singular verb 'goes.'")

        q(gp, H,
          "The expedition team had three main objectives ________ mapping the uncharted "
          "river system, cataloguing undescribed plant species, and establishing "
          "relationships with communities in the region.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", ":", ";", "—and", "B",
          "A colon introduces the list of three objectives that elaborates on 'three main objectives.'")

        q(gp, H,
          "The psychologist's study was groundbreaking ________ it challenged the "
          "prevailing view that personality traits are fixed from childhood and "
          "cannot change significantly in adulthood.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ";", ",", ":", "because,", "A",
          "A semicolon correctly joins two independent clauses. The second clause explains why the study was groundbreaking.")

        q(gp, H,
          "The opera singer's performance ________ universally praised by critics — was "
          "her debut at the Metropolitan Opera, a stage she had dreamed of since childhood.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ",", "—", ";", ":", "B",
          "The parenthetical 'universally praised by critics' is set off by dashes. Since the closing dash is present, the opening punctuation must also be a dash.")

        q(gp, H,
          "Despite the economic uncertainty of the period, the architect completed "
          "her most ambitious project in 1938 ________ a sprawling public library "
          "that remains in use today.\n\n"
          "Which choice completes the text so that it conforms to the conventions of "
          "Standard English?",
          ":", ",", ";", "—", "A",
          "A colon correctly introduces the appositive ('a sprawling public library') that identifies the ambitious project.")

        q(tr, H,
          "Roman concrete, known as opus caementicium, was renowned for its durability — "
          "some structures built with it have survived for over 2,000 years. ________ "
          "modern scientists were surprised to discover that Roman concrete actually "
          "becomes stronger over time as seawater penetrates it and causes minerals "
          "to crystallize within the structure.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Therefore,", "Moreover,", "As a result,", "Instead,", "B",
          "'Moreover' adds an additional surprising fact about Roman concrete beyond its known durability.")

        q(tr, H,
          "The novelist revised her manuscript seven times before submitting it to her "
          "publisher, each revision bringing her closer to the spare, precise prose she "
          "envisioned. ________ when the novel was finally published, it was praised for "
          "exactly the qualities she had worked so hard to achieve.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Nevertheless,", "Consequently,", "In contrast,", "Alternatively,", "B",
          "'Consequently' signals that the extensive revisions led to the praised outcome — cause and effect.")

        q(tr, H,
          "The physicist's first paper on quantum entanglement was rejected by three "
          "major journals, each citing the unconventional nature of the claims. "
          "________ the paper was eventually accepted and went on to become one of "
          "the most cited works in theoretical physics.\n\n"
          "Which choice completes the text with the most logical transition?",
          "Furthermore,", "As a result,", "Ultimately,", "Similarly,", "C",
          "'Ultimately' signals the final outcome after the difficulty — the paper eventually succeeded despite initial rejection.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- Ada Lovelace (1815–1852) is often called the world's first computer programmer.\n"
          "- She worked with mathematician Charles Babbage on his Analytical Engine.\n"
          "- Her notes on the Engine include an algorithm designed to compute Bernoulli numbers.\n"
          "- She recognized that the Engine could be used for more than just calculation — "
          "including composing music.\n"
          "- Her contributions were not widely recognized until the mid-twentieth century.\n\n"
          "The student wants to explain why Lovelace is considered a visionary beyond "
          "her programming work. Which choice most effectively uses relevant information "
          "from the notes to accomplish this goal?",
          "Ada Lovelace worked with Charles Babbage on his Analytical Engine in the early nineteenth century.",
          "Lovelace wrote an algorithm to compute Bernoulli numbers, making her the world's first computer programmer.",
          "Lovelace recognized that the Analytical Engine could be used for purposes beyond calculation — such as composing music — demonstrating a visionary understanding of computing's potential.",
          "Lovelace's contributions were not widely recognized until the mid-twentieth century.", "C",
          "Option C highlights her visionary insight that computing could go beyond calculation — the reason she is considered more than just a programmer.")

        q(rn, H,
          "While researching a topic, a student has taken the following notes:\n"
          "- The ozone layer shields Earth from harmful ultraviolet (UV) radiation from the sun.\n"
          "- In 1985, scientists discovered a large hole in the ozone layer above Antarctica.\n"
          "- The hole was caused primarily by chlorofluorocarbons (CFCs) used in refrigerants "
          "and aerosol sprays.\n"
          "- The Montreal Protocol (1987) phased out CFC production in most countries.\n"
          "- Scientists now project the ozone layer will recover to pre-1980 levels by 2065.\n\n"
          "The student wants to present the Montreal Protocol as a model of successful "
          "international environmental action. Which choice most effectively uses "
          "relevant information from the notes to accomplish this goal?",
          "The ozone hole was discovered in 1985 above Antarctica.",
          "CFCs from refrigerants and aerosol sprays were the primary cause of ozone depletion.",
          "By phasing out CFC production through the Montreal Protocol (1987), countries took coordinated action that scientists now project will allow the ozone layer to recover to pre-1980 levels by 2065.",
          "The ozone layer protects Earth from harmful UV radiation.", "C",
          "Option C traces the full arc: the international agreement (Montreal Protocol) led to action (phasing out CFCs) with measurable projected success (recovery by 2065) — making it the strongest case for the Protocol as a model.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 1 (medium)
        # ════════════════════════════════════════════════════════════════

        q(alg, M, "Solve for x: 5x + 8 = 33",
          "3", "4", "5", "6", "C",
          "5x = 25; x = 5.")

        q(alg, M, "If 2(3x − 4) = 4x + 6, what is the value of x?",
          "5", "7", "8", "10", "B",
          "6x − 8 = 4x + 6; 2x = 14; x = 7.")

        q(alg, M, "Which expression is equivalent to 3(x + 2) + 2(x − 5)?",
          "5x − 4", "5x + 4", "5x + 16", "5x − 16", "A",
          "3x + 6 + 2x − 10 = 5x − 4.")

        q(alg, M,
          "A line has equation y = −2x + 7. Which ordered pair lies on this line?",
          "(1, 4)", "(2, 2)", "(3, 1)", "(4, 0)", "C",
          "y = −2(3) + 7 = 1 ✓. Check others: (1,4): −2+7=5≠4; (2,2): −4+7=3≠2; (4,0): −8+7=−1≠0.")

        q(alg, M,
          "A line has equation y = −2x + 3. Which ordered pair lies on this line?",
          "(1, 5)", "(2, −1)", "(3, 4)", "(4, 5)", "B",
          "y = −2(2) + 3 = −4 + 3 = −1 ✓. Others: (1,5): −2+3=1≠5; (3,4): −6+3=−3≠4; (4,5): −8+3=−5≠5.")

        q(alg, M,
          "The system of equations has solution (x, y). What is x + y?\n"
          "x + 2y = 10\n2x − y = 5",
          "5", "6", "7", "8", "C",
          "From eq2: y = 2x−5. Substitute: x + 2(2x−5) = 10 → 5x−10=10 → x=4; y=3. x+y=7.")

        q(fun, M,
          "If g(x) = x² + 3, what is g(−3)?",
          "6", "9", "12", "15", "C",
          "g(−3) = (−3)² + 3 = 9 + 3 = 12.")

        q(fun, M,
          "A function f satisfies f(2) = 7 and f(5) = 16. If f is linear, what is f(0)?",
          "1", "2", "3", "4", "A",
          "Slope = (16−7)/(5−2) = 3. f(x) = 3x + b; 7 = 6+b → b=1. f(0)=1.")

        q(fun, M,
          "In the xy-plane, the line y = 2x − 5 crosses the x-axis at what point?",
          "(2.5, 0)", "(5, 0)", "(0, −5)", "(−5, 0)", "A",
          "Set y = 0: 2x − 5 = 0 → x = 2.5. The x-intercept is (2.5, 0).")

        q(fun, M,
          "The table shows values of function h:\nx: 0, 1, 2, 3\nh(x): 5, 8, 11, 14\n\n"
          "Which equation defines h(x)?",
          "h(x) = 3x + 5", "h(x) = 2x + 5", "h(x) = 4x + 1", "h(x) = 3x + 2", "A",
          "h(0)=5 ✓; h(1)=8 ✓; h(2)=11 ✓; h(3)=14 ✓ for h(x) = 3x+5.")

        q(geo, M,
          "A right triangle has a hypotenuse of 17 and one leg of 8. What is the "
          "length of the other leg?",
          "9", "13", "15", "25", "C",
          "leg = √(17² − 8²) = √(289 − 64) = √225 = 15.")

        q(geo, M,
          "The circumference of a circle is 31.4 inches. What is its radius? (Use π ≈ 3.14)",
          "3", "5", "8", "10", "B",
          "C = 2πr → 31.4 = 2(3.14)r → r = 31.4/6.28 = 5.")

        q(geo, M,
          "A regular hexagon has interior angles that each measure how many degrees?",
          "108°", "120°", "135°", "150°", "B",
          "Sum of interior angles of hexagon = (6−2)×180° = 720°. Each angle = 720°/6 = 120°.")

        q(geo, M,
          "A triangle has a base of 14 cm and a height of 9 cm. What is its area?",
          "23 cm²", "46 cm²", "63 cm²", "126 cm²", "C",
          "Area = (1/2) × 14 × 9 = 63 cm².")

        q(dsp, M,
          "The data set is: 8, 13, 5, 19, 10, 13, 7. What is the median?",
          "10", "11", "13", "19", "A",
          "Sorted: 5, 7, 8, 10, 13, 13, 19. Median = 4th value = 10.")

        q(dsp, M,
          "A class of 24 students took a quiz. If 18 students passed, what percentage "
          "of students passed?",
          "60%", "70%", "75%", "80%", "C",
          "18/24 × 100 = 75%.")

        q(dsp, M,
          "A standard deck of 52 cards has 4 suits of 13 cards each. If one card is "
          "drawn at random, what is the probability it is a heart?",
          "1/52", "1/13", "1/4", "4/13", "C",
          "13 hearts out of 52 cards: 13/52 = 1/4.")

        q(dsp, M,
          "The ages of seven teachers are: 28, 35, 42, 29, 55, 48, 35. What is the mode?",
          "28", "35", "42", "48", "B",
          "35 appears twice; all other values appear once. Mode = 35.")

        q(dsp, M,
          "In a survey, 45 of 180 participants chose option A. What percentage chose option A?",
          "20%", "25%", "30%", "35%", "B",
          "45/180 × 100 = 25%.")

        q(wp, M,
          "A recipe calls for 2.5 cups of flour to make 20 cookies. How many cups of "
          "flour are needed to make 48 cookies?",
          "4", "5", "6", "7", "C",
          "Rate: 2.5/20 cups per cookie. For 48 cookies: (2.5/20) × 48 = 6 cups.")

        q(wp, M,
          "A swimming pool holds 15,000 gallons and is currently 40% full. How many "
          "more gallons are needed to fill it completely?",
          "6,000", "7,500", "9,000", "10,000", "C",
          "Currently: 0.40 × 15,000 = 6,000 gallons. Needed: 15,000 − 6,000 = 9,000.")

        q(wp, M,
          "Tom drove 180 miles in 3 hours, then 120 miles in 2 hours. What was his "
          "average speed for the entire trip?",
          "54 mph", "57 mph", "60 mph", "65 mph", "C",
          "Total distance = 300 miles; total time = 5 hours. Average speed = 300/5 = 60 mph.")

        q(wp, M,
          "If 5 workers can build a wall in 12 days, how many days would it take "
          "10 workers to build the same wall?",
          "4", "5", "6", "8", "C",
          "Total work = 5 × 12 = 60 worker-days. With 10 workers: 60/10 = 6 days.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Easier (easy)
        # ════════════════════════════════════════════════════════════════

        q(alg, E, "Solve for x: 3x − 5 = 10",
          "3", "4", "5", "6", "C",
          "3x = 15; x = 5.")

        q(alg, E, "If y = 3x + 2 and x = 4, what is y?",
          "10", "12", "14", "16", "C",
          "y = 3(4) + 2 = 12 + 2 = 14.")

        q(alg, E, "Which value of x satisfies 2x − 1 > 7?",
          "3", "4", "5", "6", "C",
          "2x > 8; x > 4. Among the choices, x = 5 satisfies (2(5)−1=9>7) ✓.")

        q(alg, E, "What is the value of 4a − b when a = 5 and b = 3?",
          "14", "15", "17", "23", "C",
          "4(5) − 3 = 20 − 3 = 17.")

        q(alg, E, "If x + y = 10 and x = 6, what is y?",
          "2", "3", "4", "5", "C",
          "y = 10 − 6 = 4.")

        q(fun, E, "If f(x) = 2x − 3, what is f(7)?",
          "9", "10", "11", "14", "C",
          "f(7) = 2(7) − 3 = 14 − 3 = 11.")

        q(fun, E, "Which point lies on the line y = −x + 5?",
          "(1, 3)", "(2, 3)", "(3, 2)", "(5, 0)", "C",
          "y = −3 + 5 = 2 ✓ for (3,2). Check others: (1,3): −1+5=4≠3; (2,3): −2+5=3 ✓ — both B and C work.")

        q(fun, E, "Which point lies on the line y = x − 4?",
          "(3, 0)", "(4, 1)", "(6, 2)", "(8, 3)", "C",
          "y = 6−4 = 2 ✓ for (6,2). Check others: (3,0): 3−4=−1≠0; (4,1): 4−4=0≠1; (8,3): 8−4=4≠3.")

        q(fun, E, "The line y = 2x + 1 crosses the y-axis at which point?",
          "(0, 0)", "(0, 1)", "(1, 0)", "(0, 2)", "B",
          "At x = 0: y = 2(0) + 1 = 1. The y-intercept is (0, 1).")

        q(geo, E, "What is the perimeter of a rectangle with length 12 and width 5?",
          "17", "24", "34", "60", "C",
          "P = 2(12 + 5) = 2(17) = 34.")

        q(geo, E,
          "Two angles of a triangle measure 55° and 75°. What is the third angle?",
          "40°", "50°", "55°", "60°", "B",
          "180° − 55° − 75° = 50°.")

        q(geo, E, "What is the area of a square with side length 9?",
          "18", "36", "72", "81", "D",
          "Area = 9² = 81.")

        q(geo, E,
          "A right triangle has legs of 5 and 12. What is the length of the hypotenuse?",
          "7", "11", "13", "17", "C",
          "c = √(25 + 144) = √169 = 13.")

        q(dsp, E,
          "The data set is: 4, 9, 3, 7, 2. What is the median?",
          "3", "4", "7", "9", "B",
          "Sorted: 2, 3, 4, 7, 9. Median = 3rd value = 4.")

        q(dsp, E,
          "A bag has 6 red balls and 4 blue balls. What is the probability of randomly "
          "selecting a red ball?",
          "2/5", "3/5", "2/3", "1/2", "B",
          "P(red) = 6/(6+4) = 6/10 = 3/5.")

        q(dsp, E,
          "The temperatures for six days were: 68, 72, 70, 65, 74, 71. What is the mean?",
          "69", "70", "71", "72", "B",
          "(68+72+70+65+74+71) = 420; 420/6 = 70.")

        q(dsp, E,
          "There are 25 students in a class. 15 are girls. What percentage are boys?",
          "30%", "35%", "40%", "45%", "C",
          "Boys = 25 − 15 = 10; 10/25 × 100 = 40%.")

        q(dsp, E,
          "What is the range of this data set: 14, 6, 22, 9, 18?",
          "8", "13", "16", "22", "C",
          "Range = max − min = 22 − 6 = 16.")

        q(wp, E, "A bicycle costs $180 and is on sale for 15% off. What is the sale price?",
          "$135", "$145", "$153", "$165", "C",
          "Discount = 0.15 × $180 = $27. Sale price = $180 − $27 = $153.")

        q(wp, E,
          "A school bus can hold 44 students. If 176 students need to travel, how many "
          "full buses are needed?",
          "3", "4", "5", "6", "B",
          "176 ÷ 44 = 4 buses.")

        q(wp, E, "Ana reads 25 pages per day. How many days will it take her to read 175 pages?",
          "5", "6", "7", "8", "C",
          "175 ÷ 25 = 7 days.")

        q(wp, E,
          "A shop sells 3 pencils for $1.20. What is the cost of 12 pencils?",
          "$3.60", "$4.00", "$4.80", "$5.40", "C",
          "Cost per pencil = $1.20/3 = $0.40. 12 × $0.40 = $4.80.")

        # ════════════════════════════════════════════════════════════════
        # MATH — Module 2—Harder (hard)
        # ════════════════════════════════════════════════════════════════

        q(alg, H,
          "If 3x − 2y = 16 and x + y = 7, what is the value of y?",
          "1", "2", "3", "4", "A",
          "From x = 7−y: 3(7−y)−2y=16 → 21−3y−2y=16 → 5y=5 → y=1.")

        q(alg, H,
          "The sum of three consecutive integers is 81. What is the largest of "
          "the three integers?",
          "26", "27", "28", "29", "C",
          "Let the integers be n, n+1, n+2. 3n+3=81 → n=26. Largest = 28.")

        q(alg, H,
          "For what positive value of x does x² − 5x − 14 = 0?",
          "2", "5", "7", "14", "C",
          "(x−7)(x+2)=0 → x=7 (positive) or x=−2.")

        q(alg, H,
          "A clothing store marks up the wholesale price of a shirt by 40% and then "
          "offers a 25% discount on the marked-up price. If the original wholesale "
          "price is w, what is the final selling price?",
          "1.05w", "1.15w", "0.95w", "1.40w", "A",
          "Marked up: 1.40w. After 25% discount: 1.40w × 0.75 = 1.05w.")

        q(alg, H,
          "The graph of a linear equation passes through (−2, 5) and (4, −1). "
          "What is the equation of this line?",
          "y = −x + 3", "y = x + 3", "y = −x − 3", "y = x − 3", "A",
          "Slope = (−1−5)/(4−(−2)) = −6/6 = −1. Using (4,−1): −1 = −4+b → b=3. y=−x+3.")

        q(fun, H,
          "If f(x) = x² − 3x and g(x) = 2x + 1, what is f(g(2))?",
          "5", "10", "15", "20", "B",
          "g(2)=5; f(5)=25−15=10.")

        q(fun, H,
          "The vertex of the parabola y = (x − 3)² + 4 is at which point?",
          "(3, 4)", "(−3, 4)", "(3, −4)", "(−3, −4)", "A",
          "Vertex form y = a(x−h)² + k has vertex at (h, k) = (3, 4).")

        q(fun, H,
          "A function f is defined by f(x) = 3x − 7. If f(a) = 5, "
          "what is the value of a?",
          "3", "4", "5", "6", "B",
          "3a − 7 = 5 → 3a = 12 → a = 4.")

        q(fun, H,
          "If f(x) = 2x + 3, for what value of x does f(x) = f(x+1)?",
          "No such value exists",
          "x = 0",
          "x = 1",
          "x = 2", "A",
          "f(x)=2x+3; f(x+1)=2(x+1)+3=2x+5. 2x+3=2x+5 gives 3=5, which is never true. No such x exists.")

        q(geo, H,
          "Two similar triangles have corresponding sides in ratio 3:5. If the area of "
          "the smaller triangle is 27 cm², what is the area of the larger triangle?",
          "35 cm²", "45 cm²", "55 cm²", "75 cm²", "D",
          "Area ratio = (3/5)² = 9/25. 27/(area) = 9/25 → area = 27 × 25/9 = 75 cm².")

        q(geo, H,
          "A cone has a radius of 6 and a slant height of 10. What is the lateral "
          "surface area of the cone? (Use π ≈ 3.14)",
          "60π", "120π", "188.4", "376.8", "C",
          "Lateral SA = πrl = 3.14 × 6 × 10 = 188.4.")

        q(geo, H,
          "In a right triangle, one acute angle measures 30°. If the hypotenuse is 20, "
          "what is the length of the side opposite the 30° angle?",
          "8", "10", "12", "14", "B",
          "In a 30-60-90 triangle, the side opposite 30° = hypotenuse/2 = 20/2 = 10.")

        q(geo, H,
          "The area of a trapezoid with parallel sides of 8 and 14 and a height of 6 is:",
          "44", "66", "88", "132", "B",
          "Area = (1/2)(b₁+b₂)×h = (1/2)(8+14)(6) = (1/2)(22)(6) = 66.")

        q(dsp, H,
          "Nine data values have a mean of 20. When a tenth value is added, the mean "
          "becomes 21. What is the tenth value?",
          "28", "29", "30", "31", "C",
          "Sum of first 9 = 180. New sum = 21×10 = 210. Tenth value = 210−180 = 30.")

        q(dsp, H,
          "Two dice are rolled. What is the probability that the sum of the two dice "
          "equals 7?",
          "1/9", "1/8", "1/6", "1/4", "C",
          "Pairs summing to 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) — 6 out of 36 total. P = 6/36 = 1/6.")

        q(dsp, H,
          "A set of 8 data values has a sum of 96. Two values equal to 6 are "
          "removed. What is the new mean of the remaining values?",
          "12", "14", "16", "18", "B",
          "Remaining sum = 96 − (2×6) = 84. Remaining count = 6. Mean = 84/6 = 14.")

        q(dsp, H,
          "A set of 10 numbers has a mean of 15. If 5 is added to each number in "
          "the set, what is the new mean?",
          "15", "17", "20", "25", "C",
          "Adding 5 to each number increases the mean by 5: 15 + 5 = 20.")

        q(dsp, H,
          "In a class, 35% of students play a sport, 50% are in a club, and 20% "
          "do both. What percentage of students do neither?",
          "25%", "30%", "35%", "40%", "C",
          "Sport or club = 35 + 50 − 20 = 65%. Neither = 100 − 65 = 35%.")

        q(wp, H,
          "A car and a truck start from the same point and travel in opposite directions. "
          "The car travels at 55 mph and the truck at 45 mph. After how many hours will "
          "they be 250 miles apart?",
          "2", "2.5", "3", "3.5", "B",
          "Combined speed = 55 + 45 = 100 mph. Time = 250/100 = 2.5 hours.")

        q(wp, H,
          "A mixture of 40% acid solution and 70% acid solution is made to produce "
          "60 liters of a 50% solution. How many liters of the 40% solution are needed?",
          "20", "30", "40", "45", "C",
          "Let x = liters of 40% solution. 0.4x + 0.7(60−x) = 0.5(60) → 0.4x+42−0.7x=30 → −0.3x=−12 → x=40.")

        q(wp, H,
          "A printer can print 30 pages per minute. A faster printer can print 50 pages "
          "per minute. Working together, how many minutes does it take to print 400 pages?",
          "4", "5", "6", "8", "B",
          "Combined rate = 30+50 = 80 pages/min. Time = 400/80 = 5 minutes.")

        q(wp, H,
          "Sarah invested $5,000 at 4% annual simple interest and $3,000 at 6% annual "
          "simple interest. What is her total interest earned after 2 years?",
          "$640", "$760", "$760", "$760", "B",
          "Interest₁ = 5000×0.04×2 = $400. Interest₂ = 3000×0.06×2 = $360. Total = $760.")

        count = Question.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {count} total questions in database '
            f'({Question.objects.filter(subject=english).count()} English, '
            f'{Question.objects.filter(subject=math).count()} Math)'
        ))
