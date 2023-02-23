# 1.ZKP for 3-coloring Demo

<strong>Exercise 1</strong>: Currently, you can only select adjacent pairs of nodes to check. Would the proof still be zero knowledge if you could pick arbitrary pairs of nodes to check?

<Strong>A</Strong>:

No. If a validator can pick more than one node pairs, he/she may learn some "knowledge" about how the graph is parially colored.

<Strong>Exercise 2</strong>: The equation currently being used for confidence is 1-(1/E)^n, where E is the number of edges in the graph, and n is the number of trials run. Is this the correct equation? Why is there no prior?

<Strong>A</Strong>:

No. Confidence should be less than 1 - (1 - 1 / E) ^ n.

<br>

# 2. ZKP for DLOG

zkp_dlog.py & zkp_dlog_fiat_shamir.py

<br>

# 3. zkmessage.xyz

<strong>Exercise 1</strong>: Explain why you need to generate and save a “secret” value.

<Strong>A</Strong>:

<strong>Exercise 2</strong>: Write out a plain-English explanation of what statement is being proven in ZK.

<Strong>A</Strong>:

<strong>Exercise 2</strong>: Log into the same zkmessage account, from a different browser or computer. Explain why zkmessage can’t just use a simple “username/password” system like most social apps.

<Strong>A</Strong>:
