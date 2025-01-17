import os,csv
def msats_to_BTC(msats:int)->float:
    sats=msats/1000
    btc=sats/100000000
    return btc
def float_to_str(inputfloat:float)->str:
    return '{:.8f}'.format(inputfloat)

if __name__=="__main__":
    print("Phoenix exports to a CSV file, we will ask for the file location if it cannot be found")
    print('Alternatively, just rename the file phoenix.csv and place it in the same directory the script is run from')
    print("Please type in the full path if prompted")
    print(r"WINDOWS users: You must escape slashes so C:\folder\file.txt should be entered as C:\\folder\\file.txt")

    # check if csv import files already exist, prompt if they don't
    if os.path.exists('phoenix.csv'):
        invoices_path=os.path.join(os.getcwd(),'phoenix.csv')
    else:
        invoices_path=input("phoenix.csv=")
    known_paths={
    'INVOICES':invoices_path,
    }
    # verify all given files exist
    for known_path in known_paths.values():
        if known_path=="":
            continue
        if not os.path.exists(known_path):
            print("Error, path {} doesn't exist! Try running the script again.".format(known_path))
            quit()
    
    final_csv=[] # final list which will be written to the output.csv file
    # a list of keys which can be converted gracefully from import file to output file
    convert_keys={
        'Date':'Date',
    }
    # ignore these keys
    ignore_keys={'Amount Fiat','Fees Fiat'} # skip
    # a list of all keys which will be exported. More is added to this later
    export_keys={'Description','Received Currency','Sent Currency'}
    # keys which should be concatenated into the notes field
    notes_keys={'Context','Notes','Description'}

    # for each CSV file
    for csv_type,known_path in known_paths.items():
        with open(known_path, mode ='r') as file:    
            csvFile = csv.DictReader(file)
            # read in CSV file line by line
            for line in csvFile:
                notes_field='' # start with a blank notes field
                new_line={} # we put output data into here
                for key,value in line.items():
                    write_value=value
                    write_key=key
                    if key in ignore_keys:
                        continue
                    elif key in notes_keys:
                        # special handling for "notes" fields
                        if value.strip()!='':
                            notes_add='{}:{} + '.format(key,value)
                            notes_field=notes_field+notes_add
                        continue
                    elif key=='Amount Millisatoshi':
                        # special handling for this field, figure out if tx is inbound or outbound
                        numbered=int(value)
                        if numbered>0:
                            write_key='Received Amount'
                            new_line['Received Currency']='BTC'
                        elif numbered<0:
                            write_key='Sent Amount'
                            new_line['Sent Currency']='BTC'
                        elif numbered==0:
                            continue
                        converted=abs(msats_to_BTC(numbered))
                        write_value=float_to_str(converted)
                    elif key=='Fees Millisatoshi':
                        # special handling for this field, koinly wants BTC not SATs
                        numbered=int(value)
                        converted=abs(msats_to_BTC(numbered))
                        write_value=float_to_str(converted)
                        write_key='Fee Amount'
                    elif key not in convert_keys:
                        print("Error: found unknown key {}, exported CSV may not be complete!".format(key))
                        continue
                    else:
                        write_key=convert_keys[key]
                    if write_key not in export_keys:
                        export_keys.add(write_key)
                    new_line[write_key]=write_value 
                new_line['Description']=notes_field
                final_csv.append(new_line)
    # write output csv
    with open('output.csv','w') as my_file:
        dict_writer = csv.DictWriter(my_file, export_keys)
        dict_writer.writeheader()
        for transaction in final_csv:
            dict_writer.writerow(transaction)
    print('Script complete! Check output.csv for your results')
    print('If you found this script useful, please consider donating a few sats to me as a thank you')
    print('makeasnek@zeuspay.com')
    print('bc1q4zqhmyp8yw4zehw2tf4sjvqc5dv9dm747ssh0p')

        
          
    
        
                        
