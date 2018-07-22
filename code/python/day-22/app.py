from question import question
question_prompt=[

"What color are apples:\n a-Red \n b-Purple \n c-Orange\n",
    "What color are bananas:\n a-Pink \n b-Magenta \n c-Yellow\n",
    "What color are strawberry:\n a-Yellow \n b-Red \n c-Blue\n",

]

questions = [question(question_prompt[0], 'a'),
             question(question_prompt[1], 'c'), 
             question(question_prompt[2], 'b')]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print('Your score: '+str(score))

run_test(questions)
