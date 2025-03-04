all: json search pydantic er

clean:
	rm data/individual_json/*.json
	rm app/static/idx.json
	rm idx.json
	rm *.pyc

json:
	python3 scripts/to_json.py

search:
	python3 scripts/build_search.py
	cp idx.json app/static/idx.json

run:
	uvicorn app.main:app --reload

pydantic:
	datamodel-codegen --input data/records.json --input-file-type json --output scripts/data_model.py --output-model-type pydantic_v2.BaseModel

er: 
	python3 scripts/to_pydantic.py
	mv ./data/diagram.png app/static/images/diagram.png
	echo "Done ✅"
