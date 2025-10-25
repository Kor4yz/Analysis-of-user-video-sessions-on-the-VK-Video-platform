from __future__ import annotations
import argparse, os
import pandas as pd
from src.clean import clean_df
from src.features import build_features
from src.viz import save_all_figures

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--out", default="reports/img")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    df = pd.read_csv(args.input)
    df_clean = clean_df(df)                     
    feats = build_features(df_clean)
    imgs = save_all_figures(feats, args.out)

    # мини-summary для README
    with open(os.path.join(os.path.dirname(args.out), "summary.md"), "w", encoding="utf-8") as f:
        f.write(f"Всего записей после очистки: {len(df_clean)}\n")
        f.write("Сгенерированные картинки:\n" + "\n".join(f"- {os.path.basename(p)}" for p in imgs))

if __name__ == "__main__":
    main()
