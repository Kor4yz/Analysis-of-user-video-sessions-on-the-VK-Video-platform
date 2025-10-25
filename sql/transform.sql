SELECT nav_screen,
       COUNT(*) AS sessions,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY total_view_time) AS median_view_time,
       AVG(total_view_time) AS mean_view_time
FROM analytics.vk_video_sessions
WHERE total_view_time > 0
GROUP BY nav_screen
ORDER BY sessions DESC
LIMIT 20;
