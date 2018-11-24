def nbdump(infile, outfile):

    import json

    j = json.JSONDecoder()
    # line counter
    lc = 0
    
    try:
        with open(infile) as f:
            data = f.read()
            nb = j.decode(data)

        o = open(outfile,'w+')
        for cell in nb['cells']:
            if cell['cell_type'] == 'code':
                for line in cell['source']:
                    o.write(line)
                    lc += 1
                o.write('\n')
        o.close()
        print(f'Sucksessfully wrote {lc} lines to {outfile}')
                
    except Exception as e:
        print(e)
