import os
import csv


def get_std_result_str(rec_dict, rec_len): 
    max_votes = -1
    winner_str = ''
    
    out_str = ''
    out_str = out_str + '\n' + get_line_str()
    out_str = out_str + '\n' + 'Election Results'
    out_str = out_str + '\n' + get_line_str()
    out_str = out_str + '\n' + 'Total Votes: ' + str(rec_len)
    out_str = out_str + '\n' + get_line_str()
    
    for key, value in rec_dict.items(): 
        if max_votes < value: 
            max_votes = value
            winner_str = 'Winner: ' + key
        
        vote_percentage = 100 * value/rec_len
        out_str = out_str + '\n' + key + ': ' + str(round(vote_percentage, 3)) + '% (' + str(value) + ')'
    
    out_str = out_str + '\n' + get_line_str()
    out_str = out_str + '\n' + winner_str
    out_str = out_str + '\n' + get_line_str()
    
    print(out_str)
    
    return out_str


def file_to_summary_dict(file_path): 
    ## Empty_dict for cndt and the votes received
    c_votes = {}
    
    with open(file_path, 'r', newline='') as ctx: 
        csvReader = csv.reader(ctx, delimiter = ',')
        records = 0
        for row in csvReader: 
            if csvReader.line_num == 1:
                continue
            
            records += 1
            cndt = row[2].strip()

            if cndt in c_votes.keys(): 
                votes = c_votes[cndt] + 1
                c_votes.update({cndt: votes})
            else: 
                c_votes.update({cndt: 1})
    
    return c_votes, records


def get_line_str(): 
    return '--------------------------'


def write_results(out_path, content): 
    out_dir = os.path.dirname(out_path)

    if not os.path.exists(out_dir): 
        os.mkdir(out_dir, 511)
    file_name = os.path.split(out_path)[1]
    
    with open(os.path.join(out_dir, file_name), 'a') as ctx: 
        ctx.write(content)


file_path = os.path.join('.', 'Resources', 'election_data.csv')
out_path = os.path.join('.', 'output', 'out.txt')

summary_dict, rec_len = file_to_summary_dict(file_path)
out_str = get_std_result_str(summary_dict, rec_len)
write_results(out_path, out_str)
