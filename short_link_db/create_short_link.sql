BEGIN;

CREATE TABLE url_links (
    transaction_id VARCHAR(255) PRIMARY KEY,
    target_url TEXT,
    request_time TIMESTAMP DEFAULT NOW(),
    requesters_ip VARCHAR(255),
    requesters_broswer VARCHAR(255),
    requesters_device VARCHAR(255),
    short_url VARCHAR(255)
);


CREATE TABLE provisioning (
    provision VARCHAR(255) PRIMARY KEY,
    is_used INT,
    used_time TIMESTAMP
);

COMMIT;
