CREATE OR REPLACE VIEW SOME_SCHEMA.UGLY_TABLE
AS
WITH ghj AS
--
-- comments
-- evil because one column has no table prefix 
-- should be ax.no_tab_col 
-- 
(
SELECT SOME_SCHEMA.FUNCTION('INPUT','egdate','YYYYMMDD') AS some_date
)
SELECT ax.a_id
,      bx.b_col alias_b_col
,      cx.c_col alias_c_col
,      no_tab_col alias_no_tab_col
FROM   SOME_SCHEMA.AX_TABLE ax
LEFT JOIN OTHER_SCHEMA.CX_TABLE cx
    ON  ax.join_id = cx.c_join_id
	AND ax.migration_dt <= (SELECT some_date from ghj)
LEFT JOIN SOME_SCHEMA.BX_TABLE bx
	ON bx.x_id = ax.x_id
WHERE
    ax.some_date = TO_DATE('99991231','YYYYMMDD')
;