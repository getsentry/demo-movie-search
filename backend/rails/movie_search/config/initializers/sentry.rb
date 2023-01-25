Sentry.init do |config|
    config.dsn = 'https://39e168307a0d4c3a8f03cc7d6e5ff58b@o447951.ingest.sentry.io/4504560949198848'
    config.breadcrumbs_logger = [:active_support_logger, :http_logger]
  
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    config.traces_sample_rate = 1.0
  end