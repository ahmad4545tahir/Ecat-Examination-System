mcq_bank = [
    {"topic": "Maths",    "question": "2 x 3= ?",               "opt1": "0",           "opt2": "6",        "opt3": "2",            "opt4": "-1",         "correct": "B"},
    {"topic": "Maths",    "question": "Derivative of 5x^2 = ?",          "opt1": "10x",          "opt2": "6x^2",     "opt3": "4",            "opt4": "4x^3",       "correct": "A"},
    {"topic": "Maths",    "question": "500-290 = ?",            "opt1": "110",          "opt2": "100",      "opt3": "210",            "opt4": "0",          "correct": "C"},
    {"topic": "Physics",  "question": "SI unit of Electric Current = ?", "opt1": "Volt",        "opt2": "Ohm",      "opt3": "Ampere",       "opt4": "Watt",       "correct": "C"},
    {"topic": "Physics",  "question": "vf = vi+St is which law?",            "opt1": "1st Law",     "opt2": "3rd equation of motion ",  "opt3": "3rd Law",      "opt4": "Hookes Law", "correct": "B"},
    {"topic": "Physics",  "question": "Which is a base quantity?",       "opt1": "Force",       "opt2": "Velocity", "opt3": "Acceleration", "opt4": "Mass",       "correct": "D"},
    {"topic": "Computer", "question": "Statement terminator in C = ?",   "opt1": "/",           "opt2": "#",        "opt3": ";",            "opt4": ":",          "correct": "C"},
    {"topic": "Computer", "question": "input device of computer = ?",           "opt1": "Keyboard",         "opt2": "RAM",      "opt3": "ROM",          "opt4": "Keyboard",   "correct": "A"},
    {"topic": "Computer", "question": "Keyboard is a _____ device?",     "opt1": "Application", "opt2": "Software", "opt3": "Hardware",     "opt4": "Virus",      "correct": "C"},
    {"topic": "English",  "question": "Synonym of Good = ?",            "opt1": "Joyful",      "opt2": "Sad",      "opt3": "Angry",        "opt4": "Tired",      "correct": "A"},
]

student_records = []

def verify_user(valid_id, valid_key):
    tries = 0
    while tries < 3:
        entered_id  = input("User ID  : ")
        entered_key = input("Password : ")
        if entered_id == valid_id and entered_key == valid_key:
            print("Access Granted!")
            return True
        tries += 1
        print("Incorrect credentials. Attempts remaining:", 3 - tries)
    print("Too many failed attempts. Access blocked.")
    return False

def assign_grade(pct):
    if pct >= 80:
        return "EXCELLENT"
    elif pct >= 65:
        return "GOOD"
    elif pct >= 50:
        return "AVERAGE"
    return "BELOW AVERAGE"

def print_question(num, item):
    print("\nQ" + str(num) + ". [" + item["topic"] + "] " + item["question"])
    print("  A)", item["opt1"],
          " B)", item["opt2"],
          " C)", item["opt3"],
          " D)", item["opt4"])

def display_review(chosen_answers):
    print("\n Answer Review ")
    for idx in range(len(mcq_bank)):
        picked = chosen_answers[idx]
        if picked == "S":
            verdict = "Skipped"
        elif picked == mcq_bank[idx]["correct"]:
            verdict = "Correct :)"
        else:
            verdict = "Incorrect  (Right Answer: " + mcq_bank[idx]["correct"] + ")"
        print("Q" + str(idx + 1) + " | Your Answer: " + picked + " => " + verdict)

def list_all_questions():
    for idx in range(len(mcq_bank)):
        item = mcq_bank[idx]
        print("\nQ" + str(idx + 1) + ". [" + item["topic"] + "] " + item["question"])
        print("  A)", item["opt1"],
              " B)", item["opt2"],
              " C)", item["opt3"],
              " D)", item["opt4"])
        print("  Answer:", item["correct"])

def insert_question():
    t   = input("Topic      : ")
    q   = input("Question   : ")
    a   = input("Option A   : ")
    b   = input("Option B   : ")
    c   = input("Option C   : ")
    d   = input("Option D   : ")
    key = input("Answer Key (A/B/C/D): ").strip().upper()
    if key in ["A", "B", "C", "D"]:
        mcq_bank.append({"topic": t, "question": q,
                         "opt1": a, "opt2": b, "opt3": c, "opt4": d,
                         "correct": key})
        print("Question successfully added.")
    else:
        print("Invalid key entered. Question was not added.")

def remove_question():
    if not mcq_bank:
        print("Question bank is empty.")
        return
    for idx in range(len(mcq_bank)):
        print(str(idx + 1) + ". [" + mcq_bank[idx]["topic"] + "] " + mcq_bank[idx]["question"])
    entry = input("Question number to remove: ")
    if entry.isdigit():
        pos = int(entry) - 1
        if 0 <= pos < len(mcq_bank):
            deleted = mcq_bank.pop(pos)
            print("Removed:", deleted["question"])
        else:
            print("Number out of valid range.")
    else:
        print("Please enter a numeric value.")


def bank_summary():
    print("Total MCQs in Bank:", len(mcq_bank))
    topic_tally = {}
    for item in mcq_bank:
        t = item["topic"]
        topic_tally[t] = topic_tally.get(t, 0) + 1
    for t in topic_tally:
        print(t + " :", topic_tally[t], "questions")

def show_all_records():
    if not student_records:
        print("No student records available.")
        return
    for rec in student_records:
        print("Name:", rec["name"],
              "| Roll:", rec["roll"],
              "| Score:", rec["score"],
              "| %:", rec["pct"],
              "| Grade:", rec["grade"])

def detailed_record():
    if not student_records:
        print("No records to display.")
        return
    for idx in range(len(student_records)):
        print(str(idx + 1) + ".", student_records[idx]["name"], "-", student_records[idx]["roll"])
    pick = input("Select student number: ")
    if pick.isdigit():
        pos = int(pick) - 1
        if 0 <= pos < len(student_records):
            rec = student_records[pos]
            print("Name:", rec["name"], "| Score:", rec["score"], "| Grade:", rec["grade"])
            for idx in range(len(mcq_bank)):
                picked = rec["answers"][idx]
                if picked == "S":
                    verdict = "Skipped"
                elif picked == mcq_bank[idx]["correct"]:
                    verdict = "Correct"
                else:
                    verdict = "Incorrect (Correct: " + mcq_bank[idx]["correct"] + ")"
                print("Q" + str(idx + 1) + " | " + picked + " => " + verdict)
        else:
            print("Invalid selection.")

def class_overview():
    if not student_records:
        print("No student data found.")
        return

    hi  = student_records[0]["score"]
    lo  = student_records[0]["score"]
    total_score = 0
    pass_count  = 0
    fail_count  = 0
    grade_tally = {}

    for rec in student_records:
        total_score += rec["score"]
        hi = rec["score"] if rec["score"] > hi else hi
        lo = rec["score"] if rec["score"] < lo else lo
        if rec["pct"] >= 50:
            pass_count += 1
        else:
            fail_count += 1
        g = rec["grade"]
        grade_tally[g] = grade_tally.get(g, 0) + 1

    avg_score = round(total_score / len(student_records), 1)

    print("Total Students :", len(student_records))
    print("Highest Score  :", hi)
    print("Lowest Score   :", lo)
    print("Average Score  :", avg_score)
    print("Passed:", pass_count, "| Failed:", fail_count)
    for g in grade_tally:
        print(g + ":", grade_tally[g])

def display_rules():
    print("Marking Scheme:")
    print("  Correct Answer  = +4 marks")
    print("  Wrong Answer    = -1 mark")
    print("  Skipped         =  0 marks")
    print("Grade Scale: 80%+ Excellent | 65%+ Good | 50%+ Average | Below 50 = Below Average")
    print("Tip: Type SUBMIT at any time to finish the test early.")

def conduct_exam(full_name, roll_no):
    right   = 0
    wrong   = 0
    skipped = 0
    answers = []
    quit_early = False

    for idx in range(len(mcq_bank)):
        if quit_early:
            answers.append("S")
            skipped += 1
            continue

        print_question(idx + 1, mcq_bank[idx])

        while True:
            response = input("Your Answer (A/B/C/D  |  S = Skip  |  SUBMIT = End Test): ").strip().upper()
            if response == "SUBMIT":
                quit_early = True
                answers.append("S")
                skipped += 1
                break
            elif response in ["A", "B", "C", "D"]:
                answers.append(response)
                if response == mcq_bank[idx]["correct"]:
                    right += 1
                    print("  Well done! Correct.")
                else:
                    wrong += 1
                    print("  Oops! That's incorrect.")
                break
            elif response == "S":
                answers.append("S")
                skipped += 1
                print("  Question skipped.")
                break
            else:
                print("  Invalid input. Please enter A, B, C, D, S, or SUBMIT.")

    total_score = (right * 4) + (wrong * -1)
    max_possible = len(mcq_bank) * 4
    percentage   = round((total_score / max_possible) * 100, 1)
    grade        = assign_grade(percentage)

    print("\n RESULT ")
    print("Name        :", full_name)
    print("Roll No     :", roll_no)
    print("Correct     :", right)
    print("Incorrect   :", wrong)
    print("Skipped     :", skipped)
    print("Score       :", total_score, "/", max_possible)
    print("Percentage  :", percentage, "%")
    print("Grade       :", grade)

    display_review(answers)

    student_records.append({
        "name"   : full_name,
        "roll"   : roll_no,
        "score"  : total_score,
        "max"    : max_possible,
        "pct"    : percentage,
        "grade"  : grade,
        "answers": answers
    })
    print("Your result has been saved.")

def admin_panel():
    if not verify_user("ecat_admin", "ecat@2024"):
        return

    while True:
        print("\n ADMIN PANEL ")
        print("1. View Question Bank")
        print("2. Add a Question")
        print("3. Remove a Question")
        print("4. Bank Statistics")
        print("5. View All Student Results")
        print("6. Detailed Student Result")
        print("7. Class Statistics")
        print("8. Logout")
        choice = input("Enter choice: ")

        if   choice == "1": list_all_questions()
        elif choice == "2": insert_question()
        elif choice == "3": remove_question()
        elif choice == "4": bank_summary()
        elif choice == "5": show_all_records()
        elif choice == "6": detailed_record()
        elif choice == "7": class_overview()
        elif choice == "8":
            print("Admin logged out.")
            break
        else:
            print("Invalid option. Try again.")


def student_panel():
    if not verify_user("student", "student123"):
        return

    full_name = input("Full Name    : ")
    roll_no   = input("Roll Number  : ")

    while True:
        print("\n STUDENT PANEL ")
        print("1. View Exam Rules")
        print("2. Start Exam")
        print("3. Logout")
        choice = input("Enter choice: ")

        if choice == "1":
            display_rules()
        elif choice == "2":
            conduct_exam(full_name, roll_no)
            break
        elif choice == "3":
            print("Student logged out.")
            break
        else:
            print("Invalid option. Try again.")

while True:
    print("   ECAT EXAMINATION SYSTEM   ")
    print("1. Admin Portal")
    print("2. Student Portal")
    print("3. Exit")
    main_choice = input("Select: ")

    if   main_choice == "1": admin_panel()
    elif main_choice == "2": student_panel()
    elif main_choice == "3":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid input. Please select 1, 2, or 3.")