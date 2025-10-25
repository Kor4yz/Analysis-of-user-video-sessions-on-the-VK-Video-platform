from __future__ import annotations
import pandas as pd

def build_features(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    feats = {}
    feats["by_platform"] = (
        df.groupby("vk_platform")["total_view_time"]
          .agg(median="median", mean="mean", count="count")
          .reset_index()
    )
    feats["by_nav"] = (
        df.groupby("nav_screen")["total_view_time"]
          .agg(median="median", mean="mean", count="count")
          .reset_index()
          .sort_values("count", ascending=False)
    )
    feats["top_owners"] = (
        df.groupby("video_owner_id")["total_view_time"]
          .sum().sort_values(ascending=False).head(10).reset_index()
    )
    feats["top_videos_sum"] = (
        df.groupby("video_id")["total_view_time"]
          .sum().sort_values(ascending=False).head(10).reset_index()
    )
    video_views = df.groupby("video_id")["total_view_time"].agg(count="count", mean="mean").reset_index()
    feats["top_videos_mean"] = (
        video_views[video_views["count"] >= 5]     # порог устойчивости
        .sort_values("mean", ascending=False)
        .head(10)
        .reset_index(drop=True)
    )
    return feats
