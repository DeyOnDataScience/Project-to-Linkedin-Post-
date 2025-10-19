from save_to_notion import save_to_notion
from post_generator import code_based_generate_post,query_based_generate_post


if __name__ == "__main__":
    #for project or code

    #for any user query
    query_based_generate_post("LLM Over Traditional Machine Learning Approach")
    #for saving to notion
    user = str(input("Press 1 for Code Analysis Post.\nPress 2 for simple Query Post.\nAnd any other key to exit:\t"))
    if user == "1":
        try:
            user1 = str(input("Enter The Repo URL or system Path."))
            content = code_based_generate_post(user1)
            print("Press S to Save it to your Notion DB\nPress any other key to skip.")
            user2 = str(input("Enter Here\t"))
            if user2.lower() == "s":
                save_to_notion(content,user1)
        except Exception as e:
            print(f"Error Occured: {e}")
    elif user == "2":
        try:
            user1 = str(input("Enter Your Query."))
            content = query_based_generate_post(user1)
            print("Press S to Save it to your Notion DB\nPress any other key to skip.")
            user1 = str(input("Enter Here\t"))
            if user1.lower() == "s":
                save_to_notion(content,user1)
        except Exception as e:
            print(f"Error Occured: {e}")