# Nonlinear PCA using kernels

- Traditional PCA applies linear transformation (ineffective for nonlinear data)
- Solution: apply nonlinear transformation to potentially higher-dimensional spaces

$$
\varphi \colon \mathbf {x} \to \varphi (\mathbf {x})
$$

- how? apply the kernel trick: PCA rewritten in terms of dot product

$$
K (\mathbf {x} _ {i}, \mathbf {x} _ {j}) = \varphi (\mathbf {x} _ {i}) \bullet \varphi (\mathbf {x} _ {j})
$$

- Example

$$
\varphi \colon (a _ {i 1}, a _ {i 2}, a _ {i 3}) \to (a _ {i 1}, \sqrt {a _ {i 2} a _ {i 3}}, a _ {i 1} ^ {2} a _ {i 3})
$$

simplified: transform $A = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ accordingly and apply PCA

$$
\mathbf {x} _ {i} = (2, 4, 1) \rightarrow (2, 2, 4)
$$