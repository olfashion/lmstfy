BEGIN;

CREATE TABLE short_link (
    transaction_id VARCHAR(255) PRIMARY KEY,
    target_url TEXT,
    request_time TIMESTAMP DEFAULT NOW(),
    requesters_ip VARCHAR(255),
    requesters_broswer VARCHAR(255),
    requesters_device VARCHAR(255)
);

COMMIT;
