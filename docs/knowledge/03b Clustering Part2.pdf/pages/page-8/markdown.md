# Distances for mixed data

- First concern: two non-identically distributed variables – e.g. $Y_{1} \sim U(0,1)$ and $Y_{2} \sim U(0,100)$
- Problem? In the given example, distances are most affected by variable $Y_{2}$
- yet why should this variable have higher weight than $Y_{1}$!
- Possible solution? Normalize variables
- in the given example, $Y_{2} \sim U'(0,1)$ using for instance min-max scaling
- Second concern: how to deal with simultaneous categoric and numeric variables?
- distance can be a composition: $d(\mathbf{x}_1, \mathbf{x}_2) = \alpha d_{\text{numeric}}(\mathbf{x}_1, \mathbf{x}_2) + \beta d_{\text{categoric}}(\mathbf{x}_1, \mathbf{x}_2)$ where $\alpha$ and $\beta$ are parameters that reveal the relevance of each component, generally $\alpha + \beta = 1$
- parameters can be fixed based on the number of variables or available domain knowledge

TÉCNICO+ FORMAÇÃO AVANÇADA