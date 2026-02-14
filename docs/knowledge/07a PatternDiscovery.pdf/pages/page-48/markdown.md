# Constrained pattern mining

- Domain-driven constraints:
- user flexibility: provides constraints on what to be mined
- system optimization: explores such constraints for efficient mining. How? Below

- Pattern space pruning constraints
- anti-monotonic: if constraint $c$ is violated, its further mining can be terminated
- monotonic: if $c$ is satisfied, no need to check $c$ again
- succinct: $c$ must be satisfied, so one can start with the data sets satisfying $c$
- convertible: $c$ can be mapped into (anti-)monotonic $c$ when values are properly ordered

- Data space pruning constraints
- data succinct: data space can be pruned at the initial pattern mining process
- data anti-monotonic: if an observation does not satisfy $c$, it can be pruned

TÉCNICO+ FORMACÃO AVANÇADA