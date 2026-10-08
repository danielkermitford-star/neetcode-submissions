# https://neetcode.io/problems/accounts-merge/question?list=neetcode150
from collections import deque
from typing import List


class Solution:
    # up to 1000 accounts with up to 10 emails each for a total of
    # up to 10,000 emails. Looking for matches could involve 5,000 emails
    # that each occur twice or 5,000 * 10,000 = up to 50,000,000 possible.
    # So it might be small enough for exhaustive search except these are
    # strings with up to 30 characters so up to 30 * 50 million characters
    # to compare or 1.5 billion character comparisons.

    # Much quicker to create a graph with edges between the first email
    # and each of the others. Resulting in a tree with at most 10,000
    # vertices and edges.

    # Otherwise you could use the Union-Find Algorithm, or create hash
    # sets of emails in the same account always extending the larger one
    # by the smaller one (like with the Union-Find Algorithm.)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = set()
        neighbor_of = {}
        name_of = {}
        for name, first_email, *other_emails in accounts:
            emails.add(first_email)
            name_of[first_email] = name
            for email in other_emails:
                emails.add(email)
                name_of[email] = name
                neighbor_of.setdefault(email, []).append(first_email)
                neighbor_of.setdefault(first_email, []).append(email)

        # print(name_of)
        # print(neighbor_of)
        # print(emails)

        new_accounts = []
        while emails:
            # email = next(iter(emails))  # gets an element from emails without removing it
            email = emails.pop()
            account = [email]
            queue = deque([email])
            while queue:
                email = queue.popleft() # email already removed from emails
                for email2 in neighbor_of.setdefault(email, []):
                    if email2 in emails:
                        emails.remove(email2)
                        queue.append(email2)
                        account.append(email2)
            new_accounts.append([name_of[email]] + sorted(account))
        return new_accounts


accounts = [
    ["neet","neet@gmail.com","neet_dsa@gmail.com"],
    ["alice","alice@gmail.com"],
    ["neet","bob@gmail.com","neet@gmail.com"],
    ["neet","neetcode@gmail.com"]
]
print(Solution().accountsMerge(accounts))


