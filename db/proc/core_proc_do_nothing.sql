CREATE OR REPLACE PROCEDURE public.core_proc_do_nothing(
	IN inparameter integer,
	OUT outparameter text)
LANGUAGE 'plpgsql'
AS $BODY$

BEGIN
	outparameter := 'ouch! ('|| inparameter ||')';
END;
$BODY$;