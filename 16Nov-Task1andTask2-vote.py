#Task 1 and Task 2
votesForMary=0
votesForRobert=0
votesForNathan=0
votesForJoseph=0

for i in range(1,11):
    print("Please enter your choice vote for the below candidates:")
    print("Type 1 for Mary")
    print("Type 2 for Robert")
    print("Type 3 for Nathan")
    print("Type 4 for Joseph")

    choice=int(input("Please enter your choice"))
    if choice ==1:
        print("You voted for Mary")
        votesForMary=votesForMary+1
    elif choice==2:
        print("You voted for Robert")
        votesForRobert=votesForRobert+1
    elif choice==3:
        print("You voted for Nathan")
        votesForNathan=votesForNathan+1
    elif choice==4:
        print("You voted for Joseph")
        votesForJoseph=votesForJoseph+1
    else:
        print("Please enter only 1 or 2 or 3 or 4 for choice")
print("Total votes for Mary: " +str(votesForMary))
print("Total votes for Robert: " +str(votesForRobert))
print("Total votes for Nathan: " +str(votesForNathan))
print("Total votes for Joseph: " +str(votesForJoseph))
