import os

def load_legal_knowledge(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
        return None

def search_for_answer(legal_knowledge, question):
    if legal_knowledge is None:
        return "Legal knowledge file not found."
    
    found_question = False
    for line in legal_knowledge:
        if found_question:
            return line.strip()
        if question.lower() in line.lower():
            found_question = True
    return "Sorry, answer not found."

def main():
    print("Welcome to Text Search App!")

    legal_knowledge = load_legal_knowledge("Legal_knowledge.txt")
    
    if legal_knowledge is None:
        return
    
    while True:
        question = input("Enter your question (or 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Thank you for using Text Search App. Goodbye!")
            return

        answer = search_for_answer(legal_knowledge, question)
        print(answer)

if __name__ == "__main__":
    main()
