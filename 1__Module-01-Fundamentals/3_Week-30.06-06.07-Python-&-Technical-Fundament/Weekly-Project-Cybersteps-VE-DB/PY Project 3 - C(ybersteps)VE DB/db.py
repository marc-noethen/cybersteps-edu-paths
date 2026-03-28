# Datei: db.py
import sqlite3

DB_NAME = "cvedb.sqlite"

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    with open("schema.sql", "r") as f:
        schema = f.read()
    conn = connect()
    conn.executescript(schema)
    conn.commit()
    conn.close()

def insert_vendor(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO vendor (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def insert_product(name, vendor_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM vendor WHERE name = ?", (vendor_name,))
    vendor = cur.fetchone()
    if vendor:
        vendor_id = vendor[0]
        cur.execute("INSERT INTO product (name, vendor_id) VALUES (?, ?)", (name, vendor_id))
        conn.commit()
    conn.close()

def insert_cve(cve_id, description, published_date, severity, status="New"):
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO cve (cve_id, description, published_date, severity, status) VALUES (?, ?, ?, ?, ?)",
            (cve_id, description, published_date, severity, status)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"⚠️ CVE {cve_id} bereits vorhanden.")
    conn.close()


def link_cve_to_product(cve_id, product_name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id FROM cve WHERE cve_id = ?", (cve_id,))
    cve = cur.fetchone()
    cur.execute("SELECT id FROM product WHERE name = ?", (product_name,))
    product = cur.fetchone()
    if cve and product:
        cur.execute("INSERT OR IGNORE INTO cve_product (cve_id, product_id) VALUES (?, ?)", (cve[0], product[0]))
        conn.commit()
    conn.close()


def search_cves(keyword=None, severity=None, date_range=None):
    conn = connect()
    cur = conn.cursor()

    query = "SELECT cve_id, description, published_date, severity, status FROM cve WHERE 1=1"
    params = []

    if keyword:
        query += " AND description LIKE ?"
        params.append(f"%{keyword}%")
    if severity:
        query += " AND severity = ?"
        params.append(severity)
    if date_range:
        start, end = date_range
        query += " AND published_date BETWEEN ? AND ?"
        params.extend([start, end])

    cur.execute(query, params)
    results = cur.fetchall()
    conn.close()
    return results

def update_cve_status(cve_id, new_status):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE cve SET status = ? WHERE cve_id = ?", (new_status, cve_id))
    conn.commit()
    conn.close()

import csv
import json

def export_cves_to_csv(filename="export.csv"):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cve")
    rows = cur.fetchall()
    conn.close()

    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["cve_id", "description", "published_date", "severity", "status"])
        writer.writerows(rows)

def export_cves_to_json(filename="export.json"):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cve")
    rows = cur.fetchall()
    conn.close()

    data = [
        {
            "cve_id": row[0],
            "description": row[1],
            "published_date": row[2],
            "severity": row[3],
            "status": row[4],
        }
        for row in rows
    ]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

from datetime import datetime

def get_cve_stats():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM cve")
    total = cur.fetchone()[0]

    cur.execute("SELECT severity, COUNT(*) FROM cve GROUP BY severity")
    by_severity = cur.fetchall()

    current_month = datetime.now().strftime("%Y-%m")
    cur.execute("SELECT COUNT(*) FROM cve WHERE strftime('%Y-%m', published_date) = ?", (current_month,))
    this_month = cur.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "by_severity": dict(by_severity),
        "this_month": this_month,
    }

def get_statistics():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM cve")
    total = cur.fetchone()[0]

    def count_by_sev(sev):
        cur.execute("SELECT COUNT(*) FROM cve WHERE severity = ?", (sev,))
        return cur.fetchone()[0]

    stats = {
        "total": total,
        "critical": count_by_sev("CRITICAL"),
        "high": count_by_sev("HIGH"),
        "medium": count_by_sev("MEDIUM"),
        "low": count_by_sev("LOW"),
    }
    conn.close()
    return stats

