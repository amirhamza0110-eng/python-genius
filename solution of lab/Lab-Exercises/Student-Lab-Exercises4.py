raw_survey_inputs = ["  ALICE SMITH ", " dhaka, BANGLADESH  ", "  mLOpS_ENGineer  ", "  LIAM,MAYA "]
sanitized_records = []

for item in raw_survey_inputs:
    cleaned = item.strip().lower()
    sanitized_records.append(cleaned)

print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")