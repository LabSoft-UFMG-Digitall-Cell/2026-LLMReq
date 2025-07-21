-- Create the participants table
CREATE TABLE IF NOT EXISTS participants (
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

-- Load participants data
COPY participants FROM '/docker-entrypoint-initdb.d/participants.csv' DELIMITER ',' CSV HEADER;

-- Create the tasks table
CREATE TABLE IF NOT EXISTS tasks (
    code TEXT,
    task_id TEXT,
    llm TEXT,
    description TEXT,
    main_flow TEXT,
    alt_flow TEXT,
    time INT,
    grad_phd INT,
    note01 TEXT,
    note02 TEXT
);

-- Load tasks data
COPY tasks FROM '/docker-entrypoint-initdb.d/tasks.csv' DELIMITER ',' CSV HEADER;
