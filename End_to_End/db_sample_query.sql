SELECT polls_events.Time_Stamp, polls_transformer.Transformer_number
FROM polls_events
INNER JOIN polls_transformer ON polls_events.mainId_id=polls_transformer.Transformer_number

SELECT polls_events.Time_Stamp 
FROM  polls_events  
INNER JOIN polls_transformer ON polls_events.mainId_id=polls_transformer.Transformer_number
WHERE polls_transformer.Manufacturer_name = 'KEL' 

SELECT polls_events.Time_Stamp FROM  polls_events   INNER JOIN polls_transformer ON polls_events.mainId_id=polls_transformer.Transformer_number WHERE  polls_transformer.Manufacturer_name = 'KEL'
