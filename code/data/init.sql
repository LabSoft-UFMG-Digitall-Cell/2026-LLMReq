DROP TABLE IF EXISTS participants;

CREATE TABLE participants (
    code TEXT,
    institution TEXT,
    prog_oo TEXT,
    soft_arch TEXT,
    web_tech TEXT,
    db_systems TEXT,
    sw_project_mgmt TEXT,
    requirements TEXT,
    agile_methods TEXT,
    llm_usage TEXT,
    experience TEXT
);

COPY participants
FROM '/docker-entrypoint-initdb.d/participants.csv'
WITH (FORMAT csv, HEADER);

DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    code TEXT,
    "group" TEXT,
    task_id TEXT,
    llm TEXT,
    description TEXT,
    main_flow TEXT,
    alt_flow TEXT,
    time INT,
    grad_phd_01 INT,
    grad_phd_02 INT,
    grad_mean FLOAT
);

COPY tasks
FROM '/docker-entrypoint-initdb.d/tasks.csv'
WITH (FORMAT csv, HEADER);
