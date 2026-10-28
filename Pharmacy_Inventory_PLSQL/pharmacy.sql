
-- =====================================================
-- PROJECT: PHARMACY INVENTORY MANAGEMENT SYSTEM
-- AIM:
-- To manage medicines, monitor stock and expiry dates,
-- and automatically record changes in medicine quantity.
-- DATABASE: Oracle
-- =====================================================


-- STEP 1: Create the medicines table

CREATE TABLE medicines (
    medicine_id NUMBER PRIMARY KEY,
    medicine_name VARCHAR2(100) NOT NULL,
    batch_no VARCHAR2(30) NOT NULL,
    category VARCHAR2(50),
    quantity NUMBER DEFAULT 0 NOT NULL,
    unit_price NUMBER(10,2) NOT NULL,
    expiry_date DATE NOT NULL,
    reorder_level NUMBER DEFAULT 10 NOT NULL,
    CONSTRAINT chk_medicine_qty CHECK (quantity >= 0),
    CONSTRAINT chk_medicine_price CHECK (unit_price >= 0),
    CONSTRAINT uq_medicine_batch UNIQUE (medicine_name, batch_no)
);


-- STEP 2: Insert sample medicine records

INSERT INTO medicines VALUES (
    101, 'Paracetamol', 'PAR101', 'Tablet',
    100, 2.50, DATE '2027-12-31', 20
);

INSERT INTO medicines VALUES (
    102, 'Amoxicillin', 'AMX102', 'Capsule',
    15, 8.00, DATE '2027-08-30', 20
);

INSERT INTO medicines VALUES (
    103, 'Cetirizine', 'CET103', 'Tablet',
    50, 3.00, DATE '2028-05-31', 10
);

INSERT INTO medicines VALUES (
    104, 'Vitamin C', 'VTC104', 'Supplement',
    5, 5.00, DATE '2027-06-30', 10
);

COMMIT;


-- STEP 3: Create the stock audit log table

CREATE TABLE medicine_audit_log (
    log_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    medicine_id NUMBER NOT NULL,
    old_quantity NUMBER,
    new_quantity NUMBER,
    change_amount NUMBER,
    changed_by VARCHAR2(128),
    changed_on DATE
);


-- STEP 4: Create the database trigger

CREATE OR REPLACE TRIGGER trg_audit_medicine_stock
AFTER UPDATE OF quantity ON medicines
FOR EACH ROW
WHEN (OLD.quantity <> NEW.quantity)
BEGIN
    INSERT INTO medicine_audit_log (
        medicine_id,
        old_quantity,
        new_quantity,
        change_amount,
        changed_by,
        changed_on
    )
    VALUES (
        :OLD.medicine_id,
        :OLD.quantity,
        :NEW.quantity,
        :NEW.quantity - :OLD.quantity,
        USER,
        SYSDATE
    );
END trg_audit_medicine_stock;
/

-- STEP 5: Test a stock reduction
-- Example: 100 Paracetamol units become 80

UPDATE medicines
SET quantity = 80
WHERE medicine_id = 101;

COMMIT;


-- STEP 6: Test a stock increase
-- Example: Amoxicillin stock increases from 15 to 25

UPDATE medicines
SET quantity = quantity + 10
WHERE medicine_id = 102;

COMMIT;


-- STEP 7: Display all medicines

SELECT *
FROM medicines
ORDER BY medicine_id;


-- STEP 8: Display the stock audit log

SELECT *
FROM medicine_audit_log
ORDER BY log_id;


-- STEP 9: Find medicines with low stock

SELECT medicine_id, medicine_name, quantity, reorder_level
FROM medicines
WHERE quantity <= reorder_level
ORDER BY quantity;


-- STEP 10: Find expired medicines

SELECT medicine_id, medicine_name, batch_no, expiry_date
FROM medicines
WHERE expiry_date < TRUNC(SYSDATE);


-- STEP 11: Find medicines expiring within 90 days
-- Excludes medicines that are already expired

SELECT medicine_id, medicine_name, batch_no, expiry_date
FROM medicines
WHERE expiry_date >= TRUNC(SYSDATE)
  AND expiry_date < TRUNC(SYSDATE) + 90
ORDER BY expiry_date;


-- STEP 12: Display total inventory value

SELECT SUM(quantity * unit_price) AS total_inventory_value
FROM medicines;
