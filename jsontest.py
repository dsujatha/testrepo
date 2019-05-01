import json

json_string = None

class OracleBuildSchema(object):
 def __init__(self):
    self.col_names=""
    self.metadata = {}

 def build_column_names(self,fieldList,pkfield):
    colstr=""
    for field in fieldList:
            col_name = field["col_name"]
            col_data_type = field["data_type"]
            self.metadata[col_name] = col_data_type
            self.col_names = self.col_names + col_name + ","
            param3 = ""
            param4 = ""
            if(field["is_nullable"] == 'False'):
                param3 = "NOT NULL"
            if(pkfield == col_name):
                 param4 = "PRIMARY KEY"
            colstr = colstr + "{} {} {} {} \n,".format(col_name, col_data_type,param3,param4)
    return colstr[:-1]

 def format_col_value(self,colName,colValue):
     data_type = self.metadata.get(colName)
     if data_type.startswith('Timestamp') or data_type.startswith('Date'):
         return "to_date({},'yyyy-mm-dd hh24:mi:ss:SSSSS')".format(colValue)
     elif data_type.startswith('varchar') :
         return "'{}'".format(colValue)
     else:
        return colValue

 def build_create_table(self,table_name,table_metadata):
    for key, metadata in table_metadata.items():
       if(key == 'metadata'):
         col_info = self.build_column_names(metadata[0]["Fields"], metadata[1]["primary_key"])
    return "CREATE TABLE {}({});\n".format(table_name , col_info)

 def build_records(self,table_name,table_metadata):
  retval = ""

  for key, metadata in table_metadata.items():
    if(key =='records'):
       record_info = metadata
       self.col_names = self.col_names[:-1]
       columns = self.col_names.split(',')
       for record in record_info:
          row_data = ""
          for col in columns:
             if (record[col]!= None):
                format_col_value = self.format_col_value(col,record[col])
                row_data = row_data + format_col_value + ","
          retval = retval + "INSERT INTO TABLE {} ({}) VALUES ({});\n".format(table_name,self.col_names,row_data[:-1])
  return retval

 def run(self):
    with open("json_file.json") as f:
        json_string = f.read()
        try:
            parsed_json = json.loads(json_string)
            script = ""
            keys = parsed_json.items()
            for table_name,table_metadata in parsed_json.items():
                script = self.build_create_table(table_name,table_metadata)
            if('records' in table_metadata):
                records_query = self.build_records(table_name,table_metadata)
                script = script + records_query
            print(script)
        except Exception as e:
            print(e)