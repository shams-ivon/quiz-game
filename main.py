from question_model import Question
from data import question_data

question_bank = []

for question_ans_pair in question_data:
    question_object = Question(question_ans_pair["text"], question_ans_pair["answer"])
    question_bank.append(question_object)

