CREATE EVENT IF NOT EXISTS run_reopen_failed_tasks
ON SCHEDULE EVERY {DB_SETUP_RUN_REOPEN_FAILED_TASK_INTERVAL} SECOND
DO CALL reopen_failed_tasks();
