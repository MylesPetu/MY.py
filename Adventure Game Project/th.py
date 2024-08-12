def display_candidates(candidates):
    print("\nCandidates:")
    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate}")


def get_vote(candidates):
    while True:
        try:
            vote = int(input("Enter the number of the candidate you want to vote for: "))
            if 1 <= vote <= len(candidates):
                return vote - 1
            else:
                print("Invalid number. Please choose a valid candidate number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def register_voter():
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0:
                break
            else:
                print("Age cannot be negative. Please enter a valid age.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")
    if age == 17:
        print(f"Sorry, {name}. You are not eligible for voting;Could you come back next year")
    elif age < 18:
        print(f"Sorry, {name}. You must be at least 18 years old to vote. You cannot vote.")

        return None, None
    else:
        return name, age


def main():
    candidates = ["APC: Bola Ahmed Tinubu", "PDP: Atiku Abubakar", "LP: Peter Obi", "LMU: Diana Idris David"]
    votes = [0] * len(candidates)

    print("Welcome to the voting system!")
    num_voters = int(input("Enter the number of voters: "))

    for _ in range(num_voters):
        name, age = register_voter()
        if name is None:  # If the voter is under 18, skip to the next voter
            continue

        print(f"Thank you for registering, {name}!")
        display_candidates(candidates)
        vote = get_vote(candidates)
        votes[vote] += 1
        print("Thank you for voting!\n")

    print("Voting is complete. Here are the results:")
    for candidate, vote_count in zip(candidates, votes):
        print(f"{candidate}: {vote_count} votes")

    winner = candidates[votes.index(max(votes))]
    print(f"The winner is {winner}!")


if __name__ == "__main__":
    main()