 def build_insert_query_template(self,table_name,table_metadata):
     baseQuery = ""
     self.col_names = self.col_names[:-1]
     columns = self.col_names.split(',')
     print(len(columns))
     placeholder = '%s,' * len(columns)
     print("INSERT INTO TABLE {} ({}) VALUES ({});\n".format(table_name, self.col_names, placeholder[:-1]))


 def build_records(self,table_name,table_metadata):

  recordData = []
  for key, metadata in table_metadata.items():
    if(key =='records'):
       record_info = metadata
       columns = self.col_names.split(',')
       for record in record_info:
          row_data = ()
          for col in columns:
             if (record[col]!= None):
                format_col_value = self.format_col_value(col,record[col])
                row_data = row_data + (format_col_value,)
          recordData.append(row_data)
  return recordData
 
 
 def run(self):
    with open("json_file.json") as f:
        json_string = f.read()
        try:
            parsed_json = json.loads(json_string)
            script = ""
            keys = parsed_json.items()

            for table_name,table_metadata in parsed_json.items():
                script = self.build_create_table(table_name,table_metadata)
                print(script)
            if('records' in table_metadata):
                base_insert_query = self.build_insert_query_template(table_name, table_metadata)
                print(base_insert_query)
                records_query = self.build_records(table_name,table_metadata)
                print(records_query)
        except Exception as e:
            print(e)
