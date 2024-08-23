CREATE OR REPLACE FUNCTION public.core_func_do_nothing(
	inparametertwo text,
	p_offset bigint,
	p_limit bigint)
    RETURNS TABLE(col1 text, col2 text, col3 text) 
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$

BEGIN
    RETURN QUERY 
    SELECT 
        *
    FROM (
        SELECT 
            inparametertwo AS col1, 
            'Ouch!' AS col2, 
            NULL::TEXT AS col3
        UNION ALL
        SELECT 
            inparametertwo AS col1, 
            '!Ouch' AS col2, 
            NULL::TEXT AS col3
        UNION ALL
        SELECT 
            inparametertwo AS col1, 
            NULL::TEXT AS col2, 
            NULL::TEXT AS col3
        UNION ALL
        SELECT 
            inparametertwo AS col1, 
            'Ouch' AS col2, 
            NULL::TEXT AS col3
    ) subquery
    OFFSET p_offset LIMIT p_limit;
END;
$BODY$;