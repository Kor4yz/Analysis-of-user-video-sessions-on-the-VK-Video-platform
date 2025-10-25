SELECT
  user_id,
  video_owner_id,
  video_id,
  vk_platform,
  nav_screen,
  total_view_time,
  event_ts
FROM analytics.vk_video_sessions
WHERE event_date BETWEEN CURRENT_DATE - INTERVAL '1 day' AND CURRENT_DATE;
