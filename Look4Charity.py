# introduce the tool with text:
# Hi, welcome to Look4Charity, the 100% private
# Google search that works with plain English prompts
# and answers based on live Google searches.

quit = False
print("Hi, welcome to Look4Charity, the 100% private Google search that works with plain English prompts and answers based on live Google searches.")

while(quit != True):
    # ask the user to ask their question
    search = input("Search prompt here, or if you would like to exit, type quit: ").upper()
    # mock data response to question
    answer1 = "42 is the meaning of life"
    answer2 = "Grian's Hermitcraft Season 9 mega base is known as Dwane"
    answer3 = "Jimmy is not a toy"
    if search.count("HERMITCRAFT") > 0:
        print(answer2)
    elif search.count("LIFE") > 0:
        print(answer1)
    elif search.count("TOY") > 0 or search.count("JIMMY") > 0:
        print(answer3)
    # loop until user types 'quit' then exit
    elif search == 'QUIT':
        quit = True
    else:
        print("Please try again")