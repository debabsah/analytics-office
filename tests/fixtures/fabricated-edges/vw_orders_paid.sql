-- the one view we have
CREATE VIEW vw_orders_paid AS
SELECT o.order_id, o.customer_id, o.amount, p.paid_at
FROM ORDERS o
JOIN PAYMENTS p ON p.order_id = o.order_id;
