Q1 = ["The Body Shop?",
        "Correct! Is it a coincidence that it happens to be cruelty-free and vegetarian friendly? The Body Shop was previously owned by L'Oreal but was later sold to a very environmenty consciouse business Natura.",
        "The Body Shop was previously owned by L'Oreal but was later sold to a very environmenty consciouse business Natura. By Buying from them, you're not only supporting a woman business leader but the Earth.",
        "T",
        False]

Q2 = ["2. Proactiv?",
        "Founded by not only one but TWO women. They were dermatogology students at Stanford who noticed how acne affected all ages and wanted to change that.",
        "Sorry, but you're going to have to add 2 to your response. Founded by not only one but TWO women. They were dermatogology students at Stanford who noticed how acne affected all ages and wanted to change that.",
        "T",
        False]
Q3 = ["MAC Cosmetics?",
        "A favorite brand of women all over the world is in fact ran by a man. Wonder who he gets information and numbers from?",
        "Nope! A favorite brand of women all over the world is in fact ran by a man. Wonder who he gets information and numbers from?",
        "F",
        False]
Q4 = ["BET?",
        "A woman strived to connect the African American commnunity through entertainment.",
        "Nope, a woman was able to connect the Africa American community through entertainment.",
        "T",
        False]
Q5 = ["Facebook?",
        " You're probably aware of the ecentric personality of Facebook's male CEO.",
        "He may not be a woman but I advise you check him out.",
        "F",
        False]

Q6 = ["YouTube?",
        "You guessed it! Although is was founded by men, the current CEO of this source of various content is a woman and it has yet to fail.",
        "Although is was founded by men, the current CEO of this source of various content is a woman and it has yet to fail.",
        "T" ,
        False]
Q7 = ["Victoria's Secret?",
        "Both the founder and current CEOs are males. We're not judging but it does come as a slight surprise.",
        "Both the founder and current CEOs are males. We're not judging but it does come as a slight surprise.",
        "F",
        False]
Q8 = ["Yahoo?",
        "Correct! The current CEO of Yahoo is a female.",
        "The current CEO of Yahoo is a female.",
        "T",
        False]
Q9 = ["Girls Who Code?",
        "A company that was founded by a women in order to encourage more girls to join STEM fields.",
        "Nope! A favorite brand of women all over the world is in fact ran by a man. Wonder who he gets information and numbers from?",
        "T",
        False]



question_list = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9]

def check(question):
    print ("********************************************************************************")
    print (question[0])
    answer=input("Answer: ")
    if answer == question[3]:
        question[4]=True


def main():
    print ("Do you know if the businesses that frequently visit are owned or led by women or not? This TRUE or FALSE quiz will test your knowledge. Are you ready?(Responses in the form of T or F)")
    play =input()

    correct_answers = 0
    total_questions = len(question_list)

    if play == "YES":
        for question in question_list:
            check(question)
            if question[4] == True:
                print(question[1])
                correct_answers += 1
            else:
                print(question[2])

    if (correct_answers/total_questions) >= 0.85:
        print("\nIt's either you're obsessed with businesses or you're wpke. It's amazing that you are aware of these women's roles because that's the first step in supporiting them. Now study, workhard so that you can snatch up their positions XD.")
    elif correct_answers/total_questions <= 0.34:
        print("\nYour answers may have been driven by stereotypes or just a lack of knowledge. Don't be scared to ask questions and research so that we are able to give women the credit that they deserve. Now go search up these women and their companies so that you can snatch up their positions XD.")
    else:
        print("\nYou did pretty well. Through this quiz I hope that you learned more. Don't be scared to ask questions and research so that we are able to give women the credit that they deserve. Now go search up these women and their companies so that you can snatch up their positions XD.")

main()
