-- Datei: schema.sql

CREATE TABLE IF NOT EXISTS vendor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    vendor_id INTEGER NOT NULL,
    FOREIGN KEY (vendor_id) REFERENCES vendor(id)
);

CREATE TABLE IF NOT EXISTS cve (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id TEXT NOT NULL UNIQUE,
    description TEXT,
    published_date TEXT,
    severity TEXT CHECK(severity IN ('Low', 'Medium', 'High', 'Critical')),
    status TEXT CHECK(status IN ('New', 'Patched', 'Investigating'))
);

CREATE TABLE IF NOT EXISTS cve_product (
    cve_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    PRIMARY KEY (cve_id, product_id),
    FOREIGN KEY (cve_id) REFERENCES cve(id),
    FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE IF NOT EXISTS reference (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    FOREIGN KEY (cve_id) REFERENCES cve(id)
);
