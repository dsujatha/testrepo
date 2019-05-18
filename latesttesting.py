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
  print(recordData)
  return recordData
