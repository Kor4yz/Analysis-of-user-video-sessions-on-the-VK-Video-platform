from __future__ import annotations
import pandas as pd

def clean_df(df: pd.DataFrame, perc: float = 0.99) -> pd.DataFrame:
    # фильтруем пустые/нулевые просмотры
    df_pos = df[df["total_view_time"] > 0].copy()
    ub = df_pos["total_view_time"].quantile(perc)
    df_pos = df_pos[df_pos["total_view_time"] <= ub].copy()
    # нормализуем типы
    for col in ("user_id", "video_owner_id", "video_id"):
        if col in df_pos.columns:
            df_pos[col] = df_pos[col].astype(str)
    return df_pos
