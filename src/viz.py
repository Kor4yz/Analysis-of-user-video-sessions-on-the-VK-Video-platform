from __future__ import annotations
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def _save(fig, outdir, name):
    os.makedirs(outdir, exist_ok=True)
    p = os.path.join(outdir, f"{name}.png")
    fig.savefig(p, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return p

def plot_platform(feats: dict, outdir: str):
    df = feats["by_platform"]
    fig = plt.figure(figsize=(6,4))
    ax = sns.barplot(data=df.melt(id_vars="vk_platform", value_vars=["median","mean"]),
                     x="vk_platform", y="value", hue="variable")
    ax.set_title("Среднее vs медиана по платформам")
    ax.set_xlabel("Платформа"); ax.set_ylabel("сек")
    return _save(fig, outdir, "platform_mean_median")

def plot_nav(feats: dict, outdir: str):
    df = feats["by_nav"].head(8)
    fig = plt.figure(figsize=(7,4))
    ax = sns.barplot(data=df, y="nav_screen", x="count")
    ax.set_title("Распределение просмотров по источникам")
    ax.set_xlabel("кол-во"); ax.set_ylabel("источник")
    return _save(fig, outdir, "nav_counts")

def plot_nav_mean(feats: dict, outdir: str):
    df = feats["by_nav"].head(8)
    fig = plt.figure(figsize=(7,4))
    ax = sns.barplot(data=df, y="nav_screen", x="mean")
    ax.set_title("Среднее время просмотра по источникам")
    ax.set_xlabel("сек"); ax.set_ylabel("источник")
    return _save(fig, outdir, "nav_mean")

def plot_top_owners(feats: dict, outdir: str):
    df = feats["top_owners"]
    fig = plt.figure(figsize=(7,5))
    ax = sns.barplot(data=df, y="video_owner_id", x="total_view_time")
    ax.set_title("Топ-10 сообществ по суммарному времени")
    ax.set_xlabel("сек"); ax.set_ylabel("owner_id")
    return _save(fig, outdir, "owners_top10")

def plot_top_videos(feats: dict, outdir: str):
    a = feats["top_videos_sum"]; b = feats["top_videos_mean"]
    fig1 = plt.figure(figsize=(7,5))
    ax1 = sns.barplot(data=a, y="video_id", x="total_view_time")
    ax1.set_title("Топ-10 видео по суммарному времени"); ax1.set_xlabel("сек")
    p1 = _save(fig1, outdir, "videos_top10_sum")
    fig2 = plt.figure(figsize=(7,5))
    ax2 = sns.barplot(data=b, y="video_id", x="mean")
    ax2.set_title("Топ-10 видео по среднему времени (count>=5)"); ax2.set_xlabel("сек")
    p2 = _save(fig2, outdir, "videos_top10_mean")
    return [p1,p2]

def save_all_figures(feats: dict, outdir: str):
    paths = []
    paths += [plot_platform(feats, outdir)]
    paths += [plot_nav(feats, outdir), plot_nav_mean(feats, outdir)]
    paths += [plot_top_owners(feats, outdir)]
    paths += plot_top_videos(feats, outdir)
    return paths
