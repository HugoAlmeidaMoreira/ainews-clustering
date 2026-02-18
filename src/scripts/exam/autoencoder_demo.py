import argparse
from pathlib import Path

import numpy as np


def _parse_vector(raw: str) -> np.ndarray:
    vals = [float(v.strip()) for v in raw.split(",") if v.strip()]
    return np.array(vals, dtype=float)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Standalone demo para questão de autoencoder linear (sem dependências do exam_tool)."
    )
    parser.add_argument("--x", default="1,2", help="Vetor de input x (default: 1,2)")
    parser.add_argument(
        "--w1",
        default="0.5,0.5",
        help="Pesos do encoder W1 (1xd), ex: 0.5,0.5",
    )
    parser.add_argument(
        "--w2",
        default="1,1",
        help="Pesos do decoder W2 (dx1), ex: 1,1",
    )
    parser.add_argument("--out", default=None, help="Saída markdown opcional")
    args = parser.parse_args()

    x = _parse_vector(args.x)
    w1 = _parse_vector(args.w1)
    w2 = _parse_vector(args.w2)

    if x.shape[0] != 2:
        raise ValueError("Este demo está preparado para x bivariado (2 dimensões).")
    if w1.shape[0] != x.shape[0] or w2.shape[0] != x.shape[0]:
        raise ValueError("Dimensões incompatíveis: para x 2D, use w1 e w2 com 2 valores.")

    z = float(np.dot(w1, x))
    x_hat = w2 * z
    mae = float(np.mean(np.abs(x - x_hat)))

    a_true = np.isclose(mae, 0.5, atol=1e-9)
    b_true = False
    c_true = False
    d_true = True
    e_true = np.allclose(x_hat, np.array([1.5, 1.5]), atol=1e-9)

    lines = [
        "# Demo da Questão (Autoencoder Linear)",
        "",
        f"- x = {x.tolist()}",
        f"- W1 = {w1.tolist()} (encoder 1x2)",
        f"- W2 = {w2.tolist()} (decoder 2x1)",
        "",
        "## Cálculos",
        "",
        f"- Embedding z = W1·x = {w1[0]}*{x[0]} + {w1[1]}*{x[1]} = {z:.4f}",
        f"- Reconstrução x_hat = W2*z = {x_hat.tolist()}",
        f"- MAE = mean(|x - x_hat|) = {mae:.4f}",
        "",
        "## Avaliação das opções",
        "",
        f"- a) MAE da reconstrução é 0.5: {'TRUE' if a_true else 'FALSE'}",
        f"- b) embedding de x é (0.5,1): {'TRUE' if b_true else 'FALSE'}",
        f"- c) bom embedding maximiza dependência entre features latentes: {'TRUE' if c_true else 'FALSE'}",
        f"- d) uma rede pode combinar autoencoding e supervised learning para embeddings numéricos: {'TRUE' if d_true else 'FALSE'}",
        f"- e) reconstrução de x é (1.5,1.5): {'TRUE' if e_true else 'FALSE'}",
        "",
    ]

    report = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(report, encoding="utf-8")
        print(f"Relatório gravado em: {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
