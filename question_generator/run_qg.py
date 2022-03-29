import argparse
from questiongenerator import QuestionGenerator
from questiongenerator import print_qa
import pandas as pd 
from dateutil import parser
import re
import os
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--answer_style",
        default="sentences",
        type=str,
        help="The desired type of answers. Choose from ['all', 'sentences', 'multiple_choice']",
    )
    parser.add_argument("--model_dir", type=str, default=None)
    parser.add_argument("--num_questions", type=int, default=10000)
    parser.add_argument("--show_answers", dest="show_answers", action="store_true", default=True)
    parser.add_argument("--text_file", type=str, required=True)
    parser.add_argument("--use_qa_eval", dest="use_qa_eval", action="store_true", default=True)
    return parser.parse_args()


def is_valid_date(date_str):
    try:
        parser.parse(date_str)
        return True
    except:
        return False


def file_text(text):
    s=""
    m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', text);
    word=['Telegram','telegram','twitter','Contact','Twitter','TikTok','Instagram','instagram','Youtube','youtube', 'contact', 'follow','medium','Follow','Medium','?']
    for i in m:
        if any(x in i for x in word):
            pass
        else:
            if len(i)< 1000:
                
                s=s+i+os.linesep
#            textfile.write(i + "\n\")
    return s


if __name__ == "__main__":
    args = parse_args()
    with open(args.text_file, 'rb') as file:
        text = file.read().decode(errors='replace')
#    print(text_file)
    F_name=args.text_file.split(".")[0]
    data=[text]
    
    new_list = [' '.join([w for w in line.split() if not is_valid_date(w)]) for line in data]
    text=file_text(new_list[0])
    
    qg = QuestionGenerator()
    qa_list = qg.generate(
        text,
        num_questions=int(args.num_questions),
        answer_style=args.answer_style,
        use_evaluator=args.use_qa_eval
    )
    question, answer=print_qa(qa_list, show_answers=args.show_answers)
    
    pd.DataFrame({'Questions':question,"Answers": answer}).to_csv(f_name+'.csv')
#
