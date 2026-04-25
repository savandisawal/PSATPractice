"""
Management command to fix questions where the stored correct_answer contradicts
the explanation, or where the question/options are mathematically broken.

Run with: python manage.py fix_question_errors
"""
from django.core.management.base import BaseCommand
from practice.models import Question


class Command(BaseCommand):
    help = 'Fix broken/incorrect questions in the database'

    def handle(self, *args, **options):
        fixed = 0
        skipped = 0

        def fix(search_field, search_value, **updates):
            nonlocal fixed, skipped
            try:
                q = Question.objects.get(**{f'{search_field}__icontains': search_value})
                changed = False
                for k, v in updates.items():
                    if getattr(q, k) != v:
                        setattr(q, k, v)
                        changed = True
                if changed:
                    q.save()
                    fixed += 1
                    self.stdout.write(f'  FIXED: {search_value[:60]}')
                else:
                    skipped += 1
            except Question.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'  NOT FOUND: {search_value[:60]}'))
            except Question.MultipleObjectsReturned:
                self.stdout.write(self.style.WARNING(f'  MULTIPLE MATCHES: {search_value[:60]}'))

        def fix_by_id(qid, **updates):
            nonlocal fixed, skipped
            try:
                q = Question.objects.get(id=qid)
                changed = False
                for k, v in updates.items():
                    if getattr(q, k) != v:
                        setattr(q, k, v)
                        changed = True
                if changed:
                    q.save()
                    fixed += 1
                    self.stdout.write(f'  FIXED ID={qid}')
                else:
                    skipped += 1
            except Question.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'  NOT FOUND: ID={qid}'))

        self.stdout.write('Fixing broken questions...\n')

        # ── WRONG correct_answer (right answer is in the options) ─────────────

        # test5: 5(x+2)=3(x+8) → x=7 → B, was D
        fix('text', '5(x + 2) = 3(x + 8)',
            correct_answer='B',
            explanation='5x + 10 = 3x + 24 → 2x = 14 → x = 7.')

        # test5: equilateral triangle perimeter 36, area = 36√3 → B, was A
        fix('text', 'equilateral triangle has a perimeter of 36',
            correct_answer='B',
            explanation='Side = 36/3 = 12 cm. Area = (√3/4) × 12² = 36√3 cm².')

        # test4: 2x+y=9, x−y=3, x+y=5 → B, was C
        fix('text', '2x + y = 9 and x',
            correct_answer='B',
            explanation='Add equations: 3x = 12 → x = 4. Then y = 9 − 8 = 1. x + y = 5.')

        # test4: (3x+10)+(x+30)=180, larger=115° → B, was C
        fix('text', '(3x + 10)',
            correct_answer='B',
            explanation='3x+10+x+30=180 → 4x=140 → x=35. Larger: 3(35)+10 = 115°.')

        # test6: student needs 90 → C, was B
        fix('text', '72, 90, and 88',
            correct_answer='C',
            explanation='Total needed = 85 × 4 = 340. Current = 72+90+88 = 250. Need: 340 − 250 = 90.')

        # test6: (2x+1)(x−3)=0, x<0, 4x+6=4 → C, was A
        fix('text', '(2x + 1)(x',
            correct_answer='C',
            explanation='2x+1=0 → x=−1/2, or x=3. Since x<0, x=−1/2. 4(−1/2)+6 = −2+6 = 4.')

        # test6: 5x−2y=16, 3x+y=14, x+y=6 → A, was C
        fix('explanation', '11x=44',
            correct_answer='A',
            explanation='From eq2: y = 14−3x. Sub into eq1: 5x−2(14−3x)=16 → 11x=44 → x=4. y=2. x+y=6.')

        # test6: 2x+3y=18, 4x−y=8, y=4 → C, was A
        fix('text', '2x + 3y = 18 and 4x',
            correct_answer='C',
            explanation='From eq2: y = 4x−8. Sub: 2x+3(4x−8)=18 → 14x=42 → x=3. y=4(3)−8=4.')

        # test7: car depreciates 15%, $12,283 → B, was A
        fix('option_a', '$12,155',
            correct_answer='B',
            explanation='Value = 20000 × (0.85)³ = 20000 × 0.614125 ≈ $12,283.')

        # ── BROKEN questions (question/options needed rewriting) ──────────────

        # test3: f(a)=f(2a−1) → answer=1 not in {3,4,5,6} → rewrite to f(a)=5
        fix('text', 'f(a) = f(2a',
            text='A function f is defined by f(x) = 3x − 7. If f(a) = 5, what is the value of a?',
            correct_answer='B',
            explanation='3a − 7 = 5 → 3a = 12 → a = 4.')

        # test3: 8 values sum 96, remove 3 each=8 → mean=14.4 not in options
        fix('text', '8 data values has a sum of 96',
            text='A set of 8 data values has a sum of 96. Two values equal to 6 are removed. What is the new mean of the remaining values?',
            correct_answer='B',
            explanation='Remaining sum = 96 − (2×6) = 84. Remaining count = 6. Mean = 84/6 = 14.')

        # test5: 2x+3y=15, 4x−y=5 → x=15/7, not integer → fix equation
        fix('text', '2x + 3y = 15 and 4x',
            text='If 2x + 3y = 13 and 4x − y = 5, what is the value of y?',
            explanation='From eq2: y = 4x−5. Sub into eq1: 2x+3(4x−5)=13 → 14x=28 → x=2. y=4(2)−5=3.')

        # test5: f(x)=x²−4, g(x)=x+3 → discriminant 29 → fix g(x)
        fix('explanation', 'Discriminant',
            text='If f(x) = x² − 4 and g(x) = 2x − 1, for what values of x does f(x) = g(x)?',
            option_a='x = −3 or x = 1',
            option_b='x = −1 or x = 3',
            option_c='x = 3 only',
            option_d='x = −1 only',
            correct_answer='B',
            explanation='x²−4 = 2x−1 → x²−2x−3 = 0 → (x−3)(x+1) = 0 → x = 3 or x = −1.')

        # test4: 5x+2y=20, y=2x−1 → x=22/9 → fix equation
        fix('text', '5x + 2y = 20 and y = 2x',
            text='If 5x + 2y = 16 and y = 2x − 1, what is the value of x?',
            explanation='Substitute: 5x + 2(2x−1) = 16 → 9x − 2 = 16 → 9x = 18 → x = 2.')

        # test4: 4x+3y=18, y=2x → x=1.8 → fix equation
        fix('text', '4x + 3y = 18 and y = 2x',
            text='If 4x + 3y = 20 and y = 2x, what is the value of x?',
            explanation='Substitute: 4x + 3(2x) = 20 → 10x = 20 → x = 2.')

        # test4: 3x−y=11, x+2y=0 → y=−11/7 → fix equation
        fix('text', '3x − y = 11 and x + 2y',
            text='Solve the system: 3x − y = 21 and x + 2y = 0. What is the value of y?',
            explanation='From eq2: x = −2y. Substitute: 3(−2y)−y = 21 → −7y = 21 → y = −3.')

        # test4: (4x+15)+(2x+9)=180, larger=119° not in options → fix option D
        fix('text', '(4x + 15)',
            option_d='119°',
            correct_answer='D',
            explanation='4x+15+2x+9=180 → 6x+24=180 → x=26. Larger: 4(26)+15=119°.')

        # test4: y=3x+2, B and C both correct → fix option C
        fix('text', 'Which point lies on the graph of y = 3x + 2',
            option_c='(1, 4)',
            explanation='y = 3(2)+2 = 8, so (2,8) is correct. Others: (1,6): 5≠6; (1,4): 5≠4; (0,3): 2≠3.')

        # test4: y=2x−3, B and C and D all correct → fix options B, C
        fix('text', 'Which point lies on the line y = 2x',
            option_b='(2, 2)',
            option_c='(3, 4)',
            explanation='y = 2(1)−3 = −1, so (1,−1) is correct. Others: (0,3): −3≠3; (2,2): 1≠2; (3,4): 3≠4.')

        # test7: 2x+5y=24, 4x−y=2 → x=17/11 → fix eq2
        fix('explanation', '17/11',
            text='A system of equations:\n2x + 5y = 24\n4x − y = 4\n\nWhat is the value of x + y?',
            explanation='Multiply eq2 by 5: 20x−5y=20. Add to eq1: 22x=44 → x=2. y=4(2)−4=4. x+y=6.')

        # test3: y=−2x+7, all 4 options were on the line → fix A, B, D
        fix('text', '2x + 7',
            option_a='(1, 4)',
            option_b='(2, 2)',
            option_d='(4, 0)',
            explanation='y = −2(3)+7 = 1, so (3,1) is correct. Others: (1,4): 5≠4; (2,2): 3≠2; (4,0): −1≠0.')

        # test3: y=x−4, options C and D both correct → fix option D
        fix('option_c', '(6, 2)',
            option_d='(8, 3)',
            explanation='y = 6−4 = 2, so (6,2) is correct. Others: (3,0): −1≠0; (4,1): 0≠1; (8,3): 4≠3.')

        # test5: already-fixed mean question (204 sum) — ensure it's correct
        fix('explanation', '168/12',
            correct_answer='A',
            explanation='New sum = 204 − 3(30) + 3(18) = 204 − 90 + 54 = 168. New mean = 168/12 = 14.')

        self.stdout.write(
            self.style.SUCCESS(f'\nDone: {fixed} fixed, {skipped} already correct.')
        )
