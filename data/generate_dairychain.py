#!/usr/bin/env python3
"""DairyChain synthetic data generator: 10 core CSV tables, deterministic seed."""
from __future__ import annotations
import json, time, zipfile, hashlib
from datetime import datetime
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
VERSION = "2.1.1-generated"
ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw"
MANIFEST_DIR = ROOT / "data" / "manifests"
SIM_START = pd.Timestamp("2025-11-01 00:00:00")
SIM_DAYS = 365
DENSITY_KG_PER_L = 1.03


def write_csv(df: pd.DataFrame, rel: str) -> Path:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")
    return path


def generate_master(rng):
    districts = [
        ("Anand", "Gujarat"), ("Mehsana", "Gujarat"), ("Banaskantha", "Gujarat"),
        ("Sabarkantha", "Gujarat"), ("Kheda", "Gujarat"), ("Rajkot", "Gujarat"),
        ("Karnal", "Haryana"), ("Hisar", "Haryana"), ("Ludhiana", "Punjab"),
        ("Kolhapur", "Maharashtra"), ("Pune", "Maharashtra"), ("Satara", "Maharashtra"),
        ("Kolar", "Karnataka"), ("Mandya", "Karnataka"), ("Mysuru", "Karnataka"),
    ]
    villages = ["Ode", "Boriavi", "Karamsad", "Valasan", "Bakrol", "Navli", "Vadtal", "Kanjari", "Chaklasi", "Adas", "Vasad", "Sarsa", "Bhalaj", "Umreth", "Thamna", "Lingda", "Pansora", "Finav", "Dharmaj", "Tarapur"]
    first = ["Ramesh", "Suresh", "Mahesh", "Dinesh", "Prakash", "Kiran", "Vijay", "Rajesh", "Harish", "Nitin", "Ganesh", "Vikram", "Anil", "Sunil", "Ashok"]
    last = ["Patel", "Chaudhary", "Desai", "Sharma", "Verma", "Pawar", "Jadhav", "Reddy", "Gowda", "Singh", "Thakor", "Solanki", "Parmar", "Rathod", "Rabari"]
    cc = []
    for i in range(1, 21):
        district, state = districts[(i - 1) % len(districts)]
        village = villages[(i - 1) % len(villages)]
        cc.append({
            "collection_centre_id": f"CC-{i:03d}", "centre_name": f"{village} Milk Collection Centre",
            "village": village, "district": district, "state": state,
            "operating_capacity_litres": int(rng.choice([3000, 5000, 8000, 10000])),
            "opening_time": "05:30:00", "closing_time": "20:30:00", "status": "Active",
        })
    df_cc = pd.DataFrame(cc)

    types = ["Individual Farmer", "Dairy Cooperative Society", "Private Dairy Farm", "Bulk Milk Cooler Group"]
    suppliers = []
    for i in range(1, 201):
        district, state = districts[(i - 1) % len(districts)]
        village = villages[(i - 1) % len(villages)]
        status = "Active" if rng.random() > 0.05 else "Inactive"
        if i == 15:
            status = "active"  # DQ-01: inconsistent status casing
        if i == 42:
            village = f" {village} "  # DQ-02: leading/trailing whitespace
        reg_days = int(rng.integers(30, 1800))
        suppliers.append({
            "supplier_id": f"SUP-{i:04d}", "supplier_name": f"{rng.choice(first)} {rng.choice(last)} Dairy",
            "village": village, "district": district, "state": state,
            "supplier_type": rng.choice(types, p=[0.65, 0.20, 0.10, 0.05]),
            "registration_date": (SIM_START - pd.Timedelta(days=reg_days)).strftime("%Y-%m-%d"),
            "status": status, "contact_reference": f"SYNTH-REF-SUP-{i:04d}",
        })
    df_sup = pd.DataFrame(suppliers)

    product_specs = [
        ("PRD-001", "Full Cream Milk", "Liquid Milk", "Litre", "1.0 L Pouch", 2, 66.0),
        ("PRD-002", "Toned Milk", "Liquid Milk", "Litre", "0.5 L Pouch", 2, 54.0),
        ("PRD-003", "Double Toned Milk", "Liquid Milk", "Litre", "0.5 L Pouch", 2, 48.0),
        ("PRD-004", "Standardised Milk", "Liquid Milk", "Litre", "1.0 L Pouch", 2, 60.0),
        ("PRD-005", "Classic Set Curd", "Fermented", "Kilogram", "0.4 kg Cup", 7, 75.0),
        ("PRD-006", "Fresh Malai Paneer", "Coagulated", "Kilogram", "0.2 kg Pack", 15, 380.0),
        ("PRD-007", "Pure Cow & Buffalo Ghee", "Fat Rich", "Litre", "1.0 L Jar", 270, 620.0),
        ("PRD-008", "Pasteurised Table Butter", "Fat Rich", "Kilogram", "0.5 kg Carton", 180, 520.0),
        ("PRD-009", "Fresh Dairy Cream", "Fat Rich", "Litre", "0.2 L Pack", 10, 220.0),
        ("PRD-010", "Spiced Masala Buttermilk", "Beverage", "Litre", "0.2 L Pouch", 5, 30.0),
        ("PRD-011", "Elaichi Flavoured Milk", "Beverage", "Litre", "0.2 L Bottle", 90, 125.0),
        ("PRD-012", "Probiotic Lassi", "Fermented", "Litre", "0.25 L Cup", 10, 80.0),
    ]
    df_products = pd.DataFrame(product_specs, columns=["product_id", "product_name", "category", "unit_of_measure", "standard_pack_size", "shelf_life_days", "selling_price"])
    df_products["active_status"] = "Active"
    write_csv(df_sup, "data/raw/master/suppliers.csv")
    write_csv(df_cc, "data/raw/master/collection_centres.csv")
    write_csv(df_products, "data/raw/master/products.csv")
    return df_sup, df_cc, df_products


def generate_procurement_quality(rng, df_sup, df_cc, n_proc=18_000):
    sup_ids = df_sup.supplier_id.to_numpy()
    cc_ids = df_cc.collection_centre_id.to_numpy()
    sup_to_cc = {s: cc_ids[i % len(cc_ids)] for i, s in enumerate(sup_ids)}
    day = rng.integers(0, SIM_DAYS, size=n_proc)
    shifts = rng.choice(["Morning", "Evening"], size=n_proc, p=[0.55, 0.45])
    hour = np.where(shifts == "Morning", rng.integers(5, 10, size=n_proc), rng.integers(16, 21, size=n_proc))
    minute = rng.integers(0, 60, size=n_proc)
    second = rng.integers(0, 60, size=n_proc)
    raw_ts = SIM_START + pd.to_timedelta(day, unit="D") + pd.to_timedelta(hour, unit="h") + pd.to_timedelta(minute, unit="m") + pd.to_timedelta(second, unit="s")
    order = np.argsort(raw_ts.to_numpy(), kind="stable")
    proc_ts = pd.DatetimeIndex(raw_ts[order])
    shifts = shifts[order]
    chosen_sup = rng.choice(sup_ids, size=n_proc)[order]
    chosen_cc = np.array([sup_to_cc[x] for x in chosen_sup])
    qty = np.round(rng.gamma(shape=4.5, scale=95.0, size=n_proc) + 60.0, 2)[order]
    fat = np.round(np.clip(rng.normal(4.8, 0.85, size=n_proc), 2.5, 8.5), 2)[order]
    snf = np.round(np.clip(rng.normal(8.7, 0.35, size=n_proc), 7.0, 10.0), 2)[order]
    temp = np.round(np.clip(rng.normal(4.4, 1.2, size=n_proc), 2.0, 13.0), 2)[order]
    acidity = np.round(np.clip(rng.normal(0.142, 0.015, size=n_proc), 0.10, 0.24), 3)[order]
    rejected = (fat < 3.2) | (snf < 8.2) | (temp > 8.5) | (acidity > 0.17)
    status = np.where(rejected, "Rejected", "Accepted")
    reason = np.full(n_proc, "", dtype=object)
    reason[fat < 3.2] = "Low Fat (<3.2%)"
    reason[(snf < 8.2) & (reason == "")] = "Low SNF (<8.2%)"
    reason[(temp > 8.5) & (reason == "")] = "High Temperature (>8.5C)"
    reason[(acidity > 0.17) & (reason == "")] = "High Acidity (>0.17%)"
    rate = np.round(32.0 + fat * 2.8 + snf * 1.1, 2)
    cost = np.round(qty * rate, 2)
    proc_ids = np.array([f"PRC-{i:06d}" for i in range(1, n_proc + 1)], dtype=object)
    batch_ids = np.array([f"MBT-{i:06d}" for i in range(1, n_proc + 1)], dtype=object)
    test_ids = np.array([f"QCT-{i:06d}" for i in range(1, n_proc + 1)], dtype=object)
    # DQ-04 in human-readable count; DQ catalogue below has exactly 5 unique scenario types.
    cost[999] = round(cost[999] * 1.25, 2)  # DQ-04: 25% cost inflation on PRC-001000
    proc_ts_text = proc_ts.strftime("%Y-%m-%d %H:%M:%S").to_numpy(dtype=object)
    proc_ts_text[499] = proc_ts[499].strftime("%d/%m/%Y %H:%M")  # DQ-03: non-ISO timestamp
    df_proc = pd.DataFrame({
        "procurement_id": proc_ids, "batch_id": batch_ids, "supplier_id": chosen_sup,
        "collection_centre_id": chosen_cc, "procurement_timestamp": proc_ts_text,
        "shift": shifts, "quantity_litres": qty, "purchase_rate_per_litre": rate,
        "total_purchase_cost": cost, "acceptance_status": status,
    })
    test_ts = proc_ts + pd.to_timedelta(rng.integers(5, 25, size=n_proc), unit="m")
    temp_col = temp.astype(object)
    temp_col[249] = None  # DQ-05: NULL temperature on QCT-000250
    lab = rng.choice(["LAB-CC-NORTH", "LAB-CC-SOUTH", "LAB-MAIN-PLANT"], size=n_proc)
    df_qual = pd.DataFrame({
        "test_id": test_ids, "batch_id": batch_ids,
        "test_timestamp": test_ts.strftime("%Y-%m-%d %H:%M:%S"),
        "fat_percentage": fat, "snf_percentage": snf, "temperature_c": temp_col,
        "acidity": acidity, "quality_status": status, "rejection_reason": reason,
        "laboratory_id": lab,
    })
    write_csv(df_proc, "data/raw/procurement/milk_procurement.csv")
    write_csv(df_qual, "data/raw/procurement/quality_tests.csv")
    # DQ-01 and DQ-02 are present in master data.
    return df_proc, df_qual, proc_ts


def build_production_schedule(rng, n_batches=4_000):
    day_counts = np.full(SIM_DAYS, n_batches // SIM_DAYS, dtype=int)
    day_counts[: n_batches % SIM_DAYS] += 1
    rows = []
    counter = 0
    for d, count in enumerate(day_counts):
        # Spread each day's runs over a 24-hour operating cycle, starting at 05:30.
        offsets = np.linspace(0, 13 * 60 + 30, count, endpoint=True) if count else []
        for offset in offsets:
            # Start production after the first morning milk collections have arrived.
            start = SIM_START + pd.Timedelta(days=d, hours=10) + pd.Timedelta(minutes=float(offset))
            duration = int(rng.integers(90, 181))
            end = min(start + pd.Timedelta(minutes=duration), SIM_START + pd.Timedelta(days=SIM_DAYS) - pd.Timedelta(seconds=1))
            hour = start.hour
            shift = "Shift-A (06:00-14:00)" if 6 <= hour < 14 else ("Shift-B (14:00-22:00)" if 14 <= hour < 22 else "Shift-C (22:00-06:00)")
            rows.append((start, end, shift))
            counter += 1
    rows.sort(key=lambda x: x[0])
    return rows


def generate_production(rng, df_proc, proc_ts, df_products, n_batches=4_000):
    schedule = build_production_schedule(rng, n_batches)
    accepted = df_proc.acceptance_status.eq("Accepted").to_numpy()
    lots = []
    for i in np.flatnonzero(accepted):
        lots.append({"batch_id": df_proc.iloc[i].batch_id, "available": float(df_proc.iloc[i].quantity_litres), "created": proc_ts[i]})
    # The accepted procurement list is already chronologically ordered.
    cursor = 0
    prod_ids = df_products.product_id.tolist()
    specs = df_products.set_index("product_id").to_dict("index")
    # Simplified single-input recipes: raw milk is converted to each finished product.
    # Yield factors are illustrative synthetic assumptions, not plant engineering standards.
    yield_factor = {
        "PRD-001": 0.975, "PRD-002": 0.975, "PRD-003": 0.975, "PRD-004": 0.975,
        "PRD-005": 0.970, "PRD-006": 0.180, "PRD-007": 0.045, "PRD-008": 0.045,
        "PRD-009": 0.050, "PRD-010": 0.940, "PRD-011": 0.970, "PRD-012": 0.940,
    }
    batch_rows, input_rows, output_rows = [], [], []
    in_id = out_id = 1
    for b_idx, (start, end, shift) in enumerate(schedule, 1):
        production_id = f"PRD-B-{b_idx:05d}"
        product_id = prod_ids[(b_idx - 1) % len(prod_ids)]
        target = 650.0
        remaining = target
        j = cursor
        tentative = []
        while j < len(lots) and remaining > 0.01:
            lot = lots[j]
            if lot["created"] > start:
                break
            if lot["available"] <= 0.01:
                j += 1
                continue
            take = round(min(lot["available"], remaining), 2)
            tentative.append((j, take, lot["batch_id"]))
            remaining = round(remaining - take, 2)
            j += 1 if take >= lot["available"] - 0.001 else 0
            if tentative and tentative[-1][0] == j - 1 and take < lot["available"] - 0.001:
                break
        # Commit only complete 650 L allocations; otherwise leave source lots untouched.
        if remaining > 0.01:
            # There is sufficient annual supply for this run in the intended scale; guard anyway.
            batch_rows.append({
                "production_id": production_id, "product_id": product_id,
                "production_start": start.strftime("%Y-%m-%d %H:%M:%S"),
                "production_end": end.strftime("%Y-%m-%d %H:%M:%S"), "shift": shift,
                "production_status": "Cancelled - Insufficient Raw Milk", "supervisor_id": f"SUPV-{((b_idx-1)%15)+1:02d}",
            })
            continue
        total_in = 0.0
        for lot_index, amount, source_batch in tentative:
            lots[lot_index]["available"] = round(lots[lot_index]["available"] - amount, 2)
            total_in += amount
            input_rows.append({
                "production_input_id": f"PIN-{in_id:06d}", "production_id": production_id,
                "source_batch_id": source_batch, "input_material_type": "Raw Milk",
                "input_quantity": amount, "unit_of_measure": "Litre",
                "input_timestamp": start.strftime("%Y-%m-%d %H:%M:%S"),
            })
            in_id += 1
        while cursor < len(lots) and lots[cursor]["available"] <= 0.01:
            cursor += 1
        batch_rows.append({
            "production_id": production_id, "product_id": product_id,
            "production_start": start.strftime("%Y-%m-%d %H:%M:%S"),
            "production_end": end.strftime("%Y-%m-%d %H:%M:%S"), "shift": shift,
            "production_status": "Completed", "supervisor_id": f"SUPV-{((b_idx-1)%15)+1:02d}",
        })
        uom = specs[product_id]["unit_of_measure"]
        input_basis = round(total_in * DENSITY_KG_PER_L, 2) if uom == "Kilogram" else round(total_in, 2)
        primary = round(input_basis * yield_factor[product_id], 2)
        residual = round(input_basis - primary, 2)
        output_rows.append({
            "output_id": f"POU-{out_id:06d}", "production_id": production_id,
            "product_id": product_id, "output_type": specs[product_id]["product_name"],
            "output_quantity": primary, "unit_of_measure": uom,
            "output_classification": "Primary product",
        })
        out_id += 1
        output_rows.append({
            "output_id": f"POU-{out_id:06d}", "production_id": production_id,
            "product_id": product_id, "output_type": f"{specs[product_id]['product_name']} - coproduct/residual",
            "output_quantity": residual, "unit_of_measure": uom,
            "output_classification": "By-product / residual",
        })
        out_id += 1
    df_batches = pd.DataFrame(batch_rows)
    df_inputs = pd.DataFrame(input_rows)
    df_outputs = pd.DataFrame(output_rows)
    write_csv(df_batches, "data/raw/production/production_batches.csv")
    write_csv(df_inputs, "data/raw/production/production_inputs.csv")
    write_csv(df_outputs, "data/raw/production/production_outputs.csv")
    # Only completed primary outputs enter saleable FG stock; preserve chronological lot order.
    completed_ids = set(df_batches.loc[df_batches.production_status.eq("Completed"), "production_id"])
    primary_outputs = df_outputs[df_outputs.output_classification.eq("Primary product") & df_outputs.production_id.isin(completed_ids)]
    batch_end = df_batches.set_index("production_id").production_end.to_dict()
    fg = {p: [] for p in prod_ids}
    for row in primary_outputs.itertuples(index=False):
        fg[row.product_id].append({
            "available_dt": pd.Timestamp(batch_end[row.production_id]),
            "available_qty": float(row.output_quantity),
        })
    for p in fg:
        fg[p].sort(key=lambda x: x["available_dt"])
    return df_batches, df_inputs, df_outputs, fg


def generate_sales(rng, df_products, fg, n_orders=14_000):
    specs = df_products.set_index("product_id").to_dict("index")
    product_ids = df_products.product_id.to_numpy()
    # Generate then sort the complete timestamps before drawing from stock.
    days = rng.integers(1, SIM_DAYS, size=n_orders)
    minutes = rng.integers(0, 600, size=n_orders)
    timestamps = SIM_START + pd.to_timedelta(days, unit="D") + pd.to_timedelta(8, unit="h") + pd.to_timedelta(minutes, unit="m")
    order_sort = np.argsort(timestamps.to_numpy(), kind="stable")
    timestamps = pd.DatetimeIndex(timestamps[order_sort])
    stock_cursor = {p: 0 for p in product_ids}
    order_rows, line_rows = [], []
    line_id = 1

    def fulfill(product_id, requested, order_dt):
        lots = fg[product_id]
        i = stock_cursor[product_id]
        remaining = float(requested)
        fulfilled = 0.0
        while i < len(lots) and remaining > 0.001:
            lot = lots[i]
            if lot["available_dt"] > order_dt:
                break
            available = lot["available_qty"]
            if available <= 0.001:
                if i == stock_cursor[product_id]:
                    stock_cursor[product_id] += 1
                i += 1
                continue
            taken = min(available, remaining)
            lot["available_qty"] = round(available - taken, 3)
            fulfilled += taken
            remaining -= taken
            if lot["available_qty"] <= 0.001 and i == stock_cursor[product_id]:
                stock_cursor[product_id] += 1
            i += 1
        return round(fulfilled, 3)

    for o_i, o_dt in enumerate(timestamps, 1):
        order_id = f"ORD-{o_i:06d}"
        expected_date = (o_dt + pd.Timedelta(days=1)).strftime("%Y-%m-%d")
        chosen = rng.choice(product_ids, size=2, replace=False)
        cancel_request = (o_i % 25 == 0)
        fulfilled_any = False
        fully_fulfilled = True
        for product_id in chosen:
            requested = float(rng.integers(3, 11))
            quantity_fulfilled = 0.0 if cancel_request else fulfill(product_id, requested, o_dt)
            fulfilled_any |= quantity_fulfilled > 0.001
            fully_fulfilled &= quantity_fulfilled >= requested - 0.001
            price = float(specs[product_id]["selling_price"])
            gross = round(quantity_fulfilled * price, 2)
            discount = round(gross * 0.05, 2) if (line_id % 5 == 0 and gross > 0) else 0.0
            line_rows.append({
                "order_line_id": f"ORL-{line_id:06d}", "order_id": order_id,
                "product_id": product_id, "quantity_ordered": requested,
                "quantity_fulfilled": quantity_fulfilled, "unit_selling_price": price,
                "discount_amount": discount, "line_total": round(gross - discount, 2),
            })
            line_id += 1
        if not fulfilled_any:
            status, actual_delivery, payment = "Cancelled", "", "Void"
        elif fully_fulfilled:
            status, actual_delivery = "Delivered", expected_date
            payment = rng.choice(["Paid", "Pending", "Partially Paid"], p=[0.82, 0.12, 0.06])
        else:
            status, actual_delivery = "Partially Delivered", expected_date
            payment = rng.choice(["Paid", "Pending", "Partially Paid"], p=[0.75, 0.15, 0.10])
        order_rows.append({
            "order_id": order_id, "customer_code": f"CUST-{((o_i-1)%250)+1:04d}",
            "order_timestamp": o_dt.strftime("%Y-%m-%d %H:%M:%S"),
            "order_status": status, "expected_delivery_date": expected_date,
            "actual_delivery_date": actual_delivery, "payment_status": payment,
        })
    df_orders = pd.DataFrame(order_rows)
    df_lines = pd.DataFrame(line_rows)
    write_csv(df_orders, "data/raw/sales/sales_orders.csv")
    write_csv(df_lines, "data/raw/sales/sales_order_lines.csv")
    return df_orders, df_lines


def validate_frames(dfs):
    sup, cc, products, proc, qual, batches, inputs, outputs, orders, lines = dfs
    checks = {}
    checks["suppliers_pk_unique"] = sup.supplier_id.is_unique
    checks["collection_centres_pk_unique"] = cc.collection_centre_id.is_unique
    checks["products_pk_unique"] = products.product_id.is_unique
    checks["procurement_pk_unique"] = proc.procurement_id.is_unique
    checks["quality_pk_unique"] = qual.test_id.is_unique
    checks["production_batches_pk_unique"] = batches.production_id.is_unique
    checks["production_inputs_pk_unique"] = inputs.production_input_id.is_unique
    checks["production_outputs_pk_unique"] = outputs.output_id.is_unique
    checks["sales_orders_pk_unique"] = orders.order_id.is_unique
    checks["sales_order_lines_pk_unique"] = lines.order_line_id.is_unique
    checks["proc_supplier_fk"] = proc.supplier_id.isin(sup.supplier_id).all()
    checks["proc_centre_fk"] = proc.collection_centre_id.isin(cc.collection_centre_id).all()
    checks["quality_batch_fk"] = qual.batch_id.isin(proc.batch_id).all()
    checks["production_product_fk"] = batches.product_id.isin(products.product_id).all()
    checks["input_production_fk"] = inputs.production_id.isin(batches.production_id).all()
    checks["input_source_batch_fk"] = inputs.source_batch_id.isin(proc.batch_id).all()
    checks["output_production_fk"] = outputs.production_id.isin(batches.production_id).all()
    checks["output_product_fk"] = outputs.product_id.isin(products.product_id).all()
    checks["line_order_fk"] = lines.order_id.isin(orders.order_id).all()
    checks["line_product_fk"] = lines.product_id.isin(products.product_id).all()
    batch_status = batches.set_index("production_id").production_status
    checks["all_production_batches_completed"] = batch_status.eq("Completed").all()
    checks["input_from_accepted_procurement"] = inputs.source_batch_id.isin(proc.loc[proc.acceptance_status.eq("Accepted"), "batch_id"]).all()
    if len(inputs):
        src = proc.set_index("batch_id")["procurement_timestamp"]
        # Use batch IDs and input timestamps; the only non-ISO value is handled separately below.
        src_dt = {}
        for r in proc.itertuples(index=False):
            try:
                src_dt[r.batch_id] = pd.to_datetime(r.procurement_timestamp, format="%d/%m/%Y %H:%M", errors="raise") if "/" in str(r.procurement_timestamp) else pd.Timestamp(r.procurement_timestamp)
            except Exception:
                src_dt[r.batch_id] = pd.NaT
        input_src_times = inputs.source_batch_id.map(src_dt)
        input_times = pd.to_datetime(inputs.input_timestamp)
        checks["input_after_source_timestamp"] = (input_src_times <= input_times).all()
        source_qty = proc.set_index("batch_id").quantity_litres
        consumed = inputs.groupby("source_batch_id").input_quantity.sum()
        checks["source_consumption_not_over_procurement"] = (consumed <= source_qty.reindex(consumed.index) + 0.001).all()
    else:
        checks["input_after_source_timestamp"] = False
        checks["source_consumption_not_over_procurement"] = False
    checks["sales_fulfilled_not_above_ordered"] = (lines.quantity_fulfilled <= lines.quantity_ordered + 0.001).all()
    checks["sales_fulfilled_nonnegative"] = (lines.quantity_fulfilled >= 0).all()
    primary = outputs[outputs.output_classification.eq("Primary product")]
    produced = primary.groupby("product_id").output_quantity.sum()
    sold = lines.groupby("product_id").quantity_fulfilled.sum()
    checks["sales_not_above_total_primary_output"] = (sold <= produced.reindex(sold.index).fillna(0) + 0.01).all()
    checks["proc_cost_matches_except_injected_row"] = np.isclose(
        proc.loc[proc.procurement_id.ne("PRC-001000"), "total_purchase_cost"],
        (proc.loc[proc.procurement_id.ne("PRC-001000"), "quantity_litres"] * proc.loc[proc.procurement_id.ne("PRC-001000"), "purchase_rate_per_litre"]).round(2),
    ).all()
    checks["five_intentional_dq_patterns_present"] = (
        (sup.loc[sup.supplier_id.eq("SUP-0015"), "status"].iloc[0] == "active") and
        (sup.loc[sup.supplier_id.eq("SUP-0042"), "village"].iloc[0].strip() != sup.loc[sup.supplier_id.eq("SUP-0042"), "village"].iloc[0]) and
        ("/" in proc.loc[proc.procurement_id.eq("PRC-000500"), "procurement_timestamp"].iloc[0]) and
        (proc.loc[proc.procurement_id.eq("PRC-001000"), "total_purchase_cost"].iloc[0] > round(proc.loc[proc.procurement_id.eq("PRC-001000"), "quantity_litres"].iloc[0] * proc.loc[proc.procurement_id.eq("PRC-001000"), "purchase_rate_per_litre"].iloc[0], 2)) and
        pd.isna(qual.loc[qual.test_id.eq("QCT-000250"), "temperature_c"].iloc[0])
    )
    return checks


def main():
    start = time.time()
    for p in [RAW / "master", RAW / "procurement", RAW / "production", RAW / "sales", MANIFEST_DIR]:
        p.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    df_sup, df_cc, df_products = generate_master(rng)
    df_proc, df_qual, proc_ts = generate_procurement_quality(rng, df_sup, df_cc)
    df_batches, df_inputs, df_outputs, fg = generate_production(rng, df_proc, proc_ts, df_products)
    df_orders, df_lines = generate_sales(rng, df_products, fg)
    frames = (df_sup, df_cc, df_products, df_proc, df_qual, df_batches, df_inputs, df_outputs, df_orders, df_lines)
    checks = {key: bool(value) for key, value in validate_frames(frames).items()}
    if not all(checks.values()):
        failed = [k for k, v in checks.items() if not v]
        raise RuntimeError("Validation failed: " + ", ".join(failed))
    dataset_specs = [
        ("suppliers", "data/raw/master/suppliers.csv", "supplier_id", []),
        ("collection_centres", "data/raw/master/collection_centres.csv", "collection_centre_id", []),
        ("products", "data/raw/master/products.csv", "product_id", []),
        ("milk_procurement", "data/raw/procurement/milk_procurement.csv", "procurement_id", ["supplier_id", "collection_centre_id"]),
        ("quality_tests", "data/raw/procurement/quality_tests.csv", "test_id", ["batch_id"]),
        ("production_batches", "data/raw/production/production_batches.csv", "production_id", ["product_id"]),
        ("production_inputs", "data/raw/production/production_inputs.csv", "production_input_id", ["production_id", "source_batch_id"]),
        ("production_outputs", "data/raw/production/production_outputs.csv", "output_id", ["production_id", "product_id"]),
        ("sales_orders", "data/raw/sales/sales_orders.csv", "order_id", []),
        ("sales_order_lines", "data/raw/sales/sales_order_lines.csv", "order_line_id", ["order_id", "product_id"]),
    ]
    entries, total_rows, total_bytes = [], 0, 0
    for name, rel, pk, fks in dataset_specs:
        path = ROOT / rel
        df = pd.read_csv(path, low_memory=False)
        size = path.stat().st_size
        entries.append({"dataset_name": name, "relative_path": rel, "file_format": "CSV", "row_count": int(len(df)), "column_count": int(len(df.columns)), "file_size_bytes": int(size), "primary_key": pk, "foreign_keys": fks})
        total_rows += len(df); total_bytes += size
    manifest = {
        "project": "DairyChain Synthetic Dairy Factory Dataset",
        "generator_version": VERSION, "random_seed": SEED,
        "scale_mode": "full", "simulation_start": "2025-11-01", "simulation_end": "2026-10-31",
        "generated_at_utc": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "total_datasets": len(entries), "total_rows": int(total_rows), "total_size_bytes": int(total_bytes),
        "intentional_data_quality_scenarios": [
            {"id": "DQ-01", "dataset": "suppliers", "record_id": "SUP-0015", "issue": "Lowercase supplier status value"},
            {"id": "DQ-02", "dataset": "suppliers", "record_id": "SUP-0042", "issue": "Leading and trailing whitespace in village"},
            {"id": "DQ-03", "dataset": "milk_procurement", "record_id": "PRC-000500", "issue": "Non-ISO procurement timestamp format (DD/MM/YYYY HH:MM)"},
            {"id": "DQ-04", "dataset": "milk_procurement", "record_id": "PRC-001000", "issue": "Total purchase cost inflated by 25%"},
            {"id": "DQ-05", "dataset": "quality_tests", "record_id": "QCT-000250", "issue": "NULL temperature_c value"},
        ],
        "validation_checks": checks, "datasets": entries,
    }
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    (MANIFEST_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    report = ["DairyChain dataset validation", "============================", f"Status: {'PASS' if all(checks.values()) else 'FAIL'}", ""]
    report += [f"{'PASS' if value else 'FAIL'}  {key}" for key, value in checks.items()]
    report += ["", f"Total datasets: {len(entries)}", f"Total rows: {total_rows:,}", f"Total CSV size: {total_bytes / (1024*1024):.2f} MB", f"Elapsed generation time: {time.time()-start:.2f} seconds"]
    (ROOT / "validation_report.txt").write_text("\n".join(report), encoding="utf-8")
    (ROOT / "README.md").write_text(
        "# DairyChain synthetic dataset\n\n"
        "This folder contains 10 related CSV datasets for a synthetic Indian dairy factory covering 2025-11-01 through 2026-10-31.\n\n"
        "## Structure\n\n"
        "- `data/raw/master/`: suppliers, collection centres, products\n"
        "- `data/raw/procurement/`: milk procurement and quality tests\n"
        "- `data/raw/production/`: production batches, inputs and outputs\n"
        "- `data/raw/sales/`: sales orders and order lines\n"
        "- `data/manifests/manifest.json`: actual row counts, file sizes, keys, DQ scenarios and validation results\n\n"
        "## Important modeling assumptions\n\n"
        "- Every completed production batch consumes 650 L of accepted raw milk in FIFO order.\n"
        "- For this starter model, each finished product is modeled as a simplified direct raw-milk conversion. Yield factors are illustrative synthetic assumptions, not engineering specifications.\n"
        "- The second production output is a combined coproduct/residual amount to make the simplified input/output quantity balance explicit.\n"
        "- Orders are processed chronologically and fulfilled quantities are capped by finished goods available by the order timestamp.\n"
        "- Customer codes are external references; no customer master table is included in this 10-table starter scope.\n"
        "- Five intentional data-quality scenarios are documented in the manifest.\n\n"
        "## Start here\n\n"
        "Load the CSVs into PostgreSQL Bronze as raw landing tables. Preserve source values, including the five intentional DQ scenarios.\n",
        encoding="utf-8"
    )
    # SHA256 list for file integrity
    hashes = []
    for _, rel, _, _ in dataset_specs:
        path = ROOT / rel
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        hashes.append(f"{sha}  {rel}")
    (ROOT / "SHA256SUMS.txt").write_text("\n".join(hashes) + "\n", encoding="utf-8")
    zip_path = ROOT.parent / "DairyChain_dataset_full.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for path in ROOT.rglob("*"):
            if path.is_file() and path.name != zip_path.name:
                zf.write(path, arcname=Path("DairyChain_dataset") / path.relative_to(ROOT))
    print(json.dumps({"zip": str(zip_path), "total_rows": total_rows, "total_size_bytes": total_bytes, "rows_by_dataset": {e['dataset_name']: e['row_count'] for e in entries}, "validation": checks, "zip_size_bytes": zip_path.stat().st_size}, indent=2))

if __name__ == "__main__":
    main()
