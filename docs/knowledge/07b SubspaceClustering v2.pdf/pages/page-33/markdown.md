# Approaches

- Greedy iterative searches
- iteratively add/remove rows and columns to maximize a merit function
- e.g. CC minimize mean square residue (MSR) until reaching MSR &lt; δ
- Row and column clustering combination (e.g. CTWC, ITWC)
- apply clustering on rows and columns separately
- use an iterative procedure to combine the two clustering results
- Divide and conquer searches
- break the matrix into submatrices (e.g. find best row or column split)
- continue the biclustering process on the new submatrices
- Distribution parameter identification (e.g. plaid)
- use mixture to describe biclustering solution and learn its parameters (maximize likelihood)

TÉCNICO+ FORMACÃO AVANÇADA