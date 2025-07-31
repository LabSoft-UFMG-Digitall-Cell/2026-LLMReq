DROP TABLE IF EXISTS participants;

CREATE TABLE participants (
    code TEXT,
    institution TEXT,
    course TEXT,
    prog_oo TEXT,
    soft_arch TEXT,
    web_tech TEXT,
    db_systems TEXT,
    sw_project_mgmt TEXT,
    requirements TEXT,
    agile_methods TEXT,
    llm_usage TEXT,
    experience TEXT,
    positive_llm TEXT,
    negative_llm TEXT,
    positive_nollm TEXT,
    negative_nollm TEXT,
    example_positive TEXT,
    example_negative TEXT,
    llm_influence TEXT,
    general TEXT,
    link TEXT
);

COPY participants
FROM '/data/participants.csv'
WITH (
    FORMAT csv,
    HEADER,
    DELIMITER ',',
    QUOTE '"'
);

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
    note01 TEXT,
    grad_phd_02 INT,
    note02 TEXT,
    grad_mean FLOAT,
    grad_llm FLOAT,
    note_llm TEXT
);

COPY tasks
FROM '/data/tasks.csv'
WITH (
    FORMAT csv,
    HEADER,
    DELIMITER ',',
    QUOTE '"'
);
