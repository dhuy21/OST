import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <question>")
        print("  1   ->  Question 1")
        print("  2   ->  Question 2")
        print("  3   ->  Question 3")
        print("  p2  ->  Partie 2")
        return

    q = sys.argv[1]

    if q == "1":
        from question1 import run_question1
        run_question1()
    elif q == "2":
        from question2 import run_question2
        run_question2()
    elif q == "3":
        from question3 import run_question3
        run_question3()
    elif q == "p2":
        from partie2 import run_partie2
        run_partie2()
    else:
        print(f"Question inconnue : {q}")


if __name__ == "__main__":
    main()
