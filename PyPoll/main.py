import csv
import os

total_votes = []
unique_candidates =[]
candidate = ""
candidate_votes = {}
winner=0
winning_candidate =""


file = os.path.join('..','PyPoll_Resources', 'PyPoll__data.csv')

with open(file) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        total_votes.append(row)
        candidate = row["Candidate"]

        

        if not candidate in unique_candidates:
            unique_candidates.append(candidate)
            
            candidate_votes[candidate]= 0

        candidate_votes[candidate] = candidate_votes[candidate] + 1    




    total_votes2= (len(total_votes))
#print(candidate_votes)


    answer = (

        f"\n Election Results \n"
        f"\n----------------------------------\n"
        f"\n Total Votes: {total_votes2} \n"
        f"\n----------------------------------\n"
        #f"\n {candidate_votes}\n"

)
    print(answer)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes2) * 100

        if (votes > winner):
            winner = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes}) \n"
        print(voter_output)

    winner_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"--------------------------\n"

    )


    print(winner_summary)


pypoll_results = "pypoll_results.txt"

with open(pypoll_results,"w") as txt_file:
    txt_file.write(answer)
    txt_file.write(voter_output)
    txt_file.write(winner_summary)
  




