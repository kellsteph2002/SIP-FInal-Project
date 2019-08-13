Q1 = ["1. Who refused to give up her seat on the bus on December 1st,1955 in Montogmery, Alabama? \nA. Rosa Parks \nB. Diana Nash \nC. Coretta Scott King \nD. Daisy Bates",
        "You are correct! \nI hoped that you knew that one but you shouldn't forget about the other ladies. \nDiana Nash was one of the leaders of SNCC(Student Nonviolent Coordinating Committee). \nCoretta Scott King was the wife of Dr. Martin Luther King Jr. who stood by his side as a fellow activist during the civil rights movement even after his death. She founded the MLK Jr. Center of NonViolent Social Change. \nDaisy Bates helped organize the Little Rock 9s trip to school and dealing with most pf the public affairs.",
        "You are incorrect!\nI hoped that you knew that one but you shouldn't forget about the other ladies. \nDiana Nash was one of the leaders of SNCC(Student Nonviolent Coordinating Committee). \nCoretta Scott King was the wife of Dr. Martin Luther King Jr. who stood by his side as a fellow activist during the civil rights movement even after his death. She founded the MLK Jr. Center of NonViolent Social Change. \nDaisy Bates helped organize the Little Rock 9s trip to school and dealing with most pf the public affairs.",
        "A",
        False]

Q2 = ["2. Who was the first woman to win a Noble Peace Prize?\nA. Alva Myrdal \nB. Françoise Barré-Sinoussi \nC. Malala Yousafzai \nD. Marie Curie",
        "You're on a roll! In fact, she was the only person awarded twice(1903 and 1911). All of the other options were awarded as well. \nFrançoise Barré-Sinoussi(2008) discovered HIV. \n Despite being threatened and severly injured by the Taliban, Malala Yousafzai(2014) constntly advocates for education for young girls \nAlva Myrdal(1982) played a big part in the United Nation's disarmament negotiaions. \nDon't you love to see women being rewarded for their successes?",
        "Keep on trying! In fact, Marie Curie was the only person awarded twice(1903 and 1911). All of the other options were awarded as well. \nFrançoise Barré-Sinoussi(2008) discovered HIV. \nDespite being threatened and severly injured by the Taliban, Malala Yousafzai(2014) constntly advocates for education for young girls \nAlva Myrdal(1982) played a big part in the United Nation's disarmament negotiaions. \nDon't you love to see women being rewarded for their successes?",
        "D",
        False]
Q3 = ["3. Who published the first computer algothrim?\nA. Ada Lovelace \nB. Eda Heartstring \nC. Ada Shoelace \nD. Eda Lovelace",
        "Calm down! You're on fire! You managed to not get distracted by my horrible puns on her name. Her accomplishement is constantly being debated BY MEN who believe that she was unabe to understand such a thing. However, she was a well-know and very competent mathematician so I would definetly not put it past her. Don't let ANYONE discred your work!",
        "Did my wonderful puns distract you? Try not to discredit Ada Lovelace like all of the mysogynistic men did during her time.",
        "A",
        False]
Q4 = ["4. In what year and by what ammendement were women given the right to vote?\nA. 1919-19th \nB. 1920-19th \nC. 1920-20th\nD. 1919-20th",
        "Exactly! August 18, 1920, the 19th amendment granted women the right to vote.",
        "Ahhh so many numbers! I know why you may have gotten confused but just to clarify on August 18, 1920, the 19th amendment granted women the right to vote",
        "B",
        False]
Q5 = ["5. How many women are running in the current(2019) presidential election \nA. 1 \nB. 0\nC. 7\nD. 6",
        "This is the greatest amount of women who have ran. Glad it's engraved. Can't wait until the next election.",
        "It's 6! This is the greatest amount of women who have ran. You must engrave this moment into your memory forever(or until the number increases again).",
        "D",
        False]

Question_List = [Q1, Q2, Q3, Q4, Q5]

def check(question):
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (question[0])
    answer=input("Answer: ")
    if answer == question[3]:
        question[4]=True


def main():
    print ("Hello! This quiz will be testing your knowledge on the history of females. Are you aware of the various accomplishments that women have made through out the years? Take this to figure out if you have what should be considered common knowledge.Are you ready?(Note: Make sure to write your responses in UPPERCASE and you only have to include the letter of the answer choice!)")
    play =input()

    correct_answers = 0
    total_questions = len(Question_List)

    if play == "YES":
        for question in Question_List:
            check(question)
            if question[4] == True:
                print(question[1])
                correct_answers += 1
            else:
                print(question[2])

    if (correct_answers/total_questions) == 1:
        print("You've gotten them all correct. You know your women's history but don't stop. Explore our website to learn even more. Hopefully, you are inspired to follow in the footsteps of these amazing and brave women.")
    elif correct_answers/total_questions == 0:
        print("I think you need to do a lot more research. But don't you fear, if you explore our website, you can learn so much more. Hopefully, you are inspired to follow in the footsteps of these amazing and brave women.")
    else:
        print("You know somethings but it doesnt hurt to explore further. Explore our website and you will be able to learn a lot. Hopefully, you are inspired to follow in the footsteps of these amazing and brave women. ")

main()
