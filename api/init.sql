-- Create participants table
CREATE TABLE participants (
    code VARCHAR PRIMARY KEY,
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

-- Create tasks table
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    code VARCHAR,
    task_id TEXT,
    llm TEXT,
    description TEXT,
    main_flow TEXT,
    alt_flow TEXT,
    time INTEGER,
    grad_phd INTEGER,
    note01 TEXT,
    note02 TEXT,
    FOREIGN KEY (code) REFERENCES participants(code)
);
